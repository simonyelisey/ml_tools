import numpy as np
from scipy.stats import mannwhitneyu, ttest_ind


def mannwhitney_test(x: np.array, y: np.array, alternative: str, alpha: float):
    """
    A nonparametric homogeneity test for independent samples.

    if alternative == 'two-sided':
        H0 - samples have the same distribution
        H1 - samples have different distributions
    if alternative == 'less':
        H0 - x distribution is greater or equal to y distribution
        H1 - x distribution is LESS than y distribution
    if alternative == 'greater':
        H0 - x distribution is less or equal to y distribution
        H1 - x distribution is GREATER than y distribution
    :param x: sample 1
    :param y: sample 2
    :param alternative: alternative hypothesis
    :param alpha: confidence level
    """
    statistic, pvalue = mannwhitneyu(x=x, y=y, alternative=alternative)
    print(f"Statistic={statistic}, p-value={pvalue}.\n")
    if pvalue >= alpha:
        print(f"Fail to reject H0.")
    else:
        print(f"Reject H0 in favor of H1.")


def student_test_ind(x: np.array, y: np.array, alternative: str, alpha: float, equal_var=False):
    """
    A parametric homogeneity test for independent samples.

    if alternative == 'two-sided':
        H0 - samples have the identical average values
        H1 - samples have unequal mean values
    if alternative == 'less':
        H0 - the mean of x distribution is greater or equal to the mean of y distribution
        H1 - the mean of x distribution is LESS than the mean of y distribution
    if alternative == 'greater':
        H0 - the mean of x distribution is less or equal to the mean of y distribution
        H1 - the mean of x distribution is GREATER than the mean of y distribution
    :param x: sample 1
    :param y: sample 2
    :param alternative: alternative hypothesis
    :param alpha: confidence level
    :param equal_var: whether the variance of two samples are identical
    """
    statistic, pvalue = ttest_ind(a=x, b=y, alternative=alternative, equal_var=equal_var)
    print(f"Statistic={statistic}, p-value={pvalue}.\n")
    if pvalue >= alpha:
        print(f"Fail to reject H0.")
    else:
        print(f"Reject H0 in favor of H1.")
