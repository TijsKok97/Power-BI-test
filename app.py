import streamlit as st
from urllib.parse import quote

# User input for filtering
region = st.selectbox("Select Region", ["West", "East", "South", "North"])
year = st.slider("Select Year", 2018, 2025, 2025)

# Construct the filter query
filter_query = f"Sales/Region eq '{region}' and Sales/Year eq {year}"

# Encode the filter query for URL
from urllib.parse import quote
encoded_filter = quote(filter_query)

# Construct the full Power BI report URL
base_url = "https://app.powerbi.com/groups/me/apps/00ecc7c2-fe91-4201-980e-2187898da728/reports/aacd1048-20b7-42f1-99cd-866448120df8/b9d4df400e4540247e45?experience=power-bi&bookmarkGuid=08c71ace4a8148b243de"
full_url = f"{base_url}&filter={encoded_filter}"

# Embed the Power BI report in Streamlit
st.components.v1.iframe(src=full_url, height=600, width=1000)
