import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as pg

df = pd.read_csv("studentData.csv")
df.sort_index()
students = df.student_id.unique()
mean_of_attempts = {}
data =[]

for i in students:
    stud_df = df.loc[df["student_id"] == i]
    mean_of_attempts[i] = stud_df.groupby("level")["attempt"].mean()
    data.append(pg.Scatter(x = mean_of_attempts[i], y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = "v"))

graph = pg.Figure(data)
graph.show()
