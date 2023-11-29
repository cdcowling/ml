import streamlit as st
import pickle
import numpy as np

def optionToInt(option, list):
    counter = 0
    for item in list:
        if item == option:
            return counter
        counter += 1


st.title("Predicting College Student Performance")

st.write("#### *We are Group 1: Cameron Cowling, Shijie Wei, Ngai Pan Ng, and Justin Wang.*")

st.write("### We will predict your grade based on some attributes:")
st.write("##### About You:")

age_list = ["<21","22-25",">26"]
age = st.radio("Student Age", age_list, index=1, horizontal=True)

# st.write("Selected index ", optionToInt(age, age_list))

gender_list = ["Female", "Male"]
gender = st.radio("Student Gender", gender_list, index=None, horizontal=True)

high_school_list = ["Private", "Public", "Other"]
high_school = st.radio("Type of High School Graduated From", high_school_list, index=1, horizontal=True)

scholarship_list = ["None", "25%", "50%", "75%", "Full"]
scholarship = st.radio("Scholarship amount", scholarship_list, horizontal=True, index=2)

additional_work = st.toggle("Work/Study", value=False)
art_or_sport = st.toggle("Regularly do sports or art activties", value=False)
has_partner = st.toggle("Has Partner", value=False)

salary_list = ["135-200", "201-270", "271-340", "341-410", ">410"]
salary = st.radio("Salary Amount (thousands USD)", salary_list, horizontal=True)

transportation_list = ["Bus", "Car", "Bike", "Other"]
salary = st.radio("Type of Transportation", transportation_list, horizontal=True, index=2)

accomodation_list = ["Rental", "Dorm", "Family", "Other"]
accomodation = st.radio("Type of Accomodation", accomodation_list, horizontal=True)

education_list = ["Elementary School", "Middle School", "High School", "Bachelor's Degree", "Master's Degree", "Doctorate"]
mother_education = st.radio("Mother's Education Level", education_list, horizontal=False, index=2)
father_education = st.radio("Father's Education Level", education_list, horizontal=False, index=2, key='foo')
# education_list for mother and father

num_siblings_list = ["1", "2", "3", "4", "5+"]

parental_status_list = ["Married", "Divorced", "At Least One Parent Has Passed"]

mother_occupation_list = ["Retired","Housewife","Government Worker","Private Worker","Self-Employment", "Other"]

father_occupation_list = ["Retired","Government Worker","Private Worker","Self-Employment", "Other"]

weekly_study_hours_list = ["None", "<5 Hours", "6-10 Hours","11-20 Hours",">20 Hours"]

reading_frequency_list = ["None", "Sometimes","Often"]

# for non-science/science books

# attends_seminars is bool

project_impact_list = ["Positive", "Negative", "Neutral"]

attendance_list = ["Always","Sometimes","Never"]

midterm_prep_1_list = ["Alone", "With Friends", "N/A"]

midterm_prep_2_list = ["Right before exam", "Regularly during the course", "Never"]

notes_list = ["Never", "Sometimes","Always"]

listening_list = notes_list

discussion_list = notes_list

flip_classroom_list = ["Not Useful","Useful","N/A"]

last_gpa_list = ["<2.00", "2.00-2.49", "2.50-2.99","3.00-3.49",">3.49"]

expected_gpa_list = last_gpa_list

# course_id_list = range(1,10) # put on slider

