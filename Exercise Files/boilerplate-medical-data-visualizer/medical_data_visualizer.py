import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'BMI' column
# BMI = weight (kg) / [height (m) ** 2]
df['BMI'] = df['weight'] / ((df['height']/100) ** 2)

# Add 'overweight' column
# 1 if BMI > 25 otherwise 0
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)
df.drop(['BMI'], axis = 1, inplace = True)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# Change the value of cholesterol to 0 if (cholesterol = 1) else 1
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)

# Change the value of cholesterol to 0 if (cholesterol = 1) else 1
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df.melt(id_vars = 'cardio', value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']).sort_values(by = ['variable'])   

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = 'variable', kind = 'count', hue = 'value', data = df_cat, col = 'cardio').set(xlabel = 'variable', ylabel = 'total').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(20, 10))

    # Draw the heatmap with 'sns.heatmap()'

    ax = sns.heatmap(corr,
                     annot = True,
                     linewidths = 0.5,
                     mask = mask,
                     square = True,
                     center = 0,
                     vmax = 0.24,
                     vmin = -0.08,
                     fmt='.1f',
                     cbar_kws={
                               'shrink': .45,
                               'format': '%.2f'
                              })

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig