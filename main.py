import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter.ttk import *
import requests
from PIL import Image
from functools import partial



def upload_new():
    def select_file(filetype, entry_photo):
        def upload_archive():
            print(filetype)
            #Даня, пиши сюда

        if filetype==1:
            filetypes = [('all files', '.*'),
                         ('text files', '.txt'),
                         ('image files', '.png'),
                         ('image files', '.jpeg'),
                         ('image files', '.jpg')
                         ]
        if filetype==2:

            filetypes = [('zips','.zip')]

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        entry_photo.insert(0, filename)
        btn_upload=ttk.Button(window_upload_new, text='Загрузить файл', command=upload_archive)
        btn_upload.place(x=250, y=250)


        showinfo(
            title='Selected File',
            message=filename
        )
    def package():
        entry_photo = tk.Entry(window_upload_new, width=30)
        open_button= ttk.Button(window_upload_new,text='Открыть файл',command=lambda:select_file(2, entry_photo))
        entry_photo.place(x=150, y=200)
        open_button.place(x=450,y=200)
    def oneandonly():
        entry_photo = tk.Entry(window_upload_new, width=30)
        open_button = ttk.Button(window_upload_new, text='Открыть файл', command=lambda:select_file(1, entry_photo))
        entry_photo.place(x=150, y=200)
        open_button.place(x=450, y=200)


    def back2main():
        window_upload_new.destroy()
        root.deiconify()

    #window to upload new people
    #root.destroy()
    window_upload_new = tk.Toplevel()
    window_upload_new.title('Новые лица')
    window_upload_new.resizable(False, False)
    window_upload_new.geometry('800x300')
    img = tk.PhotoImage(file="/Users/valeriadudina/Downloads/back3.png")
    limg = tk.Label(window_upload_new, image=img)
    limg.place(x=0, y=0)
    btn_back=tk.Button(window_upload_new,text="Назад",
            command=back2main)
    btn_package = tk.Button(window_upload_new, text="Пакетная загрузка",width=15, height=3,
                         command=package)
    btn_one=tk.Button(window_upload_new, text="По одному",width=15, height=3,
                         command=oneandonly)
    btn_package.place(x=400, y=120)
    btn_one.place(x=150, y=120)
    btn_back.place(x=0, y=0)
    window_upload_new.mainloop()

def begin_work():
    def next_():
        print('next')
        window_begin_work2 = tk.Toplevel()
        window_begin_work2.title('Натитровали')
        window_begin_work2.resizable(False, False)
        window_begin_work2.geometry('800x100')
        fio="Дудина Валерия Романовна"
        role="Прекрасная женщина, принцесса, королева"
        img_titr = tk.PhotoImage(file="titr_template.png")
        limg_titr = tk.Label(window_begin_work2, image=img_titr)
        limg_titr.place(x=0, y=0)
        text=tk.Label(text=fio)
        canvas = Canvas(window_begin_work2, height=100, width=800, bg="#ccf9ff")
        canvas.create_text(300, 20, text=fio, fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(300, 50, text=role, fill="black", font=('Helvetica 15 bold'))
        canvas.pack()
        window_begin_work2.mainloop()



        #тут писать c Настей

    def back2main():
        window_begin_work.destroy()
        root.deiconify()


    window_begin_work = tk.Toplevel()
    window_begin_work.title('Титруемся')
    window_begin_work.resizable(False, False)
    window_begin_work.geometry('800x300')
    img = tk.PhotoImage(file="/Users/valeriadudina/Downloads/back3.png")
    limg = tk.Label(window_begin_work, image=img)
    limg.place(x=0, y=0)
    btn_back=tk.Button(window_begin_work,text="Назад",
            command=back2main)
    btn_back.place(x=0,y=0)
    img_setup = tk.PhotoImage(file="setup_odbs.png")
    limg_setup = tk.Label(window_begin_work, image=img_setup)
    limg_setup.place(x=200, y=130)

    setup_text=tk.Label(window_begin_work, text="Включите, что надо включить, а что не надо не включайте")
    setup_text.place(x=200, y=100)

    btn_next=tk.Button(window_begin_work,text="Далее",
            command=next_)
    btn_next.place(x=230, y=250)
    window_begin_work.mainloop()

def select_file():
    filetypes = [('all files', '.*'),
               ('text files', '.txt'),
               ('image files', '.png'),
               ('image files', '.jpg'),
                 ('image files', '.jpeg')
           ]

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    entry_photo.insert(0,filename)



    showinfo(
        title='Selected File',
        message=filename
    )

def send_data():
    def back_to_main():
        print('smth')
        root2.destroy()

        root.deiconify()

    root2 = tk.Toplevel()
    root2.title('Готово')
    root2.resizable(False, False)
    root2.geometry('800x300')
    img = tk.PhotoImage(file="/Users/valeriadudina/Downloads/back3.png")
    limg = tk.Label(root2, image=img)
    limg.place(x=0, y=0)
    lab_201=tk.Label(root2, text="Пользователь успешно добавлен", background='black')
    lab_422 = tk.Label(root2, text="Неверные данные, попробуйте еще раз", background='black')

    btn_back=tk.Button(root2,text="Добавить еще одного пользователя",command=back_to_main)


    extention = entry_photo.get().split(".")[-1]
    url = "http://51.250.8.218:8000"
    with open(entry_photo.get(), "rb") as f:
        chunk = f.read(15 * 1024 * 1024)
        res = requests.post(
            f"{url}/user",
            params={"extention": extention, "fio": entry_fio.get()},
            files={"file_data": chunk},
        )
    if res.status_code==201:
        lab_201.place(x=230, y=100)
        btn_back.place(x=200, y=200)

    if res.status_code==422:
        lab_422.place(x=230, y=100)
        btn_back.place(x=200, y=200)



    #root.destroy()
    root2.mainloop()

def detect_user():
    def back_to_main():

        root3.destroy()
        root.deiconify()
    def select_file2():
        filetypes = [('all files', '.*'),
                     ('text files', '.txt'),
                     ('image files', '.png'),
                     ('image files', '.jpeg'),
                     ('image files', '.jpg')
                     ]

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        entry_photo_detect.insert(0, filename)


        showinfo(
            title='Selected File',
            message=filename
        )
    def detect():
        extention = entry_photo_detect.get().split(".")[-1]
        url = "http://51.250.8.218:8000"
        with open(entry_photo_detect.get(), "rb") as f:
            chunk = f.read(15 * 1024 * 1024)
            res = requests.post(
                f"{url}/detect_user",
                params={"extention": extention},
                files={"file_data": chunk},
            )
        t = tk.Text(root3, height=20, width=100)
        t.insert('insert', res.text)
        t.pack()
        #t=tk.Label(root3, text=res.text)
        #t.place(x=100,y=100)


    root3 = tk.Toplevel()
    root3.title('Проверить')
    root3.resizable(False, False)
    root3.geometry('800x300')
    img = tk.PhotoImage(file="/Users/valeriadudina/Downloads/back3.png")
    limg = tk.Label(root3, image=img)
    limg.place(x=0, y=0)

    entry_photo_detect = tk.Entry(root3,width=30)
    open_button_detect = ttk.Button(
        root3,
        text='Открыть файл',
        command=select_file2,

    )
    detect_button=tk.Button(root3, text="Найти", command=detect)
    button_back=tk.Button(root3, text='Назад', command=back_to_main)
    entry_photo_detect.place(x=150, y=100)
    open_button_detect.place(x=450, y=100)
    detect_button.place(x=300, y=150)
    button_back.place(x=300, y=200)

    #root.destroy()
    root3.mainloop()




# open button
'''
name=''
photo=''
img = tk.PhotoImage(file="/Users/valeriadudina/Downloads/back3.png")
limg= tk.Label(root, image=img)
limg.place(x=0, y=0)

label_fio=tk.Label(root, text="ФИО", background='black')
entry_fio=tk.Entry(root, textvariable=name, width=30)
entry_photo=tk.Entry(root, textvariable=photo, width=30)


label_photo=tk.Label(root, text="Фото",background='black')
check_button=tk.Button(root, text="Проверить сотрудника", command=detect_user)
open_button = ttk.Button(
    root,
    text='Открыть файл',
    command=select_file
)
send_button=ttk.Button(root, text='Загрузить', command=send_data)

label_fio.place(x=150, y=100)
entry_fio.place(x=210, y=100)
entry_photo.place(x=210, y=150)
label_photo.place(x=150, y=150)
open_button.place(x=500, y=150)
send_button.place(x=300, y=200)
check_button.place(x=270, y=250)

'''
# create the root window
root = tk.Tk()
root.title('Титровалка')
root.resizable(True, True)
root.geometry('800x300')

#background

img = tk.PhotoImage(file="/Users/valeriadudina/Downloads/back3.png")
limg= tk.Label(root, image=img)
limg.place(x=0, y=0)
btn1=tk.Button(text="Добавить новые лица",
            width=15, height=3, command=upload_new)
btn2 = tk.Button(text="Начать работу",
            width=15, height=3, command=begin_work)

btn1.place(x=150, y=150)
btn2.place(x=400, y=150)


root.mainloop()
