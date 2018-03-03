from tqdm import tqdm
import pandas as pd
import os

df_books = pd.read_csv('params/df_libros.csv')
with open('params/terms.txt') as f:
    terms = f.read().splitlines()

list_books = os.listdir('books')

for b in tqdm(range(len(list_books))):
    name = list_books[b]
    ctg = df_books[df_books.gutenberg_id == int(name.strip('.txt'))].clave
    with open('books/' + name) as f:
        book_aux = f.read()
    for t in terms:
        book_aux = book_aux.replace(t, t + '_' + ctg.iloc[0])
    with open('books_labeled/books_labels.txt', 'a') as f:
        f.write(book_aux)
