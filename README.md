# Parser for Edvibe

Приложение разработано для преподавателей английского языка, которые работают на онлайн платформе edvibe - 
https://edvibe.com/. Парсер реализован в виде графического приложения на операционной системе windows 10 и windows 11. 
С помощью парсера можно перенести моментально материал с других сайтов таких как skyeng.ru, test-english.com, 
perfect-english-grammar.com, englisch-hilfen.de на платформу edvibe.com. Приложение генерирует автоматически шаблон с 
ответами по стандартам онлайн платформы edvibe. В деталях, приложение принимает html разметку или ссылку на задание, 
обрабатывает этот текст и создает готовый заполненный шаблон с ответами, вопросами и подсказками в зависимости от типа 
задания и сайта, с которого вы переносите материал.

Приложение работает только с выше-перечисленными сайтами. Однако приложение, при желании, легко расширяется. 
Можно добавить в приложение новые задания, шаблоны при крупном обновлении сайтов и даже дополнительные сайты 
с заданиями.

Графическое приложение работает со следующими ссылками.
- https://skyeng.ru/
- https://test-english.com/
- https://www.perfect-english-grammar.com/
- https://www.englisch-hilfen.de/en/
- https://edvibe.com/

## Особенности

* Сохраняет 95% вашего времени.
* Моментальный перенос материала с созданием шаблона задания с ответами, вопросами и подсказками по стандарту edvibe.
* Парсинг 4-х сайтов.
* Все задания относятся к группе `Exercise` или `Grammar`. При желании можно расширить группу. 
Например, добавить группу - лексика, говорение, аудировние и так далее. 

## Один из приятных отзывов преподавателя

> Благодаря этой программе процесс переноса задач с разных сайтов значительно ускорился!
> Программа определенно стала для меня незаменимым помощником.
> Теперь гораздо больше времени для творчества во время подготовки уроков. :)
> ---
>
> *Елена. Преподаватель английского языка*

## Ссылка для скачивания
1) Скачать zip архив https://drive.google.com/file/d/1Cxpkt6M5EY92EcWWHP_VQX7NpN4vHysD/view?usp=share_link
2) Разархивировать
3) Запустить parser.exe

## Небольшой гайд

### Основные шаги

1. Выберите название сайта в меню.
2. Выберите один из типов задания для переноса материала с сайта на Edvibe.
3. Скопируйте HTML-код и вставьте в окно ввода.
   * Откройте devtools, а именно нажмите `Ctrl+Shift+C` или правую кнопку мыши и выберите Исследовать.
   * Выберите блок HTML-кода в соответствии с инструкциями.
   * Скопируйте код, который максимально полно описывает задание.
   * Вставить в окно ввода.
4. Нажмите кнопку _Input_. Вы получите текст в соответствии с вашим заданием.

---

* Для каждого сайта и типа задания требуются соответствующие действия.
* Копировать блок html следует также как в видео, однако блоки html разметки на сайтах разные.
* Вы должны открыть devtools с HTML-кодом `Ctrl+Shift+C` или правой кнопкой мыши, выбрать `Исследовать`.

## Краткая видео-инструкция

https://drive.google.com/file/d/18ylkxTWSF1tfmrYhSwSNUZfQaJt1kCmb/view?usp=sharing

## Skyeng

### Choose the correct option

- Откройте сайт.
- Выберите все правильные ответы.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нажмите *Input* и получите результат.

![Skyeng](example/skyeng/Skyeng%201.choose_the_correct_option.png "choose_the_correct_option")

___

### Choose the correct option from test

- Откройте сайт.
- Выберите все правильные ответы в __test__.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нажмите *Input* и получите результат.

![Skyeng](example/skyeng/Skyeng%202.choose_the_correct_option_from_test.png "choose_the_correct_option_from_test")

___

### Fill the gaps

- Откройте сайт.
- Вставьте все правильные слова из возможных.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нажмите *Input* и получите результат.

![Skyeng](example/skyeng/Skyeng%203.fill_the_gaps.png "fill_the_gaps")

___

### Type the correct answer

- Откройте сайт.
- Напишите или лучше наведите курсор на слово с правильным ответом. Далее, нажмите на правую кнопку мыши - тогда 
правильное слово закрепится и никуда не убежит. Скопируйте правильный текст и вставьте его в пропуск.
Если эти операции занимают больше времени, чем вы бы выполнили сами, то игнорируйте этот совет. Однако, если текст 
очень большой, то предпочтительнее первый вариант.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нажмите *Input* и получите результат.

![Skyeng](example/skyeng/Skyeng%204.type_the_correct_answer.png "type_the_correct_answer")

___

### Match words

- Откройте сайт.
- Соотнесите все правильные слова.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нажмите *Input* и получите результат.
- Если вы получаете не полные слова, попробуйте взять больший фрагмент кода HTML.

![Skyeng](example/skyeng/Skyeng%205.match_words.png "match_words")

___

## TestEnglish

### Choose the correct option

- Откройте сайт.
- __НЕ__ выбирайте правильный вариант.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нажмите *Input* и получите результат.
- Вы получаете правильный шаблон для Edvibe без `*`. 
Вам нужно будет самостоятельно отметить правильные ответы знаком `*`.

![TestEnglish](example/test_english/TestEnglish%201.choose_the_correct_option.png "choose_the_correct_option")

---

### Choose from test

1. Откройте сайт.
2. Кликните `Next Page`,далее кликните `Check answer`.
3. Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
4. Нужно скопировать весь HTML-код как на картинке.
5. Нажмите *Input* и получите результат.

![TestEnglish](example/test_english/TestEnglish%202.1.choose_from_test.png "choose_from_test")
![TestEnglish](example/test_english/TestEnglish%202.2.choose_from_test.png "choose_from_test")

---

### Type the correct answer

- Откройте сайт.
- Кликните `Next Page`, далее кликните `Check answer`.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нужно скопировать весь HTML-код.
- Нажмите *Input* и получите результат.

![TestEnglish](example/test_english/TestEnglish%203.1.type_the_correct_answer.png "type_the_correct_answer")
![TestEnglish](example/test_english/TestEnglish%203.2.type_the_correct_answer.png "type_the_correct_answer")

---

## Englisch-Hilfen

### Choose the correct option

- Откройте сайт.
- Скопируйте ссылку. Пример скопированной ссылки: `https://www.englisch-hilfen.de/en/...`.
- Вставить в открытое окно ввода.
- Нажмите *Input* и получите результат.

![Englisch-Hilfen](example/englisch-hilfen/englisch-hilfen%201.choose_the_correct_option.png "choose_the_correct_option")

### Type the correct answer

- Откройте сайт.
- Кликните `Show answers`.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нажмите *Input* и получите результат.

![Englisch-Hilfen](example/englisch-hilfen/englisch-hilfen%202.type_the_correct_answer.png "type_the_correct_answer")

---

## Perfect-English

### Type the correct answer

- Откройте сайт.
- Кликните `Show` для __всех__ слов.
- Скопируйте блок outerHTML, как на картинке, и вставьте в открытое окно ввода.
- Нажмите *Input* и получите результат.


![Perfect-English](example/perfect-english/Perfect-English%201.type_the_correct_answer.png "type_the_correct_option")

---
