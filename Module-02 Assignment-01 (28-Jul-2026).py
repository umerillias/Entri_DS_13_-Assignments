#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


# Create a 1D array from 1 to 10
original_array = np.arange(1,11)

# Reshape into a 2x5 matrix
matrix_2x5 = original_array.reshape(2,5)

print(matrix_2x5)


# In[ ]:





# In[4]:


# Create a 1D array from 1 to 20
arr = np.arange(1,21)

# Extract elements between the 5th and 15th index
# This excludes the 15th index itself
sliced_arr = arr[5:15]

print("Original Array:", arr)
print("Extracted Slice:", sliced_arr)


# In[ ]:





# In[8]:


# Recreating the array from 1 to 20
arr = np.arange(1,21)

# Compute statistics
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Standard Deviation: {std_val:.2f}")


# In[ ]:





# In[11]:


# Create a 2D array x of shape(3,4)
x = np.array([[10,20,30,40],
              [50,60,70,80],
              [90,100,110,120]])

# Create a 2D array x of shape(4,)
y = np.array([1,2,3,4])


# Subtract y from each row of x using broadcasting
result = x - y

print("Array x:\n", x)
print("\nArray y:\n", y)
print("\nResult after broadcasting:\n", result)



# In[ ]:





# In[14]:


# --- Step 1: Create the initial DataFrame with 10 rows ---
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'age':[25, 35, 30, 22, 50, 37, 27, 57, 32, 45],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male']
}
df = pd.DataFrame(data)

# --- Step 2: Add the 'occupation' column ---
# We use a list that repeats 'Programmer', 'Manager', and 'Analyst' to fill the 10 rows
occupations = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']
df['occupation'] = occupations

# --- Step 3: Select rows where age is greater than or equal to 30 ---
filtered_df = df[df['age'] >= 30]

# --- Step 4: Convert to CSV, read it back, and display the contents ---
# Save to a local CSV file
df.to_csv('people_data.csv', index=False)

# Read the CSV file back into a new DataFrame
loaded_df = pd.read_csv('people_data.csv')

# --- Displaying the Outputs ---
print("--- 1 & 2) Full DataFrame with Occupation Added ---")
print(df)

print("\n--- 3) Rows where Age >= 30 ---")
print(filtered_df)

print("\n--- 4) Contents Displayed After Reading from CSV ---")
print(loaded_df)


# In[ ]:




