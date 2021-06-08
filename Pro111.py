import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import pandas as pd
import random

#For main data
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()
mean = st.mean(data)
population_mean = st.mean(data)


def random_set_of_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean_sample = st.mean(dataSet)
    return mean_sample    

mean_list = []

def setUp():
    for i in range(0,100):
        set_of_means =  random_set_of_mean(30)
        mean_list.append(set_of_means)
    showFig(mean_list)
mean = st.mean(mean_list)

def showFig(mean_list):
    df = mean_list
    fig  =ff.create_distplot([df],["Reading Time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17],mode="lines",name="mean"))
    fig.show() 

setUp()

std = st.stdev(mean_list)
print("Standard deviation of sample: ",std)

first_std_dev_start,first_std_dev_end = std-mean,std+mean
second_std_dev_start,second_std_dev_end = std-(2*mean),std+(2*mean)
third_std_dev_start,third_std_dev_end = std-(3*mean),std+(3*mean)

#to 

#get the correct  files
df = pd.read_csv("Math_score_IN1.csv")
data  = df["Math_score"].tolist()




 
