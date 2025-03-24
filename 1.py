import streamlit as st

# Define custom theme settings using CSS
custom_theme = """
    <style>
    .stApp {
        background-color: #F5F5F5;  /* Background color */
        color: #000000;  /* Text color */
    }
    .stButton>button {
        background-color: #4CAF50;  /* Button color */
        color: white;  /* Button text color */
    }
    .stSidebar {
        background-color: #FFFFFF;  /* Sidebar background color */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #4CAF50;  /* Headings color */
    }
    .css-1d391kg {
        font-family: 'sans serif';  /* Font style */
    }
    </style>
"""

# Inject custom CSS into Streamlit app
st.markdown(custom_theme, unsafe_allow_html=True)

# App content
st.title("Custom Theme with CSS Example")
st.write("This app uses a custom theme set via CSS.")
st.button("Click Me!")
