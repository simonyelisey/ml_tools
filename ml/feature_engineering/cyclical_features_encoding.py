import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def transform_cyclical_features(data: pd.DataFrame, date_cols: list):
    """
    Cyclical features transformation to two dimensions using sin and cos transformations.

        - xsin = SIN((2 * pi * x) / max(x))
        - xcos = COS((2 * pi * x) / max(x))

    :param data: pd.DataFrame with cyclical features
    :param date_cols: list of cyclical features to transform

    :return: pd.DataFrame with sin-cos transformed features
    """
    dataframe = data.copy()
    # transformation
    for col in date_cols:
        dataframe[f"sin_{col}"] = np.sin((2 * np.pi * dataframe[col]) / max(dataframe[col]))
        dataframe[f"cos_{col}"] = np.cos((2 * np.pi * dataframe[col]) / max(dataframe[col]))
    # drop old features
    dataframe.drop(date_cols, axis=1, inplace=True)

    return dataframe


def visualize_cyclical_transformation(data: pd.DataFrame, transformed_cols: list):
    """
    Visualisation of sin & cos transformed cyclical features.

    :param data: pd.DataFrame with sin cos transformed features
    :param transformed_cols: list of transformed features
    """
    plt.figure(figsize=(4, 4))
    sns.scatterplot(data.loc[:, transformed_cols[0]], data.loc[:, transformed_cols[1]])
    plt.title('Visualisation of sin & cos transformed cyclical feature.\n')
    plt.show()
