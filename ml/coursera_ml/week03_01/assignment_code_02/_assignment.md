# Text Analysis

This task is based on the materials of lectures on the support vector machine.

## You will learn:

- find optimal parameters for the support vector machine
- work with text data

## Introduction

The support vector machine (SVM) is one of the types of linear classifiers. The functionality it optimizes is aimed at maximizing the width of the dividing band between classes. From the theory of statistical learning, it is known that this width is closely related to the generalizing ability of the algorithm, and its maximization
allows you to combat overfitting.
One of the reasons for the popularity of linear methods is that they work well on sparse data. This is the name for samples with a large number of features, where most of the features on each object are equal to zero. Sparse data arises, for example, when working with texts. The point is that it is convenient to encode the text using a "bag of words" - as many features are formed as there are unique words in the texts, and the value of each feature is equal to the number of occurrences of the corresponding word in the document. It is clear that the total number of different words in a set of texts can reach tens of thousands, and only a small part of them will be found in one specific text.

You can encode texts more cleverly and record not the number of occurrences of a word in the text, but TF-IDF. This is an indicator that is equal to the product of two numbers: TF (term frequency) and IDF (inverse document frequency).
The first is equal to the ratio of the number of occurrences of a word in a document to the total
length of the document. The second value depends on how many documents in the sample this word occurs in. The more such documents, the

smaller the IDF. Thus, TF-IDF will have a high value for words that appear many times in a given document and rarely appear in the rest.

## Data

As we have already discussed above, linear methods are often used to solve various text analysis problems. In this task, we will use the support vector machine to determine which topic a news item belongs to: atheism or space.

## Implementation in Scikit-Learn

First, you will need to load the data. In this task, we will use one of the datasets available in scikit-learn - 20 newsgroups.
To do this, you need to use the datasets module:

```Python
from sklearn import datasets

newsgroups = datasets.fetch_20newsgroups(
subset=’all’ ,
categories=[’alt .atheism’ ,’sci .space’]
)
```
After executing this code, the array with texts will be in the
newsgroups.data field, the class number - in the newsgroups.target field.
One of the difficulties of working with text data is that
it needs to be given a numerical representation. One way to find such a representation is to calculate TF-IDF. In
Scikit-Learn, this is implemented in the sklearn.feature_extraction.text.TfidfVectorizer class.
The training sample must be transformed using the
fit_transform function, and the test sample - using transform.

The implementation of the SVM classifier is in the sklearn.svm.SVC class.
The weights of each feature in the trained classifier are stored in the
coef_ field.
It is convenient to select parameters using the sklearn.grid_search.GridSearchCV class.
Example of use:
```Python
grid = {’C’: np.power(10.0 , np.arange(5, 6))}
cv = KFold(y. size , n_folds=5, shuffle=True , random_state=241)
clf = svm.SVC(kernel=’linear ’, random_state=241)
gs = grid_search .GridSearchCV( clf , grid , scoring=’accuracy ’ , cv=cv)
gs. fit (X, y)
```

The first argument in GridSearchCV is the classifier for which the parameter values ​​will be selected, the second is a dictionary
(dict) that specifies the parameter grid for enumeration. After the enumeration is complete, you can analyze the quality values ​​for all parameter values ​​and select the best option:

```Python
for a in gs. grid_scores_ :
#a.mean_validation_score
#a.parameters
```
## Instructions for execution

1. Load objects from the 20 newsgroups news dataset related to the categories "space" and "atheism" (instructions are given above).
2. Calculate TF-IDF features for all texts. Please note that in this task we ask you to calculate TF-IDF for all data. With this approach, it turns out that the features on the training set use information from the test set, but this is quite natural, since we do not use the values ​​of the target variable from the test. In practice, it is not uncommon for the features of the test set objects to be known at the time of training, and therefore they can be used when training the algorithm.
3. Find the minimum best parameter C from the set [10^5, 10^4,... 104, 105] for SVM with a linear kernel (kernel=’linear’) using cross-

```
validation over 5 blocks. Specify the random_state=241 parameter for both SVM and KFold. Use the proportion of correct answers (accuracy) as a quality measure. ```
4. Train the SVM on the entire sample with the best parameter C found
on the previous