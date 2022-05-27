import requests
from os import listdir
from os.path import isfile, join

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from core.default_values import BACKGROUND_PATH, BACKEND_URL


def sent_user(image_path: str, fio: str, info: str = ""):
    extention = image_path.split(".")[-1]
    with open(image_path, "rb") as f:
        chunk = f.read(15 * 1024 * 1024)
        res = requests.post(
            f"{BACKEND_URL}/user",
            params={"extention": extention, "fio": fio, "info": info},
            files={"file_data": chunk},
        )


def upload_package(path: str):
    files = [path + "/" + f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        user_data = file.split("/")[-1]
        fio = user_data.split("-")[0]
        info = user_data.split("-")[1]
        sent_user(file, fio, info)


def upload_new():
    def back2main():
        window_upload_new.destroy()

    def select_file(entry_photo):
        filetypes = [
            ("all files", ".*"),
            ("text files", ".txt"),
            ("image files", ".png"),
            ("image files", ".jpeg"),
            ("image files", ".jpg"),
        ]

        filename = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )

        entry_photo.insert(0, filename)
        btn_upload = ttk.Button(
            window_upload_new, text="Запомнить юзера", command=back2main  # CHANGE IT
        )
        btn_upload.place(x=250, y=250)

        showinfo(title="Selected File", message=filename)

    def select_dir(entry_dir):
        chosen_dir = fd.askdirectory(title="Выбрать папку", initialdir=".")
        entry_dir.insert(0, chosen_dir)

        btn_upload = ttk.Button(
            window_upload_new,
            text="Загрузить пакет пользователей",
            command=lambda: upload_package(chosen_dir),
        )
        btn_upload.place(x=250, y=250)

    def package():
        entry_dir = tk.Entry(window_upload_new, width=30)
        open_button = ttk.Button(
            window_upload_new,
            text="Выбрать папку",
            command=lambda: select_dir(entry_dir),
        )
        entry_dir.place(x=150, y=200)
        open_button.place(x=450, y=200)

    def oneandonly():
        entry_photo = tk.Entry(window_upload_new, width=30)
        open_button = ttk.Button(
            window_upload_new,
            text="Открыть файл",
            command=lambda: select_file(1, entry_photo),
        )
        entry_photo.place(x=150, y=200)
        open_button.place(x=450, y=200)

    window_upload_new = tk.Toplevel()
    window_upload_new.title("Добавление новых пользователей")
    window_upload_new.resizable(False, False)
    window_upload_new.geometry("800x300")
    img = tk.PhotoImage(file=BACKGROUND_PATH)
    limg = tk.Label(window_upload_new, image=img)
    limg.place(x=0, y=0)
    btn_back = tk.Button(window_upload_new, text="Назад", command=back2main)
    btn_package = tk.Button(
        window_upload_new, text="Пакетная загрузка", width=15, height=3, command=package
    )
    btn_one = tk.Button(
        window_upload_new, text="По одному", width=15, height=3, command=oneandonly
    )
    btn_package.place(x=400, y=120)
    btn_one.place(x=150, y=120)
    btn_back.place(x=0, y=0)
    window_upload_new.mainloop()
