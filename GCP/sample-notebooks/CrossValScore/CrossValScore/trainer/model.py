from sklearn.linear_model import LogisticRegression

def get_estimator(flags):
    clf = LogisticRegression(max_iter=1000)

    return clf
