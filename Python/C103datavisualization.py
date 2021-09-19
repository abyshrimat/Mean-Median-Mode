import pandas as pd
import plotly.express as px

df1 = pd.read_csv("CovidData.csv")
fig1 = px.scatter(df1, x = "date", y = "cases", color = "country", title = 'Covid cases')
#fig1.show()

df2 = pd.read_csv("CovidData.csv")
fig2 = px.line(df2, x = "date", y = "cases", color = "country", title = 'Covid cases')
fig2.show()

df3 = pd.read_csv("CovidData.csv")
fig3 = px.bar(df3, x = "date", y = "cases", color = "country", title = 'Covid cases')
#fig3.show()