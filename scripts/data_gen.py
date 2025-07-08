"""
Data Generation Script for Business Dashboard
Generates realistic business data for dashboard visualization
Creates CSV and NPY files for various dashboard components
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os
from typing import Dict, List, Tuple

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
DATA_DIR = "data"
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Sales representatives
SALES_REPS = [
    "Alice", "Jared", "Heather", "Shaun", "Marsha", 
    "Polly", "Dalisu", "Marcus", "Sarah", "Kevin"
]

# US States and their coordinates (for map visualization)
US_STATES = {
    'CA': {'name': 'California', 'lat': 36.7783, 'lon': -119.4179, 'pop_weight': 0.12},
    'TX': {'name': 'Texas', 'lat': 31.9686, 'lon': -99.9018, 'pop_weight': 0.09},
    'FL': {'name': 'Florida', 'lat': 27.7663, 'lon': -82.6404, 'pop_weight': 0.07},
    'NY': {'name': 'New York', 'lat': 40.7128, 'lon': -74.0060, 'pop_weight': 0.06},
    'PA': {'name': 'Pennsylvania', 'lat': 40.2732, 'lon': -76.8750, 'pop_weight': 0.04},
    'IL': {'name': 'Illinois', 'lat': 40.3363, 'lon': -89.0022, 'pop_weight': 0.04},
    'OH': {'name': 'Ohio', 'lat': 40.3888, 'lon': -82.7649, 'pop_weight': 0.04},
    'GA': {'name': 'Georgia', 'lat': 33.0406, 'lon': -83.6431, 'pop_weight': 0.03},
    'NC': {'name': 'North Carolina', 'lat': 35.3272, 'lon': -80.8414, 'pop_weight': 0.03},
    'MI': {'name': 'Michigan', 'lat': 44.3467, 'lon': -85.4102, 'pop_weight': 0.03},
    'WA': {'name': 'Washington', 'lat': 47.0379, 'lon': -121.0187, 'pop_weight': 0.02},
    'CO': {'name': 'Colorado', 'lat': 39.0598, 'lon': -105.3111, 'pop_weight': 0.02},
    'OR': {'name': 'Oregon', 'lat': 44.5721, 'lon': -122.0709, 'pop_weight': 0.01},
    'AZ': {'name': 'Arizona', 'lat': 33.7298, 'lon': -111.4312, 'pop_weight': 0.02},
    'NV': {'name': 'Nevada', 'lat': 38.3135, 'lon': -117.0554, 'pop_weight': 0.01},
    'MA': {'name': 'Massachusetts', 'lat': 42.2352, 'lon': -71.0275, 'pop_weight': 0.02},
    'VA': {'name': 'Virginia', 'lat': 37.7693, 'lon': -78.2057, 'pop_weight': 0.03},
    'NJ': {'name': 'New Jersey', 'lat': 40.3573, 'lon': -74.4057, 'pop_weight': 0.03},
    'TN': {'name': 'Tennessee', 'lat': 35.7478, 'lon': -86.7915, 'pop_weight': 0.02},
    'IN': {'name': 'Indiana', 'lat': 39.8647, 'lon': -86.2604, 'pop_weight': 0.02},
    'MO': {'name': 'Missouri', 'lat': 38.4561, 'lon': -92.2884, 'pop_weight': 0.02},
    'WI': {'name': 'Wisconsin', 'lat': 44.2619, 'lon': -89.6165, 'pop_weight': 0.02},
    'MN': {'name': 'Minnesota', 'lat': 45.6945, 'lon': -93.9002, 'pop_weight': 0.02},
    'AL': {'name': 'Alabama', 'lat': 32.3668, 'lon': -86.7999, 'pop_weight': 0.01},
    'SC': {'name': 'South Carolina', 'lat': 33.8191, 'lon': -80.9066, 'pop_weight': 0.02},
    'LA': {'name': 'Louisiana', 'lat': 31.1801, 'lon': -91.8749, 'pop_weight': 0.01},
    'KY': {'name': 'Kentucky', 'lat': 37.6681, 'lon': -84.6701, 'pop_weight': 0.01},
    'UT': {'name': 'Utah', 'lat': 40.1135, 'lon': -111.8535, 'pop_weight': 0.01},
    'CT': {'name': 'Connecticut', 'lat': 41.5978, 'lon': -72.7554, 'pop_weight': 0.01},
    'OK': {'name': 'Oklahoma', 'lat': 35.5653, 'lon': -96.9289, 'pop_weight': 0.01},
    'KS': {'name': 'Kansas', 'lat': 38.5266, 'lon': -96.7265, 'pop_weight': 0.01},
    'IA': {'name': 'Iowa', 'lat': 42.0115, 'lon': -93.2105, 'pop_weight': 0.01},
    'NE': {'name': 'Nebraska', 'lat': 41.1254, 'lon': -98.2681, 'pop_weight': 0.01},
    'NM': {'name': 'New Mexico', 'lat': 34.8405, 'lon': -106.2485, 'pop_weight': 0.01},
    'ID': {'name': 'Idaho', 'lat': 44.2405, 'lon': -114.4788, 'pop_weight': 0.005},
    'WV': {'name': 'West Virginia', 'lat': 38.4680, 'lon': -80.9696, 'pop_weight': 0.005},
    'AR': {'name': 'Arkansas', 'lat': 34.9513, 'lon': -92.3809, 'pop_weight': 0.01},
    'MS': {'name': 'Mississippi', 'lat': 32.7673, 'lon': -89.6812, 'pop_weight': 0.01},
    'MT': {'name': 'Montana', 'lat': 47.0527, 'lon': -110.2140, 'pop_weight': 0.003},
    'ND': {'name': 'North Dakota', 'lat': 47.5289, 'lon': -99.7840, 'pop_weight': 0.002},
    'SD': {'name': 'South Dakota', 'lat': 44.2998, 'lon': -99.4388, 'pop_weight': 0.003},
    'WY': {'name': 'Wyoming', 'lat': 42.7475, 'lon': -107.2085, 'pop_weight': 0.002},
    'VT': {'name': 'Vermont', 'lat': 44.0459, 'lon': -72.7107, 'pop_weight': 0.002},
    'NH': {'name': 'New Hampshire', 'lat': 43.4525, 'lon': -71.5639, 'pop_weight': 0.004},
    'ME': {'name': 'Maine', 'lat': 44.6939, 'lon': -69.3819, 'pop_weight': 0.004},
    'RI': {'name': 'Rhode Island', 'lat': 41.6809, 'lon': -71.5118, 'pop_weight': 0.003},
    'DE': {'name': 'Delaware', 'lat': 39.3498, 'lon': -75.5148, 'pop_weight': 0.003},
    'HI': {'name': 'Hawaii', 'lat': 21.0943, 'lon': -157.4983, 'pop_weight': 0.004},
    'AK': {'name': 'Alaska', 'lat': 61.0700, 'lon': -165.4048, 'pop_weight': 0.002},
}

def create_data_directory():
    """Create data directory if it doesn't exist"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Created {DATA_DIR} directory")

def generate_sales_data() -> pd.DataFrame:
    """Generate sales data for the dashboard"""
    print("Generating sales data...")
    
    # Generate daily sales data for the past year
    date_range = pd.date_range(start=START_DATE, end=END_DATE, freq='D')
    
    sales_data = []
    base_daily_sales = 8000  # Base daily sales
    
    for date in date_range:
        # Add seasonality and trends
        day_of_year = date.timetuple().tm_yday
        seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * day_of_year / 365)
        
        # Add weekly patterns (lower on weekends)
        weekly_factor = 0.7 if date.weekday() >= 5 else 1.0
        
        # Add random variation
        random_factor = np.random.normal(1.0, 0.3)
        
        daily_sales = base_daily_sales * seasonal_factor * weekly_factor * random_factor
        daily_sales = max(1000, daily_sales)  # Ensure minimum sales
        
        sales_data.append({
            'date': date,
            'daily_sales': round(daily_sales, 2),
            'day_of_week': date.strftime('%A'),
            'month': date.strftime('%B'),
            'year': date.year
        })
    
    df = pd.DataFrame(sales_data)
    
    # Calculate running totals and metrics
    df['monthly_sales'] = df.groupby([df['date'].dt.year, df['date'].dt.month])['daily_sales'].cumsum()
    df['sales_growth'] = df['daily_sales'].pct_change().fillna(0)
    
    return df

def generate_deals_data() -> pd.DataFrame:
    """Generate individual deals data"""
    print("Generating deals data...")
    
    deals_data = []
    
    # Generate deals for each month
    for month in range(1, 13):
        # Number of deals per month (varies)
        num_deals = np.random.randint(15, 35)
        
        for _ in range(num_deals):
            rep = random.choice(SALES_REPS)
            
            # Deal amounts vary by rep (some are better performers)
            if rep in ['Alice', 'Jared']:
                amount = np.random.normal(7000, 2000)
            elif rep in ['Heather', 'Shaun']:
                amount = np.random.normal(6000, 1500)
            else:
                amount = np.random.normal(4000, 1000)
            
            amount = max(1000, amount)  # Minimum deal size
            
            # Random date in the month
            day = np.random.randint(1, 29)
            deal_date = datetime(2024, month, day)
            
            deals_data.append({
                'date': deal_date,
                'sales_rep': rep,
                'amount': round(amount, 2),
                'month': month,
                'quarter': f"Q{(month-1)//3 + 1}",
                'deal_id': f"DEAL_{len(deals_data)+1:04d}"
            })
    
    df = pd.DataFrame(deals_data)
    
    # Sort by amount to get biggest deals
    df = df.sort_values('amount', ascending=False).reset_index(drop=True)
    
    return df

def generate_social_media_data() -> pd.DataFrame:
    """Generate social media followers data"""
    print("Generating social media data...")
    
    # Generate daily follower counts
    date_range = pd.date_range(start=START_DATE, end=END_DATE, freq='D')
    
    # Starting follower counts
    linkedin_followers = 18000
    twitter_followers = 9800
    
    social_data = []
    
    for date in date_range:
        # LinkedIn growth (steady)
        linkedin_growth = np.random.normal(15, 5)  # Average 15 followers per day
        linkedin_followers += max(0, linkedin_growth)
        
        # Twitter growth (more volatile)
        twitter_growth = np.random.normal(8, 10)  # Average 8 followers per day
        twitter_followers += max(-5, twitter_growth)  # Can lose followers
        
        social_data.append({
            'date': date,
            'linkedin_followers': int(linkedin_followers),
            'twitter_followers': int(twitter_followers),
            'linkedin_growth': round(linkedin_growth, 1),
            'twitter_growth': round(twitter_growth, 1)
        })
    
    df = pd.DataFrame(social_data)
    return df

def generate_website_analytics() -> pd.DataFrame:
    """Generate website analytics data"""
    print("Generating website analytics data...")
    
    date_range = pd.date_range(start=START_DATE, end=END_DATE, freq='D')
    
    analytics_data = []
    
    for date in date_range:
        # Base metrics
        base_users = 800
        base_enquiries = 4
        
        # Add seasonality and day-of-week effects
        day_of_week = date.weekday()
        weekend_factor = 0.6 if day_of_week >= 5 else 1.0
        
        # Add some randomness
        daily_users = int(base_users * weekend_factor * np.random.normal(1.0, 0.3))
        daily_enquiries = int(base_enquiries * weekend_factor * np.random.normal(1.0, 0.4))
        
        # Ensure minimum values
        daily_users = max(100, daily_users)
        daily_enquiries = max(0, daily_enquiries)
        
        analytics_data.append({
            'date': date,
            'daily_users': daily_users,
            'daily_enquiries': daily_enquiries,
            'conversion_rate': round(daily_enquiries / daily_users * 100, 2),
            'day_of_week': date.strftime('%A')
        })
    
    df = pd.DataFrame(analytics_data)
    return df

def generate_nps_data() -> pd.DataFrame:
    """Generate Net Promoter Score data"""
    print("Generating NPS data...")
    
    # Generate monthly NPS scores
    months = pd.date_range(start=START_DATE, end=END_DATE, freq='M')
    
    nps_data = []
    base_nps = 55  # Starting NPS score
    
    for month in months:
        # NPS tends to improve over time with some volatility
        nps_change = np.random.normal(1, 8)  # Monthly change
        base_nps += nps_change
        
        # Keep NPS in realistic range
        current_nps = max(0, min(100, base_nps))
        
        # Generate individual responses
        num_responses = np.random.randint(80, 150)
        
        # Calculate promoters, passives, detractors based on NPS
        promoter_rate = (current_nps + 100) / 200  # Rough conversion
        detractor_rate = (100 - current_nps) / 200
        passive_rate = 1 - promoter_rate - detractor_rate
        
        promoters = int(num_responses * promoter_rate)
        detractors = int(num_responses * detractor_rate)
        passives = num_responses - promoters - detractors
        
        nps_data.append({
            'month': month,
            'nps_score': round(current_nps, 1),
            'total_responses': num_responses,
            'promoters': promoters,
            'passives': passives,
            'detractors': detractors,
            'promoter_rate': round(promoter_rate * 100, 1),
            'detractor_rate': round(detractor_rate * 100, 1)
        })
    
    df = pd.DataFrame(nps_data)
    return df

def generate_feedback_data() -> pd.DataFrame:
    """Generate customer feedback data"""
    print("Generating feedback data...")
    
    feedback_texts = [
        "OK",
        "Very Helpful!!",
        "very good \"thumbs up\"",
        "Great service, would recommend",
        "Could be better",
        "Excellent support team",
        "Fast response time",
        "Needs improvement",
        "Outstanding experience",
        "Average service",
        "Exceeded expectations",
        "Professional and courteous",
        "Will definitely use again",
        "Not satisfied with response",
        "Quick resolution",
        "Friendly staff",
        "Could use more features",
        "Exactly what I needed",
        "Good value for money",
        "Impressed with the service"
    ]
    
    feedback_data = []
    
    # Generate feedback over the past few months
    for days_ago in range(0, 90):
        # Random number of feedback entries per day
        num_feedback = np.random.poisson(2)  # Average 2 feedback per day
        
        for _ in range(num_feedback):
            feedback_date = datetime.now() - timedelta(days=days_ago)
            
            # Random rating (1-5 stars) with bias toward higher ratings
            rating = np.random.choice([1, 2, 3, 4, 5], p=[0.05, 0.1, 0.2, 0.35, 0.3])
            
            feedback_data.append({
                'date': feedback_date,
                'feedback_text': random.choice(feedback_texts),
                'rating': rating,
                'days_ago': days_ago,
                'sentiment': 'positive' if rating >= 4 else 'negative' if rating <= 2 else 'neutral'
            })
    
    df = pd.DataFrame(feedback_data)
    df = df.sort_values('date', ascending=False).reset_index(drop=True)
    
    return df

def generate_geographic_data() -> pd.DataFrame:
    """Generate geographic data for active users map"""
    print("Generating geographic data...")
    
    geo_data = []
    
    # Generate active user locations based on population weights
    total_active_users = 15000
    
    for state_code, state_info in US_STATES.items():
        # Number of users in this state based on population weight
        num_users = int(total_active_users * state_info['pop_weight'])
        
        if num_users > 0:
            # Generate random locations within the state (simplified)
            for _ in range(max(1, num_users // 100)):  # Cluster users into ~100 user groups
                # Add some randomness to coordinates
                lat_offset = np.random.normal(0, 1.0)
                lon_offset = np.random.normal(0, 1.0)
                
                geo_data.append({
                    'state': state_code,
                    'state_name': state_info['name'],
                    'lat': state_info['lat'] + lat_offset,
                    'lon': state_info['lon'] + lon_offset,
                    'user_count': np.random.randint(50, 200),
                    'active_sessions': np.random.randint(5, 50),
                    'avg_session_duration': np.random.normal(5.5, 2.0),  # minutes
                    'bounce_rate': np.random.normal(0.35, 0.15)
                })
    
    df = pd.DataFrame(geo_data)
    
    # Clean up data
    df['avg_session_duration'] = df['avg_session_duration'].clip(1, 15)
    df['bounce_rate'] = df['bounce_rate'].clip(0.1, 0.8)
    
    return df

def save_data_files():
    """Save all generated data to CSV and NPY files"""
    print("Saving data files...")
    
    # Generate all datasets
    sales_df = generate_sales_data()
    deals_df = generate_deals_data()
    social_df = generate_social_media_data()
    website_df = generate_website_analytics()
    nps_df = generate_nps_data()
    feedback_df = generate_feedback_data()
    geo_df = generate_geographic_data()
    
    # Save as CSV files
    sales_df.to_csv(f'{DATA_DIR}/sales_data.csv', index=False)
    deals_df.to_csv(f'{DATA_DIR}/deals_data.csv', index=False)
    social_df.to_csv(f'{DATA_DIR}/social_media_data.csv', index=False)
    website_df.to_csv(f'{DATA_DIR}/website_analytics.csv', index=False)
    nps_df.to_csv(f'{DATA_DIR}/nps_data.csv', index=False)
    feedback_df.to_csv(f'{DATA_DIR}/feedback_data.csv', index=False)
    geo_df.to_csv(f'{DATA_DIR}/geographic_data.csv', index=False)
    
    # Save as NPY files (for numerical data)
    np.save(f'{DATA_DIR}/sales_amounts.npy', sales_df['daily_sales'].values)
    np.save(f'{DATA_DIR}/deal_amounts.npy', deals_df['amount'].values)
    np.save(f'{DATA_DIR}/social_followers.npy', 
            np.column_stack([social_df['linkedin_followers'].values, 
                           social_df['twitter_followers'].values]))
    np.save(f'{DATA_DIR}/website_metrics.npy', 
            np.column_stack([website_df['daily_users'].values, 
                           website_df['daily_enquiries'].values]))
    np.save(f'{DATA_DIR}/nps_scores.npy', nps_df['nps_score'].values)
    np.save(f'{DATA_DIR}/geo_coordinates.npy', 
            np.column_stack([geo_df['lat'].values, geo_df['lon'].values]))
    
    print(f"Data files saved to {DATA_DIR}/ directory")
    print("CSV files created:")
    print("- sales_data.csv")
    print("- deals_data.csv") 
    print("- social_media_data.csv")
    print("- website_analytics.csv")
    print("- nps_data.csv")
    print("- feedback_data.csv")
    print("- geographic_data.csv")
    print("\nNPY files created:")
    print("- sales_amounts.npy")
    print("- deal_amounts.npy")
    print("- social_followers.npy")
    print("- website_metrics.npy")
    print("- nps_scores.npy")
    print("- geo_coordinates.npy")

def generate_summary_stats():
    """Generate summary statistics that match the dashboard"""
    print("\nGenerating summary statistics...")
    
    # Load the data we just created
    deals_df = pd.read_csv(f'{DATA_DIR}/deals_data.csv')
    social_df = pd.read_csv(f'{DATA_DIR}/social_media_data.csv')
    website_df = pd.read_csv(f'{DATA_DIR}/website_analytics.csv')
    nps_df = pd.read_csv(f'{DATA_DIR}/nps_data.csv')
    
    # Calculate current month statistics
    current_month = datetime.now().month
    this_month_deals = deals_df[deals_df['month'] == current_month]
    
    # Top deals this month
    top_deals = this_month_deals.nlargest(10, 'amount')
    
    # Current social media followers (latest values)
    latest_social = social_df.iloc[-1]
    
    # Website stats for past 7 days
    website_df['date'] = pd.to_datetime(website_df['date'])
    past_7_days = website_df[website_df['date'] >= (datetime.now() - timedelta(days=7))]
    
    # Current NPS score
    latest_nps = nps_df.iloc[-1]
    
    # Create summary dictionary
    summary = {
        'sales_this_month': round(this_month_deals['amount'].sum() / 1000, 1),  # in thousands
        'sales_today': round(np.random.normal(9600, 1000), 1),
        'sales_yesterday': round(np.random.normal(20600, 2000), 1),
        'linkedin_followers': f"{latest_social['linkedin_followers'] / 1000:.1f}k",
        'twitter_followers': f"{latest_social['twitter_followers'] / 1000:.1f}k",
        'website_users_7days': f"{past_7_days['daily_users'].sum() / 1000:.1f}k",
        'website_enquiries_7days': past_7_days['daily_enquiries'].sum(),
        'current_nps': round(latest_nps['nps_score']),
        'top_deals_this_month': top_deals[['sales_rep', 'amount']].head(10).to_dict('records')
    }
    
    # Save summary
    import json
    with open(f'{DATA_DIR}/dashboard_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print("Dashboard Summary:")
    print(f"Sales this month: ${summary['sales_this_month']}k")
    print(f"Sales today: ${summary['sales_today']}k")
    print(f"Sales yesterday: ${summary['sales_yesterday']}k")
    print(f"LinkedIn followers: {summary['linkedin_followers']}")
    print(f"Twitter followers: {summary['twitter_followers']}")
    print(f"Website users (7 days): {summary['website_users_7days']}")
    print(f"Website enquiries (7 days): {summary['website_enquiries_7days']}")
    print(f"Current NPS: {summary['current_nps']}")
    print(f"Top deals this month: {len(summary['top_deals_this_month'])} deals")

if __name__ == "__main__":
    print("🚀 Starting Business Dashboard Data Generation")
    print("=" * 50)
    
    # Create data directory
    create_data_directory()
    
    # Generate and save all data
    save_data_files()
    
    # Generate summary statistics
    generate_summary_stats()
    
    print("\n✅ Data generation complete!")
    print("Files are ready for dashboard visualization.")
    print("=" * 50) 