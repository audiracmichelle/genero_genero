import multiprocessing
import gensim
import time
import os


def iter_books(books_list):
    # Generator for reading files
    for file_name in books_list:
        with open('books_labeled/' + file_name) as f:
            lines = gensim.models.word2vec.LineSentence(f)
            for l in lines:
                yield l


def init_w2v_model():
    # create a w2v learner
    basemodel = gensim.models.Word2Vec(
        workers=multiprocessing.cpu_count(),  # use your cores
        iter=15,
        size=300,
        window=10)
    return basemodel


def train_w2v(books_list):
    print('Initiating Word2Vec model (%4.3f s)' % (time.time() - t))
    w2v = init_w2v_model()
    print('Building vocabulary (%4.3f s)' % (time.time() - t))
    w2v.build_vocab(iter_books(books_list))
    print('Training Word2Vec model (%4.3f s)' % (time.time() - t))
    w2v.train(
        iter_books(books_list),
        total_examples=w2v.corpus_count,
        epochs=15)
    return w2v


def main_w2v(books_dir):
    books_list = os.listdir(books_dir)
    print(
        'Generating sentences from',
        len(books_list),
        'books')
    ge_w2v = train_w2v(books_list)
    print('Saving model (%4.3f s)' % (time.time() - t))
    ge_w2v.save('models/labeled_w2v.model')
    print('Saving word embeddings (%4.3f s)' % (time.time() - t))
    ge_w2v.wv.save_word2vec_format('models/wv_labeled.txt', binary=False)
    elapsed = time.time() - t
    print("Total exec time: %4.3f s", elapsed)
    return ge_w2v


if __name__ == '__main__':
    t = time.time()
    ge_w2v = main_w2v('books_labeled')
