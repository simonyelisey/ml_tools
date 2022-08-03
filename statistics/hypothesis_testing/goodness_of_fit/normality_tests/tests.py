import numpy as np
from scipy.stats import shapiro, jarque_bera


def shapiro_test(data: np.array, alpha: float):
    """
    The Shapiro-Wilk normality test.

    P-value may not be accurate for N > 5000.

    H0 - the distribution of variable is normal
    H1 - the distribution of variable is NOT normal

    :param data: sample data
    :param alpha: significant level
    """
    statistic, pvalue = shapiro(data)
    print(f"Statistic={statistic}, p-value={pvalue}.\n")
    if pvalue <= alpha:
        print(f"The distribution of variable is NOT normal (reject H0).")
    else:
        print(f"The distribution of variable is normal (fail to reject H0).")


def jarque_bera_test(data: np.array, alpha: float):
    """
    The Jarque-Bera normality test.

    It tests whether the sample data has the skewness and kurtosis matching a normal distribution.
    This test only works for a large enough number of data samples (>2000).

    H0 - the distribution of variable is normal
    H1 - the distribution of variable is NOT normal

    :param data: sample data
    :param alpha: significant level
    """
    statistic, pvalue = jarque_bera(data)
    print(f"Statistic={statistic}, p-value={pvalue}.\n")
    if pvalue <= alpha:
        print(f"The distribution of variable is NOT normal (reject H0).")
    else:
        print(f"The distribution of variable is normal (fail to reject H0).")
