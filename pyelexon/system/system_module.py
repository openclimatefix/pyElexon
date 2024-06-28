from typing import Union
from datetime import datetime
import pandas as pd
import requests
from pyelexon.constants import BASE_URL

class SystemPricesFetcher:
    def __init__(self):
        pass

    def get_buy_prices(self, settlement_date: Union[datetime, str]) -> pd.DataFrame:
        """
        Parameters:
            settlement_date (Union[datetime, str]): The settlement date to fetch data for.

        Returns:
            pd.DataFrame: DataFrame containing system buy prices data.

        API Documentation:
        For more details on this API endpoint, refer to the : https://bmrs.elexon.co.uk/api-documentation/endpoint/balancing/settlement/system-prices/%7BsettlementDate%7D/%7BsettlementPeriod%7D

        """
        if isinstance(settlement_date, datetime):
            settlement_date = settlement_date.strftime('%Y-%m-%d')

        url = f"{BASE_URL}/balancing/settlement/system-prices/{settlement_date}?format=json"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

            data = response.json()
            df = pd.DataFrame(data["data"])

            # Filter to include only the 'systemBuyPrice' column
            buy_prices_df = df[['settlementDate', 'settlementPeriod', 'systemBuyPrice']]
            return buy_prices_df

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise

        except Exception as err:
            print(f"Other error occurred: {err}")
            raise
