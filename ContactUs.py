import streamlit as st

st.title('Get In Touch', text_alignment='center')
st.divider()

left, right = st.columns([1, 1], border=True)
with left:
    st.header("Get In Touch Through Whatsapp")
    if left.button("Chat on Whatsapp", icon="📝", use_container_width=True, width="stretch"):
        left.markdown("You clicked the whatsapp button.")

with right:
    st.header('Get In Touch Through Email')
    st.write('Have questions or need more information? We are here to help! Reach out to us through the following channels:')
    if right.button("Send Email", icon="📝", use_container_width=True, width="stretch"):
        right.markdown("You clicked the send email button.")


