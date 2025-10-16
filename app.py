import streamlit as st
import pandas as pd

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 GPA & CGPA Calculator (1st Semester)")
st.write("This app calculates your GPA and CGPA for the first semester based on your marks and credit hours.")

# --- Helper function: Convert marks to Grade & Grade Point ---
def grade_from_marks(marks):
    if marks >= 85:
        return "A+", 4.00
    elif marks >= 80:
        return "A-", 3.66
    elif marks >= 75:
        return "B+", 3.33
    elif marks >= 70:
        return "B", 3.00
    elif marks >= 65:
        return "B-", 2.66
    elif marks >= 60:
        return "C+", 2.33
    elif marks >= 55:
        return "C", 2.00
    elif marks >= 50:
        return "D", 1.66
    else:
        return "F", 0.00


# --- Tabs ---
tab1, tab2 = st.tabs(["📘 GPA & CGPA Calculator", "📚 Course Details"])

with tab1:
    st.header("Enter First Semester Courses")

    # Number of subjects
    n = st.number_input("How many courses did you take in 1st semester?", min_value=1, max_value=10, value=6)

    course_data = []

    for i in range(1, n + 1):
        st.subheader(f"Course {i}")
        course_code = st.text_input(f"Enter course code for course {i}", key=f"code_{i}")
        course_name = st.text_input(f"Enter course title for course {i}", key=f"name_{i}")
        credit = st.number_input(f"Enter credit hours for course {i}", min_value=1, max_value=4, key=f"credit_{i}")
        marks = st.number_input(f"Enter marks (0-100) for course {i}", min_value=0, max_value=100, key=f"marks_{i}")

        grade, gp = grade_from_marks(marks)
        course_data.append({
            "Course No": course_code,
            "Course Title": course_name,
            "Credit": credit,
            "Marks": marks,
            "L.G.": grade,
            "G.P.": gp
        })

    df = pd.DataFrame(course_data)

    if st.button("Calculate GPA & CGPA"):
        if not df.empty:
            df["Total Points"] = df["Credit"] * df["G.P."]
            total_credits = df["Credit"].sum()
            total_points = df["Total Points"].sum()
            gpa = round(total_points / total_credits, 2)
            cgpa = gpa  # First semester => GPA = CGPA

            st.success(f"📊 **GPA (1st Semester): {gpa}**")
            st.success(f"🎓 **CGPA (Cumulative): {cgpa}**")

            st.write("### Detailed Result")
            st.dataframe(df[["Course No", "Course Title", "Credit", "Marks", "L.G.", "G.P."]], use_container_width=True)
        else:
            st.warning("Please enter your course details first!")

with tab2:
    st.header("Example: 1st Semester Course Details")
    data = {
        "Course No": ["CSC101", "HUM104", "HUM123", "MTH103", "PHY124", "STA101"],
        "Course Title": [
            "Application of Information and Communication Technologies",
            "Functional English",
            "Fundamentals of Philosophy",
            "Exploring Quantitative Skills",
            "Applied Physics",
            "Introductory Statistics"
        ],
        "Credit": [3, 3, 2, 3, 3, 3],
        "Marks": [73, 80, 68, 87, 82, 77],
        "L.G.": ["B", "A-", "B-", "A", "A-", "B+"],
        "G.P.": [3.0, 3.66, 2.66, 4.0, 3.66, 3.33]
    }

    example_df = pd.DataFrame(data)
    example_df["Total Points"] = example_df["Credit"] * example_df["G.P."]
    total_credits = example_df["Credit"].sum()
    gpa = round(example_df["Total Points"].sum() / total_credits, 2)

    st.dataframe(example_df[["Course No", "Course Title", "Credit", "Marks", "L.G.", "G.P."]], use_container_width=True)
    st.info(f"📊 Example GPA (1st Semester): **{gpa}**")
    st.info(f"🎓 Example CGPA: **{gpa}**")
