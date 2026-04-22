import streamlit as st
st.title('Mawaheb Academy', text_alignment='center')
st.subheader('The House Of Robots', text_alignment='center')
st.image('images/Hero image.jpg',width=700)
st.divider()

left, right = st.columns([1, 1], border=True)
with left:
    st.header("Not Registered Yet?")
    st.write("Start your child's journey with us and explore the world of robotics and programming. Join our community of learners and innovators today!")
    if left.button("Go To Sign Up", icon="📝", use_container_width=True, width="stretch"):
        left.markdown("You clicked the sign up button.")
        st.switch_page("Pages/SignUp.py")

with right:
    st.header('Contact us')
    st.write('Have questions or need more information? We are here to help! Reach out to us through the following channels:')
    if right.button("Go To Contact Us", icon="📝", use_container_width=True, width="stretch"):
        right.markdown("You clicked the contact us button.")
        st.switch_page("Pages/ContactUs.py")


