# student score prediction

this project uses linear regression to predict student exam scores based on various factors like study hours, sleep, attendance, and previous performance.

## what is this?

basically we're trying to build a model that can predict how well a student will do on their exam. We take in data about how many hours they studied, how much sleep they got, how often they showed up to class, and their previous test scores. Then we use linear regression to figure out the relationship between all these factors and their final exam score.

## how to run it

first you gotta install the dependencies:

```
pip install -r req.txt
```

then just run the main script:

```
python main.py
```

or simply run the script:

```
./init.sh
```

this will train the model on some of the data, test it on the rest, and show you a graph comparing what the model predicted vs what actually happened.
 graph should show points close to the diagonal line if the model is working decent.

## the data

we got a CSV file with 200 students or so. Each row has:
- `hours_studied`: how many hours they studied
- `sleep_hours`: hours of sleep the night before
- `attendance_percent`: percentage of classes they attended
- `previous_scores`: their score from a previous test
- `exam_score`: the actual exam score (this is what we're trying to predict)

## how it works

1. read in the student data
2. split it into training and testing sets (80/20 split)
3. train a linear regression model on the training data
4. use the model to make predictions on the test data
5. plot the actual vs predicted scores to see how good we are

pretty straightforward stuff. matplotlib graph will pop up showing you how close the predictions are to reality.

## Dependencies

- numpy
- pandas
- scikit-learn
- matplotlib

## Files

- `main.py` - The main script that does all the work
- `student_exam_scores.csv` - The dataset with all the student data
- `req.txt` - List of dependencies
- `init.sh` - Setup script (if you wanna use it)
