import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

import pickle

from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot
import plotly.figure_factory as ff
import plotly.express as px
from sklearn.model_selection import train_test_split
# define the model
model = RandomForestRegressor()
# fit the model
df = pd.read_csv("C:\\Users\\yaswa\\Downloads\\Data 606\\finalDataset.csv")
df = df.drop('Unnamed: 0',axis=1)
X = df.drop(['APPROVAL_STATUS'], axis=1)
y =  df['APPROVAL_STATUS']
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state = 10)

model.fit(X_train, y_train)
# get importance
importance = model.feature_importances_
# summarize feature importance

# plot feature importance
x = X_train.columns

sorted_list = sorted(zip(x,importance), key=lambda x: x[1], reverse=True) 

x_labels = [val[0] for val in sorted_list]
y_labels = [val[1] for val in sorted_list]

fig1 = px.bar(x=x_labels, y=y_labels)

app_mode = st.sidebar.selectbox('Select Page',['Home','Credit Approval Prediction'])

income_type = {'Working':1, 'Commercial associate':2, 'Pensioner':3, 'State servant':4,'Student':5}
education_type = {'Higher education':1, 'Secondary ': 2, 'Incomplete higher': 3,'Lower secondary': 4, 'Academic degree': 5}
family_status = {'Civil marriage':1, 'Married':2, 'Single ':3, 'Separated':4, 'Widow':5}
housing_type = {'Rented apartment':1, 'House':2, 'Municipal apartment':3,'With parents':4, 'Co-op apartment':5, 'Office apartment':6}
gender = {'Male':0,'Female':1}
own_car = {'Yes':0,'No':1}
own_realty = {'Yes':0,'No':1}
work_phone = {'Yes':0,'No':1}
own_mobil = {'Yes':0,'No':1}
flag_email = {'Yes':0,'No':1}

if app_mode=='Home':
    st.title('Credit Card Approval Prediction')
    st.markdown('Dataset :')
    df=pd.read_csv('credit_data_clean.csv')
    df = df.drop('Unnamed: 0',axis=1)
    st.write(df.head())
    st.markdown('Feature Importance:')
    st.plotly_chart(fig1)


elif app_mode == 'Credit Approval Prediction':
    st.header('Fill in all details to get prediction')
    col1,col2 = st.columns(2)
    
    with col1:
        gender_input = st.selectbox('Gender',gender.keys())
        age_input = st.number_input("Age", min_value=0, max_value=120)
        family_status_input = st.selectbox('Family Status',family_status.keys())
        number_of_members_input = st.number_input("Count of Family Members", min_value=0, max_value=120)
        number_of_children_input = st.number_input("Number of Children", min_value=0, max_value=120)
        has_car_input = st.selectbox('Own a Car?',own_car.keys())
        has_realty_input = st.selectbox('Own Realty?',own_realty.keys())
        
        # pass
    with col2:
        income_type_input = st.selectbox('Income Type',income_type.keys())
        income_input = st.number_input("Income value")
        experience_input = st.number_input("Experience",min_value=0,max_value=age_input)
        education_type_input = st.selectbox('Education Type',education_type.keys())
        hoursing_type_input = st.selectbox('Housing Type',housing_type.keys())
        has_work_phone_input = st.selectbox('Have work phone?',own_mobil.keys())
        has_personal_phone_input = st.selectbox('Have personal phone?',own_mobil.keys())
        has_email_input = st.selectbox('Have EMail?',own_car.keys())

    if st.button("Predict"):

        
    


        input = {'CODE_GENDER':gender_input, 'FLAG_OWN_CAR':has_car_input, 'FLAG_OWN_REALTY':has_realty_input, 'CNT_CHILDREN':number_of_children_input,
            'AMT_INCOME_TOTAL':income_input, 'NAME_INCOME_TYPE':income_type_input, 'NAME_EDUCATION_TYPE':education_type_input,
            'NAME_FAMILY_STATUS':family_status_input, 'NAME_HOUSING_TYPE':hoursing_type_input, 'FLAG_WORK_PHONE':has_work_phone_input, 'FLAG_PHONE':has_personal_phone_input, 'FLAG_EMAIL':has_email_input,
            'CNT_FAM_MEMBERS':float(number_of_members_input),  'AGE':age_input,'EMPLOYEE_FROM_YEARS':experience_input}

        input['CODE_GENDER'] = gender[input['CODE_GENDER']]
        input['FLAG_OWN_CAR'] = own_car[input['FLAG_OWN_CAR']]
        input['FLAG_OWN_REALTY'] = own_realty[input['FLAG_OWN_REALTY']]
        input['NAME_INCOME_TYPE'] = income_type[input['NAME_INCOME_TYPE']]
        input['NAME_EDUCATION_TYPE'] = education_type[input['NAME_EDUCATION_TYPE']]
        input['NAME_FAMILY_STATUS'] = family_status[input['NAME_FAMILY_STATUS']]
        input['NAME_HOUSING_TYPE'] = housing_type[input['NAME_HOUSING_TYPE']]
        input['FLAG_PHONE'] = own_mobil[input['FLAG_PHONE']]
        input['FLAG_WORK_PHONE'] = work_phone[input['FLAG_WORK_PHONE']]
        input['FLAG_EMAIL'] = flag_email[input['FLAG_EMAIL']]


        picklefile = open("knn-hyp-model.pkl", "rb")
        model = pickle.load(picklefile)

        prediction = model.predict([[input['CODE_GENDER'],input['FLAG_OWN_CAR'],input['FLAG_OWN_REALTY'],input['CNT_CHILDREN'],input['AMT_INCOME_TOTAL'],\
            input['NAME_INCOME_TYPE'],input['NAME_EDUCATION_TYPE'],input['NAME_FAMILY_STATUS'],input['NAME_HOUSING_TYPE'],\
                    input['FLAG_WORK_PHONE'],input['FLAG_PHONE'],input['FLAG_EMAIL'],input['CNT_FAM_MEMBERS'],input['AGE'],input['EMPLOYEE_FROM_YEARS']]])
        # prediction = model.predict(results)

        print(prediction)
        if prediction[0] == 0.0:
            st.success('approved')
        elif prediction[0] == 1.0:
            st.error( 'not approved')