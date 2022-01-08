import statistics
import pandas as pd
import plotly_express as px
import csv
import plotly.figure_factory as pff
import random
import plotly.graph_objects as go

df = pd.read_csv(r"C:\Users\rajuv\Desktop\python practice\sampledistributiondataset.csv")
data = df["Math_score"].tolist()
fig = pff.create_distplot([data],["math score"],show_hist = False)
#fig.show()
mean = statistics.mean(data)
print(mean)
standard_deviation = statistics.stdev(data)
print(standard_deviation)

#making random values
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    print(mean)

#ploting graph for mean for dataset
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = pff.create_distplot([df],["Math_score"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "MEAN"))
    fig.show()

## Pass the number of time you want the mean of the data points as a parameter in range function in for loop

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)
    show_fig(mean_list)
    
mean = statistics.mean(mean_list)
print("Mean of sampling distribution :-",mean )




#Code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)


# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()
