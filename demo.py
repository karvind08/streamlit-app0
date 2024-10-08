import streamlit as st
import pandas as pd
st.title("Streamlit Tutorial")
#st.code('''for i in range(5):
#                print(i)''')
#st.header("Dataframe Example")
#data = pd.read_csv("list.csv",encoding='ISO-8859-1')
#data = pd.read_excel("list.xls")
#st.dataframe(data)
st.header("Form")
name = st.text_input("**Enter Name:**")
email = st.text_input("**Enter Email:**")
msg = st.text_area("**Enter Your Message:**")
classname = st.selectbox("**Enter Branch**",['CSE','ME','IT','CE','EC'])
#classname = st.selectbox("**Enter Class**",[1,2,3,4])
btn = st.button("Submit")

if btn:
    st.markdown(f'''
    \nName: {name}
    \nEmail: {email}
    \nMessage: {msg}
    \nClass Name: {classname}     ''') 
