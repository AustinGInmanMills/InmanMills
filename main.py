import streamlit as st

st.set_page_config(
    page_title="Inman Mills Saybrook",
    page_icon="",
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

hide_st_style = """  
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """  # Hides streamlit information on web app
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    body="""
        <style>
            .block-container{
                    padding-top: 25px;
                }
        </style>
    """,
    unsafe_allow_html=True  # Deletes white space on top of web app
)
#################################################

# Create an empty container
placeholder = st.empty()

actual_email = "email"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    #submit = st.form_submit_button("Login")
    submit = st.page_link("pages/login.py", label="Login")

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass