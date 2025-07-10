# import the streamlit library
import streamlit as st

# give a title to our app
st.title("Welcome to BMI Calculator")

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio("Select your height format: ", ("cms", "meters", "feet"))

# compare status value
if status == "cms":
    # take height input in centimeters
    height = st.number_input("Centimeters")

    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some value of height")

elif status == "meters":
    # take height input in meters
    height = st.number_input("Meters")

    try:
        bmi = weight / (height**2)
    except:
        st.text("Enter some value of height")

else:
    # take height input in feet
    height = st.number_input("Feet")

    # 1 meter = 3.28
    try:
        bmi = weight / (((height / 3.28)) ** 2)
    except:
        st.text("Enter some value of height")

# check if the button is pressed or not
if st.button("Calculate BMI"):

    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))

    # give the interpretation of BMI index
    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif bmi >= 16 and bmi < 18.5:
        st.warning("You are Underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.success("Healthy")
    elif bmi >= 25 and bmi < 30:
        st.warning("Overweight")
    elif bmi >= 30:
        st.error("Extremely Overweight")

import pandas as pd

a = pd.read_csv(r"D:\PYTHON_environment\web_app\Test_new.csv")

st.write("csv file:-")
st.write(a)
st.line_chart(a)

st.bar_chart(a)

from PIL import Image

img = Image.open(r"D:\PYTHON_environment\web_app\8788506.jpg")
st.image(img, caption="this is a wallpepar")


# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):

    # display the text if the checkbox returns True value
    st.text("Showing the widget")


# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ("Male", "Female"))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if status == "Male":
    st.success("Male")
else:
    st.success("Female")


# multi select box

# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ", ["Dancing", "Reading", "Sports"])

# write the selected options
st.write("You selected", len(hobbies), "hobbies")


# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if st.button("About"):
    st.text("Welcome To GeeksForGeeks!!!")


# st.bar_chart(a["age"])
