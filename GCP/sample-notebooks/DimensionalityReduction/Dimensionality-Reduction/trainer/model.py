from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def get_estimator(flags):
    pca = PCA(int(flags.num_components))
    
    pca_pipeline = Pipeline([('scaler', StandardScaler()), ('pca', pca)])
    return pca_pipeline