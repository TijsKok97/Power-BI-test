import streamlit as st
from urllib.parse import quote

# Streamlit app title
st.title("Interactive Power BI Dashboard")

# User input widgets
region = st.selectbox("Select Region", ["West", "East", "South", "North"])
year = st.slider("Select Year", 2018, 2025, 2025)

# Construct the filter query
filter_query = f"Sales/Region eq '{region}' and Sales/Year eq {year}"
encoded_filter = quote(filter_query)

# Base URL of your Power BI report
base_url = "https://app.powerbi.com/groups/me/apps/00ecc7c2-fe91-4201-980e-2187898da728/reports/aacd1048-20b7-42f1-99cd-866448120df8/b9d4df400e4540247e45"

# Construct the full URL with filters
full_url = f"{base_url}?filter={encoded_filter}"

# Embed the Power BI report in an iframe
st.components.v1.iframe(src=full_url, height=800, width=1200)
