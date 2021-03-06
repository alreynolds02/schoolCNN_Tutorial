# SchoolCNN_Tutorial
Code and tutorial for a CNN using Google Static API imagery to predict student success in Philippine public schools

Read here for background on the project: https://medium.com/@ClouderaFnd/can-you-determine-school-performance-with-no-access-to-test-scores-heres-one-novel-idea-cb939bf8de20

This repository has the code to replicate part of the work written about here  to predict student success in Philippine public schools. Follow the instructions below to train and evaluate your own convolutional neural network. THe code is written in juyter notebook to allow for easier visualization of the CNN results.

## Instructions

1. Fork this repository and clone it to your computer.
2. Create new folders to match the file structure shown below:
```
    |-- 1_GoogleStaticDownload.py
    |-- 2_PassFailSplit.py
    |-- 3_TrainValSplit.py 
    |-- 4_GoogleStaticCNN.py
    ...
    |-- models
    |-- epochs
    |-- data
        |-- imagery
	|-- jpg
        |-- pass
        |-- fail
        |-- train
            |-- fail
            |-- pass
        |-- val
            |-- fail
            |-- pass
```
3. Beginning with file '2_PassFailSplit.ipynb', make your way through the tutorial following the numbered files!

