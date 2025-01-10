import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the pre-trained model (make sure it is correctly loaded)
model = pickle.load(open("Employee_model.pkl", "rb"))

# App Title
st.title("💼 Employee Salary Prediction App")
st.markdown("Predict an employee's salary based on their demographic and professional details. 🚀")

# Sidebar for user input
st.sidebar.header("Enter Employee Details")

# Input fields
def user_input_features():
    age = float(st.sidebar.slider("Age", 18, 65, 30))  # Convert to float
    gender = float(st.sidebar.selectbox("Gender", (1.0, 0.0)))  # Encode as 1.0 for Male and 0.0 for Female
    education_level = float(st.sidebar.selectbox(
        "Education Level",
        (0.0, 1.0, 2.0, 3.0)  # Encode education levels as float values
    ))
    job_title = float(hash(st.sidebar.text_input("Job Title (e.g., Software Engineer, Data Analyst)")) % 1000)  # Hash job title to float
    years_experience = float(st.sidebar.slider("Years of Experience", 0, 40, 5))  # Convert to float
    
    # Create input dictionary with all values as float
    data = {
        "Age": age,
        "Gender": gender,
        "Education Level": education_level,
        "Job Title": job_title,
        "Years of Experience": years_experience
    }
    return pd.DataFrame(data, index=[0])

# Get user input
input_data = user_input_features()

# Display user input in the app
st.subheader("User Input:")
st.write(input_data)

# Predict salary (ensure you are calling predict on the model)
if st.button("Predict Salary"):
    prediction = model.predict(input_data)  # Ensure model is correct here
    st.subheader("Predicted Salary:")
    st.write(f"${prediction[0]:,.2f}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | 🚀 [GitHub](https://github.com)")
