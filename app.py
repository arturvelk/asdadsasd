import streamlit as st
import pandas as pd

st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})

df2 = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": ["asd", "sad", "das"]})


st.write(df2)