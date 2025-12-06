# auto mpg prediction with jupyter

this project uses linear regression to predict mpg (miles per gallon) of cars based on various features. unlike the other projects, this one is implemented as a jupyter notebook for interactive exploration and learning.

## what is this?

we're building a model that predicts how many miles per gallon a car can get based on its features like horsepower, weight, cylinders, acceleration, and more. the data comes from a classic auto-mpg dataset. this is a good project to learn about data preprocessing and handling messy data in real world scenarios.

## how to run it

first install the dependencies:

```
pip install -r req.txt
```

then start the jupyter notebook:

```
jupyter notebook notebook.ipynb
```

or simply use the init script:

```
./init.sh
```

the notebook will open in your browser. you can run through all the cells to see the full analysis, from loading the data to training the model and visualizing the results.

## the data

the CSV file contains auto-mpg information with the following columns:
- `mpg`: miles per gallon (what we're trying to predict)
- `horsepower`: engine horsepower (note: this column had some corrupt values with `?` marks)
- `weight`: weight of the car
- `cylinders`: number of cylinders
- `displacement`: engine displacement
- `acceleration`: time to accelerate
- `origin`: country of origin
- `model year`: year of manufacture

## how it works

1. load the auto-mpg dataset from CSV
2. inspect the data to understand its structure and identify issues
3. clean the data (handle corrupt values like `?` in horsepower)
4. split the data into training (75%) and testing (25%) sets
5. scale the features using StandardScaler (important for linear regression)
6. train a linear regression model on scaled training data
7. evaluate the model using r-squared score on both training and test data
8. visualize the predictions vs actual values with a scatter plot and diagonal line

## preprocessing lessons

this project taught me important preprocessing concepts:
- detecting and handling corrupt data (the `?` values in horsepower column)
- filling missing values with the mean of the column
- scaling features with StandardScaler (fit_transform on train, transform on test)
- understanding why we only use fit_transform once and then transform (to avoid re-learning)
- the importance of using scaled data when training linear regression models

## dependencies

- numpy
- pandas
- scikit-learn
- matplotlib
- jupyter

## files

- `notebook.ipynb` - the main jupyter notebook with all the analysis and model training
- `auto-mpg.csv` - dataset with auto information and mpg values
- `req.txt` - list of dependencies including jupyter
- `init.sh` - setup and run script to start jupyter notebook
