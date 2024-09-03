# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWC_utilities has functions to help format data printed to the console
import GWCutilities as util

columns = ['DP_earn_more_p']
desc = ['Women currently married or in union who were paid cash for their work, earning more than her partner (%)']
# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell175.csv")
for i in range(len(columns)):
  print(lwd[columns[i]].min())
  print(lwd[columns[i]].max())
#Change x here:
plt.hist(x=columns[i], data=lwd, edgecolor='white', bins=29, color = "deeppink")

#Change x-label here:
plt.xlabel(desc[i])

plt.ylabel("Number of Data Points")
plt.show()
