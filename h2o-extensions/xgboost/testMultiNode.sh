#!/bin/bash
source "${ROOT_DIR}/multiNodeUtils.sh"

# Argument parsing
if [ "$1" = "jacoco" ]
then
    JACOCO_ENABLED=true
else
    JACOCO_ENABLED=false
fi

# Clean out any old sandbox, make a new one
OUTDIR=sandbox/multi

MKDIR=mkdir
SEP=:
case "`uname`" in
    CYGWIN* )
      MKDIR=mkdir.exe
      SEP=";"
      ;;
esac
rm -fr $OUTDIR
$MKDIR -p $OUTDIR

function cleanup () {
  kill -9 ${PID_1} ${PID_2} ${PID_3} 1> /dev/null 2>&1
  wait 1> /dev/null 2>&1
  RC=`cat $OUTDIR/status.0`
  if [ $RC -ne 0 ]; then
    echo Status: $RC
    cat $OUTDIR/out.*
    echo h2o-ext-xgboost junit tests FAILED
    exit 1
  else
    echo h2o-ext-xgboost junit tests PASSED
    exit 0
  fi
}

trap cleanup SIGTERM SIGINT

# Find java command
if [ -z "$TEST_JAVA_HOME" ]; then
  # Use default
  JAVA_CMD="java"
else
  # Use test java home
  JAVA_CMD="$TEST_JAVA_HOME/bin/java"
  # Increase XMX since JAVA_HOME can point to java6
  JAVA6_REGEXP=".*1\.6.*"
  if [[ $TEST_JAVA_HOME =~ $JAVA6_REGEXP ]]; then
    JAVA_CMD="${JAVA_CMD}"
  fi
fi
# Gradle puts files:
#   build/classes/main - Main h2o core classes
#   build/classes/test - Test h2o core classes
#   build/resources/main - Main resources (e.g. page.html)

MAX_MEM=${H2O_JVM_XMX:-4g}

# Check if coverage should be run
if [ $JACOCO_ENABLED = true ]
then
    AGENT="../jacoco/jacocoagent.jar"
    COVERAGE="-javaagent:$AGENT=destfile=build/jacoco/h2o-ext-xgboost.exec"
    MAX_MEM=${H2O_JVM_XMX:-8g}
else
    COVERAGE=""
fi
# Force enable LeaderNodeRequestFilter to emulate XGBoost external cluster deployments on K8S
JVM="nice $JAVA_CMD $COVERAGE -ea -Xmx${MAX_MEM} -Xms${MAX_MEM} -Dsys.ai.h2o.ext.auth.toggle.LeaderNodeRequestFilter=true -DcloudSize=4 -cp ${JVM_CLASSPATH} ${ADDITIONAL_TEST_JVM_OPTS}"
echo "$JVM" > $OUTDIR/jvm_cmd.txt

# Tests
# Must run first, before the cloud locks (because it tests cloud locking)
JUNIT_TESTS_BOOT=""

# Runner
# Default JUnit runner is org.junit.runner.JUnitCore
JUNIT_RUNNER="water.junit.H2OTestRunner"

# find all java in the src/test directory
# Cut the "./water/MRThrow.java" down to "water/MRThrow.java"
# Cut the   "water/MRThrow.java" down to "water/MRThrow"
# Slash/dot "water/MRThrow"      becomes "water.MRThrow"

# On this h2o-ext-xgboost testMultiNode.sh only, force the tests.txt to be in the same order for all machines.
# If sorted, the result of the cd/grep varies by machine.
# If randomness is desired, replace sort with the unix 'shuf'
# Use /usr/bin/sort because of cygwin on windows.
# Windows has sort.exe which you don't want. Fails? (is it a lineend issue)
(cd src/test/java; /usr/bin/find . -name '*.java' | cut -c3- | sed 's/.....$//' | sed -e 's/\//./g') | /usr/bin/sort > $OUTDIR/tests.txt

# Output the comma-separated list of ignored/dooonly tests
# Ignored tests trump do-only tests
echo $IGNORE > $OUTDIR/tests.ignore.txt
echo $DOONLY > $OUTDIR/tests.doonly.txt

# Launch 3 helper JVMs.  All output redir'd at the OS level to sandbox files.
CLUSTER_NAME=junit_cluster_$$
CLUSTER_BASEPORT=44000
$JVM water.H2OTestNodeStarter -name $CLUSTER_NAME -ip $H2O_NODE_IP -baseport $CLUSTER_BASEPORT -ga_opt_out $SSL 1> $OUTDIR/out.1 2>&1 & PID_1=$!
$JVM water.H2OTestNodeStarter -name $CLUSTER_NAME -ip $H2O_NODE_IP -baseport $CLUSTER_BASEPORT -ga_opt_out $SSL 1> $OUTDIR/out.2 2>&1 & PID_2=$!
$JVM water.H2OTestNodeStarter -name $CLUSTER_NAME -ip $H2O_NODE_IP -baseport $CLUSTER_BASEPORT -ga_opt_out $SSL 1> $OUTDIR/out.3 2>&1 & PID_3=$!

# If coverage is being run, then pass a system variable flag so that timeout limits are increased.
if [ $JACOCO_ENABLED = true ]
then
    JACOCO_FLAG="-Dtest.jacocoEnabled=true"
else
    JACOCO_FLAG=""
fi

# Launch last driver JVM.  All output redir'd at the OS level to sandbox files.
echo Running ${PROJECT_NAME} junit tests...
($JVM $TEST_SSL -Ddoonly.tests=$DOONLY -Dbuild.id=$BUILD_ID -Dignore.tests=$IGNORE -Djob.name=$JOB_NAME -Dgit.commit=$GIT_COMMIT -Dgit.branch=$GIT_BRANCH -Dai.h2o.name=$CLUSTER_NAME -Dai.h2o.ip=$H2O_NODE_IP -Dai.h2o.baseport=$CLUSTER_BASEPORT -Dai.h2o.ga_opt_out=yes $JACOCO_FLAG $JUNIT_RUNNER $JUNIT_TESTS_BOOT `cat $OUTDIR/tests.txt` 2>&1 ; echo $? > $OUTDIR/status.0) 1> $OUTDIR/out.0 2>&1

grep EXECUTION $OUTDIR/out.0 | sed -e "s/.*TEST \(.*\) EXECUTION TIME: \(.*\) (Wall.*/\2 \1/" | sort -gr | head -n 10 >> $OUTDIR/out.0

cleanup
