import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def _column(df, *candidates):
    """Return the first matching NYC Open Data column name."""
    for candidate in candidates:
        if candidate in df.columns:
            return candidate
    raise KeyError(f"Expected one of these columns: {', '.join(candidates)}")

# Bar chart for complaint type distribution
def plot_complaint_type_distribution(df, top_n=20):
    complaint = _column(df, 'complaint_type', 'Complaint Type')
    counts = df[complaint].value_counts().head(top_n).sort_values()
    plt.figure(figsize=(11, 8))
    sns.barplot(x=counts.values, y=counts.index, color='#2878B5')
    plt.title(f'Top {top_n} NYC 311 Complaint Types')
    plt.xlabel('Number of Complaints')
    plt.ylabel('')
    plt.show()

# Pie chart for complaint type proportions
def plot_complaint_type_proportions(df, top_n=10):
    complaint = _column(df, 'complaint_type', 'Complaint Type')
    counts = df[complaint].value_counts()
    shown = pd.concat([
        counts.head(top_n),
        pd.Series({'Other complaint types': counts.iloc[top_n:].sum()}),
    ])
    plt.figure(figsize=(9, 9))
    plt.pie(shown.values, labels=shown.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'NYC 311 Complaints: Top {top_n} and Other')
    plt.show()

# Borough analysis
def plot_borough_analysis(df):
    borough = _column(df, 'borough', 'Borough')
    counts = df[borough].value_counts().drop(labels=['Unspecified'], errors='ignore')
    plt.figure(figsize=(9, 5))
    sns.barplot(x=counts.values, y=counts.index, color='#5AAE61')
    plt.title('Number of NYC 311 Complaints by Borough')
    plt.xlabel('Number of Complaints')
    plt.ylabel('')
    plt.show()


def plot_monthly_trends(df):
    created = _column(df, 'created_date', 'Created Date')
    complaint = _column(df, 'complaint_type', 'Complaint Type')
    dates = pd.to_datetime(df[created])
    monthly = df.assign(_created_date=dates).set_index('_created_date')[complaint].resample('MS').count()
    plt.figure(figsize=(12, 5))
    monthly.plot(color='#6A51A3')
    plt.title('Monthly NYC 311 Complaints')
    plt.xlabel('Month')
    plt.ylabel('Number of Complaints')
    plt.show()

# Seasonal trends
def plot_seasonal_trends(df):
    created = _column(df, 'created_date', 'Created Date')
    complaint = _column(df, 'complaint_type', 'Complaint Type')
    dates = pd.to_datetime(df[created])
    monthly = (df.assign(_created_date=dates)
                 .set_index('_created_date')[complaint]
                 .resample('MS').count())
    # Do not let an incomplete final month distort the seasonal comparison.
    if dates.max() < dates.max().to_period('M').end_time:
        monthly = monthly.iloc[:-1]
    counts = monthly.groupby(monthly.index.month).mean().reindex(range(1, 13))
    names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=names, y=counts.values, marker='o', color='#D95F0E')
    plt.title('Seasonal Pattern: Average Complaints by Calendar Month')
    plt.xlabel('Calendar Month')
    plt.ylabel('Average Complaints per Complete Month')
    plt.show()

# Example function calls
# plot_complaint_type_distribution(df)
# plot_complaint_type_proportions(df)
# plot_borough_analysis(df)
# plot_monthly_trends(df)
# plot_seasonal_trends(df)
