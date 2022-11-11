#importing libraries and reading the CSV file 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

affordable = pd.read_csv("Affordable_Housing_Production_by_Building.csv")

#grouping data by borough
grouped_borough = affordable.groupby('Borough')
brooklyngp = grouped_borough.get_group('Brooklyn')

#grouping the data by multiple zip codes 
grouped_postcode = affordable.groupby("Postcode") 
myList = [11220, 11232]
spallunits = 0
for zip in myList:
    sunsetpark = grouped_postcode.get_group(zip)
    value = sunsetpark["All Counted Units"].sum()
    spallunits += value
\
# % of affordable units in Brooklyn that belong to Sunset Park 
bkr_total = brooklyngp["All Counted Units"].sum()
percentunit = round(((spallunits/bkr_total)*100), 2)
print("Sunset park makes up ", percentunit, "% of Brooklyn's total affordable housing \n")

#grouping the data by singular zip codes
postcode1 = grouped_postcode.get_group(11220)
postcode2 = grouped_postcode.get_group(11232)

#% of units in Sunset Park by type
unitList = ['Extremely Low Income Units', 'Very Low Income Units', 'Low Income Units', 'Moderate Income Units', 'Middle Income Units', 'Other Income Units']

print("The percentage of units in Sunset Park by type: ")

for item in unitList:
    value1 = postcode1["All Counted Units"].sum()
    value2 = postcode2["All Counted Units"].sum()
    total = value1 + value2
    value = round((((postcode1[item].sum()+postcode2[item].sum())/total)*100),2)
    print(item,":", value, "%")

#graph of % of units in Sunset Park by type
labels = ['ELI', 'VLI', 'LI', 'MoI', 'MiI', 'OI']
unit_counts = [74, 6.41, 9.31, 7.86, 1.45, 0.97]

x = np.arange(len(labels))  
width = 0.3

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, unit_counts, width, label='Sunset Park')

ax.set_ylabel('Percentage of Units in Sunset Park')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)

fig.tight_layout()

plt.show()

fig.savefig('% of units in Sunset Park by type')

#% of studio units in Sunset Park by type 
print("\nThe percentage of studio units in Sunset Park by type: ")

for item in studioList:
    value1 = postcode1["All Counted Units"].sum()
    value2 = postcode2["All Counted Units"].sum()
    total = value1 + value2
    value = round((((postcode1[item].sum()+postcode2[item].sum())/total)*100),2)
    print(item,":", value, "%")

#graph of % of studio units by type
labels = ['Studio', '1-BR', '2-BR', '3-BR', '4-BR', '5-BR', '6-BR', 'Unknown']
unit_counts = [12.21, 50.54, 29.87, 7.38, 0.0, 0.0, 0.0, 0.0]

x = np.arange(len(labels))  
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, unit_counts, width, label='Sunset Park')

ax.set_ylabel('Percentage of Bedroom Units in Sunset Park')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)

fig.tight_layout()

plt.show()

fig.savefig('% of bedroom units in Sunset Park by type')

#% rental vs ownership
print("\nThe percentage of rented or owned units in Sunset Park by type: ")

ownList = ['Counted Rental Units', 'Counted Homeownership Units']

for item in ownList:
    value1 = postcode1["All Counted Units"].sum()
    value2 = postcode2["All Counted Units"].sum()
    total = value1 + value2
    value = round((((postcode1[item].sum()+postcode2[item].sum())/total)*100),2)
    print(item,":", value, "%")

#graph of % rental vs ownership
unit_counts = [99.76, 0.24]

x = np.arange(len(ownList))  
width = 0.3

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, unit_counts, width, label='Sunset Park')

ax.set_ylabel('Number of Bedroom Units in Sunset Park')
ax.set_xticks(x, ownList)
ax.legend()

ax.bar_label(rects1, padding=3)

fig.tight_layout()

plt.show()

fig.savefig('% of rental and ownership units in Sunset Park')


