# ai-hackathon-2024

## Forecasting population of Vilnius

### `predicting.ipynb` notebook (the main one)

This Jupyter notebook contains code for a population forecasting model using Prophet. 
The model is designed to analyze population trends based on various demographics such as district, age bin, and gender. 
It supports hyperparameter tuning and visualization of results.

The notebook includes the following functionalities:
- Data loading and preprocessing
- Model training with hyperparameter tuning
- Visualization of results including training data, predictions, and trend lines

Key functions and their usage:
- `load_and_preprocess`: Loads and preprocesses the training and test data from CSV files.
- `normalize_data`: Normalizes the data to improve model performance.
- `train_models`: Trains all scenarios with given general set of hyperparameters or specified for a specific case.
- `make_predictions`: Makes predictions for scenarios.
- `plot_results`: Plot generalized results of all combinations in one (total population in Vilnius).
- `plot_individual_results`: Plots the individual results for a specific scenario.model.


### `test_single_case.ipynb` notebook (to look at cases and adjusting them)

This is the same as predictig.ipynb but it takes just a single case, runs it through many hyperparameters, clusters results and outputs them. Then the next step is to select appropriate cluster and generate this cluster hyperparameters to find a perfect set for specific case.

The notebook includes the following functionalities:
- Data loading and preprocessing
- Model training with hyperparameter tuning
- Clustering of predictions to identify unique models
- Visualization of results including training data, predictions, and trend lines

Key functions and their usage:
- `load_and_preprocess`: Loads and preprocesses the training and test data from CSV files.
- `normalize_data`: Normalizes the data to improve model performance.
- `train_and_evaluate_model`: Trains and evaluates the model for a specific scenario and hyperparameters.
- `make_scenario_predictions`: Makes predictions for a specific scenario.
- `cluster_predictions`: Clusters the model predictions to identify unique models.
- `plot_individual_results`: Plots the individual results for a specific scenario.
- `plot_predictions_for_selected_model`: Plots the predictions for the selected model.

## Dataset Description

### Train data

The X features are:

* district_id - an id representing one of many districts in Vilnius
* age_bin_id - an id representing one of the age bins; For example, the age_bin_id=0 may mean people that fall between 0 and 12 years of age.
* gender_bin_id - an id representing a gender.
* as_of_date_id - an id representing the point in time. It is very crucial to note, that bigger values mean farther points in time. For example, as_of_date_id = 0 could mean the date "2000-01" and as_of_date_id = 1 could mean the date "2000-02".
* count - the count of the certain population slice; Number of people. This is the main dependant variable that you will be trying to predict.

### Test data

* ID - the identifier of the observation which will be used when scoring.

There is no count column in the test data.

The features in the test data set should be used to make the predictions for the sample submission file.

### Sample submission file

The file, which should be uploaded for scoring, should have the following columns:

* ID - the identifier (from the test.csv) that will be used to evaluate the predictions
* count - the predicted people counts for certain slice.
