import streamlit as st
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

st.title("Wage prediction")

with open('model.pickle', 'rb') as f:
  modelo = pickle.load(f)

educ = st.slider("Seleccione educación", 0, 20)
exper = st.slider("Seleccione experiencia", 0, 50)

vec = np.array([[1, educ, exper]])

if st.button("Predecir salario"):
  st.write(modelo.predict(vec))
