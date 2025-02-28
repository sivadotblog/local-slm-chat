import streamlit as st
import requests

# Define the FastAPI endpoint
FASTAPI_ENDPOINT = "http://localhost:8000/chat"

# Define the pages and their meta information
pages = {
    "Home": {"meta": "home"},
    "Data Fabric": {"meta": "data_fabric"},
    "Data Mesh": {"meta": "data_mesh"},
    "Lakehouse Architecture": {"meta": "lakehouse_architecture"},
    "Data Architecture": {"meta": "data_architecture"},
    "Modern ETL Tech Stack": {"meta": "modern_etl_tech_stack"}
}

# Function to send chat query to FastAPI
def send_query(query, page_meta):
    response = requests.post(FASTAPI_ENDPOINT, json={"query": query, "meta": page_meta})
    return response.json()

# Streamlit app
st.title("Local SLM Chat Bot")

# Sidebar for page navigation
page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Display the selected page
st.header(page)
st.write(f"Meta information: {pages[page]['meta']}")

# Chat input
query = st.text_input("Enter your query:")

# Send query to FastAPI and display response
if st.button("Send"):
    response = send_query(query, pages[page]['meta'])
    st.write("Response:", response["response"])
