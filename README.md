# Vietnamese Vehicles Dataset

## Dataset Source
This dataset has been downloaded from [Kaggle](https://www.kaggle.com/datasets/duongtran1909/vietnamese-vehicles-dataset/data). Many thanks and appreciation to the dataset author. The images in this dataset have already been labelled.

## Label Definitions
This dataset contains 4 labels:

| Label | Vehicle Type                                                                 |
|-------|------------------------------------------------------------------------------|
| 0     | Motorbike / 2-wheel vehicles                                                 |
| 1     | Normal car                                                                   |
| 2     | Minibus / Coach-bus (16 or 29 seats bus used to carry tourists)              |
| 3     | Van / Truck / Container (goods-carrying vehicles with maximum weight capacity)|

## Repository Structure
- `data_prep/`: Contains scripts to conduct stratified splitting for the dataset based on the original dataset loaded from Kaggle.
- `model/`: Contains the `data.yaml` file to guide YOLO and the Python script to train the model.
- `new_train_test_data/`: Contains the split train, validation, and test sets used for model training.
- `runs/`: An auto-generated directory created when fine-tuning the YOLOv8 model.
- `vietnamese_vehicle_detection.ipynb`: The downloaded script used to train the model from a Google Colab workspace.

## Note about Data Preparation
This repository utilizes approximately 1500 images for the entire process, not the entire 15000 images from the original dataset. The purpose of this project is to explore the process and gain an overall understanding of YOLO's performance. More detailed analysis will be conducted once the problem definition is clearly established.

The folder `new_train_test_data` was generated after running scripts in the `data_prep/` directory. However, to keep the repository clean and only show the ready-to-use training dataset, we are **not** including all intermediary files created at each step (there are about 30,000 files in total, which would overwhelm git!). Instead, you will only see the cleaned, training-ready dataset files in the repository.

If you want to reproduce the preparation steps or examine the data processing pipeline, please refer to the scripts and instructions inside the `data_prep/` directory.

## Links
- **Colab Notebook:** https://colab.research.google.com/drive/1i5MNUCd9PEV1Fm2-nTeXzHl2X--zjazs?usp=sharing
- **Fine-tuned YOLOv8 Model:** https://drive.google.com/drive/folders/1heeEydQZMvUXdCJfW5UHjVlu9apYhZ-X?usp=sharing
