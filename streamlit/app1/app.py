import streamlit as st

def main():
    st.title("Minimal Streamlit App")
    
    st.header("User Input")
    name = st.text_input("Enter your name:")
    
    st.header("Selection")
    option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    
    st.header("Results")
    if name:
        st.write(f"Hello, {name}!")
        st.write(f"You selected: {option}")
    else:
        st.write("Please enter your name to see results.")

if __name__ == "__main__":
    main()
