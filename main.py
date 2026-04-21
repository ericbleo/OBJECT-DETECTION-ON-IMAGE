import cv2
from ultralytics import YOLO

def resize(frame, size):
    width = int(frame.shape[1] * size)
    height = int(frame.shape[0] * size)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def save_image(image):
    print("Saving image...")
    cv2.imwrite("output/output_picture.jpg", image)
    print("Image saved successfully!")

image_path = "images/picture.jpg"

# This will automatically download the model if it's not already in the models folder.
model_path = "models/yolov8l.pt"

pic = cv2.imread(image_path)
pic = resize(pic, 0.3)
if pic is None:
    raise ValueError("Image not found! Check your path.")

model = YOLO(model_path)

results = model(pic)
annotated = results[0].plot()
save_image(annotated)

cv2.imshow("OBJECT DETECTION by ericbleo", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()