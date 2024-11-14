# Reducing the Number of Colors in an Image

This task is based on the K-Means lecture materials. Please note that the task is optional.

## You will learn:

- use the K-Means algorithm
- work with unsupervised learning problems
- work with images in Python

## Introduction

The most common type of machine learning problems is supervised learning problems. They have a training sample, for each
object of which there is an answer, and you need to learn to predict these answers for new objects. In this setting, you can strictly define the quality criteria.
If there are only objects, and there are no answers for them, you can still try to find some structure in the data. Problems that
look for patterns in unlabeled samples are called unsupervised learning problems. A typical example of such a problem is clustering,
where you need to find groups of similar objects.
Clustering can be used for a variety of purposes. In
this task, we will try to group similar pixels in an image. This approach allows us to move to a superpixel representation of images, which is more compact and better suited for solving a number of computer vision problems.

## Implementation in sklearn

The KMeans algorithm is implemented in the sklearn.cluster.KMeans class. Since
this is one of the examples of an unsupervised task, it is enough to pass only the feature matrix for training.
As a metric, we will use PSNR - an adaptation of the MSE metric for the task of finding image similarities.
To work with images, we recommend using the scikit-image package. To load an image, you need to run the following command:

```Python
from skimage.io import imread
image = imread(’parrots_4.jpg’)
```

After these steps, the image variable will contain the image as a numpy array of size n * m * 3, where n and m correspond to the
image dimensions, and 3 corresponds to the RGB representation format.

## Instructions for execution

1. Load the parrots.jpg image. Transform the image by bringing all values ​​into the range from 0 to 1. For this, you can use the img_as_float function from the skimage module.
2. Create a matrix of features: characterize each pixel by three coordinates - intensity values ​​in RGB space.
3. Run the K-Means algorithm with the parameters init=’k-means++’ and
random_state=241. After selecting clusters, try to fill all pixels assigned to one cluster in two ways:
median and average color for the cluster.

4. Measure the quality of the resulting segmentation using the PSNR metric. You need to implement this metric yourself (see definition).

The answer to each task is a text file containing the answer in the
first line. Please note that the files you send should not contain an empty line at the end. This nuance is a limitation of the Coursera platform. We are working to remove this
limitation.