import pandas as pd


def reduce_memory(data: pd.DataFrame, dtypes_and_cols: dict):
    """
    The function reduces the memory usage of dataframe by reducing its columns' dtypes

    :param data: dataframe reduce dtypes to
    :param dtypes_and_cols: dict where:
                                       - keys are str names of new dtypes
                                       - values are list of columns reduce dtypes to
    :return: pd.DataFrame with changed dtypes of selected columns
    """
    df = data.copy()
    for dtype in dtypes_and_cols:
        df[dtypes_and_cols[dtype]] = df[dtypes_and_cols[dtype]].astype(dtype)

    return df
  
