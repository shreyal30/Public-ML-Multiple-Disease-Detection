# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:21:26 2024

@author: hp
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabeties_model=pickle.load(open('diabetes_model.sav','rb'))
heart_model=pickle.load(open('heart_model.sav','rb'))
parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         icons=['activity','box2-heart-fill','person-add'],
                         default_index=0)
    
#DIABETES PREDICTION PAGE
if (selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.text_input("Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose")
    with col3:
        BloodPressure = st.text_input("BloodPressure")
    with col1:
        SkinThickness = st.text_input("SkinThickness")
    with col2:
        Insulin = st.text_input("Insulin")
    with col3:
        BMI = st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    with col2:
        Age = st.text_input("Age")
        
    diab_diagnosis=''
    if st.button('Diabetes Test Results'):
        diab_prediction=diabeties_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diab_prediction[0]==0):
            diab_diagnosis="The person is Not Diabetic"
        else:
            diab_diagnosis="The person is Diabetic"
    st.success(diab_diagnosis)
    
    
#HEART DISEASE PREDICTION PAGE
if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
    col1,col2,col3=st.columns(3)
    with col1:
        Age = st.text_input("Age")
    with col2:
        Sex = st.text_input("Sex")
    with col3:
        Chestpain = st.text_input("Chest Pain Type")
    with col1:
        BP = st.text_input("BP")
    with col2:
        Cholesterol = st.text_input("Cholesterol")
    with col3:
        FBSOver120 = st.text_input("FBS over 120")
    with col1:
        EKGResults = st.text_input("EKG results")
    with col2:
        MaxHR = st.text_input("Max HR")
    with col3:
        ExerciseAngina = st.text_input("Exercise angina")
    with col1:
        STDepression = st.text_input("ST depression")
    with col2:
        SlopeofST = st.text_input("Slope of ST")
    with col3:
        NumberOfVesselsFluro = st.text_input("Number of vessels fluro")
    with col1:
        Thallium = st.text_input("Thallium")
        
    heart_disease=''
    if st.button('Heart Test Results'):
        heart_disease_prediction=heart_model.predict([[Age,Sex,Chestpain,BP,Cholesterol,FBSOver120,EKGResults,MaxHR,ExerciseAngina,STDepression,SlopeofST,NumberOfVesselsFluro,Thallium]])
        if(heart_disease_prediction[0]=='Presence'):
            heart_disease="The person has Heart Disease"
        else:
            heart_disease="The person does not have Heart Disease"
    st.success(heart_disease)
    
#PARKINSONS PREDICTION PAGE
if (selected=='Parkinsons Prediction'):
    st.title('Parkinsons Prediction')
    col1,col2,col3=st.columns(3)
    with col1:
        name = st.text_input("name")
    with col2:
        MDVP_Fo_Hz = st.text_input("MDVP:Fo(Hz)")
    with col3:
        MDVP_Fhi_Hz= st.text_input("MDVP:Fhi(Hz)")
    with col1:
        MDVP_Flo_Hz = st.text_input("MDVP:Flo(Hz)")
    with col2:
        MDVP_Jitter = st.text_input("MDVP:Jitter(%)")
    with col3:
        MDVP_Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col1:
        MDVP_RAP = st.text_input("MDVP:RAP")
    with col2:
        MDVP_PPQ = st.text_input("MDVP:PPQ")
    with col3:
        Jitter_DDP = st.text_input("Jitter:DDP")
    with col1:
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")
    with col2:
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col3:
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    with col1:
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
    with col2:
        MDVP_APQ = st.text_input("MDVP:APQ")
    with col3:
        Shimmer_DDA	 = st.text_input("Shimmer:DDA	")
    with col1:
        NHR= st.text_input("NHR")
    with col2:
        HNR= st.text_input("HNR")
    with col3:
        RPDE = st.text_input("RPDE")       
    with col1:
        DFA= st.text_input("DFA")
    with col2:
        spread1= st.text_input("spread1")
    with col3:
        spread2 = st.text_input("spread2") 
    with col1:
        D2= st.text_input("D2")
    with col2:
        PPE= st.text_input("PPE")
    parkinsons_disease=''
    if st.button('Parkinsons Test Results'):
        parkinsons_prediction=parkinsons_model.predict([[name,MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if(parkinsons_prediction[0]==0):
            parkinsons_disease="The person does Not have Parkinson's Disease"
        else:
            parkinsons_disease="The person have Parkinsons's Disease"
    st.success(parkinsons_disease)
