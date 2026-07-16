from datetime import datetime
import pandas as pd
from elexonpy.batch import fetch_historical_data
from elexonpy.api_client import ApiClient
from elexonpy.api.demand_api import DemandApi

# Initialize API client
api_client = ApiClient()
demand_api = DemandApi(api_client)

yearly_df = fetch_historical_data(
    api_method=demand_api.demand_actual_total_get,
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2024, 1, 1),
    max_days=7
)

# Print Actual Total Load Data DataFrame
print("\n--- Actual Total Load Data ---")
print(yearly_df)
# yearly_df.to_csv('output.csv', index=False)

from datetime import datetime
df_outturn = fetch_historical_data(
    api_method=demand_api.demand_outturn_daily_get,
    start_date=datetime(2021, 1, 1).date(),
    end_date=datetime(2024, 1, 1).date(),
    max_days=731,
    start_param='settlement_date_from',  # <--- Telling it the correct name
    end_param='settlement_date_to'       # <--- Telling it the correct name
)

print("\n--- Actual Demand ---")
print(df_outturn)
# df_outturn.to_csv('output_demand.csv', index=False)
