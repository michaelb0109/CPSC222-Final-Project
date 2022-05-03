import pandas as pd
import matplotlib.pyplot as plt

def bar_chart(x_ser, y_ser):
    plt.figure() # to create a new "current" figure
    plt.bar(x_ser, y_ser)
    plt.xticks()
original_data = pd.read_csv("HealthAutoExport Data 2.csv")
# print(original_data)

health_df = original_data.rename(columns = {'Step Count (count)': 'Steps', 'Flights Climbed (count)': 'FC', 'Walking + Running Distance (mi)': "Distance", 'Walking Asymmetry Percentage (%)': 'Asymmetry', 'Walking Double Support Percentage (%)': 'WDS', 'Walking Speed (mi/hr)': 'Speed', 'Walking Step Length (in) ': 'Step Length'})
#print(health_df)

