def treat_outliers_if(data: pd.DataFrame, target: str, date_col: str, test_dates: list, scaler, outlier_detector):
    """
    The function detects outliers in time series using IsolationForest algorithm and treats it:
        - if outlier's index == 0 - change it to the mean of next 6 months
        - if outlier's index == -1 - change it to the mean of previous 6 months
        - else - replace it to nan and interpolate

    :param data: pd.DataFrame treat to
    :param target: str name of target treat to
    :param date_col: str name of date column
    :param test_dates: list test part dates don't treat to
    :param scaler: data scaler
    :param outlier_detector: model detect the outliers to
    :return: pd.DataFrame treated target with
    """
    whole_data = data.copy().reset_index(drop=True)
    data_to_treat = whole_data.loc[whole_data[date_col] < test_dates[0], target]
    scaled = scaler.fit_transform(data_to_treat[target].values.reshape(-1, 1))
    # detection
    outlier_detector.fit(scaled)
    prediction = outlier_detector.predict(scaled)
    data_to_treat['outlier'] = prediction
    # treatment
    data_to_treat.loc[(data_to_treat['outlier'] == -1) & (data_to_treat.index == 0),
                      target] = data_to_treat.iloc[1:7, :][target].mean()
    data_to_treat.loc[(data_to_treat['outlier'] == -1) & (data_to_treat.index == data_to_treat.index[-1]),
                      target] = data_to_treat.iloc[-7:-1][target].mean()
    data_to_treat.loc[(data_to_treat['outlier'] == -1) & (data_to_treat.index != data_to_treat.index[-1])
                      & (data_to_treat.index != 0), target] = np.nan
    data_to_treat[target] = data_to_treat[target].interpolate()
    # replace data to treated data
    whole_data.loc[data_to_treat.index.values, target] = data_to_treat[target]

    return whole_data
  
