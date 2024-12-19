import streamlit as st

st.title("web app")

st.write("*****************************")

x= st.slider("x",min_value=10,max_value=200)
st.title("{} squared is {}".format(x,x**2))
