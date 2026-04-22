import streamlit as st
st.title('Mawaheb Academy')
st.subheader('The House Of Robots')
st.success('Welcome To Mawaheb Academy')    
st.warning('This is a warning message')
st.error('This is an error message')
st.write('This is a simple text message')
st.write([1,2,3,4,5])
st.write({"name": "Mawaheb Academy", "location": "Nasr City"})
st.info('Mawaheb Academy is a great place to learn about robotics and programming.')
name = st.text_input(label='Enter your name')

if st.button('Click Me'):
    st.write('Hello, ', name)





import streamlit as st
st.title('Mawaheb Academy')
st.subheader('The House Of Robots')
st.write('Already have an account? [Login]')
name = st.text_input(label='Enter your name')
st.date_input(label='Select a date')
if st.button('Click Me'):
    st.write('Hello, ', name)
    st.Page()
