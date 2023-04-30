## Report Analysis

## Overview of the Analysis

* The purpose of this analysis is to build a model that can identify the creditworthiness of borrowers.
* A dataset of loan activity from individuals was used.You can predict the accuracy of healthy loans and high-risk loans defaulting.
* The discrepency of types of loans is significant as there are a lot more healthy loans versus high-risk loans provided in this dataset.
* At first determining the number of types of loans given and then creating a percentage of those types of loans can helped predict the more successful of the two. Although since the dataset had a lot more of one type of loan than the other, it could have potentially skewed the data to a certain loan type.
* Utilized Logistic Regression and imbalanced classification reporting to determine which model works better for the dataset.

## Results

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
      * A value of 0 in the “loan_status” column means that the loan is healthy. A value of 1 means that the loan has a high risk of defaulting.
      * With the mean of this model being 0.99, it can be predicted that healthy loans would bring a 99% chance of being the right choice versus high-risk loans which would yield 0.88, an 88% chance of defaulting.


* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
      * A value of 0 in the “loan_status” column means that the loan is healthy. A value of 1 means that the loan has a high risk of defaulting.
      * With the mean of this model being 1.00, it can be predicted that healthy loans would have a 100% chance of being the right call versus 0.91, 91% chance of defaulting with a high-risk loan. Healthy loans would yield a much better chance of not defaulting versus high-risk loans. 

## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?
    * It seems the Machine Learning Model 2 performs slightly better overall due to the 100% status of healthy loans and 91% chance of defaulting for high-risk loans, although both would be great models get an idea of what majority of peers statuses are. 
* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )
    * It is important to predict the 0's because there is significant amount of data for this set versus the 1's which has the potential to be different with more data being accrued.