from shutil import copyfile
from tqdm import tqdm
import pandas as pd
import os
import re


def get_terms(terms_file):
    with open(terms_file) as f:
        terms = f.read().splitlines()
    return terms


def replace_term(term, cat, text):
    clean_text = ' '.join(re.findall('\w{2,}', text))
    return clean_text.replace(
        ' ' + term + ' ',
        ' ' + term + '_' + cat + ' ')


def main_replace(book_dir, terms):
    list_books = os.listdir(book_dir)
    for b in tqdm(range(len(list_books))):
        name = list_books[b]
        ctg = df_books[df_books.gutenberg_id == int(name.strip('.txt'))].clave
        with open('books/' + name) as f:
            book_aux = f.read()
        for t in terms:
            book_aux = replace_term(t, ctg.iloc[0], book_aux)
        with open('books_labeled/' + name, 'w') as f:
            f.write(book_aux)


def make_cat_dirs():
    cats = df_books.clave.unique().tolist()
    for cat in cats:
        if not os.path.exists('books_divided' + '/' + cat):
            os.makedirs('books_divided' + '/' + cat)


def main_divide(book_dir):
    make_cat_dirs()
    list_books = os.listdir(book_dir)
    for b in tqdm(range(len(list_books))):
        name = list_books[b]
        ctg = df_books[df_books.gutenberg_id == int(name.strip('.txt'))].clave.iloc[0]
        copyfile('books/' + name, 'books_divided/' + ctg + '/' + name)


if __name__ == '__main__':
    df_books = pd.read_csv('params/df_libros.csv')
    terms = get_terms('params/terms.txt')
    book_dir = 'books'
    main_replace(book_dir, terms)
