import streamlit as st

st.title("web app")

st.write("this is smple text ")
import pandas as pd

a = pd.read_csv(r"D:\PYTHON_environment\web_app\null.csv")

st.write("csv file:-")
st.write(a)
# print(a)

st.line_chart(a)

age = st.slider("select age= ", 0, 100, 25)

if age:
    st.write(f"age is {age}")


aa = st.text_input("enter your name =")
st.write(f"hello{aa}")

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


st.bar_chart(a["age"])
