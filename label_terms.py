from tqdm import tqdm
import pandas as pd
import os
import re


def get_data(terms_file):
    with open(terms_file) as f:
        terms = f.read().splitlines()
    return os.listdir('books'), terms


def replace_term(term, cat, text):
    clean_text = ' '.join(re.findall('\w{2,}', text))
    return clean_text.replace(
        ' ' + term + ' ',
        ' ' + term + '_' + cat + ' ')


def main_replace(list_books, terms):
    for b in tqdm(range(len(list_books))):
        name = list_books[b]
        ctg = df_books[df_books.gutenberg_id == int(name.strip('.txt'))].clave
        with open('books/' + name) as f:
            book_aux = f.read()
        for t in terms:
            book_aux = replace_term(t, ctg.iloc[0], book_aux)
        with open('books_labeled/' + name, 'w') as f:
            f.write(book_aux)


if __name__ == '__main__':
    df_books = pd.read_csv('params/df_libros.csv')
    list_books, terms = get_data('params/terms.txt')
    main_replace(list_books, terms)
