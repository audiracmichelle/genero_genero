import os
import pandas as pd
from tqdm import tqdm
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers


def download_gutenberg(gutenberg_id):
    return strip_headers(load_etext(gutenberg_id)).strip()


def download_books(gtn_id):
    gtn_id = list(set(gtn_id) - set(dwnld))
    for i in tqdm(range(len(gtn_id))):
        try:
            with open('books/' + str(gtn_id[i]) + '.txt', 'w') as f:
                f.write(download_gutenberg(gtn_id[i]))
        except:
            print("No se bajó:", gtn_id[i])


if __name__ == '__main__':
    gtn = pd.read_csv('df_libros.csv')
    dwnld = os.listdir('books')
    dwnld = [int(s.strip('.txt')) for s in dwnld]
    gtn_id = gtn.gutenberg_id.unique().tolist()
    download_books(gtn_id)
