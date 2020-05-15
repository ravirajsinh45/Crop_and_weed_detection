# Crop_and_weed_detection
we made the crop and weed detection model using YOLOV3 on agricultural image data.
![](https://github.com/ravirajsinh45/Crop_and_weed_detection/blob/master/detection_on_images_pytorch/detection/detection.jpg)



![](https://github.com/ravirajsinh45/Crop_and_weed_detection/blob/master/detection_on_images_pytorch/detection/detection_1.jpeg)

# Problem
Weed is unwanted thing in agriculture. Weed use the nutrients, water ,land and many more thihngs that might have gone to crops.Which result less production of required crop.Farmer often use pesticides to remove weed which also affective but some pesticide may stick with crop and may causs problem for humans.

# Data
we using our dataset uploaded on [kaggle](https://www.kaggle.com/ravirajsinh45/crop-and-weed-detection-data-with-bounding-boxes).
This dataset contains 1300 images of sesame crops and different types of weeds with each image labels.
Each image is a 512 X 512 color image. Labels for images are in YOLO format.
Data on https://www.kaggle.com/ravirajsinh45/crop-and-weed-detection-data-with-bounding-boxes

# Some images
### sesame crop
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2Fdd84e10cd56c74516656e1fee2742763%2Ftal_55.jpeg?generation=1589438968788391&alt=media)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2Fbf8669472ca779a36fbd992c6ee80b9b%2Ftal_44.jpeg?generation=1589438975110310&alt=media)

### weed
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2F223e1ae1bc2b2d976ccf79685bb5ef24%2Fimage_359.jpeg?generation=1589439154681622&alt=media)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2Fec12dbafbf4b5b6e1b46cc1a47e95147%2Fimage_528.jpeg?generation=1589439166010189&alt=media)
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3745280%2Fc4e147d01af2667a293c3ff1caac6a85%2Fimage_21.jpeg?generation=1589439187082625&alt=media)



  
  # How to use this repo?

  This Repository is diveded in two part:-

    1. Training 
    2. Performig detection using pre train model


1. Training:-
 
    For traning you have to make **Agriculture** folder on your google drive, open clone repo and copy all files from `Crop_weed_detection_training` folder and paste it in google drive.

    Now from drive open crop_weed_detection.ipynb file and you will get all documentation regarding it within the file.


2. Performig detection using pre train model

   * First of all you need anaconda, if you don't have click here for [Download](https://www.anaconda.com/products/individual) and install.

    * Now open Anaconda Prompt and clone this repo
   ```
   (base) C:\Users\user> git clone https://github.com/ravirajsinh45/Crop_and_weed_detection.git
    ```  
     - (Optional) If you get any error like **git is not recogize internal command** than run below command
          ```
            (base) C:\Users\user> pip install git
          ``` 
      
    * change your working directory to clone repo.
      ```
      (base) C:\Users\user>cd Crop_and_weed_detection
      ```
    * After that you have to create environment to install require libraries. Follow the steps:-
       1. open Anaconda Prompt and write below command for install requirements.
           ```
            (base) C:\Users\user\Crop_and_weed_detection> conda create -n pytorchenv python=3.7.7
           ```
      2. After creating environment you have to activate it.
          ```
          (base) C:\Users\user\Crop_and_weed_detection> conda activate pytorchenv
         ```
      3.  Now run below command for install liraries
          ```
          (pytorchenv) C:\Users\user\Crop_and_weed_detection> pip install -r requirements.txt 
          ```
   * Now your evironment is ready to roar:)

   * Let Open jupyter lab

      ```
     (pytorchenv) C:\Users\user\Crop_and_weed_detection>jupyter-lab
     ```
   * For detection you need weights for network. Due to large file i attaching google drive link. You have to download weight file unless you have your own weights file. [click here](https://drive.google.com/open?id=1-Aam2D-fqnwecbeHwa4rtzxtNjwcDkP6)

   * You have to add weights flie into `Crop_and_weed_detection > detection_on_images_pytorch > weights` folder.

   * After that open **Perform_detection.ipynb** file and run all cell. After this you will able to detect crop and weed from images. Explore images from **images** folder. Cheers:)


 # Thank You:) 




  





