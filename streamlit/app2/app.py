import streamlit as st
import random
from dataflow.dataflow import Dataflow

def generate_data(n=10):
    return [
        {"ID": i, "Name": f"Item {i}", "Value": random.randint(1, 100)}
        for i in range(1, n + 1)
    ]

def main():
    dataflow = Dataflow()
    st.title("Streamlit Table Viewer")
    db = dataflow.connection("local_db")
    print(db)

    dummy = dataflow.variable("dummy")
    st.write("dummy global variable is:", dummy)
    dummy_1 = dataflow.variable("dummy_local")
    st.write("dummy local variable is:", dummy_1)
    dummy_2 = dataflow.variable("dummy_local_2")
    st.write("dummy local variable 2 is:", dummy_2)

    dummy_3 = dataflow.secret("dummy_secret")
    st.write("dummy global secret is:", dummy_3)
    dummy_4 = dataflow.secret("dummy_secret_local")
    st.write("dummy local secret is:", dummy_4)
    
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
