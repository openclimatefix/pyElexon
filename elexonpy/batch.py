import pandas as pd
from datetime import timedelta

def fetch_historical_data(api_method, start_date, end_date, max_days=7, start_param='_from', end_param='to', **kwargs):
    """
    Safely fetches data over long periods by chunking the requests.
    """
    current_start = start_date
    all_data = []

    while current_start < end_date:
        current_end = min(current_start + timedelta(days=max_days), end_date)
        
        # Dynamically build the arguments for the API call
        call_params = {
            start_param: current_start,
            end_param: current_end,
            'format': 'dataframe'
        }
        
        # Add in any extra kwargs the user passed (like settlement_period)
        call_params.update(kwargs)
        
        # Call the passed API method unpacking the dynamic dictionary
        df_chunk = api_method(**call_params)
        
        if df_chunk is not None and not df_chunk.empty:
            all_data.append(df_chunk)
        
        current_start = current_end

    if not all_data:
        return pd.DataFrame()
        
    return pd.concat(all_data, ignore_index=True)
