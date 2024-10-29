#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:10:27 2024

@author: jacquesaoustin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#open the csv file in a reader mode
titanic = pd.read_csv('train.csv')
data =[]


###################################### Functions #######################################

def pie_chart (val, label, color):
    
    fig, ax = plt.subplots()
    couleurs = plt.get_cmap(color)(np.linspace(0.2,0.6,len(val)))
    
    ax.pie(val, labels=label, colors = couleurs, wedgeprops={"linewidth": 2, "edgecolor": "white"}, autopct = '%1.2f%%')
    
    
def percentage(val, whole):

    return val/whole*100

##################################### Code ##############################################

#Let's get first a serie with only the people missing

wasted_people = titanic[titanic['Transported'] == False].index
header = list(titanic.columns.values)
wasted_data = []


for i in wasted_people:
          wasted_data.append(list(titanic.iloc[i]))
          
data = pd.DataFrame(wasted_data, columns=header)
data = data.dropna()

# Maybe the people who disappear were all located at the same poistion when they disappearted
# First I'll see if they came all from the same planet or had the same destination. That is maybe how was decided their allocation in a cabin

# I will in a first time determine all the planet from which people are coming and the destination

planets = []
perc_planets = []
destination = []
perc_destination = []

[planets.append(i) for i in data['HomePlanet'] if i not in planets]
[perc_planets.append(len(data[data['HomePlanet']== i])/len(data)*100) for i in planets] # Now I will determine the percentage of people who disappeared from a certain planet  


pie_chart(perc_planets, planets, 'PuBuGn')  # More than 60% of the people who died were from earth

[destination.append(i) for i in data['Destination'] if i not in destination]
[perc_destination.append(percentage(len(destination), len(data))) for i in destination]   


pie_chart(perc_destination, destination, 'YlOrBr')    # Almost 75% of the peop[le who died were going to Trappist-1e

# Now let's check the cryo people

cryo = data[data['CryoSleep'] == True]


cryo_lab = ['cryo', 'not cryo']
perc_cryo = [percentage(len(cryo),len(data)), 100-percentage(len(cryo),len(data))]
pie_chart(perc_cryo,cryo_lab, 'PuBuGn' ) # More than 80% of the people were not in cryo

# Now let's check the VIP people

VIP = data[data['VIP'] == True]

VIP_lab = ['VIP', 'not VIP']
perc_VIP = [percentage(len(VIP),len(data)), 100-percentage(len(VIP),len(data))]
pie_chart(perc_VIP,VIP_lab, 'YlOrBr' ) # Almost none of the people who died were VIP 96.9%

#let's do a diagram of the age of people

#First let's get the age of everyone
age = []
[age.append(int(data.iloc[i]['Age'])) for i in range(len(data))]
screening = list(set(age))

number = []
[number.append(age.count(screening[i])) for i in range (len(screening))]

fig = plt.figure()
plt.bar(screening, number, color ='blue', width = 0.4) # Most ofthe people who disappeared were between 19 years old and 50 years old
