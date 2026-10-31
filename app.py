import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Student Performance Predictor 🎓")
st.write("Predict student performance using a Decision Tree Classifier.")
st.caption("Educational demo using a synthetic dataset; not a verified real-world assessment.")

st.subheader("Enter Student Details")

study_hours = st.number_input(
    "Daily Study Hours", min_value=0.0, max_value=24.0, value=4.0, step=0.5
)
attendance = st.slider("Attendance (%)", min_value=0, max_value=100, value=75)
previous_marks = st.number_input(
    "Previous Exam Marks", min_value=0, max_value=100, value=60
)
assignment_score = st.number_input(
    "Assignment Score", min_value=0, max_value=100, value=70
)

if st.button("Predict Performance"):
    student_data = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_marks": previous_marks,
        "assignment_score": assignment_score
    }])

    prediction = model.predict(student_data)[0]
    st.subheader("Prediction Result")

    if prediction == "Good":
        st.success("Predicted Performance: GOOD 🎉")
    elif prediction == "Average":
        st.info("Predicted Performance: AVERAGE")
    else:
        st.warning("Predicted Performance: AT RISK")

    st.write("Prediction:", prediction)
