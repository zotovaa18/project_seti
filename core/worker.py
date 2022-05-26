import time
import json
import requests
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

import core.default_values as def_values


def begin_work():
    def next_():
        def detect_user(file_path: str) -> dict:
            extention = file_path.split(".")[-1]
            with open(file_path, "rb") as f:
                chunk = f.read(15 * 1024 * 1024)  # 50 MB

                res = requests.post(
                    f"{url}/detect_user",
                    params={"extention": extention},
                    files={"file_data": chunk},
                )

                return res

        def detect_user_from_dir(image_path: str):
            while True:
                res = detect_user(image_path)
                print("detect_user_from_dir")
                if res.status_code == 201:
                    det_user = json.loads(res.text)
                    fio = det_user.get("name")
                    print(fio)
                    role = det_user.get("info")
                    text = fio + "\n" + role

                    img = Image.new("RGB", (800, 200), color="red")
                    unicode_font = ImageFont.truetype(def_values.TEXT_FONT, 20)
                    d = ImageDraw.Draw(img)
                    d.text((10, 10), text, fill=(255, 255, 0), font=unicode_font)
                    img.save(def_values.RESULT_IMAGE)
                    break
                else:
                    print("errorsssssssss")

                time.sleep(1)

        print("next")
        url = def_values.BACKEND_URL

        detect_user_from_dir(def_values.STREAM_SCREENSHOT_PATH)

    def back2main():
        window_begin_work.destroy()

    window_begin_work = tk.Toplevel()
    window_begin_work.title("Титруемся")
    window_begin_work.resizable(False, False)
    window_begin_work.geometry("800x300")
    img = tk.PhotoImage(file=def_values.BACKGROUND_PATH)
    limg = tk.Label(window_begin_work, image=img)
    limg.place(x=0, y=0)
    btn_back = tk.Button(window_begin_work, text="Назад", command=back2main)
    btn_back.place(x=0, y=0)
    img_setup = tk.PhotoImage(file=def_values.SETUP_OBS_IMG_PATH)
    limg_setup = tk.Label(window_begin_work, image=img_setup)
    limg_setup.place(x=200, y=130)

    setup_text = tk.Label(
        window_begin_work,
        text="Включите, что надо включить, а что не надо не включайте",
    )
    setup_text.place(x=200, y=100)

    btn_next = tk.Button(window_begin_work, text="Далее", command=next_)
    btn_next.place(x=230, y=250)
    window_begin_work.mainloop()
