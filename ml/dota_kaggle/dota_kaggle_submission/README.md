# Dota 2: Win Probability Prediction (Kaggle Competition)
Predict Dota 2 match winner by the first 5 minutes of the game

[Kaggle Competition](https://www.kaggle.com/competitions/dota-2-win-probability-prediction/overview)
The training set consists of matches, for which all of the ingame events (like kills, item purchase etc.) as well as match outcome are know. You are given only the first 5 minutes of each match and you need to predict the likelihood of Radiant victory.



## Result of Kaggle Leaderboard
**169**/810 
![alt text](_readme001.png)

## Main files
- **dota2-kaggle-04.ipynb** - the notebook with main calculations
- **folders Dota2_01, Dota2_02, Dota2_03** - intermediate calculations

## Used Technologies and Packages

- **IPython.display**: For displaying objects interactively in the notebook.
- **datetime**: Utilized for handling date and time data.
- **math**: For mathematical operations.
- **numpy**: Used for numerical computations and array manipulations.
- **pandas**: For data manipulation and analysis, including handling of DataFrames.
- **scipy.sparse**: For working with sparse matrices.
- **scipy.stats**: For statistical operations.
- **sklearn.cross_validation**: Used for splitting data into training and testing sets.
- **sklearn.ensemble**: For ensemble methods like RandomForest.
- **sklearn.grid_search**: For hyperparameter optimization.
- **sklearn.linear_model**: For implementing linear models such as Logistic Regression.
- **sklearn.metrics**: For evaluating model performance.
- **sklearn.preprocessing**: For preprocessing data, such as normalization or scaling.
- **sklearn.tree**: For decision tree models.
- **sys**: Used for system-specific parameters and functions.
- **warnings**: For managing warnings during execution.


