from ultralytics import YOLO

# Load the trained model
model = YOLO('runs/detect/train/weights/best.pt')  # Path to the best model

# Validate the model using the validation dataset defined in the training config (e.g., coco8.yaml)
results = model.val(data='coco8.yaml')  # Replace with your dataset YAML file
