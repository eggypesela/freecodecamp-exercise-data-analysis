#!/usr/bin/env python 
# created by Regina Citra Pesela (reginapasela@gmail.com)

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10,5))

    # draw scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    # Create linear regression
    linout = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create array using linspace to year 2050
    x_fit = np.linspace(df['Year'].min(), 2050, 2051 - df['Year'].min())

    # Create y array by calculating slope * x-axis + intercept 
    y_fit = x_fit * linout[0] + linout[1]

    # Creating linear plot
    ax.plot(x_fit, y_fit)

    # Create second line of best fit
    # Filter linear regression from year 2000
    linout2 = linregress(df[df['Year']>= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])

    # Create array from 2000 to 2050 using linspace
    x2_fit = np.linspace(2000, 2050, 2051 - 2000)

    # Create y array by calculating slope * x-axis + intercept 
    y2_fit = x2_fit * linout2[0] + linout2[1]

    # Creating linear plot
    ax.plot(x2_fit, y2_fit)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png',
                facecolor = 'white',
                transparent = False)
                
    return plt.gca()