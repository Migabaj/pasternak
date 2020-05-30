# Стилометрия русских стихотворных переводов первой половины XX в.

Данный репозиторий содержит в себе материалы, которые были использованы в исследовании для курсовой работы Михаила Сонькина под руководительством к.ф.н. Б. В. Орехова.

## corpora
В этой папке находятся все текстовые файлы собранного корпуса русских стихотворных переводов первой половины XX века + некоторые собрания стихотворений.

### source_corpus
Изначально собранный корпус

### stylo_corpus
Корпус после чистки некоторых файлов

### POS_corpus
Корпус граммем, соответствующих переводам.

### shakespeare
Корпус, созданный для сравнения переводов Шекспира

### faust
Корпус, созданный для сравнения переводов "Фауста"

### shakespeare_POS
Файлы с набором граммем, соответствующих текстам из *shakespeare*

### faust
Файлы с набором граммем, соответствующих текстам из *faust*

## zscores
Здесь содержатся данные о z-scores из некоторых корпусов.

## code
В этой папке содержится код, который был написан для исследования. В ней можно найти 3 файла.

### morphology.py
Код, разработанный для составления набора файлов с морфологическим анализом словоформ текста. Итоговые файлы содержатся в папке *POS_corpus* внутри *corpora*.

### cleanup.py
Код, очищающий драматические тексты.

### characters.json
Словарь, содержащий в себе список персонажей нескольких драматических произведений, имеющихся в корпусе.
