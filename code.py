import plotly_express as px
import pandas as pd
import random
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig= ff.create_distplot([df["Mobile Brand"].tolist()],["Avg Rating"],show_hist= False)
fig.show()