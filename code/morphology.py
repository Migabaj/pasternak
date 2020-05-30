import os
from nltk import word_tokenize
from pymorphy2 import MorphAnalyzer
m = MorphAnalyzer()

corpuspath = "../corpora/stylo_corpus/"
files = os.listdir(corpuspath)

def main():
    for i, file in enumerate(files):
        # извлечение текстового файла, токенизация
        with open(corpuspath+file, encoding="utf-8") as f:
            text = f.read()
        words = word_tokenize(text)

        # парсинг каждого токена, модификация новых "слов"
        morph_text = ""
        for word in words:
            parsed = str(m.parse(word)[0].tag).replace(",", "И")
            parsed = parsed.replace("1", "FIRST")
            parsed = parsed.replace("2", "SCND")
            parsed = parsed.replace("3", "THIRD")
            morph_text += parsed+" "

        # записывание полученного набора граммем в файл
        with open(f'../corpora/POS_corpus/{file}', 'w', encoding="utf-8") as fw:
            fw.write(morph_text)

if __name__ == "__main__":
    main()
