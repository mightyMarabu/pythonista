# getting started with pandas

# data: natural earth, populated places

import pandas

import numpy

import matplotlib as mplot

#reading dataset using pandas
df = pandas.read_csv("/home/sebastian/Dokumente/data/ne_populated_places.csv")

#first look on data
df.head(10)

# summary
df['POP2015'].describe()

# plot
df['POP2015'].hist(bins=50)
df.boxplot(column='POP2015', by = 'LABELRANK')

# new data frame
myDF = pandas.DataFrame(myPop)

# add column to new data frame
myDF['Name'] = df.NAME

# rows with Pop higher than 0
moreThanZero = myDF.loc[myDF['POP2015']>0]
print(moreThanZero)
