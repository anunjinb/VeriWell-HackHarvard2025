import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

@st.cache_resource
def initialize_firebase():
    """
    Initializes the Firebase Admin SDK.
    Uses st.cache_resource to ensure this function runs only once.
    """
    try:
        # Check if the app is already initialized to avoid errors on rerun.
        if not firebase_admin._apps:
            # Load credentials from the file specified by the user.
            # This file should be in the same directory as your app.
            cred = credentials.Certificate("firebase_credentials.json")
            firebase_admin.initialize_app(cred)
        
        # Get a client for the Firestore database.
        db = firestore.client()
        return db
    except FileNotFoundError:
        st.error("Firebase credentials file (firebase_credentials.json) not found.")
        st.info("Please follow the setup instructions to download your Firebase credentials and place the file in the project's root directory.")
        return None
    except Exception as e:
        st.error(f"Failed to initialize Firebase: {e}")
        return None
