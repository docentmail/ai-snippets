# Stock Index Compilation

This task is based on the lecture materials on the principal component method and is devoted to getting acquainted with the method.

## You will learn:

- to work with the principal component method
- to use it to calculate the improved Dow Jones index

## Introduction

The principal component method (PCA) is one of the unsupervised learning methods that allows you to form new features that are linear combinations of old ones. In this case,
new features are constructed in such a way as to preserve as much variance in the data as possible. In other words, the principal component method reduces the
dimensionality of the data in an optimal way from the point of view of preserving variance.
The main parameter of the principal component method is the number of new features. As in most machine learning methods, there are no clear recommendations regarding the choice of the value of this parameter. One approach is to select the minimum number of components that explains at least a certain proportion of the variance (meaning that the sample retains a given proportion of the original variance).

In this task, you will need to measure the similarity of two sets of values. If you have a set of pairs of measurements (for example, one pair is the predictions of two classifiers for the same object), then you can characterize their dependence on each other using the Pearson correlation. It takes values ​​from -1 to 1 and shows how linearly dependent these values ​​are. If the correlation is -1 or 1, then the values ​​are linearly expressed through each other. If it is zero, then there is no linear dependence between the values.

## Data

In this task, we will work with data on the stock prices of 30 of the largest US companies. Based on this data, you can assess the state of the economy, for example, using the Dow Jones Index. Over
time, the composition of companies used to build the index changes. For
the data set, the period from 09/23/2013 to 03/18/2015 was taken, in which
the set of companies was fixed (you can read more about the composition
by following the link from the materials).
One of the significant drawbacks of the Dow Jones index is
the way it is calculated - when calculating the index, the prices of the shares included in it
are added up and then divided by a correction factor. As a
result, even if one company is significantly smaller in capitalization
than another, but the cost of one of its shares is higher, it has a greater effect
on the index. Even a large percentage change in the price of a relatively cheap share can be leveled out by an insignificant percentage
change in the price of a more expensive share.

## Implementation in sklearn

The principal component method is implemented in the scikit-learn package in the decomposition module
in the PCA class. The main parameter is the number of components
(n_components). For a trained transform, this class allows
to calculate various features. For example, the explained_variance_ratio_ field
contains the percentage of variance that each component explains.
The components_ field contains information on how much
features contribute to the components. To apply a trained transform to
the data, you can use the transform method.
To find the Pearson correlation coefficient, you can use the corrcoef function from the numpy package.

## Materials

Dow Jones Industrial Average History of the composition of companies included in the Dow Jones index

## Instructions for execution

1. Download the close_prices.csv data. This file contains the closing prices of 30 companies for each day of the period.

2. Using the downloaded data, train the PCA transform with 10 components. How many components are enough to explain 90% of the variance?
3. Apply the constructed transformation to the original data and take the values ​​of the first component.
4. Download the Dow Jones index information from the djia_prices.csv file.
What is the Pearson correlation between the first component and the Dow Jones index?
5. Which company has the largest weight in the first component?

Round the answer to two decimal places if necessary.
The answer to each task is a text file containing the answer in the
first line. Please note that the files submitted should not contain a blank line at the end. This is a limitation of the Coursera platform. We are working to remove this
limitation.