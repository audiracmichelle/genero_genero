import multiprocessing
import gensim
import time
import os


def iter_docs(doc_dir):
    doc_list = os.listdir(doc_dir)
    # Generator for reading files
    for file_name in doc_list:
        with open(doc_dir + '/' + file_name) as f:
            lines = gensim.models.word2vec.LineSentence(f)
            for l in lines:
                yield l


def init_w2v_model():
    # create a w2v learner
    basemodel = gensim.models.Word2Vec(
        workers=multiprocessing.cpu_count(),  # use your cores
        iter=50,
        size=300,
        window=5)
    return basemodel


def train_w2v(doc_dir, t):
    print('Initiating Word2Vec model (%4.3f s)' % (time.time() - t))
    w2v = init_w2v_model()
    print('Building vocabulary (%4.3f s)' % (time.time() - t))
    w2v.build_vocab(iter_docs(doc_dir))
    print('Training Word2Vec model (%4.3f s)' % (time.time() - t))
    w2v.train(
        iter_docs(doc_dir),
        total_examples=w2v.corpus_count,
        epochs=100)
    return w2v


def main_w2v(doc_dir):
    t = time.time()
    print(
        'Generating sentences from',
        len(os.listdir(doc_dir)),
        'docs')
    ge_w2v = train_w2v(doc_dir, t)
    print('Saving model (%4.3f s)' % (time.time() - t))
    ge_w2v.save('models/labeled_w2v.model')
    print('Saving word embeddings (%4.3f s)' % (time.time() - t))
    ge_w2v.wv.save_word2vec_format('models/wv_labeled.txt', binary=False)
    elapsed = time.time() - t
    print("Total exec time: %4.3f s", elapsed)
    return ge_w2v


if __name__ == '__main__':
    ge_w2v = main_w2v('books_labeled')
