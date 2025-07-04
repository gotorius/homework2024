def homework(url_winequality_data, n):        
    data = pd.read_csv(url_winequality_data, sep=';')
    data['va_group'] = pd.qcut(data['volatile acidity'], q=n, duplicates='drop')
    avg_alcohols = data[data['quality'] == 5].groupby('va_group')['alcohol'].mean()
    return avg_alcohols.min()
