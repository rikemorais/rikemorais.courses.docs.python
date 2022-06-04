import plotly.express as px
df = px.data.iris()
fig = px.density_heatmap(df,
                         x="sepal_width",
                         y="sepal_length",
                         marginal_x="rug",
                         marginal_y="histogram")
fig.show()
