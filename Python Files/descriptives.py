import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("brfss1_cleaned.csv")

#basic descriptive statistics on all numerical columns
print(df.describe())

#specefic column
print(f"\nBMI mean: {df["bmi"].mean()}")
print(f"BMI std: {df["bmi"].std()}")
print(f"BMI min: {df["bmi"].min()}")
print(f"BMI max: {df["bmi"].max()}")

#descriptives by groups
print(df.groupby("age_ymo")["bmi"].describe())
print(df.groupby("age_ymo")["bmi"].agg(["mean", "std", "count"]))

#min/max of PHYSHLTH based on age group -> sample size differs with question
print()
print(df.groupby("age_ymo")["PHYSHLTH"].agg(["min", "max", "count", "mean", "std"]))

#counts and percentages
print()
print(df["disabled_cat"].value_counts(normalize=True)*100)

print()
print(df.groupby("age_ymo")["disabled_cat"].value_counts(normalize=True))

#one extra breakdown
print()
print(df.groupby("GENHLTH_pos")["sex_cat"].value_counts(normalize=True)*100)

#--graphics


#bar chart example
df["disabled_cat"].value_counts(normalize=True).plot(kind="bar")
plt.ylabel("Proportion")
plt.xlabel("Disability Status")
plt.title("Proportion of Disability Status")

plt.tight_layout()
plt.savefig("figure1.png")
plt.clf() #clear the plot
plt.close()

#grouped means plot
df.groupby("disabled_cat")["bmi"].mean().plot(kind="bar")
plt.clf()
plt.close()

#histogram
df.hist(column="ment_healthy_days_30", bins=30)
plt.clf()
plt.close()

#box plots
df.boxplot(column="bmi", by="age_ymo")
plt.clf()
plt.close()

#scatterplots
df.plot(kind="scatter", x="HTM4", y="WTKG3")
plt.clf()

plt.show()
plt.close() #close the plt
