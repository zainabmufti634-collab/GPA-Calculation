import streamlit as st
import pandas as pd

# ------------------------- #
# Streamlit Page Settings
# ------------------------- #
st.set_page_config(page_title="CGPA Calculator", page_icon="🎓", layout="centered")

# ------------------------- #
# Page Styling
# ------------------------- #
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            color: #1a73e8;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        .result-box {
            background-color: #d1e7dd;
            padding: 15px;
            border-radius: 8px;
            font-size: 20px;
            text-align: center;
            color: #0f5132;
            border: 1px solid #badbcc;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------- #
# Title
# ------------------------- #
st.title("🎓 CGPA Calculator (Weighted Average Method)")
st.write("Easily calculate your CGPA semester by semester using GPA & credit hours.")

# ------------------------- #
# Session state for semesters
# ------------------------- #
if "semesters" not in st.session_state:
    st.session_state.semesters = []

st.header("➕ Add Semester Details")

semester_no = st.number_input("Semester Number", min_value=1, max_value=8, value=len(st.session_state.semesters)+1)
gpa = st.number_input("GPA of this semester", min_value=0.0, max_value=4.0, step=0.01, format="%.2f")
credits = st.number_input("Total Credit Hours in this semester", min_value=1, max_value=30)

if st.button("Add Semester"):
    st.session_state.semesters.append({"Semester": semester_no, "GPA": gpa, "Credit Hours": credits})
    st.success(f"✅ Semester {semester_no} added successfully!")

# ------------------------- #
# Semester Table and CGPA Display
# ------------------------- #
if st.session_state.semesters:
    df = pd.DataFrame(st.session_state.semesters)
    df["Weighted GPA"] = df["GPA"] * df["Credit Hours"]

    total_weighted_gpa = df["Weighted GPA"].sum()
    total_credits = df["Credit Hours"].sum()
    cgpa = round(total_weighted_gpa / total_credits, 2)

    st.write("### 📚 Semester Summary")
    st.dataframe(df, use_container_width=True)

    st.markdown(f"""
        <div class="result-box">
            ✅ <b>Cumulative CGPA:</b> {cgpa}
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("No semesters added yet. Start by adding your semester GPA above.")

