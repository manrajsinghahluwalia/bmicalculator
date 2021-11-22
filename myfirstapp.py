
#Mini Project: BODY MASS INDEX (BMI)
#let us recollect everything that we learn above and create a BMI Calculator web app.

#The formula of BMI Index when weight is in Kgs and height is in meters is:

#bmi = weight/height^2    

import streamlit as st

st.title("Welcome to BMI Calculator")

weight = st.sidebar.number_input("Enter Your weight (in kgs)")

status = st.sidebar.radio('Select Your Height category:' , ('cms', 'meters', 'feet'))

if(status == 'cms'):
    height = st.sidebarnumber_input('Centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text('Enter some value of height')
elif(status == 'meters'):
    height = st.number_input("Meters")

    try:
        bmi = weight/ (height**2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feet')
    #1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

if(st.button('Calculate BMI')):
    st.text('Your BMI Index is {}.'.format(bmi))
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >=16 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overwight")
