#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

import h2o
from h2o.base import Keyed
from h2o.frame import H2OFrame
from h2o.expr import ExprNode
from h2o.expr import ASTId
from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OANOVAGLMEstimator(H2OEstimator):
    """
    ANOVA for Generalized Linear Model

    H2O ANOVAGLM is used to calculate Type III SS which is used to evaluate the contributions of individual predictors 
    and their interactions to a model.  Predictors or interactions with negligible contributions to the model will have 
    high p-values while those with more contributions will have low p-values. 
    """

    algo = "anovaglm"
    supervised_learning = True

    def __init__(self,
                 model_id=None,  # type: Optional[Union[None, str, H2OEstimator]]
                 training_frame=None,  # type: Optional[Union[None, str, H2OFrame]]
                 seed=-1,  # type: int
                 response_column=None,  # type: Optional[str]
                 ignored_columns=None,  # type: Optional[List[str]]
                 ignore_const_cols=True,  # type: bool
                 score_each_iteration=False,  # type: bool
                 offset_column=None,  # type: Optional[str]
                 weights_column=None,  # type: Optional[str]
                 family="auto",  # type: Literal["auto", "gaussian", "binomial", "fractionalbinomial", "quasibinomial", "poisson", "gamma", "tweedie", "negativebinomial"]
                 tweedie_variance_power=0.0,  # type: float
                 tweedie_link_power=1.0,  # type: float
                 theta=0.0,  # type: float
                 solver="irlsm",  # type: Literal["auto", "irlsm", "l_bfgs", "coordinate_descent_naive", "coordinate_descent", "gradient_descent_lh", "gradient_descent_sqerr"]
                 missing_values_handling="mean_imputation",  # type: Literal["mean_imputation", "skip", "plug_values"]
                 plug_values=None,  # type: Optional[Union[None, str, H2OFrame]]
                 compute_p_values=True,  # type: bool
                 standardize=True,  # type: bool
                 non_negative=False,  # type: bool
                 max_iterations=0,  # type: int
                 link="family_default",  # type: Literal["family_default", "identity", "logit", "log", "inverse", "tweedie", "ologit"]
                 prior=0.0,  # type: float
                 alpha=None,  # type: Optional[List[float]]
                 lambda_=[0.0],  # type: List[float]
                 lambda_search=False,  # type: bool
                 stopping_rounds=0,  # type: int
                 stopping_metric="auto",  # type: Literal["auto", "deviance", "logloss", "mse", "rmse", "mae", "rmsle", "auc", "aucpr", "lift_top_group", "misclassification", "mean_per_class_error", "custom", "custom_increasing"]
                 early_stopping=False,  # type: bool
                 stopping_tolerance=0.001,  # type: float
                 balance_classes=False,  # type: bool
                 class_sampling_factors=None,  # type: Optional[List[float]]
                 max_after_balance_size=5.0,  # type: float
                 max_runtime_secs=0.0,  # type: float
                 save_transformed_framekeys=False,  # type: bool
                 highest_interaction_term=0,  # type: int
                 nparallelism=4,  # type: int
                 type=0,  # type: int
                 ):
        """
        :param model_id: Destination id for this model; auto-generated if not specified.
               Defaults to ``None``.
        :type model_id: Union[None, str, H2OEstimator], optional
        :param training_frame: Id of the training data frame.
               Defaults to ``None``.
        :type training_frame: Union[None, str, H2OFrame], optional
        :param seed: Seed for pseudo random number generator (if applicable)
               Defaults to ``-1``.
        :type seed: int
        :param response_column: Response variable column.
               Defaults to ``None``.
        :type response_column: str, optional
        :param ignored_columns: Names of columns to ignore for training.
               Defaults to ``None``.
        :type ignored_columns: List[str], optional
        :param ignore_const_cols: Ignore constant columns.
               Defaults to ``True``.
        :type ignore_const_cols: bool
        :param score_each_iteration: Whether to score during each iteration of model training.
               Defaults to ``False``.
        :type score_each_iteration: bool
        :param offset_column: Offset column. This will be added to the combination of columns before applying the link
               function.
               Defaults to ``None``.
        :type offset_column: str, optional
        :param weights_column: Column with observation weights. Giving some observation a weight of zero is equivalent
               to excluding it from the dataset; giving an observation a relative weight of 2 is equivalent to repeating
               that row twice. Negative weights are not allowed. Note: Weights are per-row observation weights and do
               not increase the size of the data frame. This is typically the number of times a row is repeated, but
               non-integer values are supported as well. During training, rows with higher weights matter more, due to
               the larger loss function pre-factor. If you set weight = 0 for a row, the returned prediction frame at
               that row is zero and this is incorrect. To get an accurate prediction, remove all rows with weight == 0.
               Defaults to ``None``.
        :type weights_column: str, optional
        :param family: Family. Use binomial for classification with logistic regression, others are for regression
               problems.
               Defaults to ``"auto"``.
        :type family: Literal["auto", "gaussian", "binomial", "fractionalbinomial", "quasibinomial", "poisson", "gamma",
               "tweedie", "negativebinomial"]
        :param tweedie_variance_power: Tweedie variance power
               Defaults to ``0.0``.
        :type tweedie_variance_power: float
        :param tweedie_link_power: Tweedie link power
               Defaults to ``1.0``.
        :type tweedie_link_power: float
        :param theta: Theta
               Defaults to ``0.0``.
        :type theta: float
        :param solver: AUTO will set the solver based on given data and the other parameters. IRLSM is fast on on
               problems with small number of predictors and for lambda-search with L1 penalty, L_BFGS scales better for
               datasets with many columns.
               Defaults to ``"irlsm"``.
        :type solver: Literal["auto", "irlsm", "l_bfgs", "coordinate_descent_naive", "coordinate_descent",
               "gradient_descent_lh", "gradient_descent_sqerr"]
        :param missing_values_handling: Handling of missing values. Either MeanImputation, Skip or PlugValues.
               Defaults to ``"mean_imputation"``.
        :type missing_values_handling: Literal["mean_imputation", "skip", "plug_values"]
        :param plug_values: Plug Values (a single row frame containing values that will be used to impute missing values
               of the training/validation frame, use with conjunction missing_values_handling = PlugValues)
               Defaults to ``None``.
        :type plug_values: Union[None, str, H2OFrame], optional
        :param compute_p_values: Request p-values computation, p-values work only with IRLSM solver and no
               regularization
               Defaults to ``True``.
        :type compute_p_values: bool
        :param standardize: Standardize numeric columns to have zero mean and unit variance
               Defaults to ``True``.
        :type standardize: bool
        :param non_negative: Restrict coefficients (not intercept) to be non-negative
               Defaults to ``False``.
        :type non_negative: bool
        :param max_iterations: Maximum number of iterations
               Defaults to ``0``.
        :type max_iterations: int
        :param link: Link function.
               Defaults to ``"family_default"``.
        :type link: Literal["family_default", "identity", "logit", "log", "inverse", "tweedie", "ologit"]
        :param prior: Prior probability for y==1. To be used only for logistic regression iff the data has been sampled
               and the mean of response does not reflect reality.
               Defaults to ``0.0``.
        :type prior: float
        :param alpha: Distribution of regularization between the L1 (Lasso) and L2 (Ridge) penalties. A value of 1 for
               alpha represents Lasso regression, a value of 0 produces Ridge regression, and anything in between
               specifies the amount of mixing between the two. Default value of alpha is 0 when SOLVER = 'L-BFGS'; 0.5
               otherwise.
               Defaults to ``None``.
        :type alpha: List[float], optional
        :param lambda_: Regularization strength
               Defaults to ``[0.0]``.
        :type lambda_: List[float]
        :param lambda_search: Use lambda search starting at lambda max, given lambda is then interpreted as lambda min
               Defaults to ``False``.
        :type lambda_search: bool
        :param stopping_rounds: Early stopping based on convergence of stopping_metric. Stop if simple moving average of
               length k of the stopping_metric does not improve for k:=stopping_rounds scoring events (0 to disable)
               Defaults to ``0``.
        :type stopping_rounds: int
        :param stopping_metric: Metric to use for early stopping (AUTO: logloss for classification, deviance for
               regression and anonomaly_score for Isolation Forest). Note that custom and custom_increasing can only be
               used in GBM and DRF with the Python client.
               Defaults to ``"auto"``.
        :type stopping_metric: Literal["auto", "deviance", "logloss", "mse", "rmse", "mae", "rmsle", "auc", "aucpr", "lift_top_group",
               "misclassification", "mean_per_class_error", "custom", "custom_increasing"]
        :param early_stopping: Stop early when there is no more relative improvement on train or validation (if
               provided).
               Defaults to ``False``.
        :type early_stopping: bool
        :param stopping_tolerance: Relative tolerance for metric-based stopping criterion (stop if relative improvement
               is not at least this much)
               Defaults to ``0.001``.
        :type stopping_tolerance: float
        :param balance_classes: Balance training data class counts via over/under-sampling (for imbalanced data).
               Defaults to ``False``.
        :type balance_classes: bool
        :param class_sampling_factors: Desired over/under-sampling ratios per class (in lexicographic order). If not
               specified, sampling factors will be automatically computed to obtain class balance during training.
               Requires balance_classes.
               Defaults to ``None``.
        :type class_sampling_factors: List[float], optional
        :param max_after_balance_size: Maximum relative size of the training data after balancing class counts (can be
               less than 1.0). Requires balance_classes.
               Defaults to ``5.0``.
        :type max_after_balance_size: float
        :param max_runtime_secs: Maximum allowed runtime in seconds for model training. Use 0 to disable.
               Defaults to ``0.0``.
        :type max_runtime_secs: float
        :param save_transformed_framekeys: true to save the keys of transformed predictors and interaction column.
               Defaults to ``False``.
        :type save_transformed_framekeys: bool
        :param highest_interaction_term: Limit the number of interaction terms, if 2 means interaction between 2 columns
               only, 3 for three columns and so on...  Default to 2.
               Defaults to ``0``.
        :type highest_interaction_term: int
        :param nparallelism: Number of models to build in parallel.  Default to 4.  Adjust according to your system.
               Defaults to ``4``.
        :type nparallelism: int
        :param type: Refer to the SS type 1, 2, 3, or 4.  We are currently only supporting 3
               Defaults to ``0``.
        :type type: int
        """
        super(H2OANOVAGLMEstimator, self).__init__()
        self._parms = {}
        self._id = self._parms['model_id'] = model_id
        self.training_frame = training_frame
        self.seed = seed
        self.response_column = response_column
        self.ignored_columns = ignored_columns
        self.ignore_const_cols = ignore_const_cols
        self.score_each_iteration = score_each_iteration
        self.offset_column = offset_column
        self.weights_column = weights_column
        self.family = family
        self.tweedie_variance_power = tweedie_variance_power
        self.tweedie_link_power = tweedie_link_power
        self.theta = theta
        self.solver = solver
        self.missing_values_handling = missing_values_handling
        self.plug_values = plug_values
        self.compute_p_values = compute_p_values
        self.standardize = standardize
        self.non_negative = non_negative
        self.max_iterations = max_iterations
        self.link = link
        self.prior = prior
        self.alpha = alpha
        self.lambda_ = lambda_
        self.lambda_search = lambda_search
        self.stopping_rounds = stopping_rounds
        self.stopping_metric = stopping_metric
        self.early_stopping = early_stopping
        self.stopping_tolerance = stopping_tolerance
        self.balance_classes = balance_classes
        self.class_sampling_factors = class_sampling_factors
        self.max_after_balance_size = max_after_balance_size
        self.max_runtime_secs = max_runtime_secs
        self.save_transformed_framekeys = save_transformed_framekeys
        self.highest_interaction_term = highest_interaction_term
        self.nparallelism = nparallelism
        self.type = type
        self._parms["_rest_version"] = 3

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``Union[None, str, H2OFrame]``.
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')

    @property
    def seed(self):
        """
        Seed for pseudo random number generator (if applicable)

        Type: ``int``, defaults to ``-1``.
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed

    @property
    def response_column(self):
        """
        Response variable column.

        Type: ``str``.
        """
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column

    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns

    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``, defaults to ``True``.
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols

    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``, defaults to ``False``.
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration

    @property
    def offset_column(self):
        """
        Offset column. This will be added to the combination of columns before applying the link function.

        Type: ``str``.
        """
        return self._parms.get("offset_column")

    @offset_column.setter
    def offset_column(self, offset_column):
        assert_is_type(offset_column, None, str)
        self._parms["offset_column"] = offset_column

    @property
    def weights_column(self):
        """
        Column with observation weights. Giving some observation a weight of zero is equivalent to excluding it from the
        dataset; giving an observation a relative weight of 2 is equivalent to repeating that row twice. Negative
        weights are not allowed. Note: Weights are per-row observation weights and do not increase the size of the data
        frame. This is typically the number of times a row is repeated, but non-integer values are supported as well.
        During training, rows with higher weights matter more, due to the larger loss function pre-factor. If you set
        weight = 0 for a row, the returned prediction frame at that row is zero and this is incorrect. To get an
        accurate prediction, remove all rows with weight == 0.

        Type: ``str``.
        """
        return self._parms.get("weights_column")

    @weights_column.setter
    def weights_column(self, weights_column):
        assert_is_type(weights_column, None, str)
        self._parms["weights_column"] = weights_column

    @property
    def family(self):
        """
        Family. Use binomial for classification with logistic regression, others are for regression problems.

        Type: ``Literal["auto", "gaussian", "binomial", "fractionalbinomial", "quasibinomial", "poisson", "gamma",
        "tweedie", "negativebinomial"]``, defaults to ``"auto"``.
        """
        return self._parms.get("family")

    @family.setter
    def family(self, family):
        assert_is_type(family, None, Enum("auto", "gaussian", "binomial", "fractionalbinomial", "quasibinomial", "poisson", "gamma", "tweedie", "negativebinomial"))
        self._parms["family"] = family

    @property
    def tweedie_variance_power(self):
        """
        Tweedie variance power

        Type: ``float``, defaults to ``0.0``.
        """
        return self._parms.get("tweedie_variance_power")

    @tweedie_variance_power.setter
    def tweedie_variance_power(self, tweedie_variance_power):
        assert_is_type(tweedie_variance_power, None, numeric)
        self._parms["tweedie_variance_power"] = tweedie_variance_power

    @property
    def tweedie_link_power(self):
        """
        Tweedie link power

        Type: ``float``, defaults to ``1.0``.
        """
        return self._parms.get("tweedie_link_power")

    @tweedie_link_power.setter
    def tweedie_link_power(self, tweedie_link_power):
        assert_is_type(tweedie_link_power, None, numeric)
        self._parms["tweedie_link_power"] = tweedie_link_power

    @property
    def theta(self):
        """
        Theta

        Type: ``float``, defaults to ``0.0``.
        """
        return self._parms.get("theta")

    @theta.setter
    def theta(self, theta):
        assert_is_type(theta, None, numeric)
        self._parms["theta"] = theta

    @property
    def solver(self):
        """
        AUTO will set the solver based on given data and the other parameters. IRLSM is fast on on problems with small
        number of predictors and for lambda-search with L1 penalty, L_BFGS scales better for datasets with many columns.

        Type: ``Literal["auto", "irlsm", "l_bfgs", "coordinate_descent_naive", "coordinate_descent",
        "gradient_descent_lh", "gradient_descent_sqerr"]``, defaults to ``"irlsm"``.
        """
        return self._parms.get("solver")

    @solver.setter
    def solver(self, solver):
        assert_is_type(solver, None, Enum("auto", "irlsm", "l_bfgs", "coordinate_descent_naive", "coordinate_descent", "gradient_descent_lh", "gradient_descent_sqerr"))
        self._parms["solver"] = solver

    @property
    def missing_values_handling(self):
        """
        Handling of missing values. Either MeanImputation, Skip or PlugValues.

        Type: ``Literal["mean_imputation", "skip", "plug_values"]``, defaults to ``"mean_imputation"``.
        """
        return self._parms.get("missing_values_handling")

    @missing_values_handling.setter
    def missing_values_handling(self, missing_values_handling):
        assert_is_type(missing_values_handling, None, Enum("mean_imputation", "skip", "plug_values"))
        self._parms["missing_values_handling"] = missing_values_handling

    @property
    def plug_values(self):
        """
        Plug Values (a single row frame containing values that will be used to impute missing values of the
        training/validation frame, use with conjunction missing_values_handling = PlugValues)

        Type: ``Union[None, str, H2OFrame]``.
        """
        return self._parms.get("plug_values")

    @plug_values.setter
    def plug_values(self, plug_values):
        self._parms["plug_values"] = H2OFrame._validate(plug_values, 'plug_values')

    @property
    def compute_p_values(self):
        """
        Request p-values computation, p-values work only with IRLSM solver and no regularization

        Type: ``bool``, defaults to ``True``.
        """
        return self._parms.get("compute_p_values")

    @compute_p_values.setter
    def compute_p_values(self, compute_p_values):
        assert_is_type(compute_p_values, None, bool)
        self._parms["compute_p_values"] = compute_p_values

    @property
    def standardize(self):
        """
        Standardize numeric columns to have zero mean and unit variance

        Type: ``bool``, defaults to ``True``.
        """
        return self._parms.get("standardize")

    @standardize.setter
    def standardize(self, standardize):
        assert_is_type(standardize, None, bool)
        self._parms["standardize"] = standardize

    @property
    def non_negative(self):
        """
        Restrict coefficients (not intercept) to be non-negative

        Type: ``bool``, defaults to ``False``.
        """
        return self._parms.get("non_negative")

    @non_negative.setter
    def non_negative(self, non_negative):
        assert_is_type(non_negative, None, bool)
        self._parms["non_negative"] = non_negative

    @property
    def max_iterations(self):
        """
        Maximum number of iterations

        Type: ``int``, defaults to ``0``.
        """
        return self._parms.get("max_iterations")

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        assert_is_type(max_iterations, None, int)
        self._parms["max_iterations"] = max_iterations

    @property
    def link(self):
        """
        Link function.

        Type: ``Literal["family_default", "identity", "logit", "log", "inverse", "tweedie", "ologit"]``, defaults to
        ``"family_default"``.
        """
        return self._parms.get("link")

    @link.setter
    def link(self, link):
        assert_is_type(link, None, Enum("family_default", "identity", "logit", "log", "inverse", "tweedie", "ologit"))
        self._parms["link"] = link

    @property
    def prior(self):
        """
        Prior probability for y==1. To be used only for logistic regression iff the data has been sampled and the mean
        of response does not reflect reality.

        Type: ``float``, defaults to ``0.0``.
        """
        return self._parms.get("prior")

    @prior.setter
    def prior(self, prior):
        assert_is_type(prior, None, numeric)
        self._parms["prior"] = prior

    @property
    def alpha(self):
        """
        Distribution of regularization between the L1 (Lasso) and L2 (Ridge) penalties. A value of 1 for alpha
        represents Lasso regression, a value of 0 produces Ridge regression, and anything in between specifies the
        amount of mixing between the two. Default value of alpha is 0 when SOLVER = 'L-BFGS'; 0.5 otherwise.

        Type: ``List[float]``.
        """
        return self._parms.get("alpha")

    @alpha.setter
    def alpha(self, alpha):
        # For `alpha` and `lambda` the server reports type float[], while in practice simple floats are also ok
        assert_is_type(alpha, None, numeric, [numeric])
        self._parms["alpha"] = alpha

    @property
    def lambda_(self):
        """
        Regularization strength

        Type: ``List[float]``, defaults to ``[0.0]``.
        """
        return self._parms.get("lambda")

    @lambda_.setter
    def lambda_(self, lambda_):
        assert_is_type(lambda_, None, numeric, [numeric])
        self._parms["lambda"] = lambda_

    @property
    def lambda_search(self):
        """
        Use lambda search starting at lambda max, given lambda is then interpreted as lambda min

        Type: ``bool``, defaults to ``False``.
        """
        return self._parms.get("lambda_search")

    @lambda_search.setter
    def lambda_search(self, lambda_search):
        assert_is_type(lambda_search, None, bool)
        self._parms["lambda_search"] = lambda_search

    @property
    def stopping_rounds(self):
        """
        Early stopping based on convergence of stopping_metric. Stop if simple moving average of length k of the
        stopping_metric does not improve for k:=stopping_rounds scoring events (0 to disable)

        Type: ``int``, defaults to ``0``.
        """
        return self._parms.get("stopping_rounds")

    @stopping_rounds.setter
    def stopping_rounds(self, stopping_rounds):
        assert_is_type(stopping_rounds, None, int)
        self._parms["stopping_rounds"] = stopping_rounds

    @property
    def stopping_metric(self):
        """
        Metric to use for early stopping (AUTO: logloss for classification, deviance for regression and anonomaly_score
        for Isolation Forest). Note that custom and custom_increasing can only be used in GBM and DRF with the Python
        client.

        Type: ``Literal["auto", "deviance", "logloss", "mse", "rmse", "mae", "rmsle", "auc", "aucpr", "lift_top_group",
        "misclassification", "mean_per_class_error", "custom", "custom_increasing"]``, defaults to ``"auto"``.
        """
        return self._parms.get("stopping_metric")

    @stopping_metric.setter
    def stopping_metric(self, stopping_metric):
        assert_is_type(stopping_metric, None, Enum("auto", "deviance", "logloss", "mse", "rmse", "mae", "rmsle", "auc", "aucpr", "lift_top_group", "misclassification", "mean_per_class_error", "custom", "custom_increasing"))
        self._parms["stopping_metric"] = stopping_metric

    @property
    def early_stopping(self):
        """
        Stop early when there is no more relative improvement on train or validation (if provided).

        Type: ``bool``, defaults to ``False``.
        """
        return self._parms.get("early_stopping")

    @early_stopping.setter
    def early_stopping(self, early_stopping):
        assert_is_type(early_stopping, None, bool)
        self._parms["early_stopping"] = early_stopping

    @property
    def stopping_tolerance(self):
        """
        Relative tolerance for metric-based stopping criterion (stop if relative improvement is not at least this much)

        Type: ``float``, defaults to ``0.001``.
        """
        return self._parms.get("stopping_tolerance")

    @stopping_tolerance.setter
    def stopping_tolerance(self, stopping_tolerance):
        assert_is_type(stopping_tolerance, None, numeric)
        self._parms["stopping_tolerance"] = stopping_tolerance

    @property
    def balance_classes(self):
        """
        Balance training data class counts via over/under-sampling (for imbalanced data).

        Type: ``bool``, defaults to ``False``.
        """
        return self._parms.get("balance_classes")

    @balance_classes.setter
    def balance_classes(self, balance_classes):
        assert_is_type(balance_classes, None, bool)
        self._parms["balance_classes"] = balance_classes

    @property
    def class_sampling_factors(self):
        """
        Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling factors will
        be automatically computed to obtain class balance during training. Requires balance_classes.

        Type: ``List[float]``.
        """
        return self._parms.get("class_sampling_factors")

    @class_sampling_factors.setter
    def class_sampling_factors(self, class_sampling_factors):
        assert_is_type(class_sampling_factors, None, [float])
        self._parms["class_sampling_factors"] = class_sampling_factors

    @property
    def max_after_balance_size(self):
        """
        Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes.

        Type: ``float``, defaults to ``5.0``.
        """
        return self._parms.get("max_after_balance_size")

    @max_after_balance_size.setter
    def max_after_balance_size(self, max_after_balance_size):
        assert_is_type(max_after_balance_size, None, float)
        self._parms["max_after_balance_size"] = max_after_balance_size

    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``, defaults to ``0.0``.
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs

    @property
    def save_transformed_framekeys(self):
        """
        true to save the keys of transformed predictors and interaction column.

        Type: ``bool``, defaults to ``False``.
        """
        return self._parms.get("save_transformed_framekeys")

    @save_transformed_framekeys.setter
    def save_transformed_framekeys(self, save_transformed_framekeys):
        assert_is_type(save_transformed_framekeys, None, bool)
        self._parms["save_transformed_framekeys"] = save_transformed_framekeys

    @property
    def highest_interaction_term(self):
        """
        Limit the number of interaction terms, if 2 means interaction between 2 columns only, 3 for three columns and so
        on...  Default to 2.

        Type: ``int``, defaults to ``0``.
        """
        return self._parms.get("highest_interaction_term")

    @highest_interaction_term.setter
    def highest_interaction_term(self, highest_interaction_term):
        assert_is_type(highest_interaction_term, None, int)
        self._parms["highest_interaction_term"] = highest_interaction_term

    @property
    def nparallelism(self):
        """
        Number of models to build in parallel.  Default to 4.  Adjust according to your system.

        Type: ``int``, defaults to ``4``.
        """
        return self._parms.get("nparallelism")

    @nparallelism.setter
    def nparallelism(self, nparallelism):
        assert_is_type(nparallelism, None, int)
        self._parms["nparallelism"] = nparallelism

    @property
    def type(self):
        """
        Refer to the SS type 1, 2, 3, or 4.  We are currently only supporting 3

        Type: ``int``, defaults to ``0``.
        """
        return self._parms.get("type")

    @type.setter
    def type(self, type):
        assert_is_type(type, None, int)
        self._parms["type"] = type


    @property
    def Lambda(self):
        """DEPRECATED. Use ``self.lambda_`` instead"""
        return self._parms["lambda"] if "lambda" in self._parms else None

    @Lambda.setter
    def Lambda(self, value):
        self._parms["lambda"] = value

    def result(self):
        """
        Get result frame that contains information about the model building process like for modelselection and anovaglm.
        :return: the H2OFrame that contains information about the model building process like for modelselection and anovaglm.
        """
        return H2OFrame._expr(expr=ExprNode("result", ASTId(self.key)))._frame(fill_cache=True)
