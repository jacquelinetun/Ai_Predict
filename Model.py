import joblib

import streamlit as st

# Load the model
loaded_model = joblib.load('model.pkl')

def main():
    st.title("Income Prediction App")
    st.write("Enter your age and years of experience to predict income.")

    age = st.slider("Age", 18, 70, 25)
    experience = st.slider("Experience (years)", 0, 50, 5)

    if st.button("Predict Income"):
        input_data = [[age, experience]]
        predicted_income = loaded_model.predict(input_data)[0]
        st.success(f"Predicted Income: ${predicted_income:.2f}")

if __name__ == "__main__":
    main()