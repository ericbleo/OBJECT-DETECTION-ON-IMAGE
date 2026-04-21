# Object detection on an image

This small project takes **one photo**, finds **objects** in it (like people, cars, animals), draws **boxes and labels** on the image, saves the result, and shows it in a window.

You do not need to know how the model works to use it.

---

## What you need first

1. **Python** installed on your computer (version 3.8 or newer is fine).  
   If you are not sure, open a terminal and type `python --version` or `py --version`.

2. **Two folders** next to `main.py` (create them if they are missing):
   - `images` — put your input photo here.
   - `output` — the program will save the result here.

3. **Your photo** named `picture.jpg` inside the `images` folder.  
   Or you can change the file name in `main.py` (look for `image_path = "images/picture.jpg"`).

---

## Install the libraries (one time)

Open a terminal in this project folder, then run:

```text
pip install ultralytics opencv-python
```

- **ultralytics** — runs the YOLO detection model.
- **opencv-python** — loads images, saves them, and opens the preview window.

If `pip` does not work, try `py -m pip install ultralytics opencv-python` on Windows.

---

## Run the program

In the same folder as `main.py`, run:

```text
python main.py
```

On some systems you may need:

```text
py main.py
```

**First run:** the script may download a model file (`yolov8l.pt`) into a `models` folder. That is normal and can take a minute depending on your internet.

**What happens:**

1. The image is loaded from `images/picture.jpg`.
2. It is resized a bit (to run faster).
3. Objects are detected and drawn on the image.
4. The result is saved as `output/output_picture.jpg`.
5. A window opens with the annotated image. Press any key in that window to close it.

---

## If something goes wrong

| Problem | What to try |
|--------|----------------|
| “Image not found” | Check that `images/picture.jpg` exists and the path in `main.py` is correct. |
| Module not found | Run the install command again in the same terminal you use to run the script. |
| Window does not appear | On some servers or remote setups, `imshow` may not work; the saved file in `output` should still be there. |

---

## Change the photo or model (optional)

- **Different image:** edit `image_path` in `main.py` to point to your file.
- **Different YOLO size:** change `model_path` (for example a smaller `yolov8n.pt` is faster and uses less memory; `yolov8l.pt` is larger and often more accurate).

---

## Credits

Script by **ericbleo** — object detection uses [Ultralytics YOLO](https://github.com/ultralytics/ultralytics).
