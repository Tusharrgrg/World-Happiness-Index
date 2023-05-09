import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from matplotlib import style
#styling the outputs
font={'family':'sans-serif',
      'weight':'bold',
      'size':18}
plt.rc('font',**font)
style.use('fivethirtyeight')

st.set_page_config(
    page_title:="Data Analytics Project",
    page_icon="🗿"
)

df=pd.read_csv("world-happiness-report.csv")
data = pd.read_csv("report_till_2021.csv")
df.isna().sum()
per=data.isna().sum()/len(df)*100
# per

data["Social support"]=data["Social support"].fillna(data["Social support"].mean())
data["Healthy life expectancy at birth"]=data["Healthy life expectancy at birth"].fillna(data["Healthy life expectancy at birth"].mean())
data["Freedom to make life choices"]=data["Freedom to make life choices"].fillna(data["Freedom to make life choices"].mean())
data["Generosity"]=data["Generosity"].fillna(data["Generosity"].mean())
data["Perceptions of corruption"]=data["Perceptions of corruption"].fillna(data["Perceptions of corruption"].mean())
data["Log GDP per capita"]=data["Log GDP per capita"].fillna(data["Log GDP per capita"].mean())

India=data[data['Country name']=='India']
India = India.sort_values('year');
world=pd.read_csv("world-happiness-report-2021.csv")

    
Southeast_Asia=world[world['Regional indicator']== 'Southeast Asia']
South_Asia=world[world['Regional indicator']== 'South Asia']
East_Asia=world[world['Regional indicator']== 'East Asia']


st.set_option('deprecation.showPyplotGlobalUse', False)

with st.sidebar:
    st.title('World Happiness Index')
    pages = ['Home', 
             'DataSet', 
             'Analysis Indian Trends',  
             'India and Asian countries', 
             'World Analysis',
             'Best Every Year'
             ]
    page = st.radio('Navigation', pages)

# Create main panel
main_panel = st.container()
with main_panel:
        
        if page == 'Home':

            st.title(' **Data Analytics and Visualization Project** ')
            st.write("Welcome, In this project we are focusing on visualization and comparison of the Ladder score and its score components on India in Asia and its surrounding neighbors. It will be followed by visualization providing insights of the world's happiness.")
            # st.title("Group Members")
            # st.write("Dev Juneja - 202011020")
            # st.write("Ajay Kumbhar - 2020110")
            # st.write("Tushar Agrawal - 202011074")
            # st.write("Karan Hadiyal - 2020110")
            # st.write("Tharun kampathi - 2020110")

            fig = px.choropleth(data.sort_values("year"),
                locations = "Country name",
                color = "Life Ladder",
                locationmode = "country names",
                animation_frame = "year")
            fig.update_layout(title="World Happiness Index Analysis")
            st.plotly_chart(fig)



        elif page == 'DataSet':
            st.title("Key Features in Our Dataset")    
            st.write("- Life Ladder: Imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. The top of the ladder represents the best possible life for you and the bottom of the ladder represents the worst possible life for you.")
            st.write("- Log GDP per capita: At its most basic interpretation, per capita GDP shows how much economic production value can be attributed to each individual citizen. Alternatively, this translates to a measure of national wealth since GDP market value per person also readily serves as a prosperity measure.")
            st.write("- Social support: Social support is defined in terms of social network characteristics such as assistance from family, friends, neighbours and other community members.")
            st.write("- Generosity: Generosity is the virtue of being liberal in giving, often as gifts.")
            st.write("- Perceptions of corruption: Corruption is a form of dishonesty or criminal offense undertaken by a person or organization entrusted with a position of authority, to acquire illicit benefit")
            st.write("- Freedom to make life choices: Freedom of choice describes an individual's opportunity and autonomy to perform an action selected from at least two available options, unconstrained by external parties.")
            st.header('There are 11 columns in the dataset')
            
            st.write('Country name ,Year ,Life Ladder ,Log GDP per capita ,Social support ,Healthy life expectancy at birth ,Freedom to make life choices,Generosity ,Perceptions of corruption ,Positive affect ,Negative affect.')
            df

            st.write("")
            st.write("")
            st.write("")
            st.write("This dataframe contains data of india between 2006 to 2021.")
            st.dataframe(India)


        elif page == 'Analysis Indian Trends':
            
            st.header("Indian Trends Over The Years")

            tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Ladder Score", "Log GDP per capita", 'Social support', 'Healthy life expectancy', 'Freedom of choice' , 'Generosity' , 'Perceptions of corruption'])


            with tab1:

                # pio.templates.default = "plotly_white"
                fig = px.line(India, x="year", y="Life Ladder", markers=True)
                fig.update_xaxes(range=[2005.9, 2021.4])
                fig.update_xaxes(dtick='M12')

                fig.update_layout(
                    title="India's ladder score over the years",
                    xaxis_title="Year",
                    yaxis_title="Life Ladder",
                    font=dict(size=24, color="black"),
                )

                st.plotly_chart(fig,theme='streamlit', use_container_width=True)
                st.write("India's Life Ladder score has fluctuated over the past 15 years, with certain peaks and drops. There are certain peaks with regards to India's ladder score as seen in the years 2008, 2010, 2012, and 2020. And there are also certain drops as seen in the years 2007, 2009, 2011, and an overall low in 2019. Also, there is an overall decreasing trend in the Life Ladder score from 2012 to 2019.")
                st.write("The overall trend for the ladder score is decreasing.")


            with tab2:

                fig = px.line(India, x="year", y="Log GDP per capita", markers=True)
                fig.update_xaxes(range=[2005.9, 2021.1])
                fig.update_xaxes(dtick='M12')

                fig.update_layout(
                    title="India's Log GDP per capita over the years",
                    xaxis_title="Year",
                    yaxis_title="Log GDP per capita",
                    font=dict(size=24, color="black"),
                )

                st.plotly_chart(fig,theme='streamlit', use_container_width=True)
                st.write("India's Log GDP per capita has been increasing over the years from 2006 to 2020, with the exception of a dip in 2020.")
                st.write("Here are few posible observations:")
                st.write("As the Log GDP per capita increases, people's standard of living improves and they are more likely to experience greater happiness and satisfaction with their lives.")
                st.write("The dip in GDP in 2020 could have significant implications for happiness and well-being in India. The COVID-19 pandemic has had a major impact on economies around the world, including in India. ")


            with tab3:

                fig = px.line(India, x="year", y="Social support", markers=True)
                fig.update_xaxes(range=[2005.9, 2021.1])
                fig.update_xaxes(dtick='M12')

                fig.update_layout(
                    title="India's Social support over the years",
                    xaxis_title="Year",
                    yaxis_title="Social support",
                    font=dict(size=24, color="black"),
                )

                st.plotly_chart(fig,theme='streamlit', use_container_width=True)
                st.write("it appears that India's Social support has been decreasing over the years from 2006 to 2020, with some distinct lows in 2007, 2012, and 2019, and some distinct highs in 2008, 2014, and 2018.")

            with tab4:

                fig = px.line(India, x="year", y="Healthy life expectancy at birth", markers=True)
                fig.update_xaxes(range=[2005.9, 2021.1])
                fig.update_xaxes(dtick='M12')

                fig.update_layout(
                    title="India's Healthy life expectancy at birth over the years",
                    xaxis_title="Year",
                    yaxis_title="Healthy life expectancy at birth",
                    font=dict(size=24, color="black"),
                )

                st.plotly_chart(fig,theme='streamlit', use_container_width=True)
                st.write("- India's Healthy life expectancy at birth has been increasing over the years from 2006 to 2020.")
                st.write("- The increasing trend in healthy life expectancy is a positive sign for overall happiness and well-being in India. Longer and healthier lives can contribute to greater life satisfaction and fulfillment, and can also provide more opportunities for personal and social growth.")

            with tab5:

                fig = px.line(India, x="year", y="Freedom to make life choices", markers=True)
                fig.update_xaxes(range=[2005.9, 2021.1])
                fig.update_xaxes(dtick='M12')

                fig.update_layout(
                    title="India's Freedom to make life choices over the years",
                    xaxis_title="Year",
                    yaxis_title="Freedom to make life choices",
                    font=dict(size=24, color="black"),
                )

                st.plotly_chart(fig,theme='streamlit', use_container_width=True)
                st.write("- There's a slight increasing trend, but there are distincts drops as seen in years 2008, 2012, 2015 and 2019. With an all time low in year 2012.There are certain peaks with regards to India's Freedom to make life choices as seen in the years 2011, 2014, 2017 and 2020.")
                st.write("- The trend in Freedom to make life choices is an important factor to consider when assessing the overall happiness and well-being of a population. As people are better able to make choices that align with their values and goals, they are likely to experience greater life satisfaction and fulfillment.")
            
            with tab6:

                fig = px.line(India, x="year", y="Generosity", markers=True)
                fig.update_xaxes(range=[2005.9, 2021.1])
                fig.update_xaxes(dtick='M12')

                fig.update_layout(
                    title="India's Generosity over the years",
                    xaxis_title="Year",
                    yaxis_title="Generosity",
                    font=dict(size=24, color="black"),
                )

                st.plotly_chart(fig,theme='streamlit', use_container_width=True)
                st.write("- Generosity amongst Indians have increased over time, with spikes in 2010, 2013, 2016 and 2019 and an all time low in 2008")

            with tab7:

                fig = px.line(India, x="year", y="Perceptions of corruption", markers=True)
                fig.update_xaxes(range=[2005.9, 2021.1])
                fig.update_xaxes(dtick='M12')

                fig.update_layout(
                    title="India's Perceptions of corruption over the years",
                    xaxis_title="Year",
                    yaxis_title="Perceptions of corruption",
                    font=dict(size=24, color="black"),
                )

                st.plotly_chart(fig,theme='streamlit', use_container_width=True)
                st.write("- The plot shows that there were peaks in the years 2011, 2014, and 2018, indicating that the perception of corruption was high during those years. However, the overall trend shows that the perception of corruption has decreased over the years.")




    #         cols = India[['Life Ladder', 'Log GDP per capita','Social support', 'Healthy life expectancy at birth',
    #    'Freedom to make life choices', 'Generosity',
    #    'Perceptions of corruption']]

    #         plt.figure(figsize=(20, 8))
    #         sns.heatmap(cols.corr(), annot = True, cmap='RdYlGn_r', mask=np.triu(np.ones_like(cols.corr())));
    #         plt.title('Correlations between factors', fontsize=24, fontweight='bold', pad=20);
    #         st.pyplot()
    #         st.write("- Freedom to make life choices and healthy life expectancy are highly correlated to logged GDP per capita.")
    #         st.write("- It is not surprising that there is a correlation between GDP per capita and healthy life expectancy, as it could be linked to things such as better healthcare infrastructure and better systems to improve quality of life like water cleanliness, etc.")

            # print(cols.corr())
            # y = ['Life Ladder' , 'Social support','Healthy life expectancy at birth']

            # fig = px.line(India, x="year", y=y, color="Country name",
            #   line_group="Country name", hover_name="Country name",
            #   animation_frame="year")
            # fig.update_layout(title='Life Ladder by Country over Time',
            #                 xaxis_title='Year', yaxis_title='Life Ladder')
            # st.plotly_chart(fig)
                    

          
        
        elif page == 'India and Asian countries':
            st.subheader("India in Asia")
            plt.figure(figsize=(35,10))
            sns.barplot(data=world,x="Country name",y="Ladder score")
            plt.xticks(rotation=90) 
            st.pyplot()

        
            plt.figure(figsize = (16,8))
            plt.xticks(rotation=90)
            sns.lineplot(x="Country name", y = "Ladder score", data = Southeast_Asia,marker='o',label='Southeast_Asia')
            sns.lineplot(x="Country name", y = "Ladder score", data = South_Asia,marker='o',label='South_Asia')
            sns.lineplot(x="Country name", y = "Ladder score", data = East_Asia,marker='o',label='East_Asia')
            st.pyplot()
            st.write("Among asian countries, India ranks 2nd last in the happiness index. In a world context, India ranks 139th, far below average.")

            plt.figure(figsize = (16,8))
            plt.xticks(rotation=90)
            sns.lineplot(x="Country name", y = "Healthy life expectancy", data = Southeast_Asia,marker='o',label='Southeast_Asia')
            sns.lineplot(x="Country name", y = "Healthy life expectancy", data = South_Asia,marker='o',label='South_Asia')
            sns.lineplot(x="Country name", y = "Healthy life expectancy", data = East_Asia,marker='o',label='East_Asia')
            st.pyplot()

            st.write("Among asian countries, India ranks 5th from the last in Healthy life expectancy scores. In a world context, India ranks 103th.")

            plt.figure(figsize = (16,8))
            plt.xticks(rotation=90)
            sns.lineplot(x="Country name", y = "Logged GDP per capita", data = Southeast_Asia,marker='o',label='Southeast_Asia')
            sns.lineplot(x="Country name", y = "Logged GDP per capita", data = South_Asia,marker='o',label='South_Asia')
            sns.lineplot(x="Country name", y = "Logged GDP per capita", data = East_Asia,marker='o',label='East_Asia')
            st.pyplot()

            st.write("Among asian countries, India ranks 16th in Log GDP per Capita scores. In a world context, India ranks 106th.")

            plt.figure(figsize = (16,8))
            plt.xticks(rotation=90)
            sns.lineplot(x="Country name", y = "Social support", data = Southeast_Asia,marker='o',label='Southeast_Asia')
            sns.lineplot(x="Country name", y = "Social support", data = South_Asia,marker='o',label='South_Asia')
            sns.lineplot(x="Country name", y = "Social support", data = East_Asia,marker='o',label='East_Asia')
            st.pyplot()

            st.write("Among asian countries, India ranks 2nd last in Social support scores. In a world context, India ranks 141th")

            plt.figure(figsize = (16,8))
            plt.xticks(rotation=90)
            sns.lineplot(x="Country name", y = "Freedom to make life choices", data = Southeast_Asia,marker='o',label='Southeast_Asia')
            sns.lineplot(x="Country name", y = "Freedom to make life choices", data = South_Asia,marker='o',label='South_Asia')
            sns.lineplot(x="Country name", y = "Freedom to make life choices", data = East_Asia,marker='o',label='East_Asia')
            st.pyplot()

            st.write("Among asian countries, India ranks 7st in Freedom to make life choices scores. In a world context, India ranks 31st.")

            plt.figure(figsize = (16,8))
            plt.xticks(rotation=90)
            sns.lineplot(x="Country name", y = "Perceptions of corruption", data = Southeast_Asia,marker='o',label='Southeast_Asia')
            sns.lineplot(x="Country name", y = "Perceptions of corruption", data = South_Asia,marker='o',label='South_Asia')
            sns.lineplot(x="Country name", y = "Perceptions of corruption", data = East_Asia,marker='o',label='East_Asia')
            st.pyplot()

            st.write("Among asian countries, India ranks 11th in Perceptions of corruption scores. In a world context, India ranks 78th.")

            st.subheader("India and its neighbourhood in 2021")

            df_2021 = world[(world["Country name"]=="Bhutan") |(world["Country name"]=="China")|(world["Country name"]=='Nepal') |(world["Country name"]=='Afghanistan')|(world["Country name"]=='India')|(world["Country name"]=='Pakistan')|(world["Country name"]=='Bangladesh')|(world["Country name"]=='Myanmar')]

            df_2021

            st.write("Ladder score")

            plt.figure(figsize=(20,7))
            sns.lineplot(data=df_2021,x="Country name",y="Ladder score",marker='o')
            st.pyplot()

            st.write("Among neighbouring countries, India ranks 2nd last in the Ladder score.")

            st.write("Logged GDP per capita")

            plt.figure(figsize=(20,7))
            sns.lineplot(data=df_2021,x="Country name",y="Logged GDP per capita",marker='o')
            st.pyplot()

            st.write("Among neighbouring countries, India ranks 2nd in the GDP per capita.")

            st.write("Social support")

            plt.figure(figsize=(20,7))
            sns.lineplot(data=df_2021,x="Country name",y="Social support",marker='o')
            st.pyplot()

            st.write("Among neighbouring countries, India ranks 2nd in the Social support.")

            st.write("Healthy life expectancy")

            plt.figure(figsize=(20,7))
            sns.lineplot(data=df_2021,x="Country name",y="Healthy life expectancy",marker='o')
            st.pyplot()

            st.write("Among neighbouring countries, India ranks 4th in the Healthy life expectancy.")

            st.write("Freedom to make life choices")

            plt.figure(figsize=(20,7))
            sns.lineplot(data=df_2021,x="Country name",y="Freedom to make life choices",marker='o')
            st.pyplot()

            st.write("Among neighbouring countries, India ranks 2nd in the Freedom to make life choices.")

            st.write("Generosity")

            plt.figure(figsize=(20,7))
            sns.lineplot(data=df_2021,x="Country name",y="Generosity",marker='o')
            st.pyplot()

            st.write("Among neighbouring countries, India ranks 4nd in Generosity.")

        elif page == 'World Analysis':
            st.header("World")

            import pycountry_convert as pc

            df2 = world.set_index('Country name')
            temp = pd.DataFrame(df2['Ladder score']).reset_index()

            #ADAPTING TO THE ISO 3166 STANDARD
            temp.loc[temp['Country name'] == 'Taiwan Province of China', 'Country name'] = 'Taiwan, Province of China' 
            temp.loc[temp['Country name'] == 'Hong Kong S.A.R. of China', 'Country name'] = 'Hong Kong' 
            temp.loc[temp['Country name'] == 'Congo (Brazzaville)','Country name'] = 'Congo' 
            temp.loc[temp['Country name'] == 'Palestinian Territories','Country name'] = 'Palestine, State of' 

            temp.drop(index=temp[temp['Country name'] == 'Kosovo'].index, inplace=True) 
            temp.drop(index=temp[temp['Country name'] == 'North Cyprus'].index, inplace=True) 


            temp['iso_alpha'] = temp['Country name'].apply(lambda x:pc.country_name_to_country_alpha3(x,))
            fig = px.choropleth(temp, locations='iso_alpha',
                                color='Ladder score',
                                hover_name='Country name',
                                color_continuous_scale=px.colors.diverging.RdYlGn,
                            )
            fig.update_layout(
                title_text='World map - Ladder score',
                showlegend=False,
                paper_bgcolor='rgb(248, 248, 255)',
                geo_bgcolor='rgb(248, 248, 255)',
                geo_showframe=False,
                title_font_size=22,
            )
            st.plotly_chart(fig)

            temp = pd.DataFrame(df2['Logged GDP per capita']).reset_index()


            temp.loc[temp['Country name'] == 'Taiwan Province of China', 'Country name'] = 'Taiwan, Province of China' 
            temp.loc[temp['Country name'] == 'Hong Kong S.A.R. of China', 'Country name'] = 'Hong Kong' 
            temp.loc[temp['Country name'] == 'Congo (Brazzaville)','Country name'] = 'Congo' 
            temp.loc[temp['Country name'] == 'Palestinian Territories','Country name'] = 'Palestine, State of' 

            temp.drop(index=temp[temp['Country name'] == 'Kosovo'].index, inplace=True) 
            temp.drop(index=temp[temp['Country name'] == 'North Cyprus'].index, inplace=True) 


            temp['iso_alpha'] = temp['Country name'].apply(lambda x:pc.country_name_to_country_alpha3(x,))
            fig = px.choropleth(temp, locations='iso_alpha',
                                color='Logged GDP per capita',
                                hover_name='Country name',
                                color_continuous_scale=px.colors.diverging.RdYlGn,
                            )

            fig.update_layout(
                title_text='World map - Logged GDP per capita',
                showlegend=False,
                paper_bgcolor='rgb(248, 248, 255)',
                geo_bgcolor='rgb(248, 248, 255)',
                geo_showframe=False,
                title_font_size=22,
            )
            st.plotly_chart(fig)

            temp = pd.DataFrame(df2['Social support']).reset_index()


            temp.loc[temp['Country name'] == 'Taiwan Province of China', 'Country name'] = 'Taiwan, Province of China' 
            temp.loc[temp['Country name'] == 'Hong Kong S.A.R. of China', 'Country name'] = 'Hong Kong' 
            temp.loc[temp['Country name'] == 'Congo (Brazzaville)','Country name'] = 'Congo' 
            temp.loc[temp['Country name'] == 'Palestinian Territories','Country name'] = 'Palestine, State of' 

            temp.drop(index=temp[temp['Country name'] == 'Kosovo'].index, inplace=True) 
            temp.drop(index=temp[temp['Country name'] == 'North Cyprus'].index, inplace=True) 


            temp['iso_alpha'] = temp['Country name'].apply(lambda x:pc.country_name_to_country_alpha3(x,))
            fig = px.choropleth(temp, locations='iso_alpha',
                                color='Social support',
                                hover_name='Country name',
                                color_continuous_scale=px.colors.diverging.RdYlGn,
                            )

            fig.update_layout(
                title_text='World map - Social support',
                showlegend=False,
                paper_bgcolor='rgb(248, 248, 255)',
                geo_bgcolor='rgb(248, 248, 255)',
                geo_showframe=False,
                title_font_size=22,
            )
            st.plotly_chart(fig)

            temp = pd.DataFrame(df2['Healthy life expectancy']).reset_index()


            temp.loc[temp['Country name'] == 'Taiwan Province of China', 'Country name'] = 'Taiwan, Province of China' 
            temp.loc[temp['Country name'] == 'Hong Kong S.A.R. of China', 'Country name'] = 'Hong Kong' 
            temp.loc[temp['Country name'] == 'Congo (Brazzaville)','Country name'] = 'Congo' 
            temp.loc[temp['Country name'] == 'Palestinian Territories','Country name'] = 'Palestine, State of' 

            temp.drop(index=temp[temp['Country name'] == 'Kosovo'].index, inplace=True) 
            temp.drop(index=temp[temp['Country name'] == 'North Cyprus'].index, inplace=True) 


            temp['iso_alpha'] = temp['Country name'].apply(lambda x:pc.country_name_to_country_alpha3(x,))
            fig = px.choropleth(temp, locations='iso_alpha',
                                color='Healthy life expectancy',
                                hover_name='Country name',
                                color_continuous_scale=px.colors.diverging.RdYlGn,
                            )

            fig.update_layout(
                title_text='World map - Healthy life expectancy',
                showlegend=False,
                paper_bgcolor='rgb(248, 248, 255)',
                geo_bgcolor='rgb(248, 248, 255)',
                geo_showframe=False,
                title_font_size=22,
            )
            st.plotly_chart(fig)

            temp = pd.DataFrame(df2['Freedom to make life choices']).reset_index()


            temp.loc[temp['Country name'] == 'Taiwan Province of China', 'Country name'] = 'Taiwan, Province of China' 
            temp.loc[temp['Country name'] == 'Hong Kong S.A.R. of China', 'Country name'] = 'Hong Kong' 
            temp.loc[temp['Country name'] == 'Congo (Brazzaville)','Country name'] = 'Congo' 
            temp.loc[temp['Country name'] == 'Palestinian Territories','Country name'] = 'Palestine, State of' 

            temp.drop(index=temp[temp['Country name'] == 'Kosovo'].index, inplace=True) 
            temp.drop(index=temp[temp['Country name'] == 'North Cyprus'].index, inplace=True) 


            temp['iso_alpha'] = temp['Country name'].apply(lambda x:pc.country_name_to_country_alpha3(x,))
            fig = px.choropleth(temp, locations='iso_alpha',
                                color='Freedom to make life choices',
                                hover_name='Country name',
                                color_continuous_scale=px.colors.diverging.RdYlGn,
                            )

            fig.update_layout(
                title_text='World map - Freedom to make life choices',
                showlegend=False,
                paper_bgcolor='rgb(248, 248, 255)',
                geo_bgcolor='rgb(248, 248, 255)',
                geo_showframe=False,
                title_font_size=22,
            )
            st.plotly_chart(fig)

            temp = pd.DataFrame(df2['Perceptions of corruption']).reset_index()


            temp.loc[temp['Country name'] == 'Taiwan Province of China', 'Country name'] = 'Taiwan, Province of China' 
            temp.loc[temp['Country name'] == 'Hong Kong S.A.R. of China', 'Country name'] = 'Hong Kong' 
            temp.loc[temp['Country name'] == 'Congo (Brazzaville)','Country name'] = 'Congo' 
            temp.loc[temp['Country name'] == 'Palestinian Territories','Country name'] = 'Palestine, State of' 

            temp.drop(index=temp[temp['Country name'] == 'Kosovo'].index, inplace=True) 
            temp.drop(index=temp[temp['Country name'] == 'North Cyprus'].index, inplace=True) 


            temp['iso_alpha'] = temp['Country name'].apply(lambda x:pc.country_name_to_country_alpha3(x,))
            fig = px.choropleth(temp, locations='iso_alpha',
                                color='Perceptions of corruption',
                                hover_name='Country name',
                                color_continuous_scale=px.colors.diverging.RdYlGn,
                            )

            fig.update_layout(
                title_text='World map - Perceptions of corruption',
                showlegend=False,
                paper_bgcolor='rgb(248, 248, 255)',
                geo_bgcolor='rgb(248, 248, 255)',
                geo_showframe=False,
                title_font_size=22,
            )
            st.plotly_chart(fig)
            
        elif  page == 'Best Every Year':
            import numpy as np # linear algebra
            import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
            import matplotlib.pyplot as plt
            import seaborn as sns
            import plotly.express as px
            import pandas as pd
            import plotly.graph_objs as go
            from plotly.offline import init_notebook_mode, iplot
            import warnings
            warnings.filterwarnings("ignore")
            plt.style.use("seaborn-notebook")
            st.write("This dataset is taken from gallup world poll. GWP surveys citizens of more than 160 counties which have world's more than 98% adult population by asking them 100 global questions and calculates happiness score since 2005.")

            df = pd.read_csv("report_till_2021.csv")
            #df
            df2021 = pd.read_csv("report_only_2021.csv")
            #df2021

            #st.write(df2021["Regional indicator"].unique())

            sns.countplot(x = df2021["Regional indicator"])
            plt.xticks(rotation= 60)
            st.pyplot()

            list_features = ["Social support","Freedom to make life choices","Generosity","Perceptions of corruption"]
            sns.boxplot(data = df2021.loc[:, list_features], orient = "v", palette = "Set1")
            st.pyplot()

            list_features = ["Ladder score","Logged GDP per capita"]
            sns.boxplot(data = df2021.loc[:, list_features], orient = "v", palette="Set2")
            st.pyplot()

            list_features = ["Healthy life expectancy"]
            sns.boxplot(data = df2021.loc[:,list_features], orient="v",palette="Set3")
            st.pyplot()

            df2021_happiest_unhappiest = df2021[(df2021.loc[:,"Ladder score"] > 7.4) | (df2021.loc[:,"Ladder score"] < 3.5)]
            sns.barplot(x = "Ladder score", y = "Country name", data = df2021_happiest_unhappiest, palette = "coolwarm")
            plt.title("Happiest and Unhappiest country in 2021")
            st.pyplot()

            plt.figure(figsize= (15,8))
            sns.kdeplot(x = df2021["Ladder score"], hue = df2021["Regional indicator"], fill=True, linewidth=2)
            plt.axvline(df2021["Ladder score"].mean(), color="black")
            plt.title("Ladder score distribution by regional indicator")
            st.pyplot()

            fig = px.choropleth(df.sort_values("year"),
                            locations = "Country name",
                            color = "Life Ladder",
                            locationmode = "country names",
                            animation_frame = "year")
            fig.update_layout(title="Life ladder comparison by countries")
            st.plotly_chart(fig)

            df2021_g =df2021[(df2021.loc[:,"Generosity"] > 0.4) | (df2021.loc[:,"Generosity"] < -0.2)]
            sns.barplot(x = "Generosity", y = "Country name", data= df2021_g, palette="coolwarm")
            plt.title("Most generous and most generois countries in 2021")
            st.pyplot()

            fig = px.choropleth(df.sort_values("year"),
                            locations = "Country name",
                            color = "Generosity",
                            locationmode = "country names",
                            animation_frame = "year")
            fig.update_layout(title = "Generosity comparison by countries")
            st.plotly_chart(fig)

            sns.swarmplot(x = "Regional indicator", y = "Generosity", data = df2021)
            plt.xticks(rotation= 60)
            plt.title("Generosity distribution by regional indicator in 2021")
            st.pyplot()

            country_continent = {}
            for i in range(len(df2021)):
                country_continent[df2021["Country name"][i]] = df2021["Regional indicator"][i]
            all_countries = df["Country name"].value_counts().reset_index()["index"].tolist()
            all_countries_2021 = df2021["Country name"].value_counts().reset_index()["index"].tolist()

            region = []
            for i in range(len(df)):
                if df["Country name"][i] == "Angola":
                    region.append("Sub-Saharan Africa")
                elif df["Country name"][i] == "Belize":
                    region.append("Latin America and Cribbean")
                elif df["Country name"][i] == "Congo (Kinshasa)":
                    region.append("Sub-Saharan Africa")
                elif df["Country name"][i] == "Syria":
                    region.append("Middle East and North Africa")
                elif df["Country name"][i] == "Trinidad and Tobago":
                    region.append("Latin America and Cribbean")
                elif df["Country name"][i] == "Cuba":
                    region.append("Latin America and Cribbean")
                elif df["Country name"][i] == "Qatar":
                    region.append("Middle East and North Africa")
                elif df["Country name"][i] == "Sudan":
                    region.append("Middle East and North Africa")
                elif df["Country name"][i] == "Central African Republic":
                    region.append("Sub-Saharan Africa")
                elif df["Country name"][i] == "Djibouti":
                    region.append("Sub-Saharan Africa")
                elif df["Country name"][i] == "Somaliland region":
                    region.append("Sub-Saharan Africa")
                elif df["Country name"][i] == "South Sudan":
                    region.append("Middle East and North Africa")
                elif df["Country name"][i] == "Somalia":
                    region.append("Sub-Saharan Africa")
                elif df["Country name"][i] == "Oman":
                    region.append("Middle East and North Africa")
                elif df["Country name"][i] == "Guyana":
                    region.append("Latin America and Cribbean")
                elif df["Country name"][i] == "Bhutan":
                    region.append("South Asia")
                elif df["Country name"][i] == "Suriname":
                    region.append("Latin America and Cribbean")
                else:
                    region.append(country_continent[df["Country name"][i]])
                    
            df["region"] = region

            fig = px.scatter(df,
                            x = "Log GDP per capita",
                            y = "Life Ladder",
                            animation_frame = "year",
                            animation_group = "Country name",
                            template = "plotly_white",
                            color = "region",
                            hover_name = "Country name",
                            size_max = 60)
            fig.update_layout(title = "Life Ladder and Log GDP per capita Comparison by Contries via Regions for each Year")
            st.plotly_chart(fig)

            fig = px.scatter(df,
                            x = "Perceptions of corruption",
                            y = "Life Ladder",
                            animation_frame = "year",
                            animation_group = "Country name",
                            template = "plotly_dark",
                            color = "region",
                            hover_name = "Country name",
                            size_max = 60)
            fig.update_layout(title = "Life ladder and Corruption comparison by countries via regions for each year")
            st.plotly_chart(fig)

            sns.heatmap(df.corr(), annot = True, fmt = ".2f", linewidth = .7)
            plt.title("Relationship Between Features")
            st.pyplot()




            