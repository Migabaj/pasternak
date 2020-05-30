# Стилометрия русских стихотворных переводов первой половины XX в.

Данный репозиторий содержит в себе материалы, которые были использованы в исследовании для курсовой работы Михаила Сонькина под руководительством к.ф.н. Б. В. Орехова.

## corpora
В этой папке находятся все текстовые файлы собранного корпуса русских стихотворных переводов первой половины XX века + некоторые собрания стихотворений.

### source_corpus
Изначально собранный корпус

### pasternak_shakespeare
Корпус пастернаковских переводов Шекспира и аналогичных переводов других переводчиков.

### faustus
Переводы "Фауста" Пастернаком и Холодковским.

### POS_corpus
Корпус граммем, соответствующих переводам.

## data
Здесь содержатся данные 

## code
В этой папке содержится код, который был написан для исследования. В ней можно найти № файла.

### morphology.py
Код, разработанный для составления набора файлов с морфологическим анализом словоформ текста. Итоговые файлы содержатся в папке *POS_corpus* внутри *corpora*.

### cleanup.py
Код, очищающий драматические тексты.

### characters.json
Словарь, содержащий в себе список персонажей драматических произведений, имеющихся в корпусе.
