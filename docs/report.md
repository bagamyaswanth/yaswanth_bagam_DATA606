# Title: Credit Card Approval Prediction

Name : Yaswanth Bagam

Campus ID : QF19336

  
## Introduction:
The most popular method of payment and purchase in recent years is using a credit card. Credit cards are a popular risk management strategy in the financial sector. To estimate the likelihood of future defaults and credit card borrowing, it uses the personal information and data provided by credit card applicants. The bank has the authority to choose whether or not to give the applicant a credit card. The degree of risk can be accurately measured by credit scores. Those scores later be used in purchase of houses, cars and other required items.

It's a very tedious process to approve the credit card. Credit card approval depends majorly up on the customers earning income, age factor and bank balances. However recently most of the applications are turndown from the bank due to the low credit score, limit credit history, insufficient income and high debts. It can be exceedingly challenging for bank workers to personally approve each and every credit card application. Therefore, we will use the attribute provided in the dataset in order to automate this process, and by running machine learning algorithms, the credit cards can be approved without any manual intervention.


## Links:

Presentation Link:

https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/Capstone_Credit_Card_Approval_Prediction.pptx

Youtube Link:

https://youtu.be/TRsRYWz6jTg

Trained picklefile Link:

https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/src/knn-hyp-model.pkl

## AIM:
This research supports the decision making process while speeding up the process to give a benefit for the bank as well as for the applicant and to attract on time paying customers by using banking data for smarter data–driven decision making. This research is highly applicable for banking and financing industries as most of the banks are granting credit card facilities to the customers. Hence the application of the model to local context to be considered. 

## Objective:
The primary objective of a credit card approval prediction project is to develop a model that can accurately predict whether a credit card application will be approved or not, based on various factors such as the applicant's credit score, income, employment status, and other relevant information.

The model can help financial institutions make informed decisions about approving or denying credit card applications and minimizing the risk of defaults and losses. By using machine learning algorithms to analyze and learn from historical data, the model can identify patterns and trends that are indicative of creditworthiness and use this information to make predictions about new applications. The ultimate goal is to improve the accuracy and efficiency of the credit card approval process, while also reducing the potential for fraud and default.

## Literature Survey:
Commercial banks contribute to economic growth in various aspects. One of the biggest revenue streams of any banking or financial institution would be from the interest charged from the lending. Banks have to face the biggest credit risk in all their lending. There are various lending products the banks are offering to the customers. However, Credit cards are one of the key lending products any bank would ever have. Almost all the financial institutions across the globe are going through challenging time and credit risk in offering credit facilities to their end customers. The repayments are least assured and it often ends up as a non-performing credit facility (NPL). This will in return affect banks cash flow and leads to build up backlogs in balance sheet which will not look good if the bank is a listed organization. 

Banks and financial institutions are critically assessing eligibility for a credit facility before granting facility to the customer due to the credit risk factor the credit card involved in. This process involves verification, validation, and approval and may cause delay of granting a facility which will be disadvantageous for the applicant as well as for the bank. Credit officers determine whether the borrowers can fulfill their requirements to being eligible for a facility and these judgments and predictions are always not accurate. Credit scoring is a traditional method assessing the credibility of a customer / entity applying for a bank credit facility. How much ever the banks and financial institutions are doing the background check of the individual customers by analyzing their eligibility, the bank most of the time end up in making wrong decisions. The study determines whether using Machine Learning Technology can assist the industry in overcoming from this risk. 

## Data Collection:
The project uses two datasets, namely credit_record.csv and application_record.csv, to offer preliminary information on the customer's credit history score and personal information.

### Two datasets:
  - application_record.csv
  - credit_record.csv

## Attribute description:

  ### application_record.csv
  The size of the dataset is 54.34MB contains 438558 records and 18 variables.
  
  - ID	: Client number
  
  - CODE_GENDER	: Gender
  
  - FLAG_OWN_CAR	: Is there a car

  - FLAG_OWN_REALTY	: Is there a property
  
  - CNT_CHILDREN	: Number of children
  
  - AMT_INCOME_TOTAL	: Annual income
  
  - NAME_INCOME_TYPE	: Income category
  
  - NAME_EDUCATION_TYPE	: Education level
  
  - NAME_FAMILY_STATUS	: Marital status
  
  - NAME_HOUSING_TYPE	: Way of living
  
  - DAYS_BIRTH	: Birthday
  
  - DAYS_EMPLOYED	: Start date of employment
  
  - FLAG_MOBIL	: Is there a mobile phone
  
  - FLAG_WORK_PHONE	: Is there a work phone
  
  - FLAG_PHONE	: Is there a phone
  
  - FLAG_EMAIL	: Is there an email
  
  - OCCUPATION_TYPE	: Occupation
  
  - CNT_FAM_MEMBERS	: Family size

  ### credit_record.csv
  The size of the dataset is 15.37MB contains 1048576 records and 3 variables.

  - ID	: Client number
  
  - MONTHS_BALANCE	: Record month
  
  - STATUS	: Status


## Merged Dataset based on Customer ID:
The combined dataset offers a thorough overview of all the data compiled from the two datasets.
![Merged_dataset_1](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/Merged_dataset_1.png)
![Attributes_merged_dataset](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/Attributes_merged_dataset.png)

## Category Distribution:
The category Distribution provides an insight into the amount of income per type and income category with respective car.
![name_income_type_wrt_amount_income](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/name_income_type_wrt_amount_income.png)
![name_income_type_wrt_car](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/name_income_type_wrt_car.png)

## Income type and Age Distribution category:
This section presents a comparison of the Income type and Age Distribution in each category.
![name_income_type](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/name_income_type.png)
![age_histogram](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/age_histogram.png)

## Attribute Correlations:
The attribute correlations provide a correlation between the different attributes such as employee from years, age , and net income.
![correlation_heatmap](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/correlation_heatmap.png)

## Machine Learning Algorithm Used:
This project uses KNN classifier, KNN is a simple, non-parametric algorithm for classification. It identifies the k nearest training data points based on a distance metric and assigns the majority class label to the new observation. It works well for large datasets and nonlinear decision boundaries and is often used as a baseline for complex models.

The KNN classifier is used for credit card prediction by training the model on a dataset of past credit card applications and their outcomes, and then using the model to predict whether a new credit card application is likely to be approved or rejected.

  ### Advantages:
  - Simple and easy to implement
  - Non-parametric and versatile
  - Robust to noisy data
  - High accuracy with sufficient data
  - No training phase required

## Machine Learning Classification Report:
The machine learing classification report provides insights about precision, recall and f1-score.
![ML_Classification_report](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/ML_Classification_report.png)

## Feature Importance:
Decision trees are commonly used to calculate feature importance. The importance of a feature is calculated based on how often it is used to split the data and the reduction in impurity achieved by each split.
![Feature_importance](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/Feature_importance.png)
![Feature_Selection_Importance](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/Feature_Selection_Importance.png)

## User Interface:
The user interface allows users to input customer details for analysis.
![User_interface](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/User_interface.png)
![User_interface_2](https://github.com/bagamyaswanth/yaswanth_bagam_DATA606/blob/main/docs/images/User_interface_2.png)

## Outcomes:
Based on the given user inputs like education, degree, family status ,assets, income value and experience the algorithms determines whether to approve or reject the credit card.
 ### Challenges:
  - Understanding the data
  - Data pre-processing
  - Feature selection
  - Modelling, finding the best model to improve the accuracy of the prediction.
  - hyperparameter tuning
  - Data Quality

## Conclusion:
In summary, a credit card approval machine learning project using KNN classifier can effectively predict credit card approval or denial. By optimizing the KNN classifier model through feature selection, hyperparameter tuning, and evaluating performance using appropriate metrics, high accuracy can be achieved to assist financial institutions and lenders to make informed decisions and reduce risk of default. However, it is crucial to ensure that the data is representative and unbiased, and that different hyperparameter values are experimented with to find the optimal configuration for the dataset. Overall, a credit card approval machine learning project using KNN classifier has the potential to provide valuable insights for data-driven decision making.

### References:
- Credit Card Approval Prediction Dataset

  https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction
  
- M. P. C. Peiris. (2019). Credit Card Approval Prediction by Using Machine Learning. 

  https://dl.ucsc.cmb.ac.lk/jspui/bitstream/123456789/4593/1/2018%20BA%20026.pdf

- Aman Sangal. (2022). Predicting Credit Card Approvals using Machine Learning.

  https://medium.com/@amansangal9/predicting-credit-card-approvals-8409c5280f91 
  
