######################################
# Pre-processing of exported information
######################################

import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Load JSON file, process time-related information
with open("History.json") as f:
    data = json.load(f)
import json

i = 0
function = True
array_time = []

while (function == True):
  if i == 3825:
      function = False
  else:
    array_time.append(data['Browser History'][i])
    i=i+1

time_usec_values = [entry['time_usec'] for entry in array_time if 'time_usec' in entry]
# print(time_usec_values)

# Excel file creation concerning 'Browser History' entries, 'time_usec' components
browser_history = data.get('Browser History', [])

time_data = [
    {
        'time_usec': entry['time_usec'],
        'datetime': datetime.utcfromtimestamp(entry['time_usec'] / 1_000_000).strftime('%Y-%m-%d %H:%M:%S')
    }
    for entry in browser_history if 'time_usec' in entry
]

df = pd.DataFrame(time_data)
df.to_excel("time_converted.xlsx", index=False)

######################################
# Plot of frequency of late-night activity by month
######################################

df = pd.read_excel("time_converted.xlsx")
df['datetime'] = pd.to_datetime(df['datetime'])

df['hour'] = df['datetime'].dt.hour
df['date'] = df['datetime'].dt.date
df['month'] = df['datetime'].dt.strftime('%Y-%m')

late_night_hours = range(0, 6) # Late-night hours (e.g., 12 AM - 6 AM)

late_night_df = df[df['hour'].isin(late_night_hours)]
late_night_count = late_night_df.groupby('month').size()

plt.figure(figsize=(10, 5))
late_night_count.plot(kind='bar', color='red', alpha=0.75)
plt.xlabel("Month")
plt.ylabel("Late-Night Activity Count (12 AM - 6 AM)")
plt.title("Frequency of Late-Night Activity by Month")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

######################################
# Summary of activity metrics by month
######################################

df = pd.read_excel("time_converted.xlsx")
df['datetime'] = pd.to_datetime(df['datetime'])

df['hour'] = df['datetime'].dt.hour
df['month'] = df['datetime'].dt.strftime('%Y-%m')

late_night_hours = range(0, 6) # Late-night: (12 AM - 6 AM)

total_activity = df.groupby('month').size() # Total activity
late_night_activity = df[df['hour'].isin(late_night_hours)].groupby('month').size() #Late-night activity
non_late_night_activity = total_activity - late_night_activity # Non late-night activity
late_night_percentage = (late_night_activity / total_activity) * 100 # Percentage of late-night activity
earliest_activity = df.groupby('month')['datetime'].min().dt.strftime('%H:%M:%S') # Earliest activity

summary_table = pd.DataFrame({
    "Total Activity": total_activity,
    "Late-Night Activity": late_night_activity,
    "Non-Late-Night Activity": non_late_night_activity,
    "Late-Night %": late_night_percentage.round(2),
    "Earliest Activity": earliest_activity
}).fillna(0)  # Fill NaN values with 0 in case some months lack late-night activity

summary_table_str = summary_table.astype(str)

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=summary_table_str.values,
                 colLabels=summary_table_str.columns,
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width([0, 1, 2, 3, 4])

plt.title("Summary of Activity Metrics by Month", fontsize=12, fontweight="bold")
plt.show()

######################################
## Hourly activity distribution per month
######################################

time_usec_values = [entry['time_usec'] for entry in data['Browser History'] if 'time_usec' in entry]
timestamps = [datetime.utcfromtimestamp(t / 1_000_000) for t in time_usec_values]

df = pd.DataFrame({'datetime': timestamps})
df['month'] = df['datetime'].dt.strftime('%Y-%m')
df['hour'] = df['datetime'].dt.hour

activity_counts = df.groupby(['month', 'hour']).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(12, 6))
activity_counts.T.plot(kind='bar', stacked=True, colormap='viridis', width=1, ax=ax)

plt.xlabel("Hour of the Day")
plt.ylabel("Activity Count")
plt.title("Hourly Activity Distribution per Month")
plt.legend(title="Month", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

######################################
# Seperate monthly distribution plots
######################################

time_usec_values = [entry['time_usec'] for entry in data['Browser History'] if 'time_usec' in entry]
timestamps = [datetime.utcfromtimestamp(t / 1_000_000) for t in time_usec_values]

df = pd.DataFrame({'datetime': timestamps})
df['month'] = df['datetime'].dt.strftime('%Y-%m')
df['hour'] = df['datetime'].dt.hour

months = df['month'].unique()

for month in months:
    monthly_data = df[df['month'] == month]
    activity_counts = monthly_data['hour'].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    plt.bar(activity_counts.index, activity_counts.values, color='skyblue', edgecolor='black')
    plt.xlabel("Hour of the Day")
    plt.ylabel("Activity Count")
    plt.title(f"Activity Distribution - {month}")
    plt.xticks(range(24))
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()
