# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import streamlit as st
import pickle

pickle_in = open("log_reg_file.pkl",'rb')
classifier = pickle.load(pickle_in)
print(classifier)

def welcome():
    return "Welcome All"

def prediction_titanic(PassengerId,Pclass,Age,SibSp,Parch,Fare,Gender):
    
    PassengerId = int(PassengerId)
    Pclass = int(Pclass)
    Age = float(Age)
    SibSp = int(SibSp)
    Parch = int(Parch)
    Fare = float(Fare)
    Gender = int(Gender)
    prediction = classifier.predict([[PassengerId,Pclass,Age,SibSp,Parch,Fare,Gender]])
    print(prediction)
    return prediction

def main():
    st.title("Titanic Surival Prediction ")
    PassengerId = st.text_input("PassengerId")
    Pclass = st.text_input("Pclass", "")
    Age = st.text_input("Age", "")
    SibSp = st.text_input("Sibsp", "")
    Parch = st.text_input("Parch" , "")
    Fare = st.text_input("Fare", "")
    Gender = st.text_input("Gender", "")
    result = ""
    if st.button("Predict"):
        if PassengerId and Pclass and Age and SibSp and Parch and Fare and Gender:
            result = prediction_titanic(PassengerId, Pclass, Age, SibSp, Parch, Fare, Gender)
            if result[0] == 0:
                result = "Not Survived"
            else:
                result = "Survived"
        else:
            st.error("Please fill in all the input fields.")
    
    st.success(f"The Person {result}")       
      
    
    
if __name__=="__main__":
    main()
    
    
              

