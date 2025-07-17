import pandas as pd

a = pd.read_csv(
    r"C:\Users\subhadip sinha\OneDrive\CODING\PYTHON\Scikit-Learn\covid.csv"
)
from sklearn.impute import SimpleImputer

sim = SimpleImputer(strategy="mean")
s = sim.fit_transform(a[["fever"]])
a["fever"] = pd.DataFrame(s, columns=["fever"])
a.isnull().sum()

from sklearn.preprocessing import OrdinalEncoder

rd = OrdinalEncoder()
a[["gender", "cough", "city"]] = rd.fit_transform(a[["gender", "cough", "city"]])

from sklearn.preprocessing import LabelEncoder

lae = LabelEncoder()
a["has_covid"] = lae.fit_transform(a["has_covid"])

x = a.iloc[:, :-1]
y = a.iloc[:, -1]
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)


from sklearn.svm import SVC

sv = SVC(kernel="linear")
sv.fit(x_train, y_train)
sv.score(x_test, y_test) * 100


import streamlit as st

st.title("COVID-19 Prediction")
st.write(
    "This is a simple web app to predict COVID-19 based on symptoms and demographics"
)

st.sidebar.title("Input Features")
age = st.sidebar.slider(
    "age",
    int(a["age"].min()),
    int(a["age"].max()),
)
gender = st.sidebar.slider(
    "gender",
    float(a["gender"].min()),
    float(a["gender"].max()),
)
# etc.

fever = st.sidebar.slider(
    "fever",
    float(a["fever"].min()),
    float(a["fever"].max()),
)
cough = st.sidebar.slider(
    "cough",
    float(a["cough"].min()),
    float(a["cough"].max()),
)

city = st.sidebar.slider(
    "city",
    float(a["city"].min()),
    float(a["city"].max()),
)


input_data = [
    [
        age,
        gender,
        fever,
        cough,
        city,
    ]
]
prediction = sv.predict(input_data)
target_name = ["Has COVID", "No COVID"]
predicted_species = target_name[prediction[0]]


st.write("Prediction")
st.write(f"The predicted species is:====> {predicted_species}")

st.line_chart(a)
st.write(a)
