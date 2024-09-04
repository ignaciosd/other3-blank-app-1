#import streamlit as st

#st.title("🎈 My new app")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)


# Write a simple source code using streamlit in Python

import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Display a text input box
name = st.text_input("Enter your name:")

# Display a slider
age = st.slider("Select your age:", 0, 100)

# Display a button
if st.button("Submit"):
    # When the button is clicked, display the inputted name and age
    st.write(f"Hello, {name}! You are {age} years old.")

# Display a checkbox
if st.checkbox("Show a random number"):
    import random
    st.write(f"Random number: {random.randint(1, 100)}")

# Display a select box
favorite_color = st.selectbox("Pick your favorite color:", ["Red", "Green", "Blue"])
st.write(f"Your favorite color is {favorite_color}.")
