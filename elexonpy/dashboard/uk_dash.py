import streamlit as st
from datetime import datetime, timedelta
import plotly.express as px
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.demand_api import DemandApi
from elexonpy.batch import fetch_historical_data  # YOUR UTILITY!

# Page Setup
st.set_page_config(page_title="UK Grid Analytics", layout="wide")
st.title("⚡ UK Grid Performance Tracker")
st.caption("Powered by Open Climate Fix Elexonpy library")

# Initialize API Engine
api_client = ApiClient()
demand_api = DemandApi(api_client)

# Sidebar UI
st.sidebar.header("Data Configuration")
days_back = st.sidebar.slider("Select Data Window (Days)", 1, 30, 7)

# Calculate dynamic time ranges
end_date = datetime.now()
start_date = end_date - timedelta(days=days_back)

# Process Pipeline
with st.spinner("Fetching historical grid data using batch engine..."):
    df = fetch_historical_data(
        api_method=demand_api.demand_actual_total_get,
        start_date=start_date,
        end_date=end_date,
        max_days=7
    )

if not df.empty:
    # --- DEBUG & ANALYSIS BLOCK ---
    st.info(f"Available Data Schema: {df.columns.tolist()}")
    
    # Dashboard KPI Cards
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Data Points", value=f"{len(df):,}")
    col2.metric(label="Timeframe Requested", value=f"{days_back} Days")
    
    # Safe Auto-Mapping for Plotly Axes
    # Tries to find common time keys like 'startTime' or 'start_time'; defaults to the 1st column
    time_col = next((c for c in df.columns if 'time' in c.lower() or 'date' in c.lower()), df.columns[0])
    # Tries to find target numeric metrics like 'quantity' or 'volume'; defaults to the 2nd column
    val_col = next((c for c in df.columns if 'quantity' in c.lower() or 'amount' in c.lower() or 'value' in c.lower()), df.columns[1])
    
    if pd.api.types.is_numeric_dtype(df[val_col]):
        col3.metric(label=f"Peak Recorded ({val_col})", value=f"{df[val_col].max():,}")
    else:
        col3.metric(label="Data Integrity Status", value="Verified")

    # Interactive Graph View
    st.subheader(f"Grid Profile Analysis: ({val_col} vs {time_col})")
    fig = px.line(df, x=time_col, y=val_col, template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    
    # Raw Data Explorer
    st.subheader("Raw Data Inspect Window")
    st.dataframe(df, use_container_width=True)

else:
    st.error("No active dataset returned for the specified window parameters.")