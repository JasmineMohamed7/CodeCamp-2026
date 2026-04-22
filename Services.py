import streamlit as st
import pandas as pd
Courses = {
    'Robotics': {
        'Juniors': 2000,
        'Seniors': 3000

    },
    'Programming':{
        'Juniors': 1500,
        'Seniors': 2500  
    }
}

# Check if the user is logged in
#if st.session_state['logged in']:
 #   st.warn("Please log in to view our products.")

#else:
Registeration = []

st.title("Our Services", text_alignment='center')
# Display the products and their prices
Robotics_Tab, Programming_Tab = st.tabs(["Robotics", "Programming"])

with Robotics_Tab:
    col1, col2 = st.columns(2)
    age_groups = ['Juniors', 'Seniors']
    
    with col1:
        st.image('images/images.jpg')
        st.subheader('Robotics for Juniors', text_alignment='center')
        junior_age = st.segmented_control('Age Group:', options=age_groups, key='Juniors')
        st.write(f'Price: :red[{Courses["Robotics"]["Juniors"]}] EGP')
        students_no = st.number_input('Students:', min_value=1, max_value=100)
        if students_no > 0:
            Registeration.append(
                {
                   'Course':f'Robotics for Juniors',
                   'Number of students':students_no,
                   'Price':Courses["Robotics"]["Juniors"] * students_no
                }
            
            )


st.divider()

#Order summery
st.subheader("Registeration Summary", text_alignment='center')
total_price = sum(each_item['Price'] for each_item in Registeration)
st.write(f'Total Price: :red[{total_price}] EGP')
if len(Registeration) > 0:
    df = pd.DataFrame(Registeration)
    st.dataframe(df,hide_index=True)
    st.subheader(f'You have registered for {students_no} studentsfor the Robotics course.')

    