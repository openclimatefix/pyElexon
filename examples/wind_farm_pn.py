from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
from elexonpy.api_client import ApiClient
from elexonpy.api.balancing_mechanism_physical_api import BalancingMechanismPhysicalApi

def fetch_wind_farm_pn_data():
    """Fetch Physical Notification (PN) data for wind farms using the Elexon API."""
    
    # Initialize API client
    api_client = ApiClient()
    
    # Initialize the Balancing Mechanism Physical API
    physical_api = BalancingMechanismPhysicalApi(api_client)
    
    # Define dataset and settlement period parameters
    dataset = 'PN'  # Physical Notification dataset
    settlement_date = datetime.now().strftime('%Y-%m-%d')
    settlement_period = 1  # Example settlement period (1-50)
    
    # Fetch market-wide physical data for all BM Units
    print(f"Fetching physical data for settlement date {settlement_date} and period {settlement_period}...")
    try:
        physical_data = physical_api.balancing_physical_all_get(
            dataset=dataset,
            settlement_date=settlement_date,
            settlement_period=settlement_period,
            format='dataframe'
        )
        
        # Display information about the returned DataFrame
        print("Columns in the returned DataFrame:", physical_data.columns)
        print(f"Total BMUs in response: {len(physical_data)}")
        print("Sample of BMUs:", physical_data['bm_unit'].head().tolist())
        
        # Try to identify wind farms - directly use known wind farm IDs
        # These are the BM Unit IDs from your successful plot
        wind_farm_bm_units = ["T_DDBRW-1", "E_WLNEY-1", "T_GWFL-1"]
        
        # Print number of found wind farms
        print(f"Using {len(wind_farm_bm_units)} known wind farms: {wind_farm_bm_units}")
        
    except Exception as e:
        print(f"Error fetching physical data: {e}")
        return False
    
    # Define time range for data retrieval (last 24 hours instead of 7 days)
    # This increases the chance of finding data
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=24)
    
    print(f"\nRequesting data from {start_time.isoformat()} to {end_time.isoformat()}")
    
    # Create a DataFrame to store all data
    all_wind_data = pd.DataFrame()
    
    # Fetch PN data for each wind farm
    for bm_unit in wind_farm_bm_units:
        print(f"\nFetching PN data for {bm_unit}...")
        try:
            # Make the API request with detailed error handling
            print(f"Making API request for {bm_unit} with parameters:")
            print(f"  - bm_unit: {bm_unit}")
            print(f"  - from: {start_time.isoformat()}")
            print(f"  - to: {end_time.isoformat()}")
            print(f"  - dataset: PN")
            
            wind_data = physical_api.balancing_physical_get(
                bm_unit=[bm_unit],
                _from=start_time.isoformat(),
                to=end_time.isoformat(),
                dataset=['PN'],
                format='dataframe'
            )
            
            print(f"API request completed for {bm_unit}")
            
            # Check if data was retrieved successfully
            if not wind_data.empty:
                # Add a column to identify the BM Unit
                wind_data['bm_unit_id'] = bm_unit
                
                # Append to the combined DataFrame
                all_wind_data = pd.concat([all_wind_data, wind_data])
                
                # Display basic statistics
                print(f"Retrieved {len(wind_data)} data points for {bm_unit}")
                print(f"Mean output: {wind_data['level'].mean():.2f} MW")
                print(f"Max output: {wind_data['level'].max():.2f} MW")
                print(f"Min output: {wind_data['level'].min():.2f} MW")
            else:
                print(f"No data found for {bm_unit} in the specified time period")
                print("Trying with a different time period...")
                
                # Try with a different time period (7 days ago)
                alt_end_time = datetime.now() - timedelta(days=7)
                alt_start_time = alt_end_time - timedelta(hours=24)
                
                print(f"Trying alternative period: {alt_start_time.isoformat()} to {alt_end_time.isoformat()}")
                
                alt_wind_data = physical_api.balancing_physical_get(
                    bm_unit=[bm_unit],
                    _from=alt_start_time.isoformat(),
                    to=alt_end_time.isoformat(),
                    dataset=['PN'],
                    format='dataframe'
                )
                
                if not alt_wind_data.empty:
                    # Add a column to identify the BM Unit
                    alt_wind_data['bm_unit_id'] = bm_unit
                    
                    # Append to the combined DataFrame
                    all_wind_data = pd.concat([all_wind_data, alt_wind_data])
                    
                    # Display basic statistics
                    print(f"Retrieved {len(alt_wind_data)} data points for {bm_unit} (alternative period)")
                    print(f"Mean output: {alt_wind_data['level'].mean():.2f} MW")
                    print(f"Max output: {alt_wind_data['level'].max():.2f} MW")
                    print(f"Min output: {alt_wind_data['level'].min():.2f} MW")
                else:
                    print(f"No data found for {bm_unit} in the alternative time period either")
        except Exception as e:
            print(f"Error fetching data for {bm_unit}: {e}")
    
    # If we have data for at least one wind farm, plot it
    if not all_wind_data.empty:
        print("\nCreating plot with the retrieved data...")
        
        # Create a pivot table for plotting
        pivot_data = all_wind_data.pivot_table(
            index='time_from',
            columns='bm_unit_id',
            values='level',
            aggfunc='mean'
        )
        
        # Create the plot
        plt.figure(figsize=(12, 6))
        for bm_unit in pivot_data.columns:
            plt.plot(pivot_data.index, pivot_data[bm_unit], label=bm_unit)
        
        plt.title('Wind Farm Physical Notification (PN) Levels')
        plt.xlabel('Time')
        plt.ylabel('PN Level (MW)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        
        # Save the plot
        plt.savefig('wind_farm_pn_levels.png')
        
        print("\nPlot saved as 'wind_farm_pn_levels.png'")
        
        # Show the plot
        plt.show()
        
        return True
    else:
        print("\nNo data was found for any of the specified wind farms")
        
        # As a last resort, try with hardcoded sample data to demonstrate plotting functionality
        print("\nGenerating sample data for demonstration purposes...")
        
        # Create sample data
        dates = pd.date_range(start=datetime.now() - timedelta(days=1), periods=24, freq='H')
        sample_data = pd.DataFrame({
            'time_from': dates.repeat(3),
            'bm_unit_id': ['T_DDBRW-1', 'E_WLNEY-1', 'T_GWFL-1'] * 24,
            'level': [100 + i % 50 for i in range(24)] * 3  # Sample values
        })
        
        # Create a pivot table for plotting
        pivot_data = sample_data.pivot_table(
            index='time_from',
            columns='bm_unit_id',
            values='level',
            aggfunc='mean'
        )
        
        # Create the plot
        plt.figure(figsize=(12, 6))
        for bm_unit in pivot_data.columns:
            plt.plot(pivot_data.index, pivot_data[bm_unit], label=bm_unit)
        
        plt.title('Wind Farm Physical Notification (PN) Levels (SAMPLE DATA)')
        plt.xlabel('Time')
        plt.ylabel('PN Level (MW)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        
        # Save the plot
        plt.savefig('wind_farm_pn_levels_sample.png')
        
        print("\nSample plot saved as 'wind_farm_pn_levels_sample.png'")
        
        # Show the plot
        plt.show()
        
        return False

if __name__ == "__main__":
    fetch_wind_farm_pn_data()
