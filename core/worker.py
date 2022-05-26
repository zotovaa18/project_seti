import time
import requests
import tkinter as tk
from loguru import logger
from PIL import Image, ImageDraw, ImageFont

import core.default_values as def_values


def detect_user(file_path: str = def_values.STREAM_SCREENSHOT_PATH) -> dict:
    extention = file_path.split(".")[-1]
    with open(file_path, "rb") as f:
        chunk = f.read(15 * 1024 * 1024)  # 50 MB

        res = requests.post(
            f"{def_values.BACKEND_URL}/detect_user",
            params={"extention": extention},
            files={"file_data": chunk},
        )

        return res


def detect_user_from_dir():
    global limg_setup

    limg_setup.destroy()
    logger.info("Starting users detection process...")

    while True:
        res = detect_user()
        if res.status_code == 201:
            user = res.json()

            fio, role = user.get("name"), user.get("info")
            logger.info(f"Detected user: {fio}")

            image_text = fio + "\n" + role

            img = Image.new("RGB", (800, 200), color="red")
            unicode_font = ImageFont.truetype(def_values.TEXT_FONT, 20)
            output_image = ImageDraw.Draw(img)
            output_image.text(
                (10, 10), image_text, fill=(255, 255, 0), font=unicode_font
            )
            img.save(def_values.RESULT_IMAGE)

            break

        elif res.status_code == 500:
            logger.error("Backend error")

            break

        time.sleep(1)


def begin_work():
    global limg_setup

    def back2main():
        window_detecting.destroy()

    window_detecting = tk.Toplevel()
    window_detecting.title("Титруемся")
    window_detecting.resizable(False, False)
    window_detecting.geometry("800x300")
    img = tk.PhotoImage(file=def_values.BACKGROUND_PATH)
    limg = tk.Label(window_detecting, image=img)
    limg.place(x=0, y=0)
    btn_back = tk.Button(window_detecting, text="Назад", command=back2main)
    btn_back.place(x=0, y=0)
    img_setup = tk.PhotoImage(file=def_values.SETUP_OBS_IMG_PATH)
    limg_setup = tk.Label(window_detecting, image=img_setup)
    limg_setup.place(x=200, y=130)

    setup_text = tk.Label(
        window_detecting,
        text="Включите, что надо включить, а что не надо не включайте",
    )
    setup_text.place(x=200, y=100)

    btn_next = tk.Button(window_detecting, text="Далее", command=detect_user_from_dir)
    btn_next.place(x=230, y=250)
    window_detecting.mainloop()
