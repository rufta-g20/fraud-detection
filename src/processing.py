import pandas as pd
import numpy as np
import ipaddress
import logging
from typing import Union

# Configure logging for better traceability in production
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def ip_to_int(ip: Union[str, float, int]) -> int:
    """
    Converts a string IP address to its integer representation.
    
    Args:
        ip (str): The IP address string (e.g., '192.168.1.1').
        
    Returns:
        int: The integer value of the IP. Returns 0 if IP is invalid.
    """
    try:
        return int(ipaddress.ip_address(str(ip)))
    except Exception as e:
        logging.warning(f"Invalid IP encountered: {ip}. Error: {e}")
        return 0

def merge_with_geo(fraud_df: pd.DataFrame, ip_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge fraud data with country data using an optimized range-based lookup.
    
    Args:
        fraud_df (pd.DataFrame): Data containing 'ip_address'.
        ip_df (pd.DataFrame): Data containing IP ranges and 'country'.
        
    Returns:
        pd.DataFrame: Merged dataframe with a validated 'country' column.
    """
    # 1. Validation: Check for required columns
    required_fraud = ['ip_address']
    required_ip = ['lower_bound_ip_address', 'upper_bound_ip_address', 'country']
    
    if not all(col in fraud_df.columns for col in required_fraud):
        raise ValueError(f"fraud_df missing required columns: {required_fraud}")
    if not all(col in ip_df.columns for col in required_ip):
        raise ValueError(f"ip_df missing required columns: {required_ip}")

    # 2. Pre-processing: Ensure IPs are integers for comparison
    if fraud_df['ip_address'].dtype == 'O':
        logging.info("Converting string IP addresses to integers...")
        fraud_df['ip_address'] = fraud_df['ip_address'].apply(ip_to_int)
    
    # 3. Range-based Lookup Preparation (Requirement for merge_asof)
    fraud_df = fraud_df.sort_values('ip_address')
    ip_df = ip_df.sort_values('lower_bound_ip_address')
    
    # 4. Merge using merge_asof (O(n log n) efficiency)
    merged = pd.merge_asof(
        fraud_df, ip_df, 
        left_on='ip_address', 
        right_on='lower_bound_ip_address'
    )
    
    # 5. Validation of Range: Ensure IP is within the upper bound
    # If it falls outside the range, mark as 'Unknown'
    merged['country'] = np.where(
        (merged['ip_address'] <= merged['upper_bound_ip_address']), 
        merged['country'], 
        'Unknown'
    )
    
    # Fill any NaNs resulting from IPs smaller than the lowest lower_bound
    merged['country'] = merged['country'].fillna('Unknown')
    
    logging.info("Geolocation merge completed successfully.")
    return merged

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicates and logs the impact on dataset size.
    """
    initial_count = len(df)
    df = df.drop_duplicates()
    final_count = len(df)
    
    if initial_count > final_count:
        logging.info(f"Data Cleaning: Removed {initial_count - final_count} duplicate rows.")
        
    return df