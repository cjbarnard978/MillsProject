import plotly
import pandas as pd
import plotly as px
df = "CourtenayMillsRecords.csv"()
fig = px.pie(df, values='ID Number', names='Denomination')
fig.show()
