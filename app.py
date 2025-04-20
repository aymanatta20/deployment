import streamlit as st
import pickle
import numpy as np


with open('D:/streamlit/model_breast-cancer.pkl', 'rb') as f:



    model = pickle.load(f)

st.title("Breast cancer diagnosis")


f1 = st.number_input("special 1")


if st.button("predict"):
    input_data = np.array([[f1]])
    prediction = model.predict(input_data)[0]
    st.success(f"Result prediction: {'injured' if prediction == 1 else 'sound'}")
