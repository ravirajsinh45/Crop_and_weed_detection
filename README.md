# Crop_and_weed_detection
we made the crop and weed detection model using YOLOV3 on agricultural image data.

# Problem
Weed is unwanted thing in agriculture. Weed use the nutrients, water ,land and many more thihngs that might have gone to crops.Which result less production of required crop.Farmer often use pesticides to remove weed which also affective but some pesticide may stick with crop and may causs problem for humans.

# Aim

Our aim is to develop system which only sprey pesticides on weed and not on crop.Which will reduce the mixing problem with crop and also reduce the waste of pesticides.

# How we developing?

STEPS:
  1. First of we have to collect dataset for it.For that we have to capture photos of weeds and crops.we collected total 589 images
  2. After collection of photos we have to clean the dataset.This step is very important because if any bed photo is remain in dataset        it causs worse effect in detection model.after cleaning we have 546 images.
  3. Now time for image processing.Our photo size is 4000X3000 color which is very large and model will take very long time for training      so we convert all images to 512X512X3 size.
  4. now 546 image is not enogh for training,so we have done some magic to convert 546 image into 1300 images.We used Data                    Augmetation technique to increase dataset.(Check it out keras ImageDataGenerator on google)
  5. This step is very tedious, Manual labeling of image data!! In this step we have to drow bounding boxes on photos whether it weed or      crop. Data on https://www.kaggle.com/ravirajsinh45/crop-and-weed-detection-data-with-bounding-boxes
  6. we have to make detection model for it. For this we using YOLOV3 Architacture. Model will train on training set and after training      it validate on testing set.Make sure you not train model on test set this will not give actual performannce of model.We using            Google Colab for inhencing free GPU provide by it. Training without GPU will take very long time aroud 22-24 hour.
  7. For this you have to add all file in google drive.Make Agriculture folder and add all file in this repo and downloaded data from        kaggle. 
