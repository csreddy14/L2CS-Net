import pandas as pd
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 4.00]
plt.rcParams["figure.autolayout"] = True


# Make a list of columns
columns = ['yaw', 'pitch']

# Read a CSV file
df = pd.read_csv("example.csv", usecols=columns)

# Plot the lines
df.plot()

plt.show()