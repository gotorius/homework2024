def homework(path_winequality_data, n):
    data = pd.read_csv(path_winequality_data, sep=';')
    data_sub = data[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality']]
    sc = StandardScaler()
    sc.fit(data_sub)
    normalized_data = sc.transform(data_sub)
    kmeans = KMeans(init='k-means++', n_clusters=n, random_state=0)
    clusters = kmeans.fit_predict(normalized_data)
    true_result = np.array([np.sum(clusters == i) for i in range(n)])
    return true_result
