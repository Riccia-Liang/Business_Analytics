import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# df = pd.read_csv('path_to_nyc_311_data.csv')

# Bar chart for complaint type distribution
def plot_complaint_type_distribution(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='complaint_type', order=df['complaint_type'].value_counts().index)
    plt.title('Distribution of NYC 311 Complaint Types')
    plt.xticks(rotation=45)
    plt.ylabel('Number of Complaints')
    plt.show()

# Pie chart for complaint type proportions
def plot_complaint_type_proportions(df):
    type_counts = df['complaint_type'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')
    plt.title('Proportion of NYC 311 Complaints by Type')
    plt.show()

# Borough analysis
def plot_borough_analysis(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='borough', order=df['borough'].value_counts().index)
    plt.title('Number of NYC 311 Complaints by Borough')
    plt.xticks(rotation=45)
    plt.ylabel('Number of Complaints')
    plt.show()

# Seasonal trends
def plot_seasonal_trends(df):
    df['created_date'] = pd.to_datetime(df['created_date'])
    df['season'] = df['created_date'].dt.month % 12 // 3 + 1
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='season')
    plt.title('NYC 311 Complaints by Season')
    plt.xlabel('Season (1: Winter, 2: Spring, 3: Summer, 4: Fall)')
    plt.ylabel('Number of Complaints')
    plt.show()

# Example function calls
# plot_complaint_type_distribution(df)
# plot_complaint_type_proportions(df)
# plot_borough_analysis(df)
# plot_seasonal_trends(df)