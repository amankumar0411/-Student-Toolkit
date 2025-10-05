import streamlit as st
import datetime

st.set_page_config(page_title="Student Toolkit", page_icon="🛠️", layout="centered")

st.title("🛠️ Student Toolkit")
st.write("A simple multi-tool app with BMI Calculator, Age Calculator, To-Do List, and Grade Calculator")

# Sidebar for navigation
menu = st.sidebar.radio("Choose a Tool", ["BMI Calculator", "Age Calculator", "To-Do List", "Grade Calculator"])

# ---------------------- BMI CALCULATOR ----------------------
if menu == "BMI Calculator":
    st.header("⚖️ BMI Calculator")

    weight = st.number_input("Enter your weight (kg)", min_value=1, max_value=300, value=60)
    height = st.number_input("Enter your height (cm)", min_value=50, max_value=250, value=170)

    if st.button("Calculate BMI"):
        bmi = weight / ((height/100)**2)
        st.write(f"**Your BMI is:** {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("You are Normal Weight")
        elif 25 <= bmi < 29.9:
            st.warning("You are Overweight")
        else:
            st.error("You are Obese")

# ---------------------- AGE CALCULATOR ----------------------
elif menu == "Age Calculator":
    st.header("📅 Age Calculator")

    birth_date = st.date_input("Enter your Date of Birth", datetime.date(2000,1,1))
    today = datetime.date.today()

    if st.button("Calculate Age"):
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        st.success(f"Your Age is: {age_years} years")

# ---------------------- TO-DO LIST ----------------------
elif menu == "To-Do List":
    st.header("📝 To-Do List")

    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []

    new_task = st.text_input("Enter a new task")
    if st.button("Add Task"):
        if new_task:
            st.session_state["tasks"].append(new_task)
            st.success("Task added!")

    st.subheader("Your Tasks")
    for i, task in enumerate(st.session_state["tasks"]):
        if st.checkbox(task, key=i):
            st.session_state["tasks"].remove(task)
            st.success(f"Task '{task}' completed and removed!")

# ---------------------- GRADE CALCULATOR ----------------------
elif menu == "Grade Calculator":
    st.header("📊 Grade Calculator")

    name = st.text_input("Enter Student Name")
    marks1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100, value=0)
    marks2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100, value=0)
    marks3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100, value=0)
    marks4 = st.number_input("Subject 4 Marks", min_value=0, max_value=100, value=0)
    marks5 = st.number_input("Subject 5 Marks", min_value=0, max_value=100, value=0)

    if st.button("Calculate Grade"):
        total = marks1 + marks2 + marks3 + marks4 + marks5
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        st.success(f"🎓 Result for {name}")
        st.write(f"**Total Marks:** {total} / 500")
        st.write(f"**Percentage:** {percentage:.2f}%")
        st.write(f"**Grade:** {grade}")