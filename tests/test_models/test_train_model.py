import pytest
from commonlit.modeling import train_model


@pytest.fixture
def example_corpus_data():

    return ['First document to test.',
            'This document is the second document to test.',
            'Third document of all the documents to testt.',
            'Testing the FOURTH and final document of all documents!']


def test_get_bow_tfidf(example_corpus_data):

    X, vectorizer = train_model.get_bow(example_corpus_data, 'tf-idf')

    assert isinstance(X.toarray()[1][2], float)


def test_get_bow_count(example_corpus_data):

    X, vectorizer = train_model.get_bow(example_corpus_data, 'count')

    assert list(X.toarray()[1]) == [0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1]


def test_get_bow_binarized(example_corpus_data):

    X, vectorizer = train_model.get_bow(example_corpus_data, 'binarized')

    assert X.toarray()[1][2] == 1


def test_get_bow_ngrams(example_corpus_data):

    X, vectorizer = train_model.get_bow(example_corpus_data,
                                        'binarized',
                                        ngram_range=(1, 2))

    assert X.shape[1] == 38
