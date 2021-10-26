from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def get_estimator(flags):
    vectorizer = TfidfVectorizer()
    naive_bayes_classifier = MultinomialNB()
    pipeline = Pipeline([('vectorizer', vectorizer), ('naiveBayes', naive_bayes_classifier)])

    return pipeline
