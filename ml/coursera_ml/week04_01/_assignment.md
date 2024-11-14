# Linear Regression: Predicting Salary from a Job Description

This task is based on the lecture materials on linear regression and is devoted to predicting salary based on a job description.

## You will learn:

- use linear regression
- apply linear regression to text data

## Introduction

Linear methods are well suited for working with sparse data - such as texts. This can be explained by the
high learning speed and a small number of parameters, due to which overfitting can be avoided.
Linear regression has several varieties depending on the
regularizer used. We will work with ridge regression, which uses a quadratic or L2-regularizer.

## Implementation in Scikit-Learn

To extract TF-IDF features from texts, use the
sklearn.feature_extraction.text.TfidfVectorizer class.
To predict the target variable, we will use ridge regression, which is implemented in the sklearn.linear_model.Ridge class.

Note that the LocationNormalized and ContractTime features
are strings, and therefore cannot be worked with directly. Such non-numeric features with unordered values ​​are called categorical or nominal. A typical approach to their processing is to encode a categorical feature with m possible values
using m binary features. Each binary feature corresponds to one of the possible values ​​of the categorical feature and is an indicator that it takes this value on a given object. This approach is sometimes called one-hot encoding. Use it to recode the LocationNormalized and
ContractTime features. It is already implemented in the sklearn.feature_extraction.DictVectorizer class.
Example of usage:

```Python
from sklearn. feature_extraction import DictVectorizer
enc = DictVectorizer()
X_train_categ = enc.fit_transform(
data_train[[’LocationNormalized’,’ContractTime’]]
.to_dict(’records’))
X_test_categ = enc. transform(
data_test[[’LocationNormalized’,’ContractTime’]]
.to_dict(’records’))
```
You will need to replace missing values ​​with special string values ​​(e.g. ’nan’). The following code is suitable for this:

```Python
data_train [ ’LocationNormalized’ ].fillna( ’nan’ , inplace=True )
data_train [ ’ContractTime’ ].fillna( ’nan’ , inplace=True )
```
## Instructions for execution

1. Load data on job descriptions and corresponding annual salaries from the salary-train.csv file.
2. Perform preprocessing:
- Convert texts to lowercase.
- Replace everything except letters and numbers with spaces - this will make it easier to further split the text into words. The following call is suitable for such a replacement in the
text line:

```Python
re. sub(’[^a−zA−Z0−9]’ , ’␣’ , text.lower() )
```
- Use TfidfVectorizer to transform texts into feature vectors. Keep only those words that appear in at least 5 objects (the min_df parameter of TfidfVectorizer).
- Replace gaps in the LocationNormalized and ContractTime columns
with a special string ’nan’. The code for this was given above.
- Use DictVectorizer to obtain one-hot encoding of the LocationNormalized and ContractTime features.
- Combine all the obtained features into a single "objects-features" matrix. Note that the matrices for texts and categorical features are sparse. To combine their columns, use the scipy.sparse.hstack function.
3. Train ridge regression with alpha=1. The target variable is written in the SalaryNormalized column.
4. Build predictions for two examples from the salary-test-mini.csv file.
The values ​​of the predictions obtained are the answer to the task. Separate them with a space.

The answer to each task is a text file containing the answer in the first line. Please note that the files submitted should not contain an empty line at the end. This is a limitation of the Coursera platform. We are working to remove this
limitation.