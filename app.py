import streamlit as st
import os
from dotenv import load_dotenv
import streamlit_google_oauth as oauth

load_dotenv()
# client_id = os.environ["GOOGLE_CLIENT_ID"]
# client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
# redirect_uri = os.environ["GOOGLE_REDIRECT_URI"]
client_id="789077120900-70qaug9ll1u978p4ue0q8lrspgj69ho7.apps.googleusercontent.com"
client_secret="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"
redirect_uri="http://127.0.0.1.nip.io:8501/dashboard/"

if __name__ == "__main__":
    app_name = '''
    Streamlit Google Authentication Demo
    '''
    app_desc = '''
    A streamlit application that authenticates users by <strong>Google Oauth</strong>.
    The user must have a google account to log in into the application.
    '''
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        app_name=app_name,
        app_desc=app_desc,
        logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        st.write(f"Welcome {user_email}")

# streamlit run app.py --server.port 8080
