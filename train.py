from ultralytics import YOLO

# Load the model
model = YOLO("yolov9t.pt")

# Train the model on the COCO8 dataset
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

