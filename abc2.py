import streamlit as st
st.title('My first app')
st.write('Hello all')
st.balloons()
x=st.text_input('Which technology you want to learn')
if x=='Ai':
    st.write('Kindly enroll in python first')
y=st.radio('Are you Graduate',options=['Yes','No'])
if y=='Yes':
    st.write('You can enroll in our diploma course')
else:
    st.write('You can do Internship')
#a=st.button('show')
#if a==1:
z=st.selectbox('Select the Technology',('Python','Java','C++'))
if z=='Python':
        st.write('contact abc 707172')
elif z=='Java':
        st.write('contact xyz 707172')
elif z=='C++':
        st.write('contact pqr 707172')

st.button('select from list given')





