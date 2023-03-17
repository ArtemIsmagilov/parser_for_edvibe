# Parser for Edvibe

___
The application was created in winfdows 10. Tested on win10 and win11.
The essence of the graphical application is the transfer of
material from various Internet sources
(skyeng, test English, perfect enslish grammar and etc...).
The conversion of html markup from the site to the format
for edvibe is automatic. Then there will be instructions on how to quickly transfer the material.
The application is designed for English language teachers working on the edvibe platform

- https://skyeng.ru/
- https://test-english.com/
- https://www.perfect-english-grammar.com/
- https://www.englisch-hilfen.de/en/

## Features

* Saves 95% of your time
* Automatically parse and create a template in seconds
* Parsing 4 sites
* All tasks belong to the `Execise` or `Grammar` group

## Drawback

* There are bugs when the task is completely new
* In the beginning, it's a little difficult to understand
* The program was written by a novice in programming

## One of the reviews

> Thanks to this program, the process of transferring tasks from different sites has accelerated significantly!
> The program has definitely become an indispensable assistant for me.
> Now there is much more time for creativity during the preparation of lessons :)
> <hr>
>
> *Elena. Teacher english language*

## A simple guide

Let's start

1. Select site name from the menu
2. Select one of the formats for transferring the task from the site to Edvibe
3. Copy the HTML code and paste into the input window
    * Set the course for a piece of the task, more can be
    * Copy the code that covers the job as much as possible
    * Paste in input window
4. Press Input. You will receive a text in accordance with your task.

* Appropriate actions are required for each site and mode.
* Select the entire block as follows. Press Ctrl+Shift+C or right mouse button and select Explore
* You have open devtools with HTML code

## Skyeng

### Choose the correct option

- Open site
- Select all correct option
- Copy block outerHTML as in the picture and insert in open input-window
- Enter *Input* and get result
  ![Skyeng](example/skyeng/Skyeng%201.choose_the_correct_option.png "choose_the_correct_option")

___

### Choose the correct option from test

- Open site
- Select all correct option in __test__
- Copy block outerHTML as in the picture and insert in open input-window
- Enter *Input* and get result
  ![Skyeng](example/skyeng/Skyeng%202.choose_the_correct_option_from_test.png "choose_the_correct_option_from_test")

___

### Fill the gaps

- Open site
- Insert all the correct words from possible
- Copy block outerHTML as in the picture and insert in open input-window
- Enter *Input* and get result
  ![Skyeng](example/skyeng/Skyeng%203.fill_the_gaps.png "fill_the_gaps")

___

### Type the correct answer

- Open site
- Write or better hover over the word with the correct answer. click on the right mouse button - then the correct word
  will be fixed and will not run away. copy the correct text and paste it into the pass.
  If these operations take longer than you would have done yourself, then ignore this mode.
  However, if the text is very large, then the first option is preferable
- Copy block outerHTML as in the picture and insert in open input-window
- Enter *Input* and get result
  ![Skyeng](example/skyeng/Skyeng%204.type_the_correct_answer.png "type_the_correct_answer")

___

### Match words

- Open site
- Match all the correct words
- Copy block outerHTML as in the picture and insert in open input-window
- Enter *Input* and get result
- If you get not full words, try to take a bigger piece of code HTML
  ![Skyeng](example/skyeng/Skyeng%205.match_words.png "match_words")

___

## TestEnglish

### Choose the correct option

- Open site
- __NOT__ Select correct option
- Copy block outerHTML as in the picture and insert in open input-window
- Enter *Input* and get result
- You get correct template for Edvibe without an `*`.
  You will need to mark the correct answers with an `*` yourself
  ![TestEnglish](example/test_english/TestEnglish%201.choose_the_correct_option.png "choose_the_correct_option")

---

### Choose from test

- Open site
- Click `Next Page`, click `Check answer`
- Copy block outerHTML as in the picture and insert in open input-window
- Need copy all code HTML
- Enter *Input* and get result
  ![TestEnglish](example/test_english/TestEnglish%202.1.choose_from_test.png "choose_from_test")
  ![TestEnglish](example/test_english/TestEnglish%202.2.choose_from_test.png "choose_from_test")

---

### Type the correct answer

- Open site
- Click `Next Page` or click `Check answer`
- Copy block outerHTML as in the picture and insert in open input-window
- Need copy all code HTML
- Enter *Input* and get result
  ![TestEnglish](example/test_english/TestEnglish%203.1.type_the_correct_answer.png "type_the_correct_answer")
  ![TestEnglish](example/test_english/TestEnglish%203.2.type_the_correct_answer.png "type_the_correct_answer")

---

## Englisch-Hilfen

### Choose the correct option

- Open site
- Copy link. Example: `https://www.englisch-hilfen.de/en/...`
- Insert in open input-window
- Enter *Input* and get result
  ![Englisch-Hilfen](example/englisch-hilfen/englisch-hilfen%201.choose_the_correct_option.png "choose_the_correct_option")

### Type the correct answer

- Open site
- Click `Show answers`
- Copy block outerHTML as in the picture and insert in open input-window
- Enter *Input* and get result
  ![Englisch-Hilfen](example/englisch-hilfen/englisch-hilfen%202.type_the_correct_answer.png "type_the_correct_answer")

---

## Perfect-English

### Type the correct answer

- Open site
- Click `Show` for __all__ words
- Copy block outerHTML as in the picture and insert in open input-window
- Enter *Input* and get result
  ![Perfect-English](example/perfect-english/Perfect-English%201.type_the_correct_answer.png "type_the_correct_option")







