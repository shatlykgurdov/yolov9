from ultralytics import YOLO

# Load a model
model = YOLO("runs/detect/train/weights/best_saved_model/best_float16.tflite")  # load a custom model

# Predict with the model
results = model("https://ultralytics.com/images/bus.jpg", save=True)  # predict on an image