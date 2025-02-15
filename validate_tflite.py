from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best_saved_model/best_float16.tflite')

results = model.val(data='coco8.yaml')
