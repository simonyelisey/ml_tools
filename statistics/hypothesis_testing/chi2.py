import numpy as np
from scipy.stats import chi2_contingency


def chi2_test(data: np.array, alpha: float) -> None:
    """
    H0 - variables in contingency table are independent
    H1 - variables in contingency table are dependent
    
    :param data: contingency table
    :param alpha: significant level
    :return: [0] - chi_square statistic
             [1] - p_value
    """

    stat, p, dof, expected = chi2_contingency(data)
    print(f"Chi-square statistic = {stat}")
    print(f"P-value = {p}")
    print(f"Alpha = {alpha}")

    if p < alpha:
        print('\nVariables are dependent (reject H0).')
    else:
        print('\nVariables are independent (fail to reject H0).')
