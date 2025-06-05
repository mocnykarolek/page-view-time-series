import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df.set_index('date')



# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]

print(df)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df.index, df.value)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.index = pd.to_datetime(df_bar.index, format='%Y-%m-%d')
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month


    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    
    
    print(df_bar)
    # Draw bar plot
    ax = df_bar.plot(kind='bar', figsize=(12,6))

    ax.set_ylabel('Average Page Views')
    fig = ax.get_figure()


    


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    

    # ax = df_box.plot(kind='box', figsize=(12,6))

    # fig = ax.get_figure() 
    fig, axes = plt.subplots(1,2, figsize=(12,5))

    sns.boxplot(data=df_box, x = df_box.year, y=df_box.value, palette='Set1', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    sns.boxplot(data=df_box, x = df_box.month, y=df_box.value, palette='Set2',order=months_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    
    fig.tight_layout()

    print(df_box)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig



