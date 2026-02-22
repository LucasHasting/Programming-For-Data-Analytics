'''
Name: Lucas Hasting
Course: DA 380
Instructor: Dr. Michael Floren
Date: 2/19/2026
Description: Get descriptive stas/graphs from brfss1_cleaned.cvs
'''

#import needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read in data
df = pd.read_csv("brfss1_cleaned.csv")

#--DESCRIPTIVE STATS

#General Health
print(f"GENHLTH mean: {round(df["GENHLTH"].mean(),2)}")
print(f"GENHLTH std: {round(df["GENHLTH"].std(),2)}")

print(f"\nmean - GENHLTH by {round(df.groupby("income_bin")["GENHLTH"].mean(),2)}")
print(f"\nstd - GENHLTH by {round(df.groupby("income_bin")["GENHLTH"].std(),2)}",end="\n\n")

#Positive Mental Health Days
print(f"ment_healthy_days_30 mean: {round(df["ment_healthy_days_30"].mean(),2)}")
print(f"ment_healthy_days_30 std: {round(df["ment_healthy_days_30"].std(),2)}")

print(f"\nmean - ment_healthy_days_30 by {round(df.groupby("bmi_cat")["ment_healthy_days_30"].mean(),2)}")
print(f"\nstd - ment_healthy_days_30 by {round(df.groupby("bmi_cat")["ment_healthy_days_30"].std(),2)}",end="\n\n")

#Exercise Participation
print(df["EXERANY2"].value_counts(),end="\n\n")
print(round(df["EXERANY2"].value_counts(normalize=True)*100,2),end="\n\n")
print(df.groupby("EXERANY2")["sex_cat"].value_counts(),end="\n\n")
print(round(df.groupby("EXERANY2")["sex_cat"].value_counts(normalize=True)*100,2),end="\n\n")

#BMI by Physical Health
print(f"mean - BMI by {round(df.groupby("perf_phys_health")["bmi"].mean(),2)}")

#--GRAPHICS

#Obesity Status
df["obese"].map({0: 'Not Obese', 1: 'Obese'}).value_counts().plot(kind="bar")
plt.ylabel("Number of People")
plt.xlabel("Obesity Status")
plt.title("Obesity Status Distribution")

plt.tight_layout()
plt.savefig("obesity.PNG")
plt.clf() #clear the plot
plt.close()

#Days with Poor Mental Health - 1
df["MENTHLTH"].value_counts().sort_index().plot(kind="bar")
plt.ylabel("Number of People")
plt.xlabel("Days with Poor Mental Health")
plt.title("Distribution of Days with Poor Mental Health")

plt.tight_layout()
plt.savefig("ment_health.PNG")
plt.clf() #clear the plot
plt.close()

#Days with Poor Mental Health - 2
df[df["MENTHLTH"] > 0]["MENTHLTH"].value_counts().sort_index().plot(kind="bar")
plt.ylabel("Number of People")
plt.xlabel("Distribution of Days with Poor Mental Health")
plt.title("Days with Poor Mental Health without Perfect Mental Health")

plt.tight_layout()
plt.savefig("ment_health_2.PNG")
plt.clf() #clear the plot
plt.close()

#BMI by education level
df.boxplot(column="bmi", by="EDUCA")
plt.suptitle('')
plt.ylabel("BMI")
plt.xlabel("Education Level")
plt.title("Dispertion of BMI by Education Level")

plt.tight_layout()
plt.savefig("bmi_edu_1.png")
plt.clf() #clear the plot
plt.close()

#Education level distribution
df["EDUCA"].value_counts().sort_index().plot(kind="bar")
plt.ylabel("Number of People")
plt.xlabel("Education Level")
plt.title("Distribution of Education Level")

plt.tight_layout()
plt.savefig("bmi_edu_2.png")
plt.clf() #clear the plot
plt.close()

#Relationship between days with poor mental health and height
df.plot(kind="scatter", x="HTM4", y="MENTHLTH")
plt.ylabel("Days with Poor Mental Health")
plt.xlabel("Height (meters)")
plt.title("Height by Mental Health Days")

plt.tight_layout()
plt.savefig("HTIN4_ment_hlth.png")
plt.clf() #clear the plot
plt.close()

#BMI by Physical Health
df["perf_phys_health_cat"] = df["perf_phys_health"].map({0: "People without perfect physical health", 1: "People with perfect physical health"})
df.boxplot(column="bmi", by="perf_phys_health_cat")
plt.suptitle('')
plt.ylabel("BMI")
plt.xlabel("Physical Health")
plt.title("Average BMI by Physical Health")

plt.tight_layout()
plt.savefig("bmi_perf_health.png")
plt.clf() #clear the plot
plt.close()
