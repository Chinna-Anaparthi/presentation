import streamlit as st

# Set the title of the app
st.title("Registration Form 💁")

# Sidebar content
st.sidebar.title("Sidebar Menu")
st.sidebar.write("You can add any widgets here")

# Registration form
st.header("Please fill out the form below:")

# Input fields
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

# Gender selection
gender = st.radio("Gender", options=["Male", "Female", "Other"])

# Date of birth
dob = st.date_input("Date of Birth")

# Address
address = st.text_area("Address")

# Phone number
phone = st.text_input("Phone Number")

# Checkbox for terms and conditions
terms = st.checkbox("I agree to the terms and conditions")

# Submit button
if st.button("Submit"):
    if not all([first_name, last_name, email, password, confirm_password, terms]):
        st.error("Please fill out all fields and agree to the terms.")
    elif password != confirm_password:
        st.error("Passwords do not match.")
    else:
        # Process the form data here
        st.success("Registration successful!")
        st.write(f"Name: {first_name} {last_name}")
        st.write(f"Email: {email}")
        st.write(f"Gender: {gender}")
        st.write(f"Date of Birth: {dob}")
        st.write(f"Address: {address}")
        st.write(f"Phone: {phone}")

# Run the app with `streamlit run registration_form.py`
