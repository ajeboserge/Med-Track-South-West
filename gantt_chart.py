import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# Define project activities and their timeline
activities = {
    'Activity': [
        'Project Planning & Requirements',
        'Synthetic Data Generation',
        'Data Validation & Cleaning',
        'Exploratory Data Analysis',
        'Feature Engineering',
        'Model Development (Random Forest)',
        'Model Training & Optimization',
        'Model Evaluation & Testing',
        'Visualization & Reporting',
        'Documentation & Final Review',
        'Repository Setup & Push',
        'Deployment & Monitoring'
    ],
    'Start': [
        '2025-12-01',
        '2025-12-05',
        '2025-12-15',
        '2025-12-20',
        '2025-12-28',
        '2026-01-05',
        '2026-01-08',
        '2026-01-12',
        '2026-01-15',
        '2026-01-18',
        '2026-01-20',
        '2026-01-22'
    ],
    'End': [
        '2025-12-04',
        '2025-12-14',
        '2025-12-19',
        '2025-12-27',
        '2026-01-04',
        '2026-01-07',
        '2026-01-11',
        '2026-01-14',
        '2026-01-17',
        '2026-01-19',
        '2026-01-21',
        '2026-01-31'
    ],
    'Status': [
        'Completed',
        'Completed',
        'Completed',
        'Completed',
        'Completed',
        'Completed',
        'Completed',
        'Completed',
        'Completed',
        'Completed',
        'Completed',
        'In Progress'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(activities)

# Convert date strings to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Duration'] = (df['End'] - df['Start']).dt.days + 1

# Create color mapping based on status
colors = {'Completed': '#2ecc71', 'In Progress': '#f39c12', 'Pending': '#e74c3c'}
df['Color'] = df['Status'].map(colors)

# Create figure
fig, ax = plt.subplots(figsize=(16, 10))

# Plot bars
y_pos = np.arange(len(df))
for idx, row in df.iterrows():
    ax.barh(idx, row['Duration'], left=row['Start'], height=0.6, 
            color=row['Color'], edgecolor='black', linewidth=1.5, alpha=0.85)
    
    # Add duration text on bars
    mid_date = row['Start'] + timedelta(days=row['Duration']/2)
    ax.text(mid_date, idx, f"{row['Duration']}d", 
            va='center', ha='center', fontweight='bold', fontsize=9, color='white')

# Format x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45, ha='right')

# Set labels and title
ax.set_yticks(y_pos)
ax.set_yticklabels(df['Activity'], fontsize=10)
ax.set_xlabel('Timeline', fontsize=12, fontweight='bold')
ax.set_title('Med-Track South-West: Project Gantt Chart\nPharmaceutical Supply Chain Analysis & Stock-Out Prediction System', 
             fontsize=14, fontweight='bold', pad=20)

# Add grid
ax.grid(True, axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2ecc71', edgecolor='black', label='Completed'),
    Patch(facecolor='#f39c12', edgecolor='black', label='In Progress'),
    Patch(facecolor='#e74c3c', edgecolor='black', label='Pending')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=10, framealpha=0.95)

# Add project info box
project_info = f"""
Project Duration: 52 days
Start Date: 2025-12-01
Current Date: 2026-01-22
Progress: 92% Complete
Expected Completion: 2026-01-31
"""
ax.text(0.02, 0.98, project_info, transform=ax.transAxes, 
        fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', 
        facecolor='wheat', alpha=0.8), family='monospace')

# Adjust layout and save
plt.tight_layout()
plt.savefig('gantt_chart.png', dpi=300, bbox_inches='tight')
print("✓ Gantt chart saved as 'gantt_chart.png'")
plt.show()

# Print summary table
print("\n" + "="*100)
print("PROJECT ACTIVITY SUMMARY")
print("="*100)
summary_df = df[['Activity', 'Start', 'End', 'Duration', 'Status']].copy()
summary_df['Start'] = summary_df['Start'].dt.strftime('%Y-%m-%d')
summary_df['End'] = summary_df['End'].dt.strftime('%Y-%m-%d')
print(summary_df.to_string(index=False))

# Print statistics
print("\n" + "="*100)
print("PROJECT STATISTICS")
print("="*100)
print(f"Total Activities: {len(df)}")
print(f"Total Duration: {(df['End'].max() - df['Start'].min()).days + 1} days")
print(f"Completed Tasks: {len(df[df['Status'] == 'Completed'])} ({len(df[df['Status'] == 'Completed'])/len(df)*100:.1f}%)")
print(f"In Progress Tasks: {len(df[df['Status'] == 'In Progress'])} ({len(df[df['Status'] == 'In Progress'])/len(df)*100:.1f}%)")
print(f"Pending Tasks: {len(df[df['Status'] == 'Pending'])} ({len(df[df['Status'] == 'Pending'])/len(df)*100:.1f}%)")
print(f"Project Start: {df['Start'].min().strftime('%Y-%m-%d')}")
print(f"Project End (Planned): {df['End'].max().strftime('%Y-%m-%d')}")
