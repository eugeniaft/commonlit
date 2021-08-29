from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def get_bow(corpus, bow_type, ngram_range=(1, 1), tokenizer=None):

    '''
    Converts corpus into matrix of token counts using sklearn
    implementation. bow_type options include: tf-idf,
    binarized (binarized counts of tokens), or count.
    Returns matrix and vectorizer instance
    '''

    if bow_type == 'tf-idf':
        vectorizer = TfidfVectorizer(ngram_range=ngram_range,
                                     tokenizer=tokenizer)
    if bow_type == 'binarized':
        vectorizer = CountVectorizer(ngram_range=ngram_range,
                                     tokenizer=tokenizer,
                                     binary=True)
    if bow_type == 'count':
        vectorizer = CountVectorizer(ngram_range=ngram_range,
                                     tokenizer=tokenizer)

    X = vectorizer.fit_transform(corpus)

    return X, vectorizer


if __name__ == "__main__":

    corpus = ['test 1', 'test 2']
    X, vectorizer = get_bow(corpus, 'count')
    print(X.toarray())
