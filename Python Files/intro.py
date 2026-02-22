import pandas as pd

df = pd.read_csv("brfss1_raw.csv")
df_raw = df.copy() #create a copy of the frame

print("Verify data set:")
print(df.head())  #first 5 obs
print(df.tail())  #last 5 obs
print(df.shape)   #rows x columns
print(df.columns) #features, can be casted as list
print("\n\n")

#summary stats
print("WTKG3:")
print(df['WTKG3'],end="\n\n")
print(df['WTKG3'].describe())

#add a new feature
print("\n\nHTM4_sq:")
df["HTM4_sq"] = df['HTM4']**2 
print(df['HTM4_sq'],end="\n\n")
print(df['HTM4_sq'].describe())

#logical filtering
print("\n\n")
print(df['WTKG3'] > 8165)
print(f"\n{(df['WTKG3'] > 8165).value_counts()}")
print(f"\n{(df['WTKG3'] > 8165).value_counts(normalize=True)}")

#meta commands
import os

#current working directory - cwd
print(os.getcwd())  #pwd equiv
print(os.listdir()) #ls equiv
os.chdir("./") #cd equiv
