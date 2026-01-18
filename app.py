import streamlit as st
import pickle

# 1. Load the saved "Brain" and "Dictionary"
model = pickle.load(open('Fake News Detection.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# 2. Design the Website
st.title("Fake News Detector 🕵️‍♂️")
st.write("Paste a news article below to check if it's Real or Fake.")

user_input = st.text_area("Enter News Text Here:")

if st.button("Predict"):
    if user_input:
        # Transform the text using your saved vectorizer
        data = vectorizer.transform([user_input])
        # Make a prediction
        prediction = model.predict(data)
        
        # Show the result
        if prediction[0] == 0:
            st.error("🚨 This looks like FAKE news!")
        else:
            st.success("✅ This looks like REAL news.")
    else:
        st.warning("Please enter some text first.")