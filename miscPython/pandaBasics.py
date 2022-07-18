# panda basics

# panda is built on numpy
# its key data structure is called the dataframe
# dataframes allow allow us to store and manipulate
# tabular data in rows of observations and columns of variables

# import pandas
import pandas as pd

# create a dataframe from a dictionary
# declare dictionary
dict = {"country": ["brazil", "russia", "India"],
"capital": ["brasilia", "moscow", "new dehli"], 
"area": [8.516, 17.10, 3.286], 
"population": [200.4, 143.5, 1252.0]}

# declare dataframe
countries = pd.DataFrame(dict)

# print dictionary
print(dict)

print("")

# print dataframe
print(countries)
print("")

# change the index values - changes the row index from numbers
countries.index = ["BR", "RU", "IN"]

# print countries again to see difference
print(countries)

# you can also create a dataframe by using a csv file
# DATAFRAME_NAME = pd.read_csv("CSV_NAME")

# INDEXING DATAFRAMES
# print out capital columns as pandas series
print(countries["capital"])
print("")

# print out capital columns as pandas dataframe
print(countries[["capital"]])
print("")

# print out country and capital columns as pandas dataframes
print(countries[["country", "capital"]])
print("")

# print out first 2 observations (rows)
print(countries[0:2])
print("")

# print out last observation (row)
print(countries[2:])
print("")
# USING LOC AND ILOC
# loc and iloc are used to perform data operations
# loc is label-based: must specify rows and columns based on labels
# iloc is integer based: must specify rows and coumns based on integer index

print(countries.iloc[1])
print("")

print(countries.loc["BR"])

