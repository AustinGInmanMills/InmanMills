









tab1, tab2, tab3 = st.tabs(["Home", "Departments", "Information"])

with tab1:
    st.markdown(
        "Welcome to Inman Mills Saybrook Plant new Employee website! You can view information about up coming layoffs, overtime, departments and much more")

with tab2:
    department_options_bttn = st.selectbox(
        "Department Options",
        ("Knitting", "Ring Spinning", "Winding", "Roven", "MJS", "MVS", "Card Room"),
        index=None,
        key="DepartmentBox"
    )
    if department_options_bttn == "Knitting":
        knitting_bttn = st.selectbox(
            "Knitting Department Options",
            ("Operator", "Technician", "Overhauler", "Supervisor"),
            index=None,
            key="KnittingBox",
        )