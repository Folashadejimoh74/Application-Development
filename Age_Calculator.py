import streamlit as st
from datetime import datetime, date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def app():
    st.title("Age Calculator")

    born = st.date_input("Enter your birthdate (YYYY-MM-DD):")
    age = None
    if born:
        age = calculate_age(born)
        st.write("Your age is:", age, "years old")

if __name__ == '__main__':
    app()