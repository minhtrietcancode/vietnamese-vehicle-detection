"""
YOLOv8 Training Script for Vietnamese Vehicles Dataset
"""

from ultralytics import YOLO

# Load a pre-trained YOLOv8n model
model = YOLO('yolov8n.pt')

# Define the path to your custom data.yaml
data_yaml_path = '/content/model/data.yaml'

# Train the model with your custom dataset
results = model.train(data=data_yaml_path, epochs=100, imgsz=640)

# Perform inference on the test set and save results with bounding boxes
inference_results = model.predict(source='/content/new_train_test_data/test', save=True, conf=0.25)

# Save the trained model
model.save('my_finetuned_yolov8.pt')

print("\nTraining completed! Model saved as 'my_finetuned_yolov8.pt'")