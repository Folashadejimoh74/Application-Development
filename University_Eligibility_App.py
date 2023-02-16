
import streamlit as st
from PIL import Image

st.header("University Eligibility App")

st.write("This App Checks if you are Eligible for Admission into Crown University")
img = Image.open('pix.jpg')
new_image = img.resize((400, 400))
st.sidebar.image(new_image)

# Eligibility criteria 1 (check JAMB scores)

ume_score = st.number_input('Enter your JAMB score: ', step = 1)
if st.button('Enter'):
    if ume_score < 200:
        st.write('you are not eligible, your JAMB score is low.')
        st.stop()
    else:
        st.write('You may proceed') 
    
# Available courses    
st.subheader('Click here for Available Courses')

course = st.selectbox( '', ['BSc. Computer Science','BSc. Mathematics', 'BSc. Biochemistry', 'BSc. Physics with Electronics'])

st.subheader('Enter five Relevant UTME subjects')

course_list = ['BSc. Computer Science','BSc. Mathematics', 'BSc. Biochemistry', 'BSc. Physics with Electronics']
# Eligibility criteria 2
subjects = st.multiselect( '',['Mathematics', 'Physics', 'Chemistry', 'Computer Studies', 'English', 'Economics','Yoruba', 'Agric Science','Biology' ])

if course == course_list[0]:
    UTME_subj = ['Mathematics', 'Physics', 'Chemistry', 'Computer Studies', 'English']
    
elif course == course_list[1]:
      UTME_subj = ['Mathematics', 'Physics', 'Chemistry', 'Economics', 'English']
    
elif course == course_list[2]:
     UTME_subj = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English']
else:
     UTME_subj = ['Mathematics', 'Physics', 'Chemistry', 'Technical Drawing', 'English']   
a = set(subjects)
b = set(UTME_subj)
if a==b:
    st.write("Enter your grades \(A1, B2, B3, C4, C5, C6, D7, E8, F9\) ")
else: 
    st.write("Your UTME subjects combination is deficient")
    st.stop() 
        
#UTME grades 
gra_1 = st.text_input(f'grade for {subjects[0]}')
gra_2 = st.text_input(f'grade for {subjects[1]}')
gra_3 = st.text_input(f'grade for {subjects[2]}')
gra_4 = st.text_input(f'grade for {subjects[3]}')
gra_5 = st.text_input(f'grade for {subjects[4]}')

grades = [ gra_1, gra_2, gra_3, gra_4,  gra_5]

# Eligibility criteria 3 
if st.button("submit"):
    grades = [ gra_1, gra_2, gra_3, gra_4,  gra_5]
    fail =['D7','E8', 'F9']
    passed =  ['A1','B2', 'B3', 'C4', 'C5', 'C6']
    if [x for x in fail if x in grades]:
        st.write(f'You are not eligible for admission into the {course} Programme')
    else:
        st.write(f'You are eligible for admission into the {course} Programme, you may go ahead to apply')

        
        
        