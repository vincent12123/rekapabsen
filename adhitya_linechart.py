import pandas as pd
import matplotlib.pyplot as plt

# load data from csv file
df = pd.read_csv('rekap.csv')

# create a list of unique names in the data
names = df['Nama'].unique()

# create a line chart for each name
for name in names:
    # filter the data for the current name
    name_data = df[df['Nama'] == name].drop('Nama', axis=1)
    
    # convert the date columns to datetime format
    name_data = name_data.apply(pd.to_datetime, format='%m/%d/%Y')
    
    # set the index of the dataframe to be the date columns
    name_data = name_data.set_index(name_data.columns)
    
    # plot the data as a line chart
    ax = name_data.T.plot.line(title=name)
    ax.set_xlabel('Date')
    ax.set_ylabel('Attendance')
    plt.show()
