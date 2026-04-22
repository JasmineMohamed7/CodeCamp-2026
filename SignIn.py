import streamlit as st
from time import sleep

st.title("Already have an account? [Login]")
st.write("Sign in to access your account!")

with st.form("signin_form"):
    st.write("Login Information")
    col3, col4 = st.columns([3, 1])
    with col3:
        email = st.text_input("Email", placeholder="example@gmail.com")
    with col4:
        password = st.text_input("Password", type="password")
        
    submit = st.form_submit_button("Sign In", use_container_width=True)
    
    if submit:
        if email and password:  
            st.session_state['email'] = email
            st.success(f"Signed in successfully as {email}!")
            # if st.button("Explore Our Services", use_container_width=True):
            #     st.switch_page("Pages/Services.py")
            # if st.button("Logout", use_container_width=True):
            #     st.session_state['logged_in'] = True
            #     st.session_state['email'] = None
            #     st.session_state['password'] = None
            #     st.success("You have been logged out.")
            #     st.switch_page("Pages/Home.py")


        else:
            st.error("Please fill in all required fields (Email, Password).")

