import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import gc

def chi2_feature_selection(dataframe: pd.DataFrame, cat_features: list, target: np.array, alpha: float) -> list:
    """
    The function determines independent features from the target variable.

    H0 - feature and target variable are independent(feature is not important)
    H1 - feature and target variable are dependent(feature is important)
    
    :param dataframe: pd.DataFrame to select the features
    :param cat_features: list of categorical features
    :param target: np.array target variable
    :param alpha: significant level
    :return: list of features which are independent from the target variable
    """
    unimportant_cols = []
    for col in cat_features:
      data = pd.crosstab(dataframe[col], target)
      stat, p, dof, expected = chi2_contingency(data)
      if p > alpha: # Variables are independent (fail to reject H0)
        unimportant_cols.append(col)

      del data, stat, p, dof, expected
    gc.collect()
    print(f"There are(is) {len(unimportant_cols)} unimportant cols.")

    return unimportant_cols
