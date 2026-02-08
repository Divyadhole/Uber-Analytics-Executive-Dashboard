import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Set style for Professional Theme
plt.style.use('seaborn-v0_8-paper')
sns.set_palette("deep")

def save_fig(filename):
    os.makedirs('visualizations', exist_ok=True)
    plt.tight_layout()
    plt.savefig(f'visualizations/{filename}', dpi=300, bbox_inches='tight')
    plt.close()

def generate_visuals():
    print("Generating visualizations...")
    try:
        df = pd.read_csv('data/uber_data_features.csv')
    except:
        print("Data not found.")
        return

    # 1. Hourly Booking Volume (Clean Bar Chart)
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Hour', bins=24, kde=True, color='#2C3E50') 
    plt.title('Hourly Booking Volume - Demand Analysis', fontsize=12, fontweight='bold')
    plt.xlabel('Hour of Day')
    plt.ylabel('Ride Volume')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    save_fig('hourly_volume.png')
    
    # 2. Vehicle Performance (Completion Rate)
    # Re-calculate completion rate
    vehicle_stats = df.groupby('Vehicle Type').agg({
        'Is_Completed': lambda x: x.mean() * 100,
        'Booking Value': 'mean'
    }).sort_values('Is_Completed', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=vehicle_stats.index, y=vehicle_stats['Is_Completed'], palette='Blues_d')
    plt.ylabel('Completion Rate (%)')
    plt.xlabel('Vehicle Class')
    plt.title('Fleet Efficiency by Vehicle Class', fontsize=12, fontweight='bold')
    plt.ylim(0, 100)
    save_fig('vehicle_completion.png')
    
    # 3. Revenue Share (Professional Donut)
    revenue = df.groupby('Vehicle Type')['Booking Value'].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 8))
    explode = [0.05 if i == 0 else 0 for i in range(len(revenue))]
    plt.pie(revenue, labels=revenue.index, autopct='%1.1f%%', 
            colors=sns.color_palette('Paired'), startangle=90, pctdistance=0.85, explode=explode)
            
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    plt.title('Revenue Contribution by Segment', fontsize=12, fontweight='bold')
    save_fig('revenue_share.png')
    
    # 4. Cancellation Reasons (Horizontal Bar)
    if 'Reason for cancelling by Customer' in df.columns:
        plt.figure(figsize=(10, 6))
        top_reasons = df['Reason for cancelling by Customer'].value_counts().head(5)
        sns.barplot(y=top_reasons.index, x=top_reasons.values, palette='Reds_r')
        plt.title('Top Cancellation Drivers', fontsize=12, fontweight='bold')
        plt.xlabel('Frequency')
        plt.ylabel('')
        save_fig('cancellation_reasons.png')

if __name__ == "__main__":
    generate_visuals()
