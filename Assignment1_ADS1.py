# PYTHON PACKAGES

import pandas as pd
import matplotlib.pyplot as plt

# TO READ DATASET

import pandas as pd
import matplotlib.pyplot as plt

Df=pd.read_csv("southern_hemisphere.annual.csv")

df = Df[['Time', 'Realization 1', 'Realization 2','Realization 3','Realization 4']].copy()
df.head()

# TO CREATE LINE_PLOT

def line_plot(data):
    
    x_values = data.iloc[:, 0]
    y_values_list = [data.iloc[:, i] for i in range(1, data.shape[1])]
    labels = data.columns[1:]
    plt.figure(figsize=(8,6))

    for i in range(len(y_values_list)):
        plt.plot(x_values, y_values_list[i], label=labels[i])
    plt.title("Time vs Realization")
    plt.xlabel("Time")
    plt.ylabel("Realization")
    plt.legend()
    plt.grid(True)
    plt.show()
        
line_plot(df)


#TO CREATE SCATTER_PLOT

def scatter_plot(data):
    
    x_values = data.iloc[:, 0]
    y_values_list = [data.iloc[:, i] for i in range(1, data.shape[1])]
    labels = data.columns[1:]
    plt.figure(figsize=(8,6))

    
    for i in range(len(y_values_list)-1):
        plt.scatter( y_values_list[i],y_values_list[i+1],label=labels[i+1])
    plt.title("Realization 1 vs other Realizations")
    plt.xlabel("Realization 1")
    plt.ylabel("Realizations")
    plt.legend()
    plt.grid(True)
    plt.show()
    
scatter_plot(df)


# TO CREATE HISTOGRAM

def hist_plot(data):
    
    x_values = data.iloc[:, 0]
    y_values_list = [data.iloc[:, i] for i in range(1, data.shape[1])]
    labels = data.columns[1:]
    plt.figure(figsize=(8,6))
    
    for i in range(len(y_values_list)):
        plt.hist( y_values_list[i], label=labels[i])
    plt.title("Frequency distubution of Tempurature Realizations")
    plt.xlabel("Realization")
    plt.ylabel("Count")
    plt.legend()
    plt.grid(True)
    plt.show()
    
hist_plot(df)