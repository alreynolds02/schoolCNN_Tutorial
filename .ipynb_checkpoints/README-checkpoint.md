# SchoolCNN_Tutorial
Code and tutorial for a CNN using Google Static API imagery to predict student success in Philippine public schools

This repository has the code to replicate part of the work written about here  to predict student success in Philippine public schools. Follow the instructions below to train and evaluate your own convolutional neural network. THe code is written in juyter notebook to allow for easier visualization of the CNN results.

## Instructions

1. Clone this repository to your computer
2. Create a new folder called 'data' and create the file structure shown below:
```
    |-- 1_GoogleStaticDownload.py
    |-- 2_PassFailSplit.py
    |-- 3_TrainValSplit.py 
    |-- 4_GoogleStaticCNN.py
    |-- data
        \-- imagery
        |-- pass
        |-- fail
        |-- train
            |-- fail
            |-- pass
        |-- val
            |-- fail
            |-- fail
```
3. Download the data in this folder: https://drive.google.com/drive/u/0/folders/19ubRi2AKjjX5ImglaX2TPTi3jfnXWJNH to the imagery folder.
4. Begining with file 'PassFaillSPit.ipynb', make your way through the tutorial following the numbered files!
