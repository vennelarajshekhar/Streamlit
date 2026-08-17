import streamlit as st
import requests

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Student Registration Portal",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.title("🎓 Student Registration Portal")
st.write("Welcome! Please enter your details below.")

# -------------------------------
# User Inputs
# -------------------------------
name = st.text_input("👤 Enter your Name")

email = st.text_input("📧 Enter your Email")

age = st.number_input(
    "🎂 Enter your Age",
    min_value=1,
    max_value=100,
    value=20
)

gender = st.radio(
    "🚻 Select Gender",
    ["Male", "Female"]
)

course = st.selectbox(
    "🎓 Select Course",
    [
        "Python",
        "Java",
        "AI & ML",
        "Data Analytics"
    ]
)

skills = st.multiselect(
    "🛠 Select Skills",
    [
        "Python",
        "Java",
        "SQL",
        "Power BI",
        "Excel"
    ]
)

experience = st.slider(
    "⭐ Years of Experience",
    0,
    10
)

resume = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

about = st.text_area(
    "📝 About Yourself"
)

agree = st.checkbox(
    "I agree to the Terms and Conditions"
)

# -------------------------------
# Register Button
# -------------------------------
if st.button("🚀 Register"):

    # Validation
    if name == "":
        st.error("Please enter your name.")
    
    elif email == "":
        st.error("Please enter your email.")

    elif agree == False:
        st.warning("Please accept the Terms and Conditions.")

    else:

        # Data to send to FastAPI
        data = {
            "name": name,
            "email": email,
            "age": age,
            "gender": gender,
            "course": course
        }

        try:

            # Send request
            response = requests.post(
                "http://127.0.0.1:8000/register",
                json=data
            )

            # Check response
            if response.status_code == 200:

                result = response.json()

                st.success(result["message"])

                st.subheader("Student Details")

                st.write("👤 Name :", result["student"]["name"])
                st.write("📧 Email :", result["student"]["email"])
                st.write("🎂 Age :", result["student"]["age"])
                st.write("🚻 Gender :", result["student"]["gender"])
                st.write("🎓 Course :", result["student"]["course"])

                st.write("🛠 Skills :", ", ".join(skills))
                st.write("⭐ Experience :", experience)
                st.write("📝 About :", about)

            else:

                st.error("FastAPI returned an error.")

        except requests.exceptions.ConnectionError:

            st.error("❌ Cannot connect to FastAPI Server.\n\nMake sure FastAPI is running on port 8000.")