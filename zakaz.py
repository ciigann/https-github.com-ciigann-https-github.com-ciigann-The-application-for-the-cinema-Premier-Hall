from tkinter import *
from random import *
from datetime import datetime
from tkinter import font
import tkinter as tk
import webbrowser
import tkintermapview
from functools import partial
import random

from PIL import ImageTk, Image
import itertools


# Кнопки перемотки зала на главной странице
def r():
    l1['image'] = m2
    br['command'] = r1


def r1():
    l1['image'] = m3
    br['command'] = r2


def r2():
    l1['image'] = m1
    br['command'] = r


def l():
    l1['image'] = m3
    bl['command'] = l11


def l11():
    l1['image'] = m2
    bl['command'] = l2


def l2():
    l1['image'] = m1
    bl['command'] = l


def b1():
    # ФУНКЦИИ ВЫЗЫВАЮЩИЕ ОПИСАНИЕ КАЖДОГО ФИЛЬМА
    def vit():
        vit = Toplevel(w1)
        vit.title('О ФИЛЬМЕ ПУШИСТЫЙ ВОЯЖ')
        vit.iconbitmap('icon.ico')
        vit.geometry('1280x960')
        vit.resizable(False, False)
        lv = Label(vit, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(vit, text="О ФИЛЬМЕ ПУШИСТЫЙ ВОЯЖ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(vit, text="1 час 33 минуты Мультфильм, комедия, приключения 6+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(vit, text="Страна: США, Канада", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(vit, text="Режиссер: Кевин Донован, Готтфрид Рудт", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(vit, text="Актеры: Билл Найи, Брук Шилдс, Дэнни Трехо",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(vit, text="Во время переезда двое домашних любимцев, Педро и Грейси, теряют своих хозяев."
                                      "\nОказавшись в пугающем и неизвестном мире, они пытаются воссоединиться с семьей."
                                      "\nНа пути их ждет множество приключений и опасностей, справиться с которыми можно,"
                                      "\nтолько действуя сообща.Смогут ли они разрешить свои разногласия и вернуться домой?",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)
        label_text5 = Label(vit, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(vit, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)


        vit.grab_set()
        vit.mainloop()

    def sltn():
        sltn = Toplevel(w1)
        sltn.title('О ФИЛЬМЕ СТО ЛЕТ ТОМУ ВПЕРЕД')
        sltn.iconbitmap('icon.ico')
        sltn.geometry('1280x960')
        sltn.resizable(False, False)
        lv = Label(sltn, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(sltn, text="О ФИЛЬМЕ СТО ЛЕТ ТОМУ ВПЕРЕД", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(sltn, text="2 часа 35 минут Приключения, экшн 6+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(sltn, text="Страна: Россия", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(sltn, text="Режиссер: Александр Андрющенко", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(sltn, text="Актеры: Даша Верещагина, Марк Эйдельштейн, Александр Петров, Юра Борисов, "
                                       "\nВиктория Исакова, Константин Хабенский, Федор Бондарчук, Софа Цибирева",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(sltn, text="Они живут в разных мирах. Коля Герасимов — в сегодняшней Москве, Алиса"
                                       "\nСелезнева — на сто лет позже. Коля – обычный парень, ему нет дела до"
                                       "\nбудущего. Алису не отпускает прошлое: она должна найти маму, которую"
                                       "\nпотеряла, когда была совсем ребенком. Встреча Алисы и Коли станет началом"
                                       "\nневероятных приключений, в которых нашим героям предстоит отвоевать у"
                                       "\nкосмических пиратов Вселенную, восстановить ход времени и обрести самое"
                                       "\nдорогое: любовь и дружбу.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=470)
        label_text5 = Label(sltn, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(sltn, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)

        sltn.grab_set()
        sltn.mainloop()

    def superp():
        superp = Toplevel(w1)
        superp.title('О ФИЛЬМЕ СУПЕРПТАШКИ')
        superp.iconbitmap('icon.ico')
        superp.geometry('1280x960')
        superp.resizable(False, False)
        lv = Label(superp, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(superp, text="О ФИЛЬМЕ СУПЕРПТАШКИ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(superp, text="1 час 31 минута Анимация 0+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(superp, text="Страна: Италия, Испания", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(superp, text="Режиссер: Нестор Ф. Деннис", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(superp, text="Актеры: Тай Шеридан, Шон Пенн, Гбенга Акиннагбе",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(superp, text="Птичка Джонни и его пернатые друзья обладают суперспособностями. Однажды"
                                         "\nони отправляются на секретную миссию, в ходе которой им предстоит спасти"
                                         "\nродной город от коварных планов злодея Отто фон Моржа.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)
        label_text5 = Label(superp, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(superp, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)

        superp.grab_set()
        superp.mainloop()

    def adel():
        adel = Toplevel(w1)
        adel.title('О ФИЛЬМЕ АСФАЛЬТОВЫЕ ДЖУНГЛИ')
        adel.iconbitmap('icon.ico')
        adel.geometry('1280x960')
        adel.resizable(False, False)
        lv = Label(adel, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(adel, text="О ФИЛЬМЕ АСФАЛЬТОВЫЕ ДЖУНГЛИ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(adel, text="2 часа 5 минут Триллер, драма 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(adel, text="Страна: США", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(adel, text="Режиссер: Жан-Стефан Совер", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(adel, text="Актеры: Тай Шеридан, Шон Пенн, Гбенга Акиннагбе",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(adel, text="Это история врача и его первого года на работе в середине 90-х в Гарлеме."
                                       "\nЭто взгляд изнутри на уличную жизнь: перестрелки, плохие копы, безнадежные"
                                       "\nпациенты, черный юмор в странных обстоятельствах и попытка одного медика"
                                       "\nсохранить свое желание помочь, несмотря на его растущую черствость.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)
        label_text5 = Label(adel, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(adel, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)

        adel.grab_set()
        adel.mainloop()

    def nez():
        nez = Toplevel(w1)
        nez.title('О ФИЛЬМЕ НЕЗНАКОМЦЫ')
        nez.iconbitmap('icon.ico')
        nez.geometry('1280x960')
        nez.resizable(False, False)
        lv = Label(nez, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(nez, text="О ФИЛЬМЕ НЕЗНАКОМЦЫ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(nez, text="1 час 37 минут Хоррор-слэшер 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(nez, text="Страна: США", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(nez, text="Режиссер: Ренни Харлин", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(nez, text="Актеры: Мэделин Петш, Гэбриел Бассо, Рэйчел Шентон, Ричард Брэйк",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(nez, text="Майя и Райан решили отметить пятую годовщину, не подозревая, что она может стать"
                                      "\nих последней. Путешествуя на своем пикапе через всю страну, они совершают"
                                      "\nвынужденную остановку в маленьком городе, где местные жители, даже дети,"
                                      "\nвстречают их с большим интересом. Оставаться в этом странном месте пара не хочет,"
                                      "\nно вынуждена провести ночь в доме, куда вскоре нагрянут безумцы в кукольных масках.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)
        label_text5 = Label(nez, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(nez, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)

        nez.grab_set()
        nez.mainloop()

    def vp():
        vp = Toplevel(w1)
        vp.title('О ФИЛЬМЕ ВИННИ ПУХ')
        vp.iconbitmap('icon.ico')
        vp.geometry('1280x960')
        vp.resizable(False, False)
        lv = Label(vp, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(vp, text="О ФИЛЬМЕ ВИННИ ПУХ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(vp, text="1 час 37 минут Ужасы, триллер 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(vp, text="Страна: Великобритания", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(vp, text="Режиссер: Рис Фрейк-Уотерфилд", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(vp, text="Актеры: Скотт Чемберс, Таллула Эванс, Райан Олива, Тереза Бенхем",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(vp, text="После событий первого фильма, Винни-Пух и Пятак больше не могут продолжать"
                                     "\nохотиться в Стоакровомом лесу. Очередное предательство Кристофера Робина,"
                                     "\nраскрывшего миру их существование, ставит под угрозу не только их дом, но и"
                                     "\nжизни. Вот только звери больше не намерены прятаться в тени и вместе c друзьями"
                                     "\nСовенком и Тигрой, отправляются в город, чтобы навести в нем свои кровавые порядки.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)
        label_text5 = Label(vp, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(vp, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)

        vp.grab_set()
        vp.mainloop()

    def sudn():
        sudn = Toplevel(w1)
        sudn.title('О ФИЛЬМЕ СУДНАЯ НОЧЬ')
        sudn.iconbitmap('icon.ico')
        sudn.geometry('1280x960')
        sudn.resizable(False, False)
        lv = Label(sudn, image=iw1)
        lv.pack(anchor=W)
        label_text = Label(sudn, text="О ФИЛЬМЕ СУДНАЯ НОЧЬ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(sudn, text="1 час 34 минуты Криминал, триллер 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(sudn, text="Страна: США", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(sudn, text="Режиссер: Дэн Браун", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(sudn, text="Актеры: Ангус Клауд, Эллиот Найт, Джессика Гарза",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(sudn, text="Несколько человек становятся свидетелями джекпота в $156 миллионов долларов."
                                       "\nСлучайные посетители, полиция, преступники - все желают заполучить лотерейный"
                                       "\nбилет с огромным выигрышем. Эта судная ночь выпустит на волю все людские пороки.",
                            font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)
        label_text5 = Label(sudn, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(sudn, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)

        sudn.grab_set()
        sudn.mainloop()

    def zam1():
        zam = Toplevel(w1)
        zam.title('О ФИЛЬМЕ ПЛАНЕТА ОБЕЗЬЯН')
        zam.iconbitmap('icon.ico')
        zam.geometry('1280x960')
        zam.resizable(False, False)
        lz = Label(zam, image=iw1)
        lz.pack(anchor=W)
        label_text = Label(zam, text="О ФИЛЬМЕ ПЛАНЕТА ОБЕЗЬЯН", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(zam, text="2 часа 30 минут Фантастика, боевик, приключения 16+", font=("Helvetica", 16))
        label_text0.place(x=220, y=240)
        label_text2 = Label(zam, text="Страна: США", font=("Helvetica", 16))
        label_text2.place(x=220, y=290)
        label_text3 = Label(zam, text="Режиссер: Уэс Болл", font=("Helvetica", 16))
        label_text3.place(x=220, y=340)
        label_text4 = Label(zam, text="Актеры: Оуэн Тиг, Питер Макон, Фрейя Аллан",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=390)
        label_text1 = Label(zam, text="Несколько поколений после правления Цезаря. Обезьяны являются доминирующим"
                                      "\nвидом, живущим в гармонии, а люди вынуждены оставаться в тени. Пока новый"
                                      "\nтиранический nлидер обезьян строит свою империю, один молодой шимпанзе "
                                      "\nотправляется в путешествие, которое заставит его усомниться во всём, что"
                                      "\nон знал о прошлом, и сделать выбор, который определит будущее как обезьян,"
                                      "\nтак и людей.", font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)
        label_text5 = Label(zam, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(zam, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)

        zam.grab_set()
        zam.mainloop()

    def tof1():
        tof = Toplevel(w1)
        tof.title('О ФИЛЬМЕ МИНЕСТЕРСТВО НЕДЖЕНТЕЛЬМЕНСКИХ ДЕЛ')
        tof.iconbitmap('icon.ico')
        tof.geometry('1280x960')
        tof.resizable(False, False)
        lt = Label(tof, image=iw1)
        lt.pack(anchor=W)
        label_text = Label(tof, text="О ФИЛЬМЕ МИНЕСТЕРСТВО \nНЕДЖЕНТЕЛЬМЕНСКИХ ДЕЛ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(tof, text="2 часа 7 минут Комедийный экшн 18+", font=("Helvetica", 16))
        label_text0.place(x=220, y=270)
        label_text2 = Label(tof, text="Страна: США, Великобритания", font=("Helvetica", 16))
        label_text2.place(x=220, y=320)
        label_text3 = Label(tof, text="Режиссер: Гай Ричи", font=("Helvetica", 16))
        label_text3.place(x=220, y=370)
        label_text4 = Label(tof, text="Актеры: Генри Кавилл, Эйса Гонсалес, Алан Ричсон, Алекс Петтифер",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=420)
        label_text1 = Label(tof, text="Они — лучшие из лучших. Отпетые авантюристы и первоклассные спецы,привыкшие"
                                      "\nдействовать в одиночку. Но когда на кону стоит судьба всего мира, им "
                                      "\nприходится объединиться в сверхсекретное боевое подразделение и отправиться"
                                      "\nна дерзкую миссию против нацистов. Теперь их дело — война, и вести они её "
                                      "\nбудут совершенно не по-джентльменски.", font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=470)
        label_text5 = Label(tof, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(tof, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)
        tof.grab_set()
        tof.mainloop()

    def sn1():
        sn = Toplevel(w1)
        sn.title('О ФИЛЬМЕ МАЙОР ГРОМ')
        sn.iconbitmap('icon.ico')
        sn.geometry('1280x960')

        sn.resizable(False, False)
        ls5 = Label(sn, image=iw1)
        ls5.pack(anchor=W)
        label_text = Label(sn, text="О ФИЛЬМЕ МАЙОР ГРОМ", font=("Helvetica", 32))
        label_text.place(x=264, y=120)
        label_text0 = Label(sn, text="3 часа Приключения, экшн 16+", font=("Helvetica", 16))
        label_text0.place(x=220, y=220)
        label_text2 = Label(sn, text="Страна: Россия", font=("Helvetica", 16))
        label_text2.place(x=220, y=270)
        label_text3 = Label(sn, text="Режиссер: Олег Трофим", font=("Helvetica", 16))
        label_text3.place(x=220, y=320)
        label_text4 = Label(sn, text="Актеры: Тихон Жизневский, Александр Сетейкин, Алексей Маклаков, Любовь Аксенова,"
                                     "\n Сергей Горошко, Константин Хабенский, Матвей Лыков, Ольга Сутулова",
                            font=("Helvetica", 16), justify='left')
        label_text4.place(x=220, y=370)
        label_text1 = Label(sn, text="Сюжет «Игры» разворачивается спустя год после того, как майор Гром поймал"
                                     "\nЧумного Доктора. Санкт-Петербург оправился от потрясений, Сергей Разумовский"
                                     "\nоказался в психиатрической лечебнице, а Игорь Гром стал главной знаменитостью"
                                     "\nв городе. Жизнь майора Грома идеальна: днем он ловит преступников вместе с "
                                     "\nнапарником Димой Дубиным, а вечера проводит в компании журналистки Юлии "
                                     "\nПчёлкиной. Полную идиллию прерывает появление в городе таинственного злодея,"
                                     "\nназывающего себя Призраком. Он предлагает Грому сыграть в опасную игру, ставка"
                                     "\n в которой — жизни обычных людей.", font=("Helvetica", 16), justify='left')
        label_text1.place(x=220, y=440)
        label_text5 = Label(sn, text="Купить билет на данный фильм можно перейдя по кнопке ниже:",
                            font=("Helvetica", 16), justify='left')
        label_text5.place(x=220, y=700)

        def change(e):
            button.configure(fg=black)

        def unchange(e):
            button.configure(fg=purple)

        button = Button(sn, bg="#F0F4F7", height=1, width=13,
                        fg=black, borderwidth=0, font=('Helvetica', 24),
                        activebackground=wh, activeforeground=black, text="РАСПИСАНИЕ", command=b2)
        button.place(x=205, y=750)
        button.bind('<Enter>', unchange)
        button.bind('<Leave>', change)
        sn.grab_set()
        sn.mainloop()

    # АФИША С ВЫБОРОМ ФИЛЬМА

    w1 = Toplevel(m)
    w1.configure(bg=wh)
    w1.iconbitmap('icon.ico')
    w1.geometry('1280x960')
    w1.resizable(False, False)
    lw1 = Label(w1, image=iw1)
    lw1.pack(anchor=W)
    w1.title('АФИША')

    label_text = Label(w1, text="Выберите фильм", font=("Helvetica", 32))
    label_text.place(x=264, y=120)

    ik1 = PhotoImage(file='Майор Гром.png')
    ik1t = PhotoImage(file='Майор Гром темный.png')

    def dk1(e):
        k1['image'] = ik1

    def dk1t(e):
        k1['image'] = ik1t

    ik2 = PhotoImage(file='Министерство неджентельменских дел.png')
    ik2t = PhotoImage(file='Министерство неджентельменских дел темный.png')

    def dk2(e):
        k2['image'] = ik2

    def dk2t(e):
        k2['image'] = ik2t

    ik3 = PhotoImage(file='Планета обезьян.png')
    ik3t = PhotoImage(file='Планета обезьян темный.png')

    def dk3(e):
        k3['image'] = ik3

    def dk3t(e):
        k3['image'] = ik3t

    ik4 = PhotoImage(file='Пушистый вояж.png')
    ik4t = PhotoImage(file='Пушистый вояж темный.png')

    def dk4(e):
        k4['image'] = ik4

    def dk4t(e):
        k4['image'] = ik4t

    ik5 = PhotoImage(file='Сто лет тому вперед.png')
    ik5t = PhotoImage(file='Сто лет тому вперед темный.png')

    def dk5(e):
        k5['image'] = ik5

    def dk5t(e):
        k5['image'] = ik5t

    ik6 = PhotoImage(file='незнакомцы.png')
    ik6t = PhotoImage(file='Незнакомцы темная.png')

    def dk6(e):
        k6['image'] = ik6

    def dk6t(e):
        k6['image'] = ik6t

    ik7 = PhotoImage(file='Винни Пух.png')
    ik7t = PhotoImage(file='Винни Пух темный.png')

    def dk7(e):
        k7['image'] = ik7

    def dk7t(e):
        k7['image'] = ik7t

    ik8 = PhotoImage(file='суперпташки.png')
    ik8t = PhotoImage(file='суперпташки темная.png')

    def dk8(e):
        k8['image'] = ik8

    def dk8t(e):
        k8['image'] = ik8t

    ik9 = PhotoImage(file='судная ночь.png')
    ik9t = PhotoImage(file='судная ночь темный.png')

    def dk9(e):
        k9['image'] = ik9

    def dk9t(e):
        k9['image'] = ik9t

    ik10 = PhotoImage(file='Асфальтовые джунгли.png')
    ik10t = PhotoImage(file='Асфальтовые джунгли темный.png')

    def dk10(e):
        k10['image'] = ik10

    def dk10t(e):
        k10['image'] = ik10t

    k1 = Button(w1, image=ik1, bg=wh, borderwidth=0, activebackground=wh, command=sn1)
    k1.place(x=264, y=200)
    k1.bind('<Enter>', dk1t)
    k1.bind('<Leave>', dk1)
    k2 = Button(w1, image=ik2, bg=wh, borderwidth=0, activebackground=wh, command=tof1)
    k2.place(x=417, y=200)
    k2.bind('<Enter>', dk2t)
    k2.bind('<Leave>', dk2)
    k3 = Button(w1, image=ik3, bg=wh, borderwidth=0, activebackground=wh, command=zam1)
    k3.place(x=567, y=200)
    k3.bind('<Enter>', dk3t)
    k3.bind('<Leave>', dk3)
    k4 = Button(w1, image=ik4, bg=wh, borderwidth=0, activebackground=wh, command=vit)
    k4.place(x=716, y=200)
    k4.bind('<Enter>', dk4t)
    k4.bind('<Leave>', dk4)
    k5 = Button(w1, image=ik5, bg=wh, borderwidth=0, activebackground=wh, command=sltn)
    k5.place(x=864, y=200)
    k5.bind('<Enter>', dk5t)
    k5.bind('<Leave>', dk5)
    k6 = Button(w1, image=ik6, bg=wh, borderwidth=0, activebackground=wh, command=nez)
    k6.place(x=264, y=519)
    k6.bind('<Enter>', dk6t)
    k6.bind('<Leave>', dk6)
    k7 = Button(w1, image=ik7, bg=wh, borderwidth=0, activebackground=wh, command=vp)
    k7.place(x=417, y=519)
    k7.bind('<Enter>', dk7t)
    k7.bind('<Leave>', dk7)
    k8 = Button(w1, image=ik8, bg=wh, borderwidth=0, activebackground=wh, command=superp)
    k8.place(x=567, y=519)
    k8.bind('<Enter>', dk8t)
    k8.bind('<Leave>', dk8)
    k9 = Button(w1, image=ik9, bg=wh, borderwidth=0, activebackground=wh, command=sudn)
    k9.place(x=716, y=519)
    k9.bind('<Enter>', dk9t)
    k9.bind('<Leave>', dk9)
    k10 = Button(w1, image=ik10, bg=wh, borderwidth=0, activebackground=wh, command=adel)
    k10.place(x=864, y=519)
    k10.bind('<Enter>', dk10t)
    k10.bind('<Leave>', dk10)

    w1.grab_set()
    w1.mainloop()


def bilet(name_of_movie, date_of_movie, name_of_theatre):
    rand = randint(100_000_000, 999_999_999)

    w_bilet = Toplevel()
    w_bilet.geometry('600x400')
    w_bilet.title('ЭЛЕКТРОННЫЙ БИЛЕТ')
    w_bilet.resizable(False, False)
    w_bilet.iconbitmap('icon.ico')

    fon_bel = ImageTk.PhotoImage(Image.open('фон для эл билета.png').resize((600, 400)))
    wh = "white"

    fon_ = Label(w_bilet, image=fon_bel)
    fon_.place(x=0, y=0)

    fon = Label(w_bilet, text="Вы успешно купили билет",
                font=('Helvetica', 20), bg=wh)
    fon.place(x=130, y=30)

    num = Label(w_bilet, text="Номер заказа", font=('Helvetica', 16), bg=wh)
    num.place(x=50, y=80)

    n = Label(w_bilet, text=f'{str(rand)[0:3]} {str(rand)[3:6]} {str(rand)[6:]}',
              font=('Helvetica', 22, 'bold'), bg=wh)
    n.place(x=50, y=110)

    film_bilet = Label(w_bilet, text=f'Фильм: {name_of_movie}', font=('Helvetica', 12), bg=wh)
    film_bilet.place(x=50, y=160)

    theatre = Label(w_bilet, text=f'Кинотеатр: {name_of_theatre}', font=('Helvetica', 12), bg=wh)
    theatre.place(x=50, y=185)

    seans = Label(w_bilet, text=f'Сеанс: {date_of_movie}', font=('Helvetica', 12), bg=wh)
    seans.place(x=50, y=210)
    summa = Label(w_bilet, text=f'Стоимость билетов: {count * 230}', font=('Helvetica', 12), bg=wh)
    summa.place(x=50, y=235)
    str_list = ' '.join(list)
    s = '\n'.join([str_list[i:i + 56] for i in range(0, len(str_list), 56)])
    mesto = Label(w_bilet, text=f'Место: {s}', font=('Helvetica', 12), bg=wh)
    mesto.place(x=50, y=260)

    iconka = ImageTk.PhotoImage(Image.open('icon.ico').resize((150, 150)))

    icon = Label(w_bilet, image=iconka, bg="white")
    icon.place(x=400, y=100)

    purple = '#951b81'
    black = 'black'

    def change(e):
        button.configure(fg=black)

    def unchange(e):
        button.configure(fg=purple)

    button = Button(w_bilet, bg=wh, height=1, width=13,
                    fg=black, borderwidth=0, font=('Helvetica', 12),
                    activebackground=wh, activeforeground=black, text="ПОКАЗАТЬ ЧЕК", command=check)
    button.place(x=400, y=330)
    button.bind('<Enter>', unchange)
    button.bind('<Leave>', change)
    w_bilet.grab_set()
    w_bilet.mainloop()
def check():
    # кассовый чек
    check = tk.Tk()
    check.geometry("535x800")
    now = datetime.now()

    text_label = tk.Label(check, text="-------------------------------------------------------------------------",
                          font=("Helvetica", 20))
    text_label.pack()
    n = random.randint(1000000000, 10000000000)
    label_center = tk.Label(check, text=f"Счёт №{n}", justify="center", font=("Helvetica", 20))
    label_center.pack()
    label_center = tk.Label(check, text=f"Кассовый чек", justify="center", font=("Helvetica", 20))
    label_center.pack()
    text_label_2 = tk.Label(check, text="-----------------------------------------------------------------------",
                            font=("Helvetica", 20))
    text_label_2.pack()

    # стоимость билета
    cost = 1000
    label_center = tk.Label(check, text=f"  Билет в кинотеатр   1 x {cost} = {count * 230} руб", justify="left",
                            font=("Helvetica", 20))
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"  НДС 10%                                    {count * 230 // 10} руб",
                            font=("Helvetica", 20))
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"  ИТОГО                                     {count * 230 // 10 + count * 230} руб",
                            font=("Helvetica", 20))
    label_center.pack(anchor="w")
    text_label_3 = tk.Label(check, text="-----------------------------------------------------------------------",
                            font=("Helvetica", 20))
    text_label_3.pack(anchor="w")
    label_center = tk.Label(check, text=f"  Юридическое лицо ООО ПРЕМЬЕР ЗАЛ", font=("Rostov", 20))
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"  Сайт                                   premierzal.ru",
                            font=("Helvetica", 20), anchor="w")
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"  ИНН                                    6686020023", font=("Helvetica", 20),
                            anchor="w")
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"", font=("Helvetica", 20), anchor="w")
    label_center.pack(anchor="w")

    label_center = tk.Label(check, text=f"  № ККТ:                 000038947580939840", font=("Helvetica", 20),
                            anchor="w")
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"  № ФН:                      7575467456754656", font=("Helvetica", 20),
                            anchor="w")
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"  № ФД:                                           77434",
                            font=("Helvetica", 20), anchor="w")
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"  ФД:                                      3795506201",
                            font=("Helvetica", 20), anchor="w")
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"", font=("Helvetica", 20), anchor="w")
    label_center.pack(anchor="w")

    label_center = tk.Label(check, text=f"  620002,Свердловская область,", font=("Helvetica", 20), anchor="w")
    label_center.pack(anchor="w")
    label_center = tk.Label(check, text=f"  г. Екатеринбург, ул. Сулиманова.,50", font=("Helvetica", 20), anchor="w")
    label_center.pack(anchor="w")
    formatted_date = now.strftime("%Y-%m-%d %H:%M")
    label_center = tk.Label(check, text=f" Дата Время               {formatted_date}", font=("Helvetica", 20),
                            anchor="w")
    label_center.pack()
    text_label_3 = tk.Label(check, text="-----------------------------------------------------------------------",
                            font=("Helvetica", 20))
    text_label_3.pack()
    check.mainloop()


# Oкно расписания
def b2():
    def b4(filmname, date, kino_teatr):
        W = Toplevel(w2)
        W.title('ВЫБОР МЕСТА')
        W.iconbitmap('icon.ico')
        W.config(width=1024, height=720)
        W.resizable(False, False)
        global count
        count = 0
        global list
        list = []
        global fname
        fname = filmname
        global time
        time = date
        global kinoteatrr
        kinoteatrr = kino_teatr

        bg_color = '#24262C'
        grey = 'grey56'
        font = ('Calibri 20')

        def buying():
            global count
            W1 = Toplevel(w2)
            W1.iconbitmap('icon.ico')
            W1.config(width=700, height=400, background=bg_color)
            W1.resizable(False, False)

            logo = PhotoImage(file='logotip-premer-zal-optimized.png')
            logotip = Label(W1, image=logo, background=bg_color).place(x=100, y=100)

            def get_value():
                return var.get()

            if count == 0:
                info = Label(W1, background=bg_color, foreground='white', text=f'Вы не выбрали ни одного билета',
                             font=font).place(x=30, y=50)
            else:
                info = Label(W1, background=bg_color, foreground='white',
                             text=f'Количество билетов: {count} шт., итого к оплате: {count * 230} рублей',
                             font=font).place(x=30, y=50)

            def get_value():
                # Эта функция вызывается при изменении состояния чекбокса
                if var.get() == 1:  # Проверка, установлен ли флажок
                    buy_button.config(state=tk.NORMAL)  # Делаем кнопку активной
                else:
                    buy_button.config(state=tk.DISABLED)  # Делаем кнопку неактивной

            var = IntVar()
            cb = Checkbutton(W1, text="""Я согласен с условиями пользования
        и правилами к-т 'Премьер Зал" """,
                             variable=var,
                             command=get_value, background=bg_color, foreground='green', activeforeground='green',
                             font=font, activebackground=bg_color).place(x=30, y=100)

            buy_button = Button(W1, image=buy_image, borderwidth=0, background=bg_color, activebackground=bg_color,
                                command=partial(bilet, filmname, date, kino_teatr), state=tk.DISABLED)
            buy_button.place(x=30, y=200)

        """                          БЛОК РАЗМЕТКИ СТРАНИЦЫ                    """

        seet_button = PhotoImage(file='seet.png')
        seet_press = PhotoImage(file='seet_press.png')
        buy_image = PhotoImage(file='buy.png')

        bg = Label(W, background=bg_color).place(x=0, y=0, width=1280, height=960)  # Цвет фона

        cinema_name = Label(W, text=f'{filmname}', font=font, background=bg_color,
                            foreground='white')  # Обозначение имени фильма
        cinema_name.place(x=10, y=10)

        buy = Button(W, image=buy_image, borderwidth=0, background=bg_color, activebackground=bg_color, command=buying)
        buy.place(x=830, y=-5)

        date_film = Label(W, background=bg_color, text=f'{date}', font='Calibri 15', foreground=grey)  # Дата показа
        date_film.place(x=10, y=45)

        border = Label(W, background='white').place(x=0, y=90, width=1280, height=1)

        screen = Label(W, background=bg_color, text='ЭКРАН', font='Calibri 23', foreground=grey)
        screen.place(x=450, y=110)

        # cnt = Label(W, background=bg_color, text=f'КОЛИЧЕСТВО: {count}', font=font, foreground=grey).place(x=650, y=110)
        # char = Label(W, background=bg_color, text=count.get(), font=font, foreground=grey).place(x=830, y=110)

        """                            БЛОК ФУНКЦИОНАЛА КНОПОК                      """

        def navod_11(e):
            global list
            global count
            if seet11['state'] == NORMAL:
                seet11['image'] = seet_press
                seet11.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 1")
                seet11['image'] = seet_press

        def otvod_11(e):
            global count
            global list
            if seet11['state'] == DISABLED:
                seet11.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 1')
                seet11['image'] = seet_button

        def navod_12(e):
            global list
            global count
            if seet12['state'] == NORMAL:
                seet12.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 2")
                seet12['image'] = seet_press

        def otvod_12(e):
            global count
            global list
            if seet12['state'] == DISABLED:
                seet12.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 2')
                seet12['image'] = seet_button

        def navod_13(e):
            global count
            global list
            if seet13['state'] == NORMAL:
                seet13.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 3")
                seet13['image'] = seet_press

        def otvod_13(e):
            global count
            global list
            if seet13['state'] == DISABLED:
                seet13.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 3')
                seet13['image'] = seet_button

        def navod_14(e):
            global count
            global list
            if seet14['state'] == NORMAL:
                seet14.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 4")
                seet14['image'] = seet_press

        def otvod_14(e):
            global count
            global list
            if seet14['state'] == DISABLED:
                seet14.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 4')
                seet14['image'] = seet_button

        def navod_15(e):
            global count
            global list
            if seet15['state'] == NORMAL:
                seet15.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 5")
                seet15['image'] = seet_press

        def otvod_15(e):
            global count
            global list
            if seet15['state'] == DISABLED:
                seet15.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 5')
                seet15['image'] = seet_button

        def navod_16(e):
            global count
            global list
            if seet16['state'] == NORMAL:
                seet16.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 6")
                seet16['image'] = seet_press

        def otvod_16(e):
            global count
            global list
            if seet16['state'] == DISABLED:
                seet16.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 6')
                seet16['image'] = seet_button

        def navod_17(e):
            global count
            global list
            if seet17['state'] == NORMAL:
                seet17.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 7")
                seet17['image'] = seet_press

        def otvod_17(e):
            global count
            global list
            if seet17['state'] == DISABLED:
                seet17.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 7')
                seet17['image'] = seet_button

        def navod_18(e):
            global count
            global list
            if seet18['state'] == NORMAL:
                seet18.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 8")
                seet18['image'] = seet_press

        def otvod_18(e):
            global count
            global list
            if seet18['state'] == DISABLED:
                seet18.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 8')
                seet18['image'] = seet_button

        def navod_19(e):
            global count
            global list
            if seet19['state'] == NORMAL:
                seet19.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 9")
                seet19['image'] = seet_press

        def otvod_19(e):
            global count
            global list
            if seet19['state'] == DISABLED:
                seet19.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 9')

                seet19['image'] = seet_button

        def navod_110(e):
            global count
            global list
            if seet110['state'] == NORMAL:
                seet110.config(state=DISABLED)
                count += 1
                list.append("Ряд 1 место 10")
                seet110['image'] = seet_press

        def otvod_110(e):
            global count
            global list
            if seet110['state'] == DISABLED:
                seet110.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 1 место 10')
                seet110['image'] = seet_button

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        def navod_21(e):
            global count
            global list
            if seet21['state'] == NORMAL:
                seet21.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 1")
                seet21['image'] = seet_press

        def otvod_21(e):
            global count
            global list
            if seet21['state'] == DISABLED:
                seet21.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 1')
                seet21['image'] = seet_button

        def navod_22(e):
            global count
            global list
            if seet22['state'] == NORMAL:
                seet22.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 2")
                seet22['image'] = seet_press

        def otvod_22(e):
            global count
            global list
            if seet22['state'] == DISABLED:
                seet22.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 2')
                seet22['image'] = seet_button

        def navod_23(e):
            global count
            global list
            if seet23['state'] == NORMAL:
                seet23.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 3")
                seet23['image'] = seet_press

        def otvod_23(e):
            global count
            global list
            if seet23['state'] == DISABLED:
                seet23.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 3')
                seet23['image'] = seet_button

        def navod_24(e):
            global count
            global list
            if seet24['state'] == NORMAL:
                seet24.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 4")
                seet24['image'] = seet_press

        def otvod_24(e):
            global count
            global list
            if seet24['state'] == DISABLED:
                seet24.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 4')
                seet24['image'] = seet_button

        def navod_25(e):
            global count
            global list
            if seet25['state'] == NORMAL:
                seet25.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 5")
                seet25['image'] = seet_press

        def otvod_25(e):
            global count
            global list
            if seet25['state'] == DISABLED:
                seet25.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 5')
                seet25['image'] = seet_button

        def navod_26(e):
            global count
            global list
            if seet26['state'] == NORMAL:
                seet26.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 6")
                seet26['image'] = seet_press

        def otvod_26(e):
            global count
            global list
            if seet26['state'] == DISABLED:
                seet26.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 6')
                seet26['image'] = seet_button

        def navod_27(e):
            global count
            global list
            if seet27['state'] == NORMAL:
                seet27.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 7")
                seet27['image'] = seet_press

        def otvod_27(e):
            global count
            global list
            if seet27['state'] == DISABLED:
                seet27.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 7')
                seet27['image'] = seet_button

        def navod_28(e):
            global count
            global list
            if seet28['state'] == NORMAL:
                seet28.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 8")
                seet28['image'] = seet_press

        def otvod_28(e):
            global count
            global list
            if seet28['state'] == DISABLED:
                seet28.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 8')
                seet28['image'] = seet_button

        def navod_29(e):
            global count
            global list
            if seet29['state'] == NORMAL:
                seet29.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 9")
                seet29['image'] = seet_press

        def otvod_29(e):
            global count
            global list
            if seet29['state'] == DISABLED:
                seet29.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 9')
                seet29['image'] = seet_button

        def navod_210(e):
            global count
            global list
            if seet210['state'] == NORMAL:
                seet210.config(state=DISABLED)
                count += 1
                list.append("Ряд 2 место 10")
                seet210['image'] = seet_press

        def otvod_210(e):
            global count
            global list
            if seet210['state'] == DISABLED:
                seet210.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 2 место 10')
                seet210['image'] = seet_button

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        def navod_31(e):
            global count
            global list
            if seet31['state'] == NORMAL:
                seet31.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 1")
                seet31['image'] = seet_press

        def otvod_31(e):
            global count
            global list
            if seet31['state'] == DISABLED:
                seet31.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 1')
                seet31['image'] = seet_button

        def navod_32(e):
            global count
            global list
            if seet32['state'] == NORMAL:
                seet32.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 2")
                seet32['image'] = seet_press

        def otvod_32(e):
            global count
            global list
            if seet32['state'] == DISABLED:
                seet32.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 2')
                seet32['image'] = seet_button

        def navod_33(e):
            global count
            global list
            if seet33['state'] == NORMAL:
                seet33.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 3")
                seet33['image'] = seet_press

        def otvod_33(e):
            global count
            global list
            if seet33['state'] == DISABLED:
                seet33.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 3')
                seet33['image'] = seet_button

        def navod_34(e):
            global count
            global list
            if seet34['state'] == NORMAL:
                seet34.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 4")
                seet34['image'] = seet_press

        def otvod_34(e):
            global count
            global list
            if seet34['state'] == DISABLED:
                seet34.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 4')
                seet34['image'] = seet_button

        def navod_35(e):
            global count
            global list
            if seet35['state'] == NORMAL:
                seet35.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 5")
                seet35['image'] = seet_press

        def otvod_35(e):
            global count
            global list
            if seet35['state'] == DISABLED:
                seet35.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 5')
                seet35['image'] = seet_button

        def navod_36(e):
            global count
            global list
            if seet36['state'] == NORMAL:
                seet36.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 6")
                seet36['image'] = seet_press

        def otvod_36(e):
            global count
            global list
            if seet36['state'] == DISABLED:
                seet36.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 6')
                seet36['image'] = seet_button

        def navod_37(e):
            global count
            global list
            if seet37['state'] == NORMAL:
                seet37.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 7")
                seet37['image'] = seet_press

        def otvod_37(e):
            global count
            global list
            if seet37['state'] == DISABLED:
                seet37.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 7')
                seet37['image'] = seet_button

        def navod_38(e):
            global count
            global list
            if seet38['state'] == NORMAL:
                seet38.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 8")
                seet38['image'] = seet_press

        def otvod_38(e):
            global count
            global list
            if seet38['state'] == DISABLED:
                seet38.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 8')
                seet38['image'] = seet_button

        def navod_39(e):
            global count
            global list
            if seet39['state'] == NORMAL:
                seet39.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 9")
                seet39['image'] = seet_press

        def otvod_39(e):
            global count
            global list
            if seet39['state'] == DISABLED:
                seet39.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 9')
                seet39['image'] = seet_button

        def navod_310(e):
            global count
            global list
            if seet310['state'] == NORMAL:
                seet310.config(state=DISABLED)
                count += 1
                list.append("Ряд 3 место 10")
                seet310['image'] = seet_press

        def otvod_310(e):
            global count
            global list
            if seet310['state'] == DISABLED:
                seet310.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 3 место 10')
                seet310['image'] = seet_button

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        def navod_41(e):
            global count
            global list
            if seet41['state'] == NORMAL:
                seet41.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 1")
                seet41['image'] = seet_press

        def otvod_41(e):
            global count
            global list
            if seet41['state'] == DISABLED:
                seet41.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 1')
                seet41['image'] = seet_button

        def navod_42(e):
            global count
            global list
            if seet42['state'] == NORMAL:
                seet42.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 2")
                seet42['image'] = seet_press

        def otvod_42(e):
            global count
            global list
            if seet42['state'] == DISABLED:
                seet42.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 2')
                seet42['image'] = seet_button

        def navod_43(e):
            global count
            global list
            if seet43['state'] == NORMAL:
                seet43.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 3")
                seet43['image'] = seet_press

        def otvod_43(e):
            global count
            global list
            if seet43['state'] == DISABLED:
                seet43.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 3')
                seet43['image'] = seet_button

        def navod_44(e):
            global count
            global list
            if seet44['state'] == NORMAL:
                seet44.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 4")
                seet44['image'] = seet_press

        def otvod_44(e):
            global count
            global list
            if seet44['state'] == DISABLED:
                seet44.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 4')
                seet44['image'] = seet_button

        def navod_45(e):
            global count
            global list
            if seet45['state'] == NORMAL:
                seet45.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 5")
                seet45['image'] = seet_press

        def otvod_45(e):
            global count
            global list
            if seet45['state'] == DISABLED:
                seet45.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 5')
                seet45['image'] = seet_button

        def navod_46(e):
            global count
            global list
            if seet46['state'] == NORMAL:
                seet46.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 6")
                seet46['image'] = seet_press

        def otvod_46(e):
            global count
            global list
            if seet46['state'] == DISABLED:
                seet46.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 6')
                seet46['image'] = seet_button

        def navod_47(e):
            global count
            global list
            if seet47['state'] == NORMAL:
                seet47.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 7")
                seet47['image'] = seet_press

        def otvod_47(e):
            global count
            global list
            if seet47['state'] == DISABLED:
                seet47.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 7')
                seet47['image'] = seet_button

        def navod_48(e):
            global count
            global list
            if seet48['state'] == NORMAL:
                seet48.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 8")
                seet48['image'] = seet_press

        def otvod_48(e):
            global count
            global list
            if seet48['state'] == DISABLED:
                seet48.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 8')
                seet48['image'] = seet_button

        def navod_49(e):
            global count
            global list
            if seet49['state'] == NORMAL:
                seet49.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 9")
                seet49['image'] = seet_press

        def otvod_49(e):
            global count
            global list
            if seet49['state'] == DISABLED:
                seet49.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 9')
                seet49['image'] = seet_button

        def navod_410(e):
            global count
            global list
            if seet410['state'] == NORMAL:
                seet410.config(state=DISABLED)
                count += 1
                list.append("Ряд 4 место 10")
                seet410['image'] = seet_press

        def otvod_410(e):
            global count
            global list
            if seet410['state'] == DISABLED:
                seet410.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 4 место 10')
                seet410['image'] = seet_button

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        def navod_51(e):
            global count
            global list
            if seet51['state'] == NORMAL:
                seet51.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 1")
                seet51['image'] = seet_press

        def otvod_51(e):
            global count
            global list
            if seet51['state'] == DISABLED:
                seet51.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 1')
                seet51['image'] = seet_button

        def navod_52(e):
            global count
            global list
            if seet52['state'] == NORMAL:
                seet52.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 2")
                seet52['image'] = seet_press

        def otvod_52(e):
            global count
            global list
            if seet52['state'] == DISABLED:
                seet52.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 2')
                seet52['image'] = seet_button

        def navod_53(e):
            global count
            global list
            if seet53['state'] == NORMAL:
                seet53.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 3")
                seet53['image'] = seet_press

        def otvod_53(e):
            global count
            global list
            if seet53['state'] == DISABLED:
                seet53.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 3')
                seet53['image'] = seet_button

        def navod_54(e):
            global count
            global list
            if seet54['state'] == NORMAL:
                seet54.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 4")
                seet54['image'] = seet_press

        def otvod_54(e):
            global count
            global list
            if seet54['state'] == DISABLED:
                seet54.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 4')
                seet54['image'] = seet_button

        def navod_55(e):
            global count
            global list
            if seet55['state'] == NORMAL:
                seet55.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 5")
                seet55['image'] = seet_press

        def otvod_55(e):
            global count
            global list
            if seet55['state'] == DISABLED:
                seet55.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 5')
                seet55['image'] = seet_button

        def navod_56(e):
            global count
            global list
            if seet56['state'] == NORMAL:
                seet56.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 6")
                seet56['image'] = seet_press

        def otvod_56(e):
            global count
            global list
            if seet56['state'] == DISABLED:
                seet56.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 6')
                seet56['image'] = seet_button

        def navod_57(e):
            global count
            global list
            if seet57['state'] == NORMAL:
                seet57.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 7")
                seet57['image'] = seet_press

        def otvod_57(e):
            global count
            global list
            if seet57['state'] == DISABLED:
                seet57.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 7')
                seet57['image'] = seet_button

        def navod_58(e):
            global count
            global list
            if seet58['state'] == NORMAL:
                seet58.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 8")
                seet58['image'] = seet_press

        def otvod_58(e):
            global count
            global list
            if seet58['state'] == DISABLED:
                seet58.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 8')
                seet58['image'] = seet_button

        def navod_59(e):
            global count
            global list
            if seet59['state'] == NORMAL:
                seet59.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 9")
                seet59['image'] = seet_press

        def otvod_59(e):
            global count
            global list
            if seet59['state'] == DISABLED:
                seet59.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 9')
                seet59['image'] = seet_button

        def navod_510(e):
            global count
            global list
            if seet510['state'] == NORMAL:
                seet510.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 10")

                seet510['image'] = seet_press

        def otvod_510(e):
            global count
            global list
            if seet510['state'] == DISABLED:
                seet510.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 10')
                seet510['image'] = seet_button

        def navod_511(e):
            global count
            global list
            if seet511['state'] == NORMAL:
                seet511.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 11")
                seet511['image'] = seet_press

        def otvod_511(e):
            global count
            global list
            if seet511['state'] == DISABLED:
                seet511.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 11')
                seet511['image'] = seet_button

        def navod_512(e):
            global count
            global list
            if seet512['state'] == NORMAL:
                seet512.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 12")
                seet512['image'] = seet_press

        def otvod_512(e):
            global count
            global list
            if seet512['state'] == DISABLED:
                seet512.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 12')
                seet512['image'] = seet_button

        def navod_513(e):
            global count
            global list
            if seet513['state'] == NORMAL:
                seet513.config(state=DISABLED)
                count += 1
                list.append("Ряд 5 место 13")
                seet513['image'] = seet_press

        def otvod_513(e):
            global count
            global list
            if seet513['state'] == DISABLED:
                seet513.config(state=NORMAL)
                count -= 1
                list.remove('Ряд 5 место 13')
                seet513['image'] = seet_button

        """ПЕРВЫЙ РЯД"""
        seet11 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color,
                        state=NORMAL)
        seet11.place(x=170, y=200)
        seet11.bind('<Button-1>', navod_11)
        seet11.bind('<ButtonRelease-3>', otvod_11)

        seet12 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet12.place(x=220, y=200)
        seet12.bind('<Button-1>', navod_12)
        seet12.bind('<ButtonRelease-3>', otvod_12)

        seet13 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet13.place(x=270, y=200)
        seet13.bind('<Button-1>', navod_13)
        seet13.bind('<ButtonRelease-3>', otvod_13)

        seet14 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet14.place(x=320, y=200)
        seet14.bind('<Button-1>', navod_14)
        seet14.bind('<ButtonRelease-3>', otvod_14)

        seet15 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet15.place(x=370, y=200)
        seet15.bind('<Button-1>', navod_15)
        seet15.bind('<ButtonRelease-3>', otvod_15)

        seet16 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet16.place(x=570, y=200)
        seet16.bind('<Button-1>', navod_16)
        seet16.bind('<ButtonRelease-3>', otvod_16)

        seet17 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet17.place(x=620, y=200)
        seet17.bind('<Button-1>', navod_17)
        seet17.bind('<ButtonRelease-3>', otvod_17)

        seet18 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet18.place(x=670, y=200)
        seet18.bind('<Button-1>', navod_18)
        seet18.bind('<ButtonRelease-3>', otvod_18)

        seet19 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet19.place(x=720, y=200)
        seet19.bind('<Button-1>', navod_19)
        seet19.bind('<ButtonRelease-3>', otvod_19)

        seet110 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet110.place(x=770, y=200)
        seet110.bind('<Button-1>', navod_110)
        seet110.bind('<ButtonRelease-3>', otvod_110)

        """ВТОРОЙ РЯД"""
        seet21 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet21.place(x=170, y=300)
        seet21.bind('<Button-1>', navod_21)
        seet21.bind('<ButtonRelease-3>', otvod_21)

        seet22 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet22.place(x=220, y=300)
        seet22.bind('<Button-1>', navod_22)
        seet22.bind('<ButtonRelease-3>', otvod_22)

        seet23 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet23.place(x=270, y=300)
        seet23.bind('<Button-1>', navod_23)
        seet23.bind('<ButtonRelease-3>', otvod_23)

        seet24 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet24.place(x=320, y=300)
        seet24.bind('<Button-1>', navod_24)
        seet24.bind('<ButtonRelease-3>', otvod_24)

        seet25 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet25.place(x=370, y=300)
        seet25.bind('<Button-1>', navod_25)
        seet25.bind('<ButtonRelease-3>', otvod_25)

        seet26 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet26.place(x=570, y=300)
        seet26.bind('<Button-1>', navod_26)
        seet26.bind('<ButtonRelease-3>', otvod_26)

        seet27 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet27.place(x=620, y=300)
        seet27.bind('<Button-1>', navod_27)
        seet27.bind('<ButtonRelease-3>', otvod_27)

        seet28 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet28.place(x=670, y=300)
        seet28.bind('<Button-1>', navod_28)
        seet28.bind('<ButtonRelease-3>', otvod_28)

        seet29 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet29.place(x=720, y=300)
        seet29.bind('<Button-1>', navod_29)
        seet29.bind('<ButtonRelease-3>', otvod_29)

        seet210 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet210.place(x=770, y=300)
        seet210.bind('<Button-1>', navod_210)
        seet210.bind('<ButtonRelease-3>', otvod_210)

        """ТРЕТИЙ РЯД"""
        seet31 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet31.place(x=170, y=400)
        seet31.bind('<Button-1>', navod_31)
        seet31.bind('<ButtonRelease-3>', otvod_31)

        seet32 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet32.place(x=220, y=400)
        seet32.bind('<Button-1>', navod_32)
        seet32.bind('<ButtonRelease-3>', otvod_32)

        seet33 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet33.place(x=270, y=400)
        seet33.bind('<Button-1>', navod_33)
        seet33.bind('<ButtonRelease-3>', otvod_33)

        seet34 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet34.place(x=320, y=400)
        seet34.bind('<Button-1>', navod_34)
        seet34.bind('<ButtonRelease-3>', otvod_34)

        seet35 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet35.place(x=370, y=400)
        seet35.bind('<Button-1>', navod_35)
        seet35.bind('<ButtonRelease-3>', otvod_35)

        seet36 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet36.place(x=570, y=400)
        seet36.bind('<Button-1>', navod_36)
        seet36.bind('<ButtonRelease-3>', otvod_36)

        seet37 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet37.place(x=620, y=400)
        seet37.bind('<Button-1>', navod_37)
        seet37.bind('<ButtonRelease-3>', otvod_37)

        seet38 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet38.place(x=670, y=400)
        seet38.bind('<Button-1>', navod_38)
        seet38.bind('<ButtonRelease-3>', otvod_38)

        seet39 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet39.place(x=720, y=400)
        seet39.bind('<Button-1>', navod_39)
        seet39.bind('<ButtonRelease-3>', otvod_39)

        seet310 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet310.place(x=770, y=400)
        seet310.bind('<Button-1>', navod_310)
        seet310.bind('<ButtonRelease-3>', otvod_310)

        """ЧЕТВЕРТЫЙ РЯД"""
        seet41 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet41.place(x=170, y=500)
        seet41.bind('<Button-1>', navod_41)
        seet41.bind('<ButtonRelease-3>', otvod_41)

        seet42 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet42.place(x=220, y=500)
        seet42.bind('<Button-1>', navod_42)
        seet42.bind('<ButtonRelease-3>', otvod_42)

        seet43 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet43.place(x=270, y=500)
        seet43.bind('<Button-1>', navod_43)
        seet43.bind('<ButtonRelease-3>', otvod_43)

        seet44 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet44.place(x=320, y=500)
        seet44.bind('<Button-1>', navod_44)
        seet44.bind('<ButtonRelease-3>', otvod_44)

        seet45 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet45.place(x=370, y=500)
        seet45.bind('<Button-1>', navod_45)
        seet45.bind('<ButtonRelease-3>', otvod_45)

        seet46 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet46.place(x=570, y=500)
        seet46.bind('<Button-1>', navod_46)
        seet46.bind('<ButtonRelease-3>', otvod_46)

        seet47 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet47.place(x=620, y=500)
        seet47.bind('<Button-1>', navod_47)
        seet47.bind('<ButtonRelease-3>', otvod_47)

        seet48 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet48.place(x=670, y=500)
        seet48.bind('<Button-1>', navod_48)
        seet48.bind('<ButtonRelease-3>', otvod_48)

        seet49 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet49.place(x=720, y=500)
        seet49.bind('<Button-1>', navod_49)
        seet49.bind('<ButtonRelease-3>', otvod_49)

        seet410 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet410.place(x=770, y=500)
        seet410.bind('<Button-1>', navod_410)
        seet410.bind('<ButtonRelease-3>', otvod_410)

        """ПЯТЫЙ РЯД"""

        seet51 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet51.place(x=170, y=600)
        seet51.bind('<Button-1>', navod_51)
        seet51.bind('<ButtonRelease-3>', otvod_51)

        seet52 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet52.place(x=220, y=600)
        seet52.bind('<Button-1>', navod_52)
        seet52.bind('<ButtonRelease-3>', otvod_52)

        seet53 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet53.place(x=270, y=600)
        seet53.bind('<Button-1>', navod_53)
        seet53.bind('<ButtonRelease-3>', otvod_53)

        seet54 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet54.place(x=320, y=600)
        seet54.bind('<Button-1>', navod_54)
        seet54.bind('<ButtonRelease-3>', otvod_54)

        seet55 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet55.place(x=370, y=600)
        seet55.bind('<Button-1>', navod_55)
        seet55.bind('<ButtonRelease-3>', otvod_55)

        seet56 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet56.place(x=420, y=600)
        seet56.bind('<Button-1>', navod_56)
        seet56.bind('<ButtonRelease-3>', otvod_56)

        seet57 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet57.place(x=470, y=600)
        seet57.bind('<Button-1>', navod_57)
        seet57.bind('<ButtonRelease-3>', otvod_57)

        seet58 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet58.place(x=520, y=600)
        seet58.bind('<Button-1>', navod_58)
        seet58.bind('<ButtonRelease-3>', otvod_58)

        seet59 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet59.place(x=570, y=600)
        seet59.bind('<Button-1>', navod_59)
        seet59.bind('<ButtonRelease-3>', otvod_59)

        seet510 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet510.place(x=620, y=600)
        seet510.bind('<Button-1>', navod_510)
        seet510.bind('<ButtonRelease-3>', otvod_510)

        seet511 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet511.place(x=670, y=600)
        seet511.bind('<Button-1>', navod_511)
        seet511.bind('<ButtonRelease-3>', otvod_511)

        seet512 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet512.place(x=720, y=600)
        seet512.bind('<Button-1>', navod_512)
        seet512.bind('<ButtonRelease-3>', otvod_512)

        seet513 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
        seet513.place(x=770, y=600)
        seet513.bind('<Button-1>', navod_513)
        seet513.bind('<ButtonRelease-3>', otvod_513)

        W.mainloop()

    w2 = Toplevel(m)
    w2.iconbitmap('icon.ico')
    w2.title('РАСПИСАНИЕ')
    w2.resizable(False, False)
    w2.geometry('1280x960')
    ik6 = PhotoImage(file='незнакомцы.png')
    ik7 = PhotoImage(file='Винни Пух.png')
    ik8 = PhotoImage(file='суперпташки.png')
    ik9 = PhotoImage(file='судная ночь.png')
    ik10 = PhotoImage(file='Асфальтовые джунгли.png')

    def on_mouse_wheel(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def on_selection_change(*args):
        option = selected_option.get()
        if option in "30.05.2024":
            canvas.create_image(300, 500, image=ik6)
            canvas.create_image(300, 850, image=ik7)
            canvas.create_image(300, 1200, image=ik8)
            canvas.create_image(300, 1550, image=ik9)
            canvas.create_image(300, 1900, image=ik10)
        elif option in "31.05.2024":
            canvas.create_image(300, 500, image=ik2)
            canvas.create_image(300, 850, image=ik4)
            canvas.create_image(300, 1200, image=ik6)
            canvas.create_image(300, 1550, image=ik8)
            canvas.create_image(300, 1900, image=ik10)
        elif option in "01.06.2024":
            canvas.create_image(300, 500, image=ik1)
            canvas.create_image(300, 850, image=ik3)
            canvas.create_image(300, 1200, image=ik5)
            canvas.create_image(300, 1550, image=ik7)
            canvas.create_image(300, 1900, image=ik9)
        elif option in "02.06.2024":
            canvas.create_image(300, 500, image=ik3)
            canvas.create_image(300, 850, image=ik4)
            canvas.create_image(300, 1200, image=ik5)
            canvas.create_image(300, 1550, image=ik6)
            canvas.create_image(300, 1900, image=ik7)
        else:
            canvas.create_image(300, 500, image=ik1)
            canvas.create_image(300, 850, image=ik2)
            canvas.create_image(300, 1200, image=ik3)
            canvas.create_image(300, 1550, image=ik4)
            canvas.create_image(300, 1900, image=ik5)

    scrollable_frame = tk.Frame(w2)
    scrollable_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(scrollable_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(scrollable_frame, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.config(yscrollcommand=scrollbar.set)

    canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox("all")))
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    image = tk.PhotoImage(file="raspback2.png")
    canvas.create_image(0, 0, image=image, anchor=tk.NW)

    canvas.create_text(400, 200, text='Расписание', fill="Black", font=("Rostov", 48))

    selected_option = StringVar(canvas)
    selected_option.set("29.05.2024")
    options = ["29.05.2024", "30.05.2024", "31.05.2024", "1.06.2024", "2.06.2024"]
    custom_font = font.Font(family="Helvetica", size=14)

    dropdown = OptionMenu(canvas, selected_option, *options)
    dropdown_window = canvas.create_window(230, 270, anchor=tk.NW, window=dropdown)
    dropdown.config(font=custom_font)
    menu = dropdown["menu"]

    for i in range(len(options)):
        menu.entryconfig(i, font=custom_font)
        menu.entryconfig(i, foreground="black", background="white")

    selected_option.trace("w", on_selection_change)
    ik1 = ImageTk.PhotoImage(file='Майор Гром.png')
    canvas.create_text(420, 380, text='Премьер Зал Парк Хаус', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 450, text='ККЦ "Премьер Зал Омега"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 520, text='ККЦ "Премьер Зал Гранат"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_image(300, 500, image=ik1)
    ik2 = ImageTk.PhotoImage(file='Министерство неджентельменских дел.png')
    canvas.create_text(420, 730, text='Премьер Зал Парк Хаус', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 800, text='ККЦ "Премьер Зал Омега"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 870, text='ККЦ "Премьер Зал Гранат"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_image(300, 850, image=ik2)
    ik3 = ImageTk.PhotoImage(file='Планета обезьян.png')
    canvas.create_text(420, 1080, text='Премьер Зал Парк Хаус', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 1150, text='ККЦ "Премьер Зал Омега"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 1220, text='ККЦ "Премьер Зал Гранат"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_image(300, 1200, image=ik3)
    ik4 = ImageTk.PhotoImage(file='Пушистый вояж.png')
    canvas.create_text(420, 1430, text='Премьер Зал Парк Хаус', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 1500, text='ККЦ "Премьер Зал Омега"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 1570, text='ККЦ "Премьер Зал Гранат"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_image(300, 1550, image=ik4)
    ik5 = ImageTk.PhotoImage(file='Сто лет тому вперед.png')
    canvas.create_text(420, 1780, text='Премьер Зал Парк Хаус', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 1850, text='ККЦ "Премьер Зал Омега"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_text(420, 1920, text='ККЦ "Премьер Зал Гранат"', fill="Black", width=270, font=("Helvetica", 15),
                       anchor=tk.W)
    canvas.create_image(300, 1900, image=ik5)
    f1 = font.Font(family="Helvetica", size=12, weight="bold")

    # изменение кнопки при наведении
    g = "#f0f4f7"

    def e1_1_1(e):
        button1_1_1.config(bg=purple, fg=black)

    def l1_1_1(e):
        button1_1_1.config(bg=g, fg=purple)

    def e1_1_2(e):
        button1_1_2.config(bg=purple, fg=black)

    def l1_1_2(e):
        button1_1_2.config(bg=g, fg=purple)

    def e1_1_3(e):
        button1_1_3.config(bg=purple, fg=black)

    def l1_1_3(e):
        button1_1_3.config(bg=g, fg=purple)

    def e1_2_1(e):
        button1_2_1.config(bg=purple, fg=black)

    def l1_2_1(e):
        button1_2_1.config(bg=g, fg=purple)

    def e1_2_2(e):
        button1_2_2.config(bg=purple, fg=black)

    def l1_2_2(e):
        button1_2_2.config(bg=g, fg=purple)

    def e1_3_1(e):
        button1_3_1.config(bg=purple, fg=black)

    def l1_3_1(e):
        button1_3_1.config(bg=g, fg=purple)

    def e1_3_2(e):
        button1_3_2.config(bg=purple, fg=black)

    def l1_3_2(e):
        button1_3_2.config(bg=g, fg=purple)

    def e1_3_3(e):
        button1_3_3.config(bg=purple, fg=black)

    def l1_3_3(e):
        button1_3_3.config(bg=g, fg=purple)

    def e2_1_1(e):
        button2_1_1.config(bg=purple, fg=black)

    def l2_1_1(e):
        button2_1_1.config(bg=g, fg=purple)

    def e2_1_2(e):
        button2_1_2.config(bg=purple, fg=black)

    def l2_1_2(e):
        button2_1_2.config(bg=g, fg=purple)

    def e2_2_1(e):
        button2_2_1.config(bg=purple, fg=black)

    def l2_2_1(e):
        button2_2_1.config(bg=g, fg=purple)

    def e2_2_2(e):
        button2_2_2.config(bg=purple, fg=black)

    def l2_2_2(e):
        button2_2_2.config(bg=g, fg=purple)

    def e2_2_3(e):
        button2_2_3.config(bg=purple, fg=black)

    def l2_2_3(e):
        button2_2_3.config(bg=g, fg=purple)

    def e2_3_1(e):
        button2_3_1.config(bg=purple, fg=black)

    def l2_3_1(e):
        button2_3_1.config(bg=g, fg=purple)

    def e2_3_2(e):
        button2_3_2.config(bg=purple, fg=black)

    def l2_3_2(e):
        button2_3_2.config(bg=g, fg=purple)

    def e2_3_3(e):
        button2_3_3.config(bg=purple, fg=black)

    def l2_3_3(e):
        button2_3_3.config(bg=g, fg=purple)

    def e3_1_1(e):
        button3_1_1.config(bg=purple, fg=black)

    def l3_1_1(e):
        button3_1_1.config(bg=g, fg=purple)

    def e3_1_2(e):
        button3_1_2.config(bg=purple, fg=black)

    def l3_1_2(e):
        button3_1_2.config(bg=g, fg=purple)

    def e3_1_3(e):
        button3_1_3.config(bg=purple, fg=black)

    def l3_1_3(e):
        button3_1_3.config(bg=g, fg=purple)

    def e3_2_1(e):
        button3_2_1.config(bg=purple, fg=black)

    def l3_2_1(e):
        button3_2_1.config(bg=g, fg=purple)

    def e3_2_2(e):
        button3_2_2.config(bg=purple, fg=black)

    def l3_2_2(e):
        button3_2_2.config(bg=g, fg=purple)

    def e3_2_3(e):
        button3_2_3.config(bg=purple, fg=black)

    def l3_2_3(e):
        button3_2_3.config(bg=g, fg=purple)

    def e3_3_1(e):
        button3_3_1.config(bg=purple, fg=black)

    def l3_3_1(e):
        button3_3_1.config(bg=g, fg=purple)

    def e3_3_2(e):
        button3_3_2.config(bg=purple, fg=black)

    def l3_3_2(e):
        button3_3_2.config(bg=g, fg=purple)

    def e4_1_1(e):
        button4_1_1.config(bg=purple, fg=black)

    def l4_1_1(e):
        button4_1_1.config(bg=g, fg=purple)

    def e4_1_2(e):
        button4_1_2.config(bg=purple, fg=black)

    def l4_1_2(e):
        button4_1_2.config(bg=g, fg=purple)

    def e4_1_3(e):
        button4_1_3.config(bg=purple, fg=black)

    def l4_1_3(e):
        button4_1_3.config(bg=g, fg=purple)

    def e4_2_1(e):
        button4_2_1.config(bg=purple, fg=black)

    def l4_2_1(e):
        button4_2_1.config(bg=g, fg=purple)

    def e4_2_2(e):
        button4_2_2.config(bg=purple, fg=black)

    def l4_2_2(e):
        button4_2_2.config(bg=g, fg=purple)

    def e4_3_1(e):
        button4_3_1.config(bg=purple, fg=black)

    def l4_3_1(e):
        button4_3_1.config(bg=g, fg=purple)

    def e4_3_2(e):
        button4_3_2.config(bg=purple, fg=black)

    def l4_3_2(e):
        button4_3_2.config(bg=g, fg=purple)

    def e4_3_3(e):
        button4_3_3.config(bg=purple, fg=black)

    def l4_3_3(e):
        button4_3_3.config(bg=g, fg=purple)

    def e5_1_1(e):
        button5_1_1.config(bg=purple, fg=black)

    def l5_1_1(e):
        button5_1_1.config(bg=g, fg=purple)

    def e5_1_2(e):
        button5_1_2.config(bg=purple, fg=black)

    def l5_1_2(e):
        button5_1_2.config(bg=g, fg=purple)

    def e5_2_1(e):
        button5_2_1.config(bg=purple, fg=black)

    def l5_2_1(e):
        button5_2_1.config(bg=g, fg=purple)

    def e5_2_2(e):
        button5_2_2.config(bg=purple, fg=black)

    def l5_2_2(e):
        button5_2_2.config(bg=g, fg=purple)

    def e5_2_3(e):
        button5_2_3.config(bg=purple, fg=black)

    def l5_2_3(e):
        button5_2_3.config(bg=g, fg=purple)

    def e5_3_1(e):
        button5_3_1.config(bg=purple, fg=black)

    def l5_3_1(e):
        button5_3_1.config(bg=g, fg=purple)

    def e5_3_2(e):
        button5_3_2.config(bg=purple, fg=black)

    def l5_3_2(e):
        button5_3_2.config(bg=g, fg=purple)

    def e5_3_3(e):
        button5_3_3.config(bg=purple, fg=black)

    def l5_3_3(e):
        button5_3_3.config(bg=g, fg=purple)

    # КНОПКИ В РАСПИСАНИИ ФИЛЬМ 1
    film = "Майор Гром: Игра"
    time = ["11:45", "14:50", "19:50", "10:30", "17:45", "11:45", "14:50", "19:50"]
    kino_teatr = "Премьер Зал Парк Хаус"
    border_frame1_1_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame1_1_1.pack(pady=15, padx=15)
    button1_1_1 = tk.Button(border_frame1_1_1, text="11:45", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[0], kino_teatr))
    button1_1_1.pack()
    button_window1_1_1 = canvas.create_window(700, 365, anchor=tk.NW, window=border_frame1_1_1)
    button1_1_1.bind('<Enter>', e1_1_1)
    button1_1_1.bind('<Leave>', l1_1_1)

    border_frame1_1_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame1_1_2.pack(pady=15, padx=15)
    button1_1_2 = tk.Button(border_frame1_1_2, text="14:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[1], kino_teatr))
    button1_1_2.pack()
    button_window1_1_2 = canvas.create_window(800, 365, anchor=tk.NW, window=border_frame1_1_2)
    button1_1_2.bind('<Enter>', e1_1_2)
    button1_1_2.bind('<Leave>', l1_1_2)

    border_frame1_1_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame1_1_3.pack(pady=15, padx=15)
    button1_1_3 = tk.Button(border_frame1_1_3, text="19:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[2], kino_teatr))
    button1_1_3.pack()
    button_window1_1_2 = canvas.create_window(900, 365, anchor=tk.NW, window=border_frame1_1_3)
    button1_1_3.bind('<Enter>', e1_1_3)
    button1_1_3.bind('<Leave>', l1_1_3)

    kino_teatr = 'ККЦ "Премьер Зал Омега"'
    border_frame1_2_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame1_2_1.pack(pady=15, padx=15)
    button1_2_1 = tk.Button(border_frame1_2_1, text="10:30", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[3], kino_teatr))
    button1_2_1.pack()
    button_window1_2_1 = canvas.create_window(700, 435, anchor=tk.NW, window=border_frame1_2_1)
    button1_2_1.bind('<Enter>', e1_2_1)
    button1_2_1.bind('<Leave>', l1_2_1)
    border_frame1_2_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame1_2_2.pack(pady=15, padx=15)
    button1_2_2 = tk.Button(border_frame1_2_2, text="17:45", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[4], kino_teatr))
    button1_2_2.pack()
    button_window1_2_2 = canvas.create_window(800, 435, anchor=tk.NW, window=border_frame1_2_2)
    button1_2_2.bind('<Enter>', e1_2_2)
    button1_2_2.bind('<Leave>', l1_2_2)

    kino_teatr = 'ККЦ "Премьер Зал Гранат"'
    border_frame1_3_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame1_3_1.pack(pady=15, padx=15)
    button1_3_1 = tk.Button(border_frame1_3_1, text="11:45", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[5], kino_teatr))
    button1_3_1.pack()
    button_window1_3_1 = canvas.create_window(700, 505, anchor=tk.NW, window=border_frame1_3_1)
    button1_3_1.bind('<Enter>', e1_3_1)
    button1_3_1.bind('<Leave>', l1_3_1)
    border_frame1_3_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame1_3_2.pack(pady=15, padx=15)
    button1_3_2 = tk.Button(border_frame1_3_2, text="14:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[6], kino_teatr))
    button1_3_2.pack()
    button_window1_3_2 = canvas.create_window(800, 505, anchor=tk.NW, window=border_frame1_3_2)
    button1_3_2.bind('<Enter>', e1_3_2)
    button1_3_2.bind('<Leave>', l1_3_2)
    border_frame1_3_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame1_3_3.pack(pady=15, padx=15)
    button1_3_3 = tk.Button(border_frame1_3_3, text="19:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[7], kino_teatr))
    button1_3_3.pack()
    button_window1_3_3 = canvas.create_window(900, 505, anchor=tk.NW, window=border_frame1_3_3)
    button1_3_3.bind('<Enter>', e1_3_3)
    button1_3_3.bind('<Leave>', l1_3_3)

    # КНОПКИ В РАСПИСАНИИ ФИЛЬМ 2
    film = "Министерство неджентельменских дел"
    time = ["10:00", "13:15", "12:40", "15:15", "19:50", "10:10", "13:15", "21:40"]
    kino_teatr = "Премьер Зал Парк Хаус"
    border_frame2_1_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame2_1_1.pack(pady=15, padx=15)
    button2_1_1 = tk.Button(border_frame2_1_1, text="10:00", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[0], kino_teatr))
    button2_1_1.pack()
    button_window2_1_1 = canvas.create_window(700, 715, anchor=tk.NW, window=border_frame2_1_1)
    button2_1_1.bind('<Enter>', e2_1_1)
    button2_1_1.bind('<Leave>', l2_1_1)

    border_frame2_1_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame2_1_2.pack(pady=15, padx=15)
    button2_1_2 = tk.Button(border_frame2_1_2, text="13:15", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[1], kino_teatr))
    button2_1_2.pack()
    button_window2_1_2 = canvas.create_window(800, 715, anchor=tk.NW, window=border_frame2_1_2)
    button2_1_2.bind('<Enter>', e2_1_2)
    button2_1_2.bind('<Leave>', l2_1_2)

    kino_teatr = 'ККЦ "Премьер Зал Омега"'
    border_frame2_2_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame2_2_1.pack(pady=15, padx=15)
    button2_2_1 = tk.Button(border_frame2_2_1, text="12:40", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[2], kino_teatr))
    button2_2_1.pack()
    button_window2_2_1 = canvas.create_window(700, 785, anchor=tk.NW, window=border_frame2_2_1)
    button2_2_1.bind('<Enter>', e2_2_1)
    button2_2_1.bind('<Leave>', l2_2_1)
    border_frame2_2_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame2_2_2.pack(pady=15, padx=15)
    button2_2_2 = tk.Button(border_frame2_2_2, text="15:15", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[3], kino_teatr))
    button2_2_2.pack()
    button_window2_2_2 = canvas.create_window(800, 785, anchor=tk.NW, window=border_frame2_2_2)
    button2_2_2.bind('<Enter>', e2_2_2)
    button2_2_2.bind('<Leave>', l2_2_2)

    border_frame2_2_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame2_2_3.pack(pady=15, padx=15)
    button2_2_3 = tk.Button(border_frame2_2_3, text="19:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[4], kino_teatr))
    button2_2_3.pack()
    button_window2_2_2 = canvas.create_window(900, 785, anchor=tk.NW, window=border_frame2_2_3)
    button2_2_3.bind('<Enter>', e2_2_3)
    button2_2_3.bind('<Leave>', l2_2_3)

    kino_teatr = 'ККЦ "Премьер Зал Гранат"'
    border_frame2_3_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame2_3_1.pack(pady=15, padx=15)
    button2_3_1 = tk.Button(border_frame2_3_1, text="10:10", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[5], kino_teatr))
    button2_3_1.pack()
    button_window2_3_1 = canvas.create_window(700, 855, anchor=tk.NW, window=border_frame2_3_1)
    button2_3_1.bind('<Enter>', e2_3_1)
    button2_3_1.bind('<Leave>', l2_3_1)

    border_frame2_3_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame2_3_2.pack(pady=15, padx=15)
    button2_3_2 = tk.Button(border_frame2_3_2, text="13:15", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[6], kino_teatr))
    button2_3_2.pack()
    button_window2_3_2 = canvas.create_window(800, 855, anchor=tk.NW, window=border_frame2_3_2)
    button2_3_2.bind('<Enter>', e2_3_2)
    button2_3_2.bind('<Leave>', l2_3_2)

    border_frame2_3_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame2_3_3.pack(pady=15, padx=15)
    button2_3_3 = tk.Button(border_frame2_3_3, text="21:40", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[7], kino_teatr))
    button2_3_3.pack()
    button_window2_3_3 = canvas.create_window(900, 855, anchor=tk.NW, window=border_frame2_3_3)
    button2_3_3.bind('<Enter>', e2_3_3)
    button2_3_3.bind('<Leave>', l2_3_3)

    # КНОПКИ В РАСПИСАНИИ ФИЛЬМ 3
    film = "Планета обезьян: Новое царство"
    time = ["16:20", "18:30", "21:40", "21:40", "23:00", "00:20", "17:45", "23:10"]
    kino_teatr = "Премьер Зал Парк Хаус"
    border_frame3_1_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame3_1_1.pack(pady=15, padx=15)
    button3_1_1 = tk.Button(border_frame3_1_1, text="16:20", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[0], kino_teatr))
    button3_1_1.pack()
    button_window3_1_1 = canvas.create_window(700, 1065, anchor=tk.NW, window=border_frame3_1_1)
    button3_1_1.bind('<Enter>', e3_1_1)
    button3_1_1.bind('<Leave>', l3_1_1)

    border_frame3_1_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame3_1_2.pack(pady=15, padx=15)
    button3_1_2 = tk.Button(border_frame3_1_2, text="18:30", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[1], kino_teatr))
    button3_1_2.pack()
    button_window3_1_2 = canvas.create_window(800, 1065, anchor=tk.NW, window=border_frame3_1_2)
    button3_1_2.bind('<Enter>', e3_1_2)
    button3_1_2.bind('<Leave>', l3_1_2)

    border_frame3_1_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame3_1_3.pack(pady=15, padx=15)
    button3_1_3 = tk.Button(border_frame3_1_3, text="21:40", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[2], kino_teatr))
    button3_1_3.pack()
    button_window3_1_3 = canvas.create_window(900, 1065, anchor=tk.NW, window=border_frame3_1_3)
    button3_1_3.bind('<Enter>', e3_1_3)
    button3_1_3.bind('<Leave>', l3_1_3)

    kino_teatr = 'ККЦ "Премьер Зал Омега"'
    border_frame3_2_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame3_2_1.pack(pady=15, padx=15)
    button3_2_1 = tk.Button(border_frame3_2_1, text="21:40", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[3], kino_teatr))
    button3_2_1.pack()
    button_window3_2_1 = canvas.create_window(700, 1135, anchor=tk.NW, window=border_frame3_2_1)
    button3_2_1.bind('<Enter>', e3_2_1)
    button3_2_1.bind('<Leave>', l3_2_1)

    border_frame3_2_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame3_2_2.pack(pady=15, padx=15)
    button3_2_2 = tk.Button(border_frame3_2_2, text="23:00", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[4], kino_teatr))
    button3_2_2.pack()
    button_window3_2_2 = canvas.create_window(800, 1135, anchor=tk.NW, window=border_frame3_2_2)
    button3_2_2.bind('<Enter>', e3_2_2)
    button3_2_2.bind('<Leave>', l3_2_2)

    border_frame3_2_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame3_2_3.pack(pady=15, padx=15)
    button3_2_3 = tk.Button(border_frame3_2_3, text="00:20", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[5], kino_teatr))
    button3_2_3.pack()
    button_window3_2_3 = canvas.create_window(900, 1135, anchor=tk.NW, window=border_frame3_2_3)
    button3_2_3.bind('<Enter>', e3_2_3)
    button3_2_3.bind('<Leave>', l3_2_3)

    kino_teatr = 'ККЦ "Премьер Зал Гранат"'
    border_frame3_3_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame3_3_1.pack(pady=15, padx=15)
    button3_3_1 = tk.Button(border_frame3_3_1, text="17:45", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[6], kino_teatr))
    button3_3_1.pack()
    button_window3_3_1 = canvas.create_window(700, 1205, anchor=tk.NW, window=border_frame3_3_1)
    button3_3_1.bind('<Enter>', e3_3_1)
    button3_3_1.bind('<Leave>', l3_3_1)

    border_frame3_3_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame3_3_2.pack(pady=15, padx=15)
    button3_3_2 = tk.Button(border_frame3_3_2, text="23:10", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[7], kino_teatr))
    button3_3_2.pack()
    button_window3_3_2 = canvas.create_window(800, 1205, anchor=tk.NW, window=border_frame3_3_2)
    button3_3_2.bind('<Enter>', e3_3_2)
    button3_3_2.bind('<Leave>', l3_3_2)

    # КНОПКИ В РАСПИСАНИИ ФИЛЬМ 4
    film = "Пушистый вояж"
    time = ["11:45", "14:50", "19:50", "10:30", "17:45", "11:45", "14:50", "19:50"]
    kino_teatr = "Премьер Зал Парк Хаус"
    border_frame4_1_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame4_1_1.pack(pady=15, padx=15)
    button4_1_1 = tk.Button(border_frame4_1_1, text="11:45", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[0], kino_teatr))
    button4_1_1.pack()
    button_window4_1_1 = canvas.create_window(700, 1415, anchor=tk.NW, window=border_frame4_1_1)
    button4_1_1.bind('<Enter>', e4_1_1)
    button4_1_1.bind('<Leave>', l4_1_1)

    border_frame4_1_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame4_1_2.pack(pady=15, padx=15)
    button4_1_2 = tk.Button(border_frame4_1_2, text="14:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[1], kino_teatr))
    button4_1_2.pack()
    button_window4_1_2 = canvas.create_window(800, 1415, anchor=tk.NW, window=border_frame4_1_2)
    button4_1_2.bind('<Enter>', e4_1_2)
    button4_1_2.bind('<Leave>', l4_1_2)

    border_frame4_1_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame4_1_3.pack(pady=15, padx=15)
    button4_1_3 = tk.Button(border_frame4_1_3, text="19:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[2], kino_teatr))
    button4_1_3.pack()
    button_window4_4_2 = canvas.create_window(900, 1415, anchor=tk.NW, window=border_frame4_1_3)
    button4_1_3.bind('<Enter>', e4_1_3)
    button4_1_3.bind('<Leave>', l4_1_3)

    kino_teatr = 'ККЦ "Премьер Зал Омега"'
    border_frame4_2_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame4_2_1.pack(pady=15, padx=15)
    button4_2_1 = tk.Button(border_frame4_2_1, text="10:30", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[3], kino_teatr))
    button4_2_1.pack()
    button_window4_2_1 = canvas.create_window(700, 1485, anchor=tk.NW, window=border_frame4_2_1)
    button4_2_1.bind('<Enter>', e4_2_1)
    button4_2_1.bind('<Leave>', l4_2_1)

    border_frame4_2_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame4_2_2.pack(pady=15, padx=15)
    button4_2_2 = tk.Button(border_frame4_2_2, text="17:45", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[4], kino_teatr))
    button4_2_2.pack()
    button_window4_2_2 = canvas.create_window(800, 1485, anchor=tk.NW, window=border_frame4_2_2)
    button4_2_2.bind('<Enter>', e4_2_2)
    button4_2_2.bind('<Leave>', l4_2_2)

    kino_teatr = 'ККЦ "Премьер Зал Гранат"'
    border_frame4_3_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame4_3_1.pack(pady=15, padx=15)
    button4_3_1 = tk.Button(border_frame4_3_1, text="11:45", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[5], kino_teatr))
    button4_3_1.pack()
    button_window4_3_1 = canvas.create_window(700, 1555, anchor=tk.NW, window=border_frame4_3_1)
    button4_3_1.bind('<Enter>', e4_3_1)
    button4_3_1.bind('<Leave>', l4_3_1)

    border_frame4_3_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame4_3_2.pack(pady=15, padx=15)
    button4_3_2 = tk.Button(border_frame4_3_2, text="14:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[6], kino_teatr))
    button4_3_2.pack()
    button_window4_3_2 = canvas.create_window(800, 1555, anchor=tk.NW, window=border_frame4_3_2)
    button4_3_2.bind('<Enter>', e4_3_2)
    button4_3_2.bind('<Leave>', l4_3_2)

    border_frame4_3_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame4_3_3.pack(pady=15, padx=15)
    button4_3_3 = tk.Button(border_frame4_3_3, text="19:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[7], kino_teatr))
    button4_3_3.pack()
    button_window4_3_3 = canvas.create_window(900, 1555, anchor=tk.NW, window=border_frame4_3_3)
    button4_3_3.bind('<Enter>', e4_3_3)
    button4_3_3.bind('<Leave>', l4_3_3)

    # КНОПКИ В РАСПИСАНИИ ФИЛЬМ 5
    film = "Сто лет тому вперед"
    time = ["11:20", "16:10", "10:20", "14:30", "19:50", "11:50", "17:40", "23:20"]
    kino_teatr = "Премьер Зал Парк Хаус"
    border_frame5_1_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame5_1_1.pack(pady=15, padx=15)
    button5_1_1 = tk.Button(border_frame5_1_1, text="11:20", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[0], kino_teatr))
    button5_1_1.pack()
    button_window5_1_1 = canvas.create_window(700, 1765, anchor=tk.NW, window=border_frame5_1_1)
    button5_1_1.bind('<Enter>', e5_1_1)
    button5_1_1.bind('<Leave>', l5_1_1)

    border_frame5_1_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame5_1_2.pack(pady=15, padx=15)
    button5_1_2 = tk.Button(border_frame5_1_2, text="16:10", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[1], kino_teatr))
    button5_1_2.pack()
    button_window5_1_2 = canvas.create_window(800, 1765, anchor=tk.NW, window=border_frame5_1_2)
    button5_1_2.bind('<Enter>', e5_1_2)
    button5_1_2.bind('<Leave>', l5_1_2)

    border_frame5_2_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame5_2_1.pack(pady=15, padx=15)
    button5_2_1 = tk.Button(border_frame5_2_1, text="10:20", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[2], kino_teatr))
    button5_2_1.pack()
    button_window5_2_1 = canvas.create_window(700, 1835, anchor=tk.NW, window=border_frame5_2_1)
    button5_2_1.bind('<Enter>', e5_2_1)
    button5_2_1.bind('<Leave>', l5_2_1)

    kino_teatr = 'ККЦ "Премьер Зал Омега"'
    border_frame5_2_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame5_2_2.pack(pady=15, padx=15)
    button5_2_2 = tk.Button(border_frame5_2_2, text="14:30", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[3], kino_teatr))
    button5_2_2.pack()
    button_window5_2_2 = canvas.create_window(800, 1835, anchor=tk.NW, window=border_frame5_2_2)
    button5_2_2.bind('<Enter>', e5_2_2)
    button5_2_2.bind('<Leave>', l5_2_2)

    border_frame5_2_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame5_2_3.pack(pady=15, padx=15)
    button5_2_3 = tk.Button(border_frame5_2_3, text="19:50", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[4], kino_teatr))
    button5_2_3.pack()
    button_window5_2_2 = canvas.create_window(900, 1835, anchor=tk.NW, window=border_frame5_2_3)
    button5_2_3.bind('<Enter>', e5_2_3)
    button5_2_3.bind('<Leave>', l5_2_3)

    kino_teatr = 'ККЦ "Премьер Зал Гранат"'
    border_frame5_3_1 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame5_3_1.pack(pady=15, padx=15)
    button5_3_1 = tk.Button(border_frame5_3_1, text="11:50", font=f1, fg="purple", bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[5], kino_teatr))
    button5_3_1.pack()
    button_window5_3_1 = canvas.create_window(700, 1905, anchor=tk.NW, window=border_frame5_3_1)
    button5_3_1.bind('<Enter>', e5_3_1)
    button5_3_1.bind('<Leave>', l5_3_1)

    border_frame5_3_2 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame5_3_2.pack(pady=15, padx=15)
    button5_3_2 = tk.Button(border_frame5_3_2, text="17:40", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[6], kino_teatr))
    button5_3_2.pack()
    button_window5_3_2 = canvas.create_window(800, 1905, anchor=tk.NW, window=border_frame5_3_2)
    button5_3_2.bind('<Enter>', e5_3_2)
    button5_3_2.bind('<Leave>', l5_3_2)

    border_frame5_3_3 = tk.Frame(canvas, highlightbackground=purple, highlightcolor=purple, highlightthickness=2, bd=0)
    border_frame5_3_3.pack(pady=15, padx=15)
    button5_3_3 = tk.Button(border_frame5_3_3, text="23:20", font=f1, fg=purple, bd=0, padx=7, pady=3,
                            command=partial(b4, film, time[7], kino_teatr))
    button5_3_3.pack()
    button_window5_3_3 = canvas.create_window(900, 1905, anchor=tk.NW, window=border_frame5_3_3)
    button5_3_3.bind('<Enter>', e5_3_3)
    button5_3_3.bind('<Leave>', l5_3_3)

    w2.grab_set()
    w2.mainloop()


# ОКНО КОНТАКТЫ
def b3():
    w3 = Toplevel(m)
    w3.title('КОНТАКТЫ')
    w3.iconbitmap('icon.ico')
    w3.resizable(False, False)
    w3.geometry('1200x700')
    lw3 = Label(w3, image=iw3)
    l3 = Label(w3, text="Контактная информация", font=("Helvetica", 24))
    l3_1 = Label(w3, text="Сеть кинотеатров «Премьер Зал» - это "
                          "уникальный холдинг, в который входит "
                          "3 собственных кинотеатра \nв Екатеринбурге "
                          "и свыше 300 кинотеатров-партнеров по всей России",
                 font=("Helvetica", 12), justify='left')
    l3_1.place(x=190, y=150)

    l3_2 = Label(w3, text="— ККЦ «Омега», г. Екатеринбург,"
                          " просп. Космонавтов, 41, 4 этаж, тел.: 23-666-65",
                 font=("Helvetica", 12), justify='left')
    l3_2.place(x=190, y=210)

    l3_2 = Label(w3, text="— «Премьер Зал Гранат», г. Екатеринбург,"
                          " ул.Амундсена, 63, 3 этаж, тел.: 23-666-61",
                 font=("Helvetica", 12), justify='left')
    l3_2.place(x=190, y=240)

    l3_3 = Label(w3, text="— «Премьер Зал Парк Хаус», г. Екатеринбург,"
                          " ул.Сулимова, 50, 3 этаж, тел.: 23-666-67",
                 font=("Helvetica", 12), justify='left')
    l3_3.place(x=190, y=270)

    l3_4 = Label(w3, text="Единый справочный номер: 3-726-726",
                 font=("Helvetica", 12, "bold"), justify='left', )
    l3_4.place(x=190, y=300)

    l3_5 = Label(w3, text="Отдел персонала:",
                 font=("Helvetica", 12, "bold"), justify='left')
    l3_5.place(x=190, y=340)

    l3_6 = Label(w3, text="тел.: 8-932-123-89-37, эл. почта: personal@premierzal.ru",
                 font=("Helvetica", 12), justify='left')
    l3_6.place(x=190, y=370)

    l3_7 = Label(w3, text="Мы в соцсетях", font=("Helvetica", 20), justify='left')
    l3_7.place(x=190, y=400)

    l3_8 = Label(w3, text="Местоположение", font=("Helvetica", 20), justify='left')
    l3_8.place(x=190, y=500)

    vk = ImageTk.PhotoImage(Image.open('vk.png').resize((40, 40)))
    vk_t = ImageTk.PhotoImage(Image.open('vk_t.png').resize((40, 40)))

    def btn_1_e(e):
        btn_1['image'] = vk_t

    def btn_1_l(e):
        btn_1['image'] = vk

    def open_vk():
        webbrowser.open('https://vk.com/premierzal')

    btn_1 = Button(w3, image=vk, bg="#F0F4F7", borderwidth=0, command=open_vk)
    btn_1.place(x=190, y=450)
    btn_1.bind('<Enter>', btn_1_e)
    btn_1.bind('<Leave>', btn_1_l)

    youtube = ImageTk.PhotoImage(Image.open('youtube.png').resize((40, 40)))
    youtube_t = ImageTk.PhotoImage(Image.open('youtube_t.png').resize((40, 40)))

    def btn_2_e(e):
        btn_2['image'] = youtube_t

    def btn_2_l(e):
        btn_2['image'] = youtube

    def open_youtube():
        webbrowser.open('https://www.youtube.com/channel/UCf2QiK-LXkqsJYNLMdkWD6A')

    btn_2 = Button(w3, image=youtube, bg="#F0F4F7", borderwidth=0, command=open_youtube)
    btn_2.place(x=250, y=450)
    btn_2.bind('<Enter>', btn_2_e)
    btn_2.bind('<Leave>', btn_2_l)
    # btn_2 = Button(w3, bg=wh, borderwidth=0, height=1, width=10, text='ФИЛЬМЫ', fg=black, font=f, activebackground=wh,
    #          activeforeground=black, command=b1)

    twit = ImageTk.PhotoImage(Image.open('twitter.png').resize((40, 40)))
    twit_t = ImageTk.PhotoImage(Image.open('twitter_t.png').resize((40, 40)))

    def btn_3_e(e):
        btn_3['image'] = twit_t

    def btn_3_l(e):
        btn_3['image'] = twit

    def open_twit():
        webbrowser.open('https://x.com/premierzal?mx=2')

    btn_3 = Button(w3, image=twit, bg="#F0F4F7", borderwidth=0, command=open_twit)
    btn_3.place(x=310, y=450)
    btn_3.bind('<Enter>', btn_3_e)
    btn_3.bind('<Leave>', btn_3_l)

    map = ImageTk.PhotoImage(Image.open('map.png').resize((40, 40)))
    map_t = ImageTk.PhotoImage(Image.open('map_t.png').resize((40, 40)))

    def btn_4_e(e):
        btn_4['image'] = map_t

    def btn_4_l(e):
        btn_4['image'] = map

    def open_map():
        w_map = Toplevel(w3)
        w_map.title('КАРТА')
        w_map.iconbitmap('icon.ico')
        w_map.resizable(False, False)
        w_map.geometry('800x600')
        w_fr = LabelFrame(w_map)
        w_fr.pack(pady=20)

        mw = tkintermapview.TkinterMapView(w_map, width=800, height=600, corner_radius=0)
        mw.set_position(56.89992921209157, 60.612832723260446)
        mw.set_zoom(11)
        marker_1 = mw.set_position(56.89992921209157, 60.612832723260446, marker=True)

        marker_2 = mw.set_position(56.79728684849465, 60.581814468466696, marker=True)

        marker_3 = mw.set_position(56.863124789835425, 60.63004649795355, marker=True)

        # print(marker_1.position, marker_1.text)

        marker_1.set_text("")
        mw.pack
        mw.place(x=0, y=0)

        W.mainloop()

    btn_4 = Button(w3, image=map, bg="#F0F4F7", borderwidth=0, command=open_map)
    btn_4.place(x=190, y=550)
    btn_4.bind('<Enter>', btn_4_e)
    btn_4.bind('<Leave>', btn_4_l)

    odn = ImageTk.PhotoImage(Image.open('odnokl.png').resize((40, 40)))
    odn_t = ImageTk.PhotoImage(Image.open('odnokl_t.png').resize((40, 40)))

    def btn_5_e(e):
        btn_5['image'] = odn_t

    def btn_5_l(e):
        btn_5['image'] = odn

    def open_odn():
        webbrowser.open('https://ok.ru/premierzal')

    btn_5 = Button(w3, image=odn, bg="#F0F4F7", borderwidth=0, command=open_odn)
    btn_5.place(x=370, y=450)
    btn_5.bind('<Enter>', btn_5_e)
    btn_5.bind('<Leave>', btn_5_l)

    l3.place(x=190, y=80)
    lw3.pack()
    w3.grab_set()
    w3.mainloop()


def fb1(e):
    bw1.configure(fg=purple)


def fb1l(e):
    bw1.configure(fg=black)


def fb2(e):
    bw2.configure(fg=purple)


def fb2l(e):
    bw2.configure(fg=black)


def fb3(e):
    bw3.configure(fg=purple)


def fb3l(e):
    bw3.configure(fg=black)


def fbre(e):
    br.place(x=1232, y=382)


def fbrl(e):
    br.place(x=1230, y=380)


def fble(e):
    bl.place(x=10, y=382)


def fbll(e):
    bl.place(x=8, y=380)


purple = '#951b81'
gr = '#54C590'
dgr = '#1F855C'
wh = 'white'
wh1 = 'white'
black = 'black'
ser = '#343434'
ls = '#4D5257'
red = '#fb3100'
fon = '#f3f9fd'
g = list()
gray = '#7f7679'
m = Tk()

# ОСНОВНОЙ ЭКРАН
m.geometry('1280x960')

m.title('ПРЕМЬЕР ЗАЛ')
m.resizable(False, False)
m.iconbitmap('icon.ico')
m1 = PhotoImage(file='main1.png')
m2 = PhotoImage(file='main2.png')
m3 = PhotoImage(file='main3.png')

iw3 = ImageTk.PhotoImage(Image.open('фон афиша.png').resize((1200, 700)))
iw1 = PhotoImage(file='фон афиша.png')
l1 = Label(m, image=m1)
l1.place(x=-2, y=0)

f = font.Font(family="Rostov", size=30, weight="bold")
f.actual()
mainlabel = Label(m, text='Компания «Премьер Зал» появилась в 1998 году,'
                          '\nименно тогда мы открыли свой первый кинотеатр. '
                          '\nМы развивалинаш бренд, и уже сейчас в нашей '
                          '\nСети 4 кинотеатра в Екатеринбурге и свыше 300 – '
                          '\nпо всей стране! Наши площадки оснащены '
                          '\nсовременным и технологичным оборудованием'
                          '\n – это звуковая система Dolby, комфортные '
                          '\nкресла-реклайнеры c регуляцией положения '
                          '\nи встроенной зарядкой,многофункциональный '
                          '\nконсешн-бар и изготовление попкорна по '
                          '\nспециальной технологии. ', font=('Helvetica', 12), bg=wh, fg=gray, width=45,
                  justify='left')
mainlabel.place(x=60, y=730)
mainlabel1 = Label(m, text='В наших кинотеатрах можно не просто посмотреть '
                           '\nкино в хорошем качестве, но и перекусить '
                           '\nклассным попкорном и разными снеками,'
                           '\nинтересно и познавательно провести время с '
                           '\nдрузьями и семьей.Кинотеатры «Премьер Зала»'
                           '\nдоступны для зрителей и по ценам, и по '
                           '\nрасположению, поэтому до нас вы легко '
                           '\nдоберетесь и после работы, и в выходной день!'
                           '\nНа наших площадках мы также проводим различные'
                           '\nкультурные мероприятия: устраиваем праздники,'
                           '\nконцерты и лекции, проводим фестивали', font=('Helvetica', 12), bg=wh, fg=gray, width=46,
                   justify='left')
mainlabel1.place(x=440, y=730)
mainlabel2 = Label(m, text='мастер-классы, клубы по интересам.'
                           '\nНаши кинотеатры становятся полноценными '
                           '\nкультурными центрами, где найдется место '
                           '\nдля любого досуга – детского, семейного,'
                           '\nразвлекательного и интеллектуального. '
                           '\nУ нас вы отлично проведете время и с ребенком,'
                           '\nи с коллегами, и на романтическом свидании.'
                           '\nЗадача «Премьер Зала» – обеспечить наших'
                           '\nгостей качественным и интересным досугом,'
                           '\n создать комфортные условия.', font=('Helvetica', 12), bg=wh, fg=gray, width=42,
                   justify='left')
mainlabel2.place(x=830, y=730)
bw1 = Button(m, bg=wh, borderwidth=0, height=1, width=10, text='ФИЛЬМЫ', fg=black, font=f, activebackground=wh,
             activeforeground=black, command=b1)
bw1.place(x=300, y=23)
bw1.bind('<Enter>', fb1)
bw1.bind('<Leave>', fb1l)

bw2 = Button(m, bg=wh, borderwidth=0, height=1, width=12, text='РАСПИСАНИЕ', fg=black, font=f, activebackground=wh,
             activeforeground=black, command=b2)
bw2.place(x=550, y=23)
bw2.bind('<Enter>', fb2)
bw2.bind('<Leave>', fb2l)

bw3 = Button(m, bg=wh, borderwidth=0, height=1, width=10, text='КОНТАКТЫ', fg=black, font=f, activebackground=wh,
             activeforeground=black, command=b3)
bw3.place(x=865, y=23)

bw3.bind('<Enter>', fb3)
bw3.bind('<Leave>', fb3l)

br1 = ImageTk.PhotoImage(Image.open('r.png').resize((45, 60)))
br = Button(m, image=br1, bg=red, borderwidth=0, highlightthickness=0, command=r, activebackground=red)
br.place(x=1230, y=380)
br.bind('<Enter>', fbre)
br.bind('<Leave>', fbrl)
bl1 = ImageTk.PhotoImage(Image.open('l.png').resize((45, 60)))
bl = Button(m, image=bl1, bg=red, borderwidth=0, highlightthickness=0, command=l, activebackground=red)
bl.place(x=8, y=380)
bl.bind('<Enter>', fble)
bl.bind('<Leave>', fbll)
photos = [ImageTk.PhotoImage(Image.open(f"main{i}.png").resize((1280, 960))) for i in range(1, 4)]
photo_iterator = itertools.cycle(photos)


def update_photo():
    l1.config(image=next(photo_iterator))
    l1.after(5000, update_photo)


update_photo()

m.mainloop()

