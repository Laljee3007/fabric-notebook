#!/usr/bin/env python
# coding: utf-8

# ## Poc Test
# 
# New notebook

# In[13]:


# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.read.format("csv").option("header","true").option("delimiter", "\t").load("abfss://c1e72755-9b54-4045-a6b0-52d3c80bb28a@onelake.dfs.fabric.microsoft.com/bf8498d9-0581-4f4c-8908-324596f5b1b4/Files/Sales.csv")
# df now is a Spark DataFrame containing CSV data from "abfss://c1e72755-9b54-4045-a6b0-52d3c80bb28a@onelake.dfs.fabric.microsoft.com/bf8498d9-0581-4f4c-8908-324596f5b1b4/Files/Sales.csv".
display(df)
df.createOrReplaceGlobalTempView('df')

