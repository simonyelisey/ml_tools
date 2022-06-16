import numpy as np
from scipy.stats import chi2_contingency
from statsmodels.stats.contingency_tables import mcnemar


def chi2_model_eval(data: np.array, alpha: float) -> None:
    """
    Function calculates whether model is random guesser or not.

    H0 - variables in contingency table are independent (model is a random guesser)
    H1 - variables in contingency table are dependent (model is not a random guesser)

    :param data: model's confusion matrix
    :param alpha: significant level
    :return: [0] - chi_square statistic
             [1] - p_value
    """

    stat, p, dof, expected = chi2_contingency(data)
    print(f"Chi-square statistic = {stat}")
    print(f"P-value = {p}")
    print(f"Alpha = {alpha}")

    if p < alpha:
        print('\nModel is Not a random guesser (reject H0).')
    else:
        print('\nModel ia a random guesser (fail to reject H0).')



def mcnemar_comparison(data: np.array, alpha: float) -> None:
    """
    Test of homogeneity of two classifiers

    H0 - classifiers have a similar proportion of errors on the test set
    H1 - classifiers have a different proportion of errors on the test set

    :param data:
    :param alpha: significant level
    :return: [0] - chi_square statistic
             [1] - p_value
    """
    result = mcnemar(data)
    print(f"McNemar statistic = {result.statistic}")
    print(f"P-value = {result.pvalue}")
    print(f"Alpha = {alpha}")

    if result.pvalue < alpha:
        print('\nDifferent proportions of errors (reject H0)')
    else:
        print('\nSame proportions of errors (fail to reject H0)')