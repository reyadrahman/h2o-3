from ..estimators.estimator_base import H2OEstimator


class H2OPCA(H2OEstimator):
    """
    Principal Component Analysis
    """
    algo = "pca"

    def __init__(self, model_id=None, k=None, max_iterations=None, seed=None,
                 transform=("NONE", "DEMEAN", "DESCALE", "STANDARDIZE", "NORMALIZE"),
                 use_all_factor_levels=False,
                 pca_method=("GramSVD", "Power", "GLRM"),
                 ignore_const_cols=True,
                 impute_missing=False):
        """
        Principal Components Analysis

        :param str model_id: The unique hex key assigned to the resulting model. Automatically generated if
            none is provided.
        :param int k: The number of principal components to be computed. This must be between ``1`` and
            ``min(ncol(training_frame), nrow(training_frame))`` inclusive.
        :param str transform: A character string that indicates how the training data should be transformed
            before running PCA. Possible values are:

            - ``"NONE"``: for no transformation,
            - ``"DEMEAN"``: for subtracting the mean of each column,
            - ``"DESCALE"``: for dividing by the standard deviation of each column,
            - ``"STANDARDIZE"``: for demeaning and descaling, and
            - ``"NORMALIZE"``: for demeaning and dividing each column by its range (max - min).

        :param int seed: Random seed used to initialize the right singular vectors at the beginning of each
            power method iteration.
        :param int max_iterations: The maximum number of iterations when pca_method is "Power".
        :param bool use_all_factor_levels: A logical value indicating whether all factor levels should be included
            in each categorical column expansion. If False, the indicator column corresponding to the first factor
            level of every categorical variable will be dropped. Default is False.
        :param str pca_method: A character string that indicates how PCA should be calculated. Possible values are:

            - ``"GramSVD"``: distributed computation of the Gram matrix followed by a local SVD using the JAMA package,
            - ``"Power"``: computation of the SVD using the power iteration method,
            - ``"GLRM"``: fit a generalized low rank model with an l2 loss function (no regularization) and solve for
              the SVD using local matrix algebra.

        :returns: A new instance of H2OPCA.
        """
        super(H2OPCA, self).__init__()
        self._parms = locals()
        self._parms = {k: v for k, v in self._parms.items() if k != "self"}
        self._parms["pca_method"] = "GramSVD" if isinstance(pca_method, tuple) else pca_method
        self._parms["transform"] = "NONE" if isinstance(transform, tuple) else transform


    def fit(self, X, y=None, **params):
        return super(H2OPCA, self).fit(X)


    def transform(self, X, y=None, **params):
        """
        Transform the given H2OFrame with the fitted PCA model.

        :param H2OFrame X: May contain NAs and/or categorical data.
        :param H2OFrame y: Ignored for PCA. Should be None.
        :param params: Ignored.

        :returns: The input H2OFrame transformed by the Principal Components.
        """
        return self.predict(X)




class H2OSVD(H2OEstimator):
    """Singular Value Decomposition"""
    algo = "svd"

    def __init__(self, nv=None, max_iterations=None, transform=None, seed=None,
                 use_all_factor_levels=None, svd_method=None):
        """
        Singular value decomposition of an H2OFrame.

        :param int nv: The number of right singular vectors to be computed. This must be between 1 and
            min(ncol(training_frame), snrow(training_frame)) inclusive.
        :param int max_iterations: The maximum number of iterations to run each power iteration loop. Must be
            between 1 and 1e6 inclusive.
        :param str transform: A character string that indicates how the training data should be transformed
            before running SVD. Possible values are:

            - ``"NONE"``: for no transformation,
            - ``"DEMEAN"``: for subtracting the mean of each column,
            - ``"DESCALE"``: for dividing by the standard deviation of each column,
            - ``"STANDARDIZE"``: for demeaning and descaling, and
            - ``"NORMALIZE"``: for demeaning and dividing each column by its range (max - min).

        :param int seed: Random seed used to initialize the right singular vectors at the beginning of each
            power method iteration.
        :param bool use_all_factor_levels: A logical value indicating whether all factor levels should be included
            in each categorical column expansion. If False, the indicator column corresponding to the first factor
            level of every categorical variable will be dropped. Defaults to True.
        :param str svd_method: A character string that indicates how SVD should be calculated. Possible values are:

            - ``"GramSVD"``: distributed computation of the Gram matrix followed by a local SVD
              using the JAMA package,
            - ``"Power"``: computation of the SVD using the power iteration method,
            - ``"Randomized"``: approximate SVD by projecting onto a random subspace.

        :returns: a new H2OSVD model
        """
        super(H2OSVD, self).__init__()
        self._parms = locals()
        self._parms = {k: v for k, v in self._parms.items() if k != "self"}
        self._parms["svd_method"] = "GramSVD" if isinstance(svd_method, tuple) else svd_method
        self._parms["transform"] = "NONE" if isinstance(transform, tuple) else transform
        self._parms['_rest_version'] = 99


    def fit(self, X, y=None, **params):
        return super(H2OSVD, self).fit(X)


    def transform(self, X, y=None, **params):
        """
        Transform the given H2OFrame with the fitted SVD model.

        :param H2OFrame X: May contain NAs and/or categorical data.
        :param H2OFrame y: Ignored for SVD. Should be None.
        :param params: Ignored.

        :returns: The input H2OFrame transformed by the SVD.
        """
        return self.predict(X)
