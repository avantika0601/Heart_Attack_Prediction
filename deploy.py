import numpy as np
import pandas as pd
import pickle
import streamlit as st


pickle_in=open("class_final.pkl",'rb')
classifier=pickle.load(pickle_in)

def predictor(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    if sex=='Male':
        sex=1
    elif sex=='Female':
        sex=0
    
    
    if cp=='Typical Angina':
        cp=0
    elif cp=='Atypical Angina':
        cp=1
    elif cp=='Non-anginal Pain':
        cp=2
    elif cp=='Asymptomatic':
        cp=3
    
    if fbs=='True':
        fbs=1
    elif fbs=='False':
        fbs=0
    
    if restecg=='Normal':
        restecg=0
    elif restecg=='ST-T Wave Normality':
        restecg=1
    elif restecg=='Left Ventricular Hypertrophy':
        restecg=2
    
    if exang=='Yes':
        exang=1
    elif exang=='No':
        exang=0
    
    if thal=='0':
        thal=0
    elif thal=='1':
        thal=1
    elif thal=='2':
        thal=2
    elif thal=='3':
        thal=3
    
    
    prediction=classifier.predict(pd.DataFrame([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]],columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']))
    return prediction   
        
        
    
    



st.title('Heart Attack Prediction')
st.header('Enter the required details below')
age=st.number_input('Age:')
sex=st.selectbox('Sex:',['Male','Female'])
cp=st.selectbox('Chest Pain Type:',['Typical Angina','Atypical Angina','Non-anginal Pain','Asymptomatic'])
trestbps=st.number_input('Resting Blood Pressure:')
chol=st.number_input('Cholesterol:')
fbs=st.selectbox('Fasting Blood Sugar:',['True','False'])
restecg=st.selectbox('Resting ECG Results',['Normal','ST-T Wave Normality','Left Ventricular Hypertrophy'])
thalach=st.number_input('Max Heart Rate Achieved')
exang=st.selectbox('Exercise Induced Angina',['Yes','No'])
oldpeak=st.number_input('Previous Peak')
slope=st.number_input('Slope',min_value=0,max_value=2,value=1)
ca=st.number_input('Number of Major Vessels',min_value=0,max_value=3,value=1)
thal=st.selectbox('Thalium Stress Test Result',['0','1','2','3'])

if st.button('Predict Heart Attack'):
    my_predict=predictor(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    if my_predict==1:
        st.success('There is a high risk of heart attack')
    else:
        st.success('Low risk of heart Attack')
    