import streamlit as st
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from matplotlib import style

# styling the outputs
font = {'family': 'sans-serif',
        'weight': 'bold',
        'size': 18}
plt.rc('font', **font)
style.use('fivethirtyeight')

st.set_page_config(
    page_title := "Data Analytics Project",
    page_icon="🗿"
)

# title of project
st.title("Data Analytics Project")
st.sidebar.success("Select something")
st.write("Welcome, In this project we are focusing on visualization and comparison of the Ladder score and its score components on India in Asia and its surrounding neighbors. It will be followed by visualization providing insights of the world's happiness.")

# Load the dataset 
df = pd.read_csv("report_till_2021.csv")
df


st.write("India from 2006 to 2020")

India = df[df['Country name'] == 'India']

India

st.set_option('deprecation.showPyplotGlobalUse', False)

plt.figure(figsize=(20, 7))
sns.lineplot(data=India, x="year", y="Life Ladder", marker='o')
plt.title("Life Ladder")
st.pyplot()

st.write("There are certain peaks with regards to India's ladder score as seen in the years 2008, 2010, 2012 and 2020. There are also certain drops as seen in the years 2007, 2009, 2011 and an overall low in 2019. A continouse decrease can be seen from 2012 to 2019. The overall trend for the ladder score is decreasing.")

plt.figure(figsize=(20, 7))
sns.lineplot(data=India, x="year", y="Log GDP per capita", marker='o')
plt.title("Log GDP per capita")
st.pyplot()

st.write("India's GDP is on an increasing trend over the years, with the exception of 2020.")

plt.figure(figsize=(20, 7))
sns.lineplot(data=India, x="year", y="Social support", marker='o')
plt.title("Social support")
st.pyplot()

st.write("There are some distinct lows in 2007, 2012 and 2019, 2012 being the lowest and some distinct highs in 2008, 2014 and 2018. India's social support is on a decreasing trend over the years.")

plt.figure(figsize=(20, 7))
sns.lineplot(data=India, x="year",
             y="Healthy life expectancy at birth", marker='o')
plt.title("Healthy life expectancy at birth")
st.pyplot()

st.write("An increasing trend over the years.")

plt.figure(figsize=(20, 7))
sns.lineplot(data=India, x="year",
             y="Freedom to make life choices", marker='o')
plt.title("Freedom to make life choices")
st.pyplot()

st.write("There's a slight increasing trend, but there are distincts drops as seen in years 2008, 2012, 2015 and 2019. With an all time low in year 2012.There are certain peaks with regards to India's Freedom to make life choices as seen in the years 2011, 2014, 2017 and 2020.")

plt.figure(figsize=(20, 7))
sns.lineplot(data=India, x="year", y="Generosity", marker='o')
plt.title("Generosity")
st.pyplot()

st.write("Generosity amongst Indians have increased over time, with spikes in 2010, 2013, 2016 and 2019 and an all time low in 2008")

plt.figure(figsize=(20, 7))
sns.lineplot(data=India, x="year", y="Perceptions of corruption", marker='o')
plt.title("Perceptions of corruption")
st.pyplot()

st.write("There were peaks in 2011, 2014 and 2018, and the perception of corruption has decreased over the years.")

st.subheader("India in Asia")

world = pd.read_csv("report_only_2021.csv")

world

plt.figure(figsize=(35, 10))
sns.barplot(data=world, x="Country name", y="Ladder score")
plt.xticks(rotation=90)
st.pyplot()

Southeast_Asia = world[world['Regional indicator'] == 'Southeast Asia']

South_Asia = world[world['Regional indicator'] == 'South Asia']

East_Asia = world[world['Regional indicator'] == 'East Asia']

plt.figure(figsize=(16, 8))
plt.xticks(rotation=90)
sns.lineplot(x="Country name", y="Ladder score",
             data=Southeast_Asia, marker='o', label='Southeast_Asia')
sns.lineplot(x="Country name", y="Ladder score",
             data=South_Asia, marker='o', label='South_Asia')
sns.lineplot(x="Country name", y="Ladder score",
             data=East_Asia, marker='o', label='East_Asia')
st.pyplot()

st.write("Among asian countries, India ranks 2nd last in the happiness index. In a world context, India ranks 139th, far below average.")

plt.figure(figsize=(16, 8))
plt.xticks(rotation=90)
sns.lineplot(x="Country name", y="Healthy life expectancy",
             data=Southeast_Asia, marker='o', label='Southeast_Asia')
sns.lineplot(x="Country name", y="Healthy life expectancy",
             data=South_Asia, marker='o', label='South_Asia')
sns.lineplot(x="Country name", y="Healthy life expectancy",
             data=East_Asia, marker='o', label='East_Asia')
st.pyplot()

st.write("Among asian countries, India ranks 5th from the last in Healthy life expectancy scores. In a world context, India ranks 103th.")

plt.figure(figsize=(16, 8))
plt.xticks(rotation=90)
sns.lineplot(x="Country name", y="Logged GDP per capita",
             data=Southeast_Asia, marker='o', label='Southeast_Asia')
sns.lineplot(x="Country name", y="Logged GDP per capita",
             data=South_Asia, marker='o', label='South_Asia')
sns.lineplot(x="Country name", y="Logged GDP per capita",
             data=East_Asia, marker='o', label='East_Asia')
st.pyplot()

st.write("Among asian countries, India ranks 16th in Log GDP per Capita scores. In a world context, India ranks 106th.")

plt.figure(figsize=(16, 8))
plt.xticks(rotation=90)
sns.lineplot(x="Country name", y="Social support",
             data=Southeast_Asia, marker='o', label='Southeast_Asia')
sns.lineplot(x="Country name", y="Social support",
             data=South_Asia, marker='o', label='South_Asia')
sns.lineplot(x="Country name", y="Social support",
             data=East_Asia, marker='o', label='East_Asia')
st.pyplot()

st.write("Among asian countries, India ranks 2nd last in Social support scores. In a world context, India ranks 141th")

plt.figure(figsize=(16, 8))
plt.xticks(rotation=90)
sns.lineplot(x="Country name", y="Freedom to make life choices",
             data=Southeast_Asia, marker='o', label='Southeast_Asia')
sns.lineplot(x="Country name", y="Freedom to make life choices",
             data=South_Asia, marker='o', label='South_Asia')
sns.lineplot(x="Country name", y="Freedom to make life choices",
             data=East_Asia, marker='o', label='East_Asia')
st.pyplot()

st.write("Among asian countries, India ranks 7st in Freedom to make life choices scores. In a world context, India ranks 31st.")

plt.figure(figsize=(16, 8))
plt.xticks(rotation=90)
sns.lineplot(x="Country name", y="Perceptions of corruption",
             data=Southeast_Asia, marker='o', label='Southeast_Asia')
sns.lineplot(x="Country name", y="Perceptions of corruption",
             data=South_Asia, marker='o', label='South_Asia')
sns.lineplot(x="Country name", y="Perceptions of corruption",
             data=East_Asia, marker='o', label='East_Asia')
st.pyplot()

st.write("Among asian countries, India ranks 11th in Perceptions of corruption scores. In a world context, India ranks 78th.")

st.subheader("India and its neighbourhood in 2021")

df_2021 = world[(world["Country name"] == "Bhutan") | (world["Country name"] == "China") | (world["Country name"] == 'Nepal') | (world["Country name"] == 'Afghanistan') | (
    world["Country name"] == 'India') | (world["Country name"] == 'Pakistan') | (world["Country name"] == 'Bangladesh') | (world["Country name"] == 'Myanmar')]

df_2021

st.write("Ladder score")

plt.figure(figsize=(20, 7))
sns.lineplot(data=df_2021, x="Country name", y="Ladder score", marker='o')
st.pyplot()

st.write("Among neighbouring countries, India ranks 2nd last in the Ladder score.")

st.write("Logged GDP per capita")

plt.figure(figsize=(20, 7))
sns.lineplot(data=df_2021, x="Country name",
             y="Logged GDP per capita", marker='o')
st.pyplot()

st.write("Among neighbouring countries, India ranks 2nd in the GDP per capita.")

st.write("Social support")

plt.figure(figsize=(20, 7))
sns.lineplot(data=df_2021, x="Country name", y="Social support", marker='o')
st.pyplot()

st.write("Among neighbouring countries, India ranks 2nd in the Social support.")

st.write("Healthy life expectancy")

plt.figure(figsize=(20, 7))
sns.lineplot(data=df_2021, x="Country name",
             y="Healthy life expectancy", marker='o')
st.pyplot()

st.write("Among neighbouring countries, India ranks 4th in the Healthy life expectancy.")

st.write("Freedom to make life choices")

plt.figure(figsize=(20, 7))
sns.lineplot(data=df_2021, x="Country name",
             y="Freedom to make life choices", marker='o')
st.pyplot()

st.write("Among neighbouring countries, India ranks 2nd in the Freedom to make life choices.")

st.write("Generosity")

plt.figure(figsize=(20, 7))
sns.lineplot(data=df_2021, x="Country name", y="Generosity", marker='o')
st.pyplot()

st.write("Among neighbouring countries, India ranks 4nd in Generosity.")
