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

def intToArray(integer, max):
    array = []
    for x in range(0, max):
        if integer == x:
            array.append(1)
        else:
            array.append(0)
    return array

st.title("Predicting Student Performance in Math, Reading, and Writing")

st.write("#### *We are Group 1: Cameron Cowling, Shijie Wei, Ngai Pan Ng, and Justin Wang.*")

gender_list = ["Female", "Male"]
gender = st.radio("Student Gender", gender_list, index=0, horizontal=True)

st.write("Ethnicity has been randomly given labels to protect privacy." )
race_ethnicity_list = ["Group A", "Group B", "Group C", "Group D", "Group E"]
race_ethnicity = st.radio("Race/Ethnicity", race_ethnicity_list, index=0, horizontal=True)
race_ethnicity_int = optionToInt(race_ethnicity, race_ethnicity_list)
race_ethnicity_array = intToArray(race_ethnicity_int, len(race_ethnicity_list))

parental_education_list = ["Associate's Degree", "Bachelor's Degree", "Graduated High School", "Master's Degree or Above", "Some College", "Some High School"]
parental_education_sorted = ["Some High School", "Graduated High School", "Some College", "Associate's Degree", "Bachelor's Degree", "Master's Degree or Above"]
parental_education = st.radio("Parent's Highest Level of Education", parental_education_sorted, index=1, horizontal=False)
parental_education_int = optionToInt(parental_education, parental_education_list)
parental_education_array = intToArray(parental_education_int, len(parental_education_list))

lunch = st.toggle("Free/Reduced Lunch", value=False)
st.write(int(lunch))
test_prep = st.toggle("Completed Test Preperation Course", value=True)

with open('model.pkl', 'rb') as file:
    data = pickle.load(file)

coef = data["coefficients"]
intercept = data["intercept"]

array = []
array.append(int(gender == "Male"))
array.append(int(lunch))
array.append(int(test_prep))
array += parental_education_array
array += race_ethnicity_array

st.write(array)
st.write(sum(coef[0] * array) + intercept[0])