import streamlit as st
import random

def generate_data(n=10):
    return [
        {"ID": i, "Name": f"Item {i}", "Value": random.randint(1, 100)}
        for i in range(1, n + 1)
    ]

def main():
    st.title("Streamlit Table Viewer")

    # Sidebar controls
    st.sidebar.header("Controls")
    num_rows = st.sidebar.slider("Number of rows", min_value=5, max_value=50, value=10)
    min_value = st.sidebar.number_input("Minimum value filter", value=0)
    sort_asc = st.sidebar.checkbox("Sort ascending by value", value=True)

    # Generate and filter data
    data = generate_data(num_rows)
    filtered_data = [row for row in data if row["Value"] >= min_value]
    filtered_data.sort(key=lambda x: x["Value"], reverse=not sort_asc)

    # Display data
    st.subheader("Generated Table")
    if filtered_data:
        st.table(filtered_data)
    else:
        st.write("No data matches your filter.")

if __name__ == "__main__":
    main()
