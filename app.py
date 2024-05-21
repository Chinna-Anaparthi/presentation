import streamlit as st

# Page title
st.title('Registration Form')

# Form to collect user information
with st.form(key='register_form'):
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    email = st.text_input('Email')
    bio = st.text_area('Bio (optional)')
    
    # Submit button
    submit_button = st.form_submit_button(label='Register')

# Logic after form submission
if submit_button:
    if not username or not password or not email:
        st.error('Please fill out all required fields')
    else:
        st.success(f'Registration successful for {username}!')
        st.write('Here is the information you provided:')
        st.write(f'Username: {username}')
        st.write(f'Email: {email}')
        st.write(f'Bio: {bio}')