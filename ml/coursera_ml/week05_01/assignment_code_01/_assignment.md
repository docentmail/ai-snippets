# Random Forest Size

This task is based on the materials of lectures on logical methods and is aimed at familiarizing with random forests.

## You will learn:

- work with a random forest - one of the most common families of algorithms
- solve regression problems with it
- select random forest parameters

## Introduction

A random forest is a classification model that combines a number of decision trees into one composition, thereby improving their performance and generalization ability. Trees are built independently of each other. To make them different from each other,
training is carried out not on the entire training sample, but on its random
subset. Also, to further reduce the similarity of trees,
the optimal feature for splitting is selected not from all possible
features, but only from their random subset. The predictions given by the
trees are combined into a single answer by averaging.
A feature of the random forest is that it does not retrain as the number of trees in the composition increases. This is achieved due to the fact that the trees are independent of each other, and therefore
adding a new tree to the composition does not complicate the model, but only
reduces the noise level in the predictions.

## Implementation in Scikit-Learn

In the scikit-learn library, random forests are implemented in the classes
sklearn.ensemble.RandomForestClassifier (for classification) and
sklearn.ensemble.RandomForestRegressor (for regression). The model is trained using the fit function, and predictions are made using the predict function. The number of trees is specified using the class field
n_estimators.
Example of usage:

```Python
import numpy as np
from sklearn. ensemble import RandomForestRegressor
X = np.array([[ 1,2],[3,4],[5,6]])
y = np.array([−3,1,10])
clf = RandomForestRegressor(n_estimators =100)
clf.fit(X, y)
predictions = clf.predict(X)
```

Also in this task you will need to calculate the quality of predictions on the test sample. We will use the R2 metric - in essence, this is the root mean square error (RMSE), normalized to the interval [0, 1] and inverted so that its best value is one. It can be calculated using the sklearn.metrics.r2_score function.
The first argument is the list of correct answers in the sample,
the second is the list of predicted answers. Example of usage:

```Python
from sklearn.metrics import r2_score
print r2_score([10,11,12],[9,11,12.1])
```

## Instructions for execution

In this task, you need to track the change in the quality of a random forest depending on the number of trees in it.

1. Load the data from the abalone.csv file. This is a dataset in which it is required to predict the age of a shell (number of rings) based on physical

measurements. 2. Transform the Sex feature into a numeric one: the F value should go

to -1, I - to 0, M - to 1. If you are using Pandas, the following code will

work:
```Python
data[’Sex’] = data[’Sex’].map(lambda x: 1 if x == ’M’ else (-1 if x == ’F’ else 0))
```

3. Divide the contents of the files into features and the target variable.
The last column contains the target variable, the rest contain the
features.
4. Train a random forest (sklearn.ensemble.RandomForestRegressor)
with a different number of trees: from 1 to 50 (random_state=1). For
each of the options, evaluate the quality of the resulting forest
on cross-validation in 5 blocks. Use the parameters "random_state=1" and
"shuffle=True" when creating the cross-validation generator sklearn.cross_validation.KFold.
Use the proportion of correct answers (sklearn.metrics.r2_score) as a quality measure.
5. Determine the minimum number of trees at which the random forest shows a cross-validation quality higher than 0.52. This

number will be the answer to the task.
6. Note how the quality changes as the number of trees increases. Does it get worse?

The answer to each task is a text file containing the answer in
the first line. Please note that the files submitted should not contain an empty line at the end. This is a limitation of the Coursera platform. We are working to remove this

limitation.