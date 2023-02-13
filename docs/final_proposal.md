# Credit Card Approval Prediction:

The most popular method of payment and purchase in recent years is using a credit card. Credit cards are a popular risk management strategy in the financial sector. To estimate the likelihood of future defaults and credit card borrowing, it uses the personal information and data provided by credit card applicants. The bank has the authority to choose whether or not to give the applicant a credit card. The degree of risk can be accurately measured by credit scores. Those scores later be used in purchase of houses, cars and other required items. 

Having a prior experience in the banking and financing sector it's a very tedious process to approve the credit card. Credit card approval depends majorly up on the customers earning income, age factor and bank balances. However recently most of the applications are turndown from the bank due to the low credit score, limit credit history, insufficient income and high debts.  It can be exceedingly challenging for bank workers to personally approve each and every credit card application. Therefore, we will use the attribute provided in the dataset in order to automate this process, and by running machine learning algorithms, the credit cards can be approved without any manual intervention.

# Source of the Dataset:
https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction

# Two datasets:
application_record.csv
credit_record.csv

# Attributes:
## application_record.csv
The size of the dataset is 54.34MB contains 438558 records and 18 variables.

- Feature name	Explanation
- ID	Client number
- CODE_GENDER	Gender
- FLAG_OWN_CAR	Is there a car
- FLAG_OWN_REALTY	Is there a property
- CNT_CHILDREN	Number of children
- AMT_INCOME_TOTAL	Annual income
- NAME_INCOME_TYPE	Income category
- NAME_EDUCATION_TYPE	Education level
- NAME_FAMILY_STATUS	Marital status
- NAME_HOUSING_TYPE	Way of living
- DAYS_BIRTH	Birthday
- DAYS_EMPLOYED	Start date of employment
- FLAG_MOBIL	Is there a mobile phone
- FLAG_WORK_PHONE	Is there a work phone
- FLAG_PHONE	Is there a phone
- FLAG_EMAIL	Is there an email
- OCCUPATION_TYPE	Occupation
- CNT_FAM_MEMBERS	Family size

## credit_record.csv
The size of the dataset is 15.37MB contains 1048576 records and 3 variables.

- Feature name	Explanation
- ID	Client number
- MONTHS_BALANCE	Record month
- STATUS	Status

# Analysis :
- Clean and transform the data frame using various machine learning library like sklearn, numpy, pandas
- Plot various plots to understand relationship between various features of dataset.
- After applying all the pre-processing steps in our dataset we have to create our machine learning column.
- Split data into training and testing data.
- performing EDA for data visualization and data insights.
- using machine learning models to predict the credit card scores.
- Identify the suitable and unsuitable candidates.
- Create the most reliable models to forecast credit card acceptance

# Techniques and models:
To predict whether or not the Customer will get credit card approved using classification algorithms such as
- Random forest
- Support vector machine
- Decision tree
- K-nearest neighbour
- Logistic Regression

# Outcome:
In this project, Since application record and credit record are two separate data files, they are combined using the ID key. I'd like to create a model using a pipeline that includes pre-processing, feature selection, classification, and post-processing after completing exploratory data analysis. I want to fine-tune the model using hyper-parameter tuning for optimization. The accuracy of each classifier will be evaluated using a voting classifier and boosting approaches. Finally, I would select the model that best fits the data based on the classification, clustering, and regression challenges as well as the performance, recall, and accuracy of the model.
