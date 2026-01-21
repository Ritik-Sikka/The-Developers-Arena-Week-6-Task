import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

fig = px.bar(
    df,
    x="Category",
    y="Sales",
    color="Customer_Type",
    title="Sales Dashboard Overview",
    hover_data=["Profit", "Price"]
)

fig.show()