# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell175.csv")

# Add Step 1 code here:
listOfCountries = lwd['country_name'].unique()
#print(util.vformat_list(listOfCountries))
oneCountryBooleanList = lwd['country_name'] == "Colombia"
oneCountryData = lwd.loc[oneCountryBooleanList]

plt.scatter(oneCountryData["HH_women_time_water_mean"],oneCountryData["ED_attainment_secondary_higher_p"],color="deeppink")
# add a title to the plot
plt.legend(lwd['country_name'])
plt.ylim(0, 100)
plt.title("Women with secondary education or higher education(%) vs Average time to get to drinking water")

#Label the x-axis
plt.xlabel("Average time to get to drinking water")

# label the y-axis
plt.ylabel("Women with secondary education or higher education(%)")

# show the plot
plt.show()

# 