import streamlit as st
import pickle
import numpy as np
import pandas as pd

def optionToInt(option, list):
    counter = 0
    for item in list:
        if item == option:
            return counter
        counter += 1


st.title("Predicting Student Performance in Math, Reading, and Writing")

st.write("#### *We are Group 1: Cameron Cowling, Shijie Wei, Ngai Pan Ng, and Justin Wang.*")

gender_list = ["Female", "Male"]
gender = st.radio("Student Gender", gender_list, index=None, horizontal=True)

st.write("Ethnicity has been randomly given labels to protect privacy." )
race_ethnicity_list = ["Group A", "Group B", "Group C", "Group D", "Group E"]
race_ethnicity_list = st.radio("Race/Ethnicity", race_ethnicity_list, index=None, horizontal=True)

parental_education_list = ["No High School Diploma", "High School", "Some College", "Associate's Degree", "Bachelor's Degree or Higher"]
parental_education = st.radio("Parent's Highest Level of Education", parental_education_list, index=1, horizontal=False)

lunch = st.toggle("Free/Reduced Lunch", value=False)

test_prep = st.toggle("Completed Test Preperation Course", value=True)

with open('model.pkl', 'rb') as file:
    data = pickle.load(file)

coef = data["coefficients"]
intercept = data["intercept"]

st.write(sum(coef[0] * [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) + intercept[0])