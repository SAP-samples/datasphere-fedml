from sklearn.cluster import AgglomerativeClustering

def get_estimator(flags):
    clf = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')

    return clf
