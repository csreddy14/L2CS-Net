import pandas as pd
import matplotlib.pyplot as mp

# take data
data = pd.read_csv("example.csv")

# form dataframe
data = data.head()

df = pd.DataFrame(data, columns=["frame", "yaw", "pitch"])

# plot the dataframe
df.plot(x="frame", y=["yaw", "pitch"], figsize=(10, 10))

# print bar graph
mp.show()
