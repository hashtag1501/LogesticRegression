import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("escape_velocity.csv")

velocity_list = df["Velocity"].tolist() 
escaped_list = df["Escaped"].tolist()


x = np.reshape(velocity_list,(len(velocity_list),1))
y = np.reshape(escaped_list,(len(escaped_list),1))

def model():
    return 1/1+np.e(-x)

plt.ylabel('y')
plt.xlabel('X')
plt.xlim(0,30)
plt.show