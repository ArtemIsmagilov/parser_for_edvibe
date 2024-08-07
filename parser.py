import tkinter
import random
import re
from tkinter import *
from tkinter import scrolledtext

import requests
from PIL import ImageTk, Image
from bs4 import BeautifulSoup

from compile_reg_consts import PATTERN1, PATTERN2, PATTERN3, PATTERN4, PATTERN5, PATTERN6, PATTERN7, PATTERN8


def get_result(res, text):
    if res:
        return res
    return text


def get_tk_img():
    ks = ("menu", "skyeng", "testenglish", "englisch-hilfen", "perfect_english_grammar", "exit")
    vs = (
        ("imgs/menu.png", (50, 50)),
        ("imgs/skyeng.png", (100, 40)),
        ("imgs/testenglish.png", (100, 40)),
        ("imgs/englisch-hilfen.PNG", (100, 40)),
        ("imgs/perfect_english_grammar.png", (100, 40)),
        ("imgs/exit.png", (80, 20)),
    )
    res_dict = {k: create_image(*v) for k, v in zip(ks, vs)}
    return res_dict


def create_image(path, size):
    img1 = Image.open(path)
    img1.thumbnail(size)
    tk_img = ImageTk.PhotoImage(img1)
    return tk_img


def filter_line(text):
    text = PATTERN1.sub("", text)
    return text


def valid_html(text_user):
    return bool(BeautifulSoup(text_user, "html.parser").find())


def find_bs4_tag(bs4_soup):
    if bs4_soup.find("p"):
        tag = "p"
    elif bs4_soup.find("vim-conversation-interactive"):
        tag = "vim-conversation-interactive"
    elif bs4_soup.find("li"):
        tag = "li"
    else:
        tag = None
    return tag


class Skyeng:
    """
    https://skyeng.ru/
    """

    color = "deep sky blue"

    def choose_the_correct_option(self, html_doc):
        if not valid_html(html_doc):
            return "This is not HTML code"

        soup = BeautifulSoup(html_doc, "lxml")
        result = []

        bs4_tag = find_bs4_tag(soup)

        for count, t in enumerate(soup.find_all(bs4_tag), 1):
            if not t.get_text().replace("\n", ""):
                continue

            r = f"{t}"
            for v in t.find_all("vim-select-item-title"):
                repl = PATTERN2.sub("<vim-select-item-title>#</vim-select-item-title>", f"{v}")
                r = r.replace(f"{v}", repl)
            line = BeautifulSoup(r, "lxml").get_text()
            for ans in t.find_all("button"):
                new_items = [
                    j.get_text()
                    for i in ans.find_next_siblings("div", id="items")
                    for j in i.find_all("vim-select-item-title")
                ]
                correct = ans.get_text()
                try:
                    index = new_items.index(correct)
                except ValueError:
                    return "Empty answer options. Choose the correct answer options in Skyeng, then try again."
                new_items[index] = correct + "*"
                random.shuffle(new_items)
                line = PATTERN3.sub(" [%s]" % "/".join(new_items), line, 1)

            line = filter_line(line)
            result.append("%s) %s\n" % (count, line))

        return get_result(
            "".join(result), "Empty html, not correct html markdown or is it not choose_the_correct_option task."
        )

    def feel_the_gaps(self, html_doc):
        if not valid_html(html_doc):
            return "This is not HTML code"

        soup = BeautifulSoup(html_doc, "lxml")
        result = []

        bs4_tag = find_bs4_tag(soup)

        for count, t in enumerate(soup.find_all(bs4_tag), 1):
            if not t.get_text().replace("\n", ""):
                continue

            r = f"{t}"
            for a in t.find_all("span", "answer-text"):
                r = re.sub(f"{a}", f"<vals>[{a}]</vals>", r)
            line = BeautifulSoup(r, "lxml").get_text()

            line = filter_line(line)

            if bs4_tag == "li":
                result.append("%s) %s\n" % (count, line))
            else:
                result.append("%s\n" % line)
        return get_result("".join(result), "Empty html, not correct html markdown or is it not feel_the_gaps task.")

    def type_the_correct_answer(self, html_doc):
        if not valid_html(html_doc):
            return "This is not HTML code"

        soup = BeautifulSoup(html_doc, "lxml")
        result = []

        bs4_tag = find_bs4_tag(soup)

        for count, t in enumerate(soup.find_all(bs4_tag), 1):
            if not t.get_text().replace("\n", ""):
                continue
            r = f"{t}"
            for inp in t.find_all("span", "input"):
                hints = inp.get("placeholder", "").replace("/", ";")
                right_answers = inp.get_text()
                new_html = "<vals>[%s/%s]</vals>" % (hints, right_answers)
                r = re.sub(f"{inp}", new_html, r, 1).replace("\n", "")
            line = BeautifulSoup(r, "lxml").get_text()
            line = filter_line(line)
            if bs4_tag == "li":
                result.append("%s) %s\n" % (count, line))
            else:
                result.append("%s\n" % line)

        return get_result(
            "".join(result), "Empty html, not correct html markdown or is it not type_the_correct_answer task."
        )

    def match(self, html):
        def find_row(tag):
            px = PATTERN4.search(tag["style"]).group(1)
            if int(px) not in sort_items:
                sort_items.append(int(px))

            if px not in data:
                data[px] = [tag]
            else:
                data[px].append(tag)

        if not valid_html(html):
            return "This is not HTML code"
        soup = BeautifulSoup(html, "lxml")
        result = []
        data = {}
        sort_items = []

        box = soup.find("div", "container -two-columns")
        for w in box.find_all("div", "item ng-star-inserted animated success"):
            find_row(w)

        for w in box.find_all("div", "item -dot-left ng-star-inserted animated success"):
            find_row(w)

        for s in sorted(sort_items):
            a, b = data[f"{s}"]
            line = "%s\t%s" % (a.get_text(), b.get_text())
            line = filter_line(line)
            result.append(line + "\n")
        return get_result("".join(result), "Empty html, not correct html markdown or is it not match_words task.")

    def choose_from_test(self, html):
        if not valid_html(html):
            return "This is not HTML code"

        soup = BeautifulSoup(html, "lxml")
        box = soup.find("ol", "questions")
        result = []
        if box:
            for count, li in enumerate(box.find_all("li", "ng-star-inserted"), 1):
                text = li.find("span", "question-text-container").get_text()

                a = "[%s]" % "/".join(
                    i.get_text() + "*" if i.find("span", "answer -right") else i.get_text()
                    for i in li.find_all("vim-test-question-answer", "question-answer ng-star-inserted")
                )
                line = text + a
                line = filter_line(line)
                result.append("%s) %s\n" % (count, line))
        return get_result("".join(result), "Empty html, not correct html markdown or is it not choose_from_test task.")


class TestEnglish:
    """
    https://test-english.com/
    """

    color = "green yellow"

    def choose_the_correct_option(self, html):
        if not valid_html(html):
            return "This is not HTML code"
        soup = BeautifulSoup(html, "lxml")
        result = []
        for count, l in enumerate(soup.find_all("div", "question-content"), 1):
            line = f"{l}"
            # delete span tag
            sn1 = l.find("span", "watupro_num")
            line = re.sub(f"{sn1}", "", line)
            # delete span numBox
            for sn2 in l.find_all("span", "numBox"):
                line = line.replace(f"{sn2}", "")
            # select answers and replace empty selects tags
            for s in l.find_all("select"):
                pattern = "[%s]" % "/".join(o["value"].strip() for o in s.find_all("option") if o["value"])
                line = re.sub(f"{s}", pattern, line)

            line = BeautifulSoup(line, "lxml").get_text()
            line = filter_line(line)

            line = "%s) %s\n" % (count, line)
            result.append(line)
        return get_result(
            "".join(result), "Empty html, not correct html markdown or is it not choose_the_correct_option task."
        )

    def type_the_correct_answer(self, html):
        if not valid_html(html):
            return "This is not HTML code"
        soup = BeautifulSoup(html, "lxml")
        result = []
        for count, l in enumerate(soup.find_all("div", "show-question-content"), 1):
            r = f"{l}"
            # del nums
            for s in l.find_all("span", "watupro_num"):
                r = r.replace(f"{s}", "")
            # find hints
            hints = re.findall(r"\(.*?\)", r)

            for h in range(len(hints)):
                r = r.replace(hints[h], "")
                hints[h] = hints[h].replace("/", ";")

            # find answers
            find_answers = l.parent.find("div", "watupro-main-feedback")
            # error AttributeError: 'NoneType' object has no attribute 'find_all'

            tag = find_answers.find_all("font", color="#50af31") or find_answers.find_all(
                "span", style="color: #50af31;"
            )
            answer_list = []
            for a in tag:
                slash = a.get_text().partition(":")[-1]
                if slash.find("/") != -1:
                    answer_list.extend(slash.split("/"))
                elif slash.find(" (") != -1:
                    search_brackets = PATTERN5.search(slash)
                    slash_answer = slash.partition("(")[0]
                    answer_list.append("%s/%s" % (slash_answer, search_brackets.group(1)))
                else:
                    answer_list.append(slash)
            # replace answers
            for a in answer_list:
                if hints:
                    h = hints.pop(0)
                else:
                    h = ""
                pattern = "[%s/%s]" % (h, a)
                r = r.replace("[no answer]", pattern, 1)

            for sn2 in l.find_all("span", "numBox"):
                r = r.replace(f"{sn2}", "")
            # simple correcting text
            sub_line = BeautifulSoup(r, "lxml").get_text()
            # clear line
            sub_line = filter_line(sub_line)
            sub_line = sub_line.replace("\xa0", "")
            result.append("%s) %s\n" % (count, sub_line))
        return get_result(
            "".join(result), "Empty html, not correct html markdown or it is not type_the_correct_answer task."
        )

    def choose_from_test(self, html):
        if not valid_html(html):
            return "This is not HTML code"
        result = []
        soup = BeautifulSoup(html, "lxml")
        for count, l in enumerate(
            soup.find_all(
                "div", "watupro-choices-columns show-question watupro-unresolved watupro-unanswered-question"
            ),
            1,
        ):
            r = f"{l}"

            r = re.sub(f'{l.find("div", "watupro-screen-reader")}', "", r)
            r = re.sub(f'{l.find("span", "highlighter")}', "", r)

            l = BeautifulSoup(r, "lxml")
            answers = l.find_all("li", "answer correct-answer")
            vals = l.find_all("li", "answer")
            pattern = []
            for i in vals:
                if i in answers:
                    word = i.span.get_text().partition(". ")[-1] + "*"
                else:
                    word = i.get_text().partition(". ")[-1]
                pattern.append(word.replace("/", ";"))
            random.shuffle(pattern)
            pattern = "[%s]" % "/".join(pattern)
            line = l.find("div", "show-question-content")
            sp = l.find("span", "watupro_num")
            line = re.sub(f"{sp}", "", f"{line}")
            if len(PATTERN6.findall(line)) > 1:
                line += pattern
            else:
                line = PATTERN6.sub(pattern, line)
                # line += pattern
            # clear trash

            line = BeautifulSoup(line, "lxml").get_text()
            line = filter_line(line)
            result.append("%s) %s\n" % (count, line))
        return get_result("".join(result), "Empty html, not correct html markdown or it is not choose_from_test task.")


class EnglischHilfen:
    """
    https://www.englisch-hilfen.de/en/
    """

    color = "cyan"

    def choose_the_correct_option(self, url):
        result = []
        url = url.rstrip("\n")
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError as connect_err:
            return "There is no internet connection"
        except requests.exceptions.MissingSchema as input_err:
            return f"Incorrect link - {url[:50]}... Please, insert correct link from site."
        except requests.exceptions.InvalidSchema as big_text_input:
            return f"Please, insert correct link from site. You insert : {url[:50]}..."
        html = r.text
        soup = BeautifulSoup(html, "lxml")
        box = soup.find("ol", "tasks")
        if box:
            for count, li in enumerate(box.find_all("li"), 1):
                r = f"{li}"
                answers = []
                for s in li.find_all("select"):
                    a = "[%s]" % "/".join(
                        o.get_text() for o in s.find_all("option") if re.sub(r"[\n ]", "", o.get_text())
                    )
                    answers.append(a)
                    r = re.sub(str(s), a, r)
                # clear line
                r = PATTERN7.sub("", r)
                line = BeautifulSoup(r, "lxml").get_text()
                result.append("%s) %s\n" % (count, line))
        return get_result(
            "".join(result), "Empty link line, not correct link or it is not choose_the_correct_option task."
        )

    def type_the_correct_answer(self, html):
        if not valid_html(html):
            return "This is not HTML code"
        soup = BeautifulSoup(html, "lxml")
        box = soup.find("ol", "tasks")
        result = []
        if box:
            for count, li in enumerate(box.find_all("li", "correct"), 1):
                r = f"{li}"
                for a in li.find_all("span", "correct-input"):
                    r = re.sub(f"{a}", "[/%s]" % a.get_text(), r)
                # clear trash
                r = PATTERN7.sub("", r)
                line = BeautifulSoup(r, "lxml").get_text()
                result.append("%s) %s\n" % (count, line))
        return get_result(
            "".join(result), "Empty html, not correct html markdown or it is not type_the_correct_answer task."
        )


class PerfectEnglishGrammar:
    """
    https://www.perfect-english-grammar.com/
    """

    color = "violet red"

    def type_the_correct_answer(self, html):
        if not valid_html(html):
            return "This is not HTML code"
        soup = BeautifulSoup(html, "lxml")
        box = soup.find("div", id="exercise")
        result = []
        if box:
            for tr in box.find_all("td"):
                if tr.button:
                    continue
                r = f"tr"
                hints = []
                answers = []
                for i in tr.find_all("span", "textPart"):
                    hint = PATTERN8.search(f"{i}")
                    if hint:
                        hints.append(hint.group(0)[1:-1].replace("/", ";"))
                        r = r.replace(hint.group(0), "")
                for i in tr.find_all("span", style="color: rgb(28, 97, 99); padding: 1px;"):
                    r = r.replace(f"{i}", "")
                    answers.append(i.get_text()[1:-1].strip())

                for d in tr.find_all("input"):
                    a = answers.pop(1) if answers else None
                    if hints:
                        h = hints.pop(0)
                    else:
                        h = ""
                    pattern = "[%s/%s]" % (h, a)
                    r = r.replace(f"{d}", pattern, 1)

                # clear
                r = PATTERN7.sub("", r)

                line = BeautifulSoup(r, "lxml").get_text()
                line = filter_line(line)
                result.append(line + "\n")
        return get_result(
            "".join(result), "Empty html, not correct html markdown or it is not type_the_correct_answer task."
        )


class App:
    """
    A graphical application that parses Skyeng, Test English and Englisch-hilfen html markup into readable text for the
    Edvibe platform. The user will need to copy the html markup. Automatic text transfer and conversion.
    """

    frames = []
    mode = None

    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x500")
        self.root.title("Parser for Edvibe")

        self.img = Image.open("imgs/background.png")
        self.bg = ImageTk.PhotoImage(self.img)
        self.bg_lbl = tkinter.Label(self.root, image=self.bg)
        self.bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        self.tk_imgs = get_tk_img()
        self.mainmenu1 = Menubutton(self.root, image=self.tk_imgs["menu"])
        self.mainmenu1.pack(anchor=NW)
        self.submenu1 = Menu(self.mainmenu1)
        self.mainmenu1.config(menu=self.submenu1)
        self.submenu1.add_command(label="Skyeng", image=self.tk_imgs["skyeng"], compound=LEFT, command=self.skyeng)
        self.submenu1.add_command(
            label="Test English", image=self.tk_imgs["testenglish"], compound=LEFT, command=self.test_english
        )
        self.submenu1.add_command(
            label="Englisch Hilfen", image=self.tk_imgs["englisch-hilfen"], compound=LEFT, command=self.englisch_hilfen
        )
        self.submenu1.add_command(
            label="Perfect English Grammar",
            image=self.tk_imgs["perfect_english_grammar"],
            compound=LEFT,
            command=self.perfect_english_grammar,
        )
        self.submenu1.add_command(label="Exit", image=self.tk_imgs["exit"], compound=LEFT, command=self.root.quit)

        self.root.iconbitmap("imgs/click.ico")

        mainloop()

    def change_color(self, active_button):
        for b in self.user_buttons:
            if b is active_button:
                b.config(bg=self.handler.color)
            elif b:
                b.config(bg="white")

    def choosing(self):
        App.mode = self.handler.choose_the_correct_option
        self.change_color(self.btn_task1)

    def choosing_from_test(self):
        App.mode = self.handler.choose_from_test
        self.change_color(self.btn_task2)

    def filling(self):
        App.mode = self.handler.feel_the_gaps
        self.change_color(self.btn_task3)

    def typing(self):
        App.mode = self.handler.type_the_correct_answer
        self.change_color(self.btn_task4)

    def matching(self):
        App.mode = self.handler.match
        self.change_color(self.btn_task5)

    def update_window(self):
        self.bg_lbl.destroy()
        self.root.config(bg="wheat1")

        self.f2 = Frame(self.root)
        self.txt_input = scrolledtext.ScrolledText(self.f2, width=70, height=4, font="Times 15")

        self.f3 = Frame(self.root)
        self.btn_input = Button(self.f3, text="Input", command=self.input_text)
        self.btn_clear = Button(self.f3, text="Clear", command=self.delete_text)
        self.btn_copy = Button(self.f3, text="Copy", command=self.copy_text)
        self.btn_paste = Button(self.f3, text="Paste", command=self.paste_text)

        self.f4 = Frame(self.root)
        self.txt_output = scrolledtext.ScrolledText(self.f4, width=70, height=13, font="Times 15")

        self.f1.pack()
        self.lbl.pack(side=LEFT)
        self.user_buttons = (self.btn_task1, self.btn_task2, self.btn_task3, self.btn_task4, self.btn_task5)

        for user_b in self.user_buttons:
            if user_b:
                user_b.pack(side=LEFT)

        self.f2.pack()
        self.txt_input.pack()

        self.f3.pack()
        self.gui_buttons = (self.btn_clear, self.btn_paste, self.btn_input, self.btn_copy)

        for gui_b in self.gui_buttons:
            if gui_b:
                gui_b.pack(side=LEFT)

        self.f4.pack()
        self.txt_output.pack()

        App.frames = [self.f1, self.f2, self.f3, self.f4]

    def create_handler(self, handler, mode):
        for f in App.frames:
            f.destroy()
        self.handler = handler
        App.mode = mode

    def create_empty_buttons(self, *pack):
        for b in pack:
            self.__dict__[b] = None

    def input_text(self):
        self.txt_output.delete("1.0", END)
        input_user = self.txt_input.get("1.0", END)
        self.txt_output.insert(END, App.mode(App, input_user))

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.txt_output.get("1.0", END))

    def paste_text(self):
        self.delete_text()
        self.txt_input.insert(END, self.root.clipboard_get())

    def delete_text(self):
        self.txt_input.delete("1.0", END)
        self.txt_output.delete("1.0", END)

    def skyeng(self):
        self.create_handler(Skyeng, Skyeng.choose_the_correct_option)

        self.f1 = Frame(self.root)
        self.lbl = Label(self.f1, image=self.tk_imgs["skyeng"])

        self.btn_task1 = Button(self.f1, text="Choose the correct option", bg=self.handler.color, command=self.choosing)
        self.btn_task2 = Button(self.f1, text="Choose... from test", bg="white", command=self.choosing_from_test)
        self.btn_task3 = Button(self.f1, text="Fill the gaps", bg="white", command=self.filling)
        self.btn_task4 = Button(self.f1, text="Type the correct answer", bg="white", command=self.typing)
        self.btn_task5 = Button(self.f1, text="Match words", bg="white", command=self.matching)

        self.update_window()

    def test_english(self):
        self.create_handler(TestEnglish, TestEnglish.choose_the_correct_option)

        self.f1 = Frame(self.root)
        self.lbl = Label(self.f1, image=self.tk_imgs["testenglish"])
        self.btn_task1 = Button(self.f1, text="Choose the correct option", bg=self.handler.color, command=self.choosing)
        self.btn_task2 = Button(self.f1, text="Choose ...(from test)", bg="white", command=self.choosing_from_test)
        self.btn_task4 = Button(self.f1, text="Type the correct answer", bg="white", command=self.typing)
        self.create_empty_buttons("btn_task3", "btn_task5")

        self.update_window()

    def englisch_hilfen(self):
        self.create_handler(EnglischHilfen, EnglischHilfen.choose_the_correct_option)

        self.f1 = Frame(self.root)
        self.lbl = Label(self.f1, image=self.tk_imgs["englisch-hilfen"])
        self.btn_task1 = Button(self.f1, text="Choose the correct option", bg=self.handler.color, command=self.choosing)
        self.btn_task4 = Button(self.f1, text="Type the correct answer", bg="white", command=self.typing)
        self.create_empty_buttons("btn_task2", "btn_task3", "btn_task5")

        self.update_window()

    def perfect_english_grammar(self):
        self.create_handler(PerfectEnglishGrammar, PerfectEnglishGrammar.type_the_correct_answer)

        self.f1 = Frame(self.root)
        self.lbl = Label(self.f1, image=self.tk_imgs["perfect_english_grammar"])
        self.btn_task4 = Button(self.f1, text="Type the correct answer", bg=self.handler.color, command=self.typing)

        self.create_empty_buttons("btn_task1", "btn_task2", "btn_task3", "btn_task5")

        self.update_window()


if __name__ == "__main__":
    App()
