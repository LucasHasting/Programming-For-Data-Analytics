#Name: Lucas Hasting
#Course: DA 380
#Instructor: Dr. Michael Floren
#Date: 4/16/2026
#Description: Show graphs/descriptive statistics for gss1_cleaned.csv

#**NOTE**: Using R version 4.4.3

#load data
#**NOTE**: do this before hand: setwd("C:/path/to/my/working_directory")
#could also do session-> set working directory -> source file location
#assuming the R file is in the same directory as the csv file
dat = read.csv("gss1_cleaned.csv")

#additional cleaning needed
dat$marital_cat = ifelse(dat$marital_cat == "", NA, dat$marital_cat)
dat$sex_cat = ifelse(dat$sex_cat == "", NA, dat$sex_cat)
dat$wrkstat = ifelse(dat$wrkstat == "", NA, dat$wrkstat)

#display mean/standard deviation of family_work_hours
print(round(mean(dat$family_work_hours, na.rm = T),2))
print(round(sd(dat$family_work_hours, na.rm = T),2))

#display mean/standard deviation of family_work_hours grouped by marital_bin
grouped_frame = na.omit(data.frame(dat$family_work_hours, dat$marital_bin))
split_data = split(grouped_frame$dat.family_work_hours, grouped_frame$dat.marital_bin)
print(round(mean(split_data$'0'),2))
print(round(sd(split_data$'0'),2))
print(round(mean(split_data$'1'),2))
print(round(sd(split_data$'1'),2))

#display mean/standard deviation of realinc
print(round(mean(dat$realinc, na.rm = T),2))
print(round(sd(dat$realinc, na.rm = T),2))

#display mean/standard deviation of realinc grouped by marital_bin
grouped_frame = na.omit(data.frame(dat$realinc, dat$marital_bin))
split_data = split(grouped_frame$dat.realinc, grouped_frame$dat.marital_bin)
print(round(mean(split_data$'0'),2))
print(round(sd(split_data$'0'),2))
print(round(mean(split_data$'1'),2))
print(round(sd(split_data$'1'),2))

#get count for happiness bin
tab = table(na.omit(dat$happy_bin))
print(tab)
print(round(prop.table(tab) * 100, 2))

#get count for happiness bin grouped by sex_cat
grouped_frame = na.omit(data.frame(dat$happy_bin, dat$sex_cat))
tab = table(grouped_frame)
print(tab)
print(round(prop.table(tab, margin = 2) * 100, 2))

#create happy_cat variable based on happy_bin
dat$happy_cat = ifelse(dat$happy_bin == 1, "Happy", NA)
dat$happy_cat = ifelse(dat$happy_bin == 0, "Unhappy", dat$happy_cat)

#display distribution of happy using a bar chart
barplot(table(dat$happy_cat), xlab = "Happiness", ylab = "Responses")
dev.print(png, "happy.PNG", width = 800, height = 600)

#display distribution of family_work_hours using a bar chart
barplot(table(dat$family_work_hours), xlab = "Household Work Hours", 
        ylab = "Responses", xaxt = "n")
axis(side = 1, at = seq(0, max(dat$family_work_hours, na.rm = T), by = 10))
dev.print(png, "family_1.png", width = 800, height = 600)

#display distribution of family_work_hours without 40 hours using a bar chart
barplot(table(ifelse(dat$family_work_hours == 40, NA, dat$family_work_hours)), 
        xlab = "Household Work Hours", ylab = "Responses", xaxt = "n")
axis(side = 1, at = seq(0, max(dat$family_work_hours,na.rm = T), by = 10))
dev.print(png, "family_2.png", width = 800, height = 600)

#display distribution of income by wrkstat_cat using a box and whisker plot - 2 plots
#hist()
boxplot(dat$income ~ dat$wrkstat, xlab = "Employment Status", ylab = "Income")
dev.print(png, "income_wrkstat.png", width = 800, height = 600)

#scatter plot to show relationship between income and age
grouped_frame = na.omit(data.frame(dat$income, dat$age))
plot(grouped_frame$dat.age, grouped_frame$dat.income, 
     xlab = "Age", ylab = "Income")
dev.print(png, "age_income.png", width = 800, height = 600)

#display distribution of income by wrkstat_cat using a box and whisker plot
boxplot(dat$family_work_hours ~ dat$marital_cat,
        xlab = "Marital Staus", ylab = "Total Work Hours")
dev.print(png, "family_marital.png", width = 800, height = 600)

#average family_work_hours by marital_cat
grouped_frame = na.omit(data.frame(dat$family_work_hours, dat$marital_cat))
split_data = split(grouped_frame$dat.family_work_hours, grouped_frame$dat.marital_cat)
lapply(split_data, function(x) round(mean(x, na.rm = TRUE), 2))