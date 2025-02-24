import pandas as pd
from yahoo_fin import stock_info as si
from datetime import datetime, timedelta

def get_spy_last_30_days():
    """
    Retrieves daily stock data for SPY for the last 30 days using yahoo_fin.

    Returns:
        pandas.DataFrame: DataFrame containing the stock data, or None if an error occurs.
    """
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)

        spy_data = si.get_data("SPY", start_date=start_date, end_date=end_date, interval="1d")
        return spy_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    spy_last_30_days = get_spy_last_30_days()

    if spy_last_30_days is not None:
        print(spy_last_30_days)
        #Example of accessing columns
        #print(spy_last_30_days['close'])
        #Example of accessing the first row
        #print(spy_last_30_days.iloc[0])
