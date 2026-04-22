import streamlit as st

# Pages title and icons 
home_page = st.Page(page= 'pages/Home.py', title='Home', icon='🏠', default=True)
signIn_page = st.Page(page= 'pages/SignIn.py', title='Sign In', icon='🔑')
signUp_page = st.Page(page= 'pages/SignUp.py', title='Sign Up', icon='📝')
services_page = st.Page(page= 'pages/Services.py', title='Services', icon='🛠️')
chatbot_page = st.Page(page= 'pages/Chatbot.py', title='Chatbot', icon='🤖')
ContactUs_page = st.Page(page= 'pages/ContactUs.py', title='Contact Us', icon='📞')

#Create navigationbar
all_pages = st.navigation(
    pages=[
    home_page,
    services_page,
    signIn_page,
    signUp_page,
    chatbot_page,
    ContactUs_page
    ],
)
all_pages.run()







