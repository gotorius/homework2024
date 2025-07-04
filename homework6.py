def homework(path_winequality_data, X_column, Y_column):

    df = pd.read_csv(path_winequality_data, delimiter=';')

    x = df[X_column].values
    y = df[Y_column].values

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    covariance = np.sum((x - x_mean) * (y - y_mean))
    variance = np.sum((x - x_mean) ** 2)

    a = covariance / variance
    b = y_mean - a * x_mean
    y_pred = a * x + b

    ss_total = np.sum((y - y_mean) ** 2)
    ss_residual = np.sum((y - y_pred) ** 2)
    r_squared = 1 - (ss_residual / ss_total)
    return r_squared

