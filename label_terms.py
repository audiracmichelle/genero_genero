from tqdm import tqdm
import pandas as pd
import os
import re

df_books = pd.read_csv('params/df_libros.csv')
with open('params/terms.txt') as f:
    terms = f.read().splitlines()

list_books = os.listdir('books')


def replace_term(term, cat, text):
    clean_text = ' '.join(re.findall('\w{2,}', text))
    return clean_text.replace(
        ' ' + term + ' ',
        ' ' + term + '_' + cat + ' ')


for b in tqdm(range(len(list_books))):
    name = list_books[b]
    ctg = df_books[df_books.gutenberg_id == int(name.strip('.txt'))].clave
    with open('books/' + name) as f:
        book_aux = f.read()
    for t in terms:
        book_aux = replace_term(t, ctg.iloc[0], book_aux)
    with open('books_labeled/' + name, 'w') as f:
        f.write(book_aux)
