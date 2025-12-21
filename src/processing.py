import pandas as pd
import numpy as np
import ipaddress
import logging

# Configure logging to help diagnose data issues
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def ip_to_int(ip: str) -> int:
    """
    Convert IP address string to integer with error handling and type hints.
    """
    try:
        return int(ipaddress.ip_address(ip))
    except Exception as e:
        # Instead of failing silently, we log the specific invalid IP
        logging.warning(f"Invalid IP encountered: {ip}. Error: {e}")
        return 0

def merge_with_geo(fraud_df: pd.DataFrame, ip_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge fraud data with country data using range-based lookup.
    Includes explicit validation of required columns.
    """
    # 1. Validation: Check for required columns
    required_fraud = ['ip_address']
    required_ip = ['lower_bound_ip_address', 'upper_bound_ip_address', 'country']
    
    if not all(col in fraud_df.columns for col in required_fraud):
        raise ValueError(f"fraud_df missing required columns: {required_fraud}")
    if not all(col in ip_df.columns for col in required_ip):
        raise ValueError(f"ip_df missing required columns: {required_ip}")

    # 2. Pre-processing: Convert IP to integer if it's currently a string
    if fraud_df['ip_address'].dtype == 'O':
        logging.info("Converting string IP addresses to integers...")
        fraud_df['ip_address'] = fraud_df['ip_address'].apply(ip_to_int)
    
    # 3. Range-based Lookup Preparation
    fraud_df = fraud_df.sort_values('ip_address')
    ip_df = ip_df.sort_values('lower_bound_ip_address')
    
    # 4. Merge using merge_asof (optimizes range lookup)
    merged = pd.merge_asof(
        fraud_df, ip_df, 
        left_on='ip_address', 
        right_on='lower_bound_ip_address'
    )
    
    # 5. Validation of Range: Ensure IP is within the upper bound
    merged['country'] = np.where(
        merged['ip_address'] <= merged['upper_bound_ip_address'], 
        merged['country'], 
        'Unknown'
    )
    
    logging.info("Geolocation merge completed successfully.")
    return merged

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    General purpose cleaning: Removes duplicates and logs findings.
    """
    initial_count = len(df)
    df = df.drop_duplicates()
    final_count = len(df)
    
    if initial_count > final_count:
        logging.info(f"Removed {initial_count - final_count} duplicate rows.")
        
    return df