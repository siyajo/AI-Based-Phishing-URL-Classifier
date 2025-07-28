import streamlit as st
import pickle
import numpy as np
import re
import socket
from urllib.parse import urlparse

# Load model
with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

# Extract feature function
def extract_features(url):
    features = []

    # 1. Having IP Address
    try:
        ip = socket.gethostbyname(urlparse(url).netloc)
        features.append(-1)
    except:
        features.append(1)

    # 2. URL Length
    features.append(-1 if len(url) < 54 else (0 if len(url) <= 75 else 1))

    # 3. Shortening service
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd"
    features.append(-1 if re.search(shortening_services, url) else 1)

    # 4. Having '@' Symbol
    features.append(-1 if "@" in url else 1)

    # 5. Double slash redirecting
    features.append(-1 if url.rfind("//") > 6 else 1)

    # 6. Prefix/Suffix '-'
    features.append(-1 if '-' in urlparse(url).netloc else 1)

    # 7. Sub domain
    dots = urlparse(url).netloc.split('.')
    features.append(1 if len(dots) <= 2 else (-1 if len(dots) > 3 else 0))

    # 8. SSL final state (simplified)
    features.append(1 if url.startswith("https") else -1)

    # 22 dummy features (can be replaced with logic later)
    for _ in range(22):
        features.append(0)

    return features


# Title
st.title("Phishing URL Classifier")

# User input
url = st.text_input("Enter the URL to check:")

# Predict
if st.button("Predict"):
    if url:
        features = extract_features(url)
        prediction = model.predict([features])[0]
        if prediction == 1:
            st.success("This URL is Legitimate!")
        else:
            st.error("This URL is Phishing!")
    else:
        st.warning("Please enter a URL.")
