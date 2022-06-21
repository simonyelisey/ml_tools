def non_informative_features(dataframe: pd.DataFrame, threshold: float) -> list:
  """
  Function finds non-informative features.
  
  param: dataframe - pd.DataFrame where to search low informative features
  param: treshold - float of the minimum proportion of constant values in a feature to consider the feature to be non-informative
  return: list of non-informative features
  
  """
  low_inf_feat = []

  for col in dataframe.columns:
      vc = dataframe[col].value_counts()
      first_value_proportion = vc.values[0] / dataframe.shape[0]

      if first_value_proportion >= threshold:
          low_inf_feat.append(col)

  if len(low_inf_feat) == 0:
      print('There is NO low informative features in dataframe.')
  else:
      print(f'There is(are) {len(low_inf_feat)} low informative feature(s).')

      return low_inf_feat
