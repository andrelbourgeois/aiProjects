# numpy basics

# import numpy
import numpy as np

# create 2 lists, height and weight
height = [1.87, 1.87, 1.82, 1.78, 1.91, 1.70, 1.85]
weight = [71.1, 81.0, 80.4, 83.1, 92.2, 76.7, 87.6]

# create numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# ELEMENT-WISE CALCULATION
# numpy arrays allow operations to be performed across
# entire arrays 
bmi = np_weight / np_height **2

# results = [20.33229432 23.16337327 24.27243087 26.22774902 25.27343 26.53979239 25.59532505]
print(bmi)

# SUBSETTING
# get all bmi values less than 23
print(bmi[bmi < 23])
