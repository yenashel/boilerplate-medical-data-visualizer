import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# 1
df = pd.read_csv("medical_examination.csv")

# 2
#Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
df["overweight"] = (df["weight"] / (df["height"] / 100 * df["height"] / 100)).apply(lambda x: 1 if x > 25 else 0) 

# 3
df["cholesterol"] = df["cholesterol"].apply(lambda x: 1 if x > 1 else 0) 
df["gluc"] = df["gluc"].apply(lambda x: 1 if x > 1 else 0) 


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(frame=df, id_vars=["cardio"], value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # 6
    df_cat = df_cat.reset_index().groupby(["variable", "cardio", "value"]).agg("count").rename(columns={"index": "total"}).reset_index()
    df_cat["value"] = df_cat["value"].astype(str)

    # 7
    graphic = sns.catplot(data=df_cat, x="variable", y="total", col="cardio", hue="value", kind="bar")

    # 8
    fig = graphic.figure

    # 9
    fig.savefig("catplot.png")
    return fig

# 10
def draw_heat_map():
    # 11
    
    df_heat = df[
      (df["ap_lo"] <= df["ap_hi"])
      & (df["height"] >= df["height"].quantile(0.025))
      & (df["height"] <= df["height"].quantile(0.975))
      & (df["weight"] >= df["weight"].quantile(0.025))
      & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13

    mask = np.triu(np.ones_like(corr, dtype=bool))

   
    # 14
    fig, ax = plt.subplots(figsize=(20, 10))

    # 15
    sns.heatmap(data=corr, mask=mask, annot=True, fmt=".1f")

    # 16
    fig.savefig("heatmap.png")
    return fig
