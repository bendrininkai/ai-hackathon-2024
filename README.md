# ai-hackathon-2024

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
