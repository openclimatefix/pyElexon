# This script demonstrates the use of methods from the DemandApi
# to retrieve various types of demand data from the Elexon API.

from datetime import datetime
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.demand_api import DemandApi
from elexonpy.batch import fetch_historical_data


# Initialize API client
api_client = ApiClient()
demand_api = DemandApi(api_client)

# Define date range
from_date = datetime(2024, 7, 1)
to_date = datetime(2024, 7, 2)

# Fetch Actual Total Load Data from API
df = demand_api.demand_actual_total_get(
    _from=from_date,
    to=to_date,
    settlement_period_from=1,
    settlement_period_to=48,
    format='dataframe'
)

# Print Actual Total Load Data DataFrame
print("\n--- Actual Total Load Data ---")
print((df.head()))
df.to_clipboard()

# Define date range
from_date = datetime(2024, 6, 1)
to_date = datetime(2024, 6, 2)

# Fetch Demand Outturn Daily Data from API
response = demand_api.demand_outturn_daily_get(
    settlement_date_from=from_date.date(),
    settlement_date_to=to_date.date(),
    format='json'
)

df = pd.DataFrame([data.to_dict() for data in response.data])

# Print Demand Outturn Daily Data DataFrame
print("\n--- Demand Outturn Daily Data ---")
print((df.head()))