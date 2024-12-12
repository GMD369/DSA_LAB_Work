import matplotlib.pyplot as plt  
import pandas as pd 

# BAR CHART
def barChartForDistance():
    df = pd.read_csv('dailyActivity_merged.csv' )
    print(df.dtypes)

    list1 = df['TotalDistance'].values.tolist()
    list2 = df['ActivityDate'].values.tolist()
    plt.bar(list1,list2)
    plt.show()

# LINE CHART
def lineChart():
    df = pd.read_csv('dailyActivity_merged.csv' )
    print(df.dtypes)
    list1 = df['TotalSteps'].values.tolist()
    list2 = df['ActivityDate'].values.tolist()
    plt.plot(list1,list2)
    plt.show()
      
# PIE CHART
def pieChart():
     df = pd.read_csv('hourlySteps_merged.csv')

# Convert 'ActivityHour' to a datetime object
     df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])

# Filter for the specific date - 12th April 2016
     df_filtered = df[df['ActivityHour'].dt.date == pd.to_datetime('4/12/2016').date()]

# Extract hour from the 'ActivityHour' column
     df_filtered['Hour'] = df_filtered['ActivityHour'].dt.hour

# Group by hour and sum the 'StepTotal'
     steps_per_hour = df_filtered.groupby('Hour')['StepTotal'].sum()

# Create a pie chart
     plt.pie(steps_per_hour, labels=steps_per_hour.index, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
     plt.axis('equal')
     plt.title('Hourly Steps on 12th April 2016')
     plt.show()     

# SCATTER CHART
def scatterChart():
     df = pd.read_csv('sleepDay_merged.csv' )
     print(df.dtypes)

     list1 = df['TotalTimeInBed'].values.tolist()
     list2 = df['SleepDay'].values.tolist()
     plt.scatter(list1,list2)
     plt.show() 

pieChart()
lineChart()
scatterChart()
barChartForDistance()