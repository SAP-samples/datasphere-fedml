from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def get_estimator(flags):
    n_components=int(flags.n_components)
    pca = PCA(n_components)
    pca_pipeline = Pipeline([('scaler', StandardScaler()), ('pca', pca), ('classifier', LogisticRegression())])

    return pca_pipeline
