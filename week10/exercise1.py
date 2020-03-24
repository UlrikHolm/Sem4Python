from urllib.parse import urlparse
import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

urls=['https://www.gutenberg.org/files/1342/1342-0.txt',
'https://www.gutenberg.org/files/1080/1080-0.txt',
'https://www.gutenberg.org/files/215/215-0.txt']

class NotFoundException(Exception):
    pass

class MyClass():
    def __init__(self, url_list=[]):
        self.url_list = url_list
        self.filelist = []
    
    def download(self,url,filename):
        r = requests.get(url)
        if r.status_code == '404':
            raise NotFoundException
        fname = 'book_' + str(filename) + '.txt'
        with open(fname, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)

    def multi_download(self, url_list):
        with ThreadPoolExecutor(5) as ex:
            res = ex.map(self.download,url_list, range(len(url_list)))
        return list(res)


    def __iter__(self):
        return self

    def __next__(self):
        try:
            filename = next(self.filelist)
            with open(filename, encoding='utf8') as file:
                result = file.read()
        except ImportError:
            raise StopIteration
        return result

    def filelist_generator(self, url_list):
            self.filelist = ('book_' + str(n) + '.txt' for n in range(len(url_list)))

    def avg_vowels(self, text): 
        vowels = 'aAeEiIoOuUyY'
        txt_len = len(text.split())
        vowel_count = len([each for each in text if each in vowels])
        avg_vowel = vowel_count/txt_len

        # print('avg vow: ' + str(vowel_count))
        # print('wrds: ' + str(txt_len))
        # print('vwl/wrd: ' + str(avg_vowel))
        return avg_vowel

    def hardest_read(self):
        with multiprocessing.Pool(len(self.url_list)) as pool:
            for file in self.filelist:
                print('filename: ' + file)
                print(self.avg_vowels(file))
        

if __name__ == '__main__':
    #freeze_support()
    print('vi kører!')
    my_class = MyClass(urls)
    #my_class.multi_download(urls)
    my_class.filelist_generator(urls)
    #my_class.avg_vowels(next(my_class))
    my_class.hardest_read()

