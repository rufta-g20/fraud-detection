import pandas as pd
import numpy as np
import ipaddress

def ip_to_int(ip):
    """Convert IP address string to integer[cite: 122, 245]."""
    try:
        return int(ipaddress.ip_address(ip))
    except:
        return 0

def merge_with_geo(fraud_df, ip_df):
    """Merge fraud data with country data[cite: 123]."""
    # Convert IP to integer if not already done
    if fraud_df['ip_address'].dtype == 'O':
        fraud_df['ip_address'] = fraud_df['ip_address'].apply(ip_to_int)
    
    # Sort for range-based lookup [cite: 246]
    fraud_df = fraud_df.sort_values('ip_address')
    ip_df = ip_df.sort_values('lower_bound_ip_address')
    
    # Merge using merge_asof [cite: 123, 246]
    merged = pd.merge_asof(
        fraud_df, ip_df, 
        left_on='ip_address', 
        right_on='lower_bound_ip_address'
    )
    
    # Check if IP is within upper bound [cite: 43]
    merged['country'] = np.where(
        merged['ip_address'] <= merged['upper_bound_ip_address'], 
        merged['country'], 
        'Unknown'
    )
    return merged