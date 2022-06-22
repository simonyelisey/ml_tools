import numpy as np
from statsmodels.stats.contingency_tables import mcnemar


def mcnemar_test(data: np.array, alpha: float) -> None:
    """
    Test of homogeneity of two variables
    
    H0 - variables have the same distribution
    H1 - variables have a different distributions
    
    :param data: continguency table of two variables
    :param alpha: significant level
    :return: [0] - chi_square statistic
             [1] - p_value
    """
    result = mcnemar(data)
    print(f"McNemar statistic = {result.statistic}")
    print(f"P-value = {result.pvalue}")
    print(f"Alpha = {alpha}")

    if result.pvalue < alpha:
        print('\nVariables have different distributions (reject H0)')
    else:
        print('\nVariables have the same distribution (fail to reject H0)')
