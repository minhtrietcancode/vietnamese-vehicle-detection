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

## Note about Data Preparation
The folder `new_train_test_data` was generated after running scripts in the `data_prep/` directory. However, to keep the repository clean and only show the ready-to-use training dataset, we are **not** including all intermediary files created at each step (there are about 30,000 files in total, which would overwhelm git!). Instead, you will only see the cleaned, training-ready dataset files in the repository.

If you want to reproduce the preparation steps or examine the data processing pipeline, please refer to the scripts and instructions inside the `data_prep/` directory.
