# Проект 3. EDA + Feature Engineering. Соревнование на Kaggle

## Оглавление  

[1. Описание проекта](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Краткая-информация-о-данных)

[4. Что практикуем](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Что-практикуем)

[5. Этапы работы над проектом](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Этапы-работы-над-проектом)

[6. Результат](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Результаты) 

### Описание проекта  

Представьте, что вы работаете дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

:arrow_up:[к оглавлению](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Оглавление)

### Задачи проекта

1. ознакомиться с входными данными (датасет с информацией об отелях);
2. изучить пример машинного обучения (scikit-learn класс RandomForestRegressor);
3. выполнить подготовку данных, которые будут использованы для обучения модели;
4. проверить эффективность предлагаемой модели, используя метрику MAPE
5. принять участие в соревновании на площадке в kaggle.com.

:arrow_up:[к оглавлению](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Оглавление)

### Краткая информация о данных

Первоначальная версия датасета содержит 17 полей со следующей информацией:

- hotel_address — адрес отеля;
- review_date — дата, когда рецензент разместил соответствующий отзыв;
- average_score — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
- hotel_name — название отеля;
- reviewer_nationality — страна рецензента;
- negative_review — отрицательный отзыв, который рецензент дал отелю;
- review_total_negative_word_counts — общее количество слов в отрицательном отзыв;
- positive_review — положительный отзыв, который рецензент дал отелю;
- review_total_positive_word_counts — общее количество слов в положительном отзыве;
- reviewer_score — оценка, которую рецензент поставил отелю на основе своего опыта;
- total_number_of_reviews_reviewer_has_given — количество отзывов, которые рецензенты дали в прошлом;
- total_number_of_reviews — общее количество действительных отзывов об отеле;
- tags — теги, которые рецензент дал отелю;
- days_since_review — количество дней между датой проверки и датой очистки;
- additional_number_of_scoring — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв.
- lat — географическая широта отеля;
- lng — географическая долгота отеля.
  
:arrow_up:[к оглавлению](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Оглавление)

### Что практикуем

Создадим и улучшим свою первую модель, основанную на алгоритмах машинного обучения. Примем участие в соревновании на Kaggle.

:arrow_up:[к оглавлению](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Оглавление)

### Этапы работы над проектом  

- знакомство с данными;
- предварительный анализ данных;
- удаление строковых значений;
- очистка от пропущенных значений;
- создание новых признаков;
- преобразование признаков;
- отбор признаков;
- создание модели;
- оценка качества модели с помошью метрики MAPE;
- участие в соревновании на Kaggle.

:arrow_up:[к оглавлению](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Оглавление)

### Результаты:

Модель создана, оценка качества произведена, выводы сделаны.

:arrow_up:[к оглавлению](https://github.com/antonova-ts/SF_DATA_SCIENCE/tree/main/project_3/README.md#Оглавление)
