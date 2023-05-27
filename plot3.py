from matplotlib import pyplot as plt
import pandas as pd
import csv
import numpy as np
from itertools import accumulate
  
f = []
x = []
y = []

with open('example.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        f.append(row[0])
        x.append(row[1])
        y.append((row[2]))

f.pop(0)
x.pop(0)
y.pop(0)

z = len(x)

lngth = [int(z/4), int(z/4), int(z/4), int(z/4)]

outputt1 = [x[a - b: a] for a, b in zip(
        accumulate(lngth), lngth)]

outputt2 = [y[a - b: a] for a, b in zip(
        accumulate(lngth), lngth)]

outputt3 = [f[a - b: a] for a, b in zip(
        accumulate(lngth), lngth)]


x1 = outputt1[0:1]
x1_new = []
for sublist in x1:
    x1_new.extend(sublist)

x2 = outputt1[1:2]
x2_new = []
for sublist in x2:
    x2_new.extend(sublist)

x3 = outputt1[2:3]
x3_new = []
for sublist in x3:
    x3_new.extend(sublist)

x4 = outputt1[3:4]
x4_new = []
for sublist in x4:
    x4_new.extend(sublist)


y1 = outputt2[0:1]
y1_new = []
for sublist in y1:
    y1_new.extend(sublist)
y2 = outputt2[1:2]
y2_new = []
for sublist in y2:
    y2_new.extend(sublist)
y3 = outputt2[2:3]
y3_new = []
for sublist in y3:
    y3_new.extend(sublist)
y4 = outputt2[3:4]
y4_new = []
for sublist in y4:
    y4_new.extend(sublist)


f1 = outputt3[0:1]
f1_new = []
for sublist in f1:
    f1_new.extend(sublist)
f2 = outputt3[1:2]
f2_new = []
for sublist in f2:
    f2_new.extend(sublist)
f3 = outputt3[2:3]
f3_new = []
for sublist in f3:
    f3_new.extend(sublist)
f4 = outputt3[3:4]
f4_new = []
for sublist in f4:
    f4_new.extend(sublist)


# removing n% elements from first and last for every list
def percent(num_a, num_b):
    return (num_a * num_b) / 100

n = int(percent(15, len(x1[0])))

x1_n1 = x1[0][n:]
x1_n2 = x1_n1[:len(x1_n1) - n]
x1_n3 = [x1_n2]

x2_n1 = x2[0][n:]
x2_n2 = x2_n1[:len(x2_n1) - n]
x2_n3 = [x2_n2]

x3_n1 = x3[0][n:]
x3_n2 = x3_n1[:len(x3_n1) - n]
x3_n3 = [x3_n2]

x4_n1 = x4[0][n:]
x4_n2 = x4_n1[:len(x4_n1) - n]
x4_n3 = [x4_n2]

y1_n1 = y1[0][n:]
y1_n2 = y1_n1[:len(y1_n1) - n]
y1_n3 = [y1_n2]

y2_n1 = y2[0][n:]
y2_n2 = y2_n1[:len(y2_n1) - n]
y2_n3 = [y2_n2]

y3_n1 = y3[0][n:]
y3_n2 = y3_n1[:len(y3_n1) - n]
y3_n3 = [y3_n2]

y4_n1 = y4[0][n:]
y4_n2 = y4_n1[:len(y4_n1) - n]
y4_n3 = [y4_n2]



# plt.style.use('fivethirtyeight')
# plt.scatter(x1, y1)


# plt.scatter(x2, y2)


# plt.scatter(x3, y3)


# plt.scatter(x4, y4)
# plt.show()


# Before dropping frames

# plt.scatter(x1, y1)
# plt.scatter(x2, y2)
# plt.scatter(x3, y3)
# plt.scatter(x4, y4)

# plt.xlabel('yaw')
# plt.ylabel('pitch')
# plt.title('Scatter Plot of yaw and pitch')

# plt.legend()
# plt.show()

# After dropping frames

plt.scatter(x1_n3, y1_n3)
plt.scatter(x2_n3, y2_n3)
plt.scatter(x3_n3, y3_n3)
plt.scatter(x4_n3, y4_n3)

plt.xlabel('yaw')
plt.ylabel('pitch')
plt.title('Scatter Plot of yaw and pitch')

plt.legend()
plt.show()

