#!/usr/bin/env python 
# created by Regina Citra Pesela (reginapasela@gmail.com)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 parse_dates = ['date'],
                 index_col = ['date'])

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot        
    fig = plt.figure(figsize = (15,5))

    plt.xlabel('Date',
               fontsize = 13)

    plt.ylabel('Page Views',
               fontsize = 13)

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
              fontsize = 15)

    plt.plot(df.index,
             df['value'],
             color = 'Red')

    # I had to add facecolor and transparent properties
    # because frameon is not supported on matplotlib >3.3
    # source: https://stackoverflow.com/questions/59204749/matplotlib-savefig-background-always-transparent
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png',
                facecolor = 'white',
                transparent = False)
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    
    # create year and month columns by extracting from index
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # group the data means by year and month
    df_bar = df_bar.groupby(['year','month']).mean()

    # creating year variable for bar plot
    years = df_bar.index.get_level_values(0).unique()

    # creating month variable for bar plot
    january, february, march, april, may, june, july, august, september, october, november, december = [list() for i in range(12)]

    for i in years:
        try: january.append(df_bar.loc[i, 1]['value'])     
        except: january.append(0)

        try: february.append(df_bar.loc[i, 2]['value'])     
        except: february.append(0)

        try: march.append(df_bar.loc[i, 3]['value'])     
        except: march.append(0)

        try: april.append(df_bar.loc[i, 4]['value'])     
        except: april.append(0)

        try: may.append(df_bar.loc[i, 5]['value'])     
        except: may.append(0)

        try: june.append(df_bar.loc[i, 6]['value'])     
        except: june.append(0)

        try: july.append(df_bar.loc[i, 7]['value'])     
        except: july.append(0)

        try: august.append(df_bar.loc[i, 8]['value'])     
        except: august.append(0)

        try: september.append(df_bar.loc[i, 9]['value'])     
        except: september.append(0)

        try: october.append(df_bar.loc[i, 10]['value'])     
        except: october.append(0)

        try: november.append(df_bar.loc[i, 11]['value'])     
        except: november.append(0)

        try: december.append(df_bar.loc[i, 12]['value'])     
        except: december.append(0)
    
    # Draw bar plot
    fig = plt.figure(figsize=(7,7))

    # set bar width
    bar_width = .04

    # set bar x position for each months
    bar1 = [float(i) for i in range(len(years))]
    bar2 = [i + bar_width for i in bar1]
    bar3 = [i + bar_width for i in bar2]
    bar4 = [i + bar_width for i in bar3]
    bar5 = [i + bar_width for i in bar4]
    bar6 = [i + bar_width for i in bar5]
    bar7 = [i + bar_width for i in bar6]
    bar8 = [i + bar_width for i in bar7]
    bar9 = [i + bar_width for i in bar8]
    bar10 = [i + bar_width for i in bar9]
    bar11 = [i + bar_width for i in bar10]
    bar12 = [i + bar_width for i in bar11]

    # draw bar for each months
    plt.bar(bar1, january, bar_width, label = 'January')
    plt.bar(bar2, february, bar_width, label = 'February')
    plt.bar(bar3, march, bar_width, label = 'March')
    plt.bar(bar4, april, bar_width, label = 'April')
    plt.bar(bar5, may, bar_width, label = 'May')
    plt.bar(bar6, june, bar_width, label = 'June')
    plt.bar(bar7, july, bar_width, label = 'July')
    plt.bar(bar8, august, bar_width, label = 'August')
    plt.bar(bar9, september, bar_width, label = 'September')
    plt.bar(bar10, october, bar_width, label = 'October')
    plt.bar(bar11, november, bar_width, label = 'November')
    plt.bar(bar12, december, bar_width, label = 'December')

    # setting x ticks label and set rotation to vertical
    plt.xticks(bar6, years, rotation = 'vertical')

    # plot properties
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title = 'Months')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png',
                facecolor = 'white',
                transparent = False)
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # set month_num column for easier month sorting
    df_box['month_num'] = [df_box['date'][mo].month for mo in range(len(df_box['date']))]

    # Draw box plots (using Seaborn)    
    fig = plt.figure(figsize = (24, 8))

    # set plot 1
    plt.subplot(1,2,1)

    # draw boxplot
    sns.boxplot(x = 'year', y = 'value', data = df_box,
                linewidth = 1,
                fliersize = 2)

    # plot properties
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')

    # set plot 2
    plt.subplot(1,2,2)

    # draw boxplot
    sns.boxplot(x = 'month', y = 'value', data = df_box.sort_values(by = 'month_num'),
                linewidth = 1,
                fliersize = 2)

    # plot properties
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png',
                facecolor = 'white',
                transparent = False)
    return fig