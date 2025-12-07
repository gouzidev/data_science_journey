# breast cancer classification with jupyter

this project uses logistic regression to classify breast cancer tumors as malignant or benign based on various cell features. this is implemented as a jupyter notebook for interactive exploration and learning about binary classification.

## what is this?

we're building a classification model that predicts whether a breast tumor is malignant (cancerous) or benign (non-cancerous) based on features computed from cell nucleus characteristics. the data comes from the sklearn breast cancer dataset. this is a good project to learn about binary classification, confusion matrices, and model evaluation metrics.

## how to run it

simply use the init script:

```
./init.sh
```

this will:
1. create a virtual environment
2. activate it
3. install all dependencies
4. launch jupyter notebook

the notebook will open in your browser. you can run through all the cells to see the full analysis, from loading the data to training the model and evaluating predictions with confusion matrices and probability distributions.

## the data

the dataset contains breast cancer tumor measurements with 30 features including:
- mean radius, texture, perimeter, area, smoothness
- compactness, concavity, symmetry
- fractal dimension
- and their standard errors and worst values
- target: 0 (malignant) or 1 (benign)

## how it works

1. load the breast cancer dataset from sklearn
2. inspect the data to understand its structure with columns, describe, and info
3. split the data into training (75%) and testing (25%) sets
4. scale the features using StandardScaler (important for logistic regression)
5. train a logistic regression model on scaled training data
6. make predictions on test data
7. evaluate using confusion matrix to see true positives, true negatives, false positives, false negatives
8. calculate accuracy manually from confusion matrix
9. visualize confusion matrix with seaborn heatmap
10. analyze prediction confidence with probability distribution histogram

## evaluation metrics learned

this project taught me important classification evaluation concepts:
- confusion matrix structure: [[TN, FP], [FN, TP]]
- calculating accuracy: (TP + TN) / (TP + FP + TN + FN)
- understanding true positives vs false positives
- using predict_proba to see model confidence
- visualizing prediction probabilities to understand model certainty
- the importance of scaling features for logistic regression

## preprocessing lessons

- scaling features with StandardScaler (fit_transform on train, transform on test)
- understanding why we only use fit_transform once and then transform (to avoid re-learning)
- we don't scale y in classification (only X features need scaling)
- using random_state for reproducible train/test splits

## dependencies

- numpy
- pandas
- scikit-learn
- matplotlib
- seaborn
- jupyter

## files

- `notebook.ipynb` - the main jupyter notebook with all the analysis and model training
- `req.txt` - list of dependencies including jupyter
- `init.sh` - setup and run script to start jupyter notebook