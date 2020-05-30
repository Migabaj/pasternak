import json
import os
import re

# json-файл из персонажей
DC = json.load(open("characters.json"))

def drama_clean_up(path, filename):
    
    artpiece = (filename.split('_')[1]+'_'+filename.split('_')[2]).strip('.txt')
    
    if artpiece in DC.keys():
        with open(path+filename, encoding='utf-8') as f:
            text = f.read()

        # очистка от персонажей и ремарок (если они в скобках)
        text = re.sub('\n\d*', '\n', text)
        for char in DC[artpiece]:
            char_regex = f'\s+?(?:(?:[1-5]|Первы|Второ|Трети|Четверты|Пяты)-?й)?\s+?{char}\s+?'
            text = re.sub(char_regex, '\n', text)
        text = re.sub('\(.+?\)', '', text)
        with open("../corpora/clean_corpus/"+filename, 'w', encoding='utf-8') as fw:
            fw.write(text)

def main():
    files = os.listdir('../corpora/stylo_corpus/')
    for file in files:
        drama_clean_up('../corpora/stylo_corpus/', file)

if __name__ == '__main__':
    main()
