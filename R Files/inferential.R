#Name: Lucas Hasting
#Course: DA 380
#Instructor: Dr. Michael Floren
#Date: 4/21/2026
#Description: Make inferences with gss1_cleaned.csv

#**NOTE**: Using R version 4.4.3

#load data
#**NOTE**: do this before hand: setwd("C:/path/to/my/working_directory")
#could also do session-> set working directory -> source file location
#assuming the R file is in the same directory as the csv file
dat = read.csv("gss1_cleaned.csv")

#additional cleaning
dat$generation = ifelse(dat$generation == "", NA, dat$generation)
dat$wrkstat_cat = ifelse(dat$wrkstat_cat == "", NA, dat$wrkstat_cat)
dat$educ_cat = ifelse(dat$educ_cat == "", NA, dat$educ_cat)

#t-test on hrs1 grouped by married
grouped_frame = na.omit(data.frame(dat$hrs1, dat$marital_bin))
split_data = split(grouped_frame$dat.hrs1, grouped_frame$dat.marital_bin)
t.test(split_data$'1', split_data$'0')
print(sd(split_data$'1'))
print(sd(split_data$'0'))

#ANOVA on hrs1 grouped by generation
grouped_frame = na.omit(data.frame(dat$hrs1, dat$generation))
split_data = split(grouped_frame$dat.hrs1, grouped_frame$dat.generation)
print(anova(aov(dat$hrs1~dat$generation, data=dat)))
lapply(split_data, function(x) round(mean(x, na.rm = TRUE), 2))
lapply(split_data, function(x) round(sd(x, na.rm = TRUE), 2))

#chi-square test on work status and education
grouped_frame = na.omit(data.frame(dat$wrkstat_cat, dat$educ_cat))
print(length(grouped_frame$dat.educ_cat))
chisq.test(table(grouped_frame))
print(table(grouped_frame))
print(rowSums(table(grouped_frame), na.rm = TRUE))
print(colSums(table(grouped_frame), na.rm = TRUE))

#linear regression on family hours with income
print(anova(lm(dat$family_work_hours~dat$income, data=dat)))
print(summary(lm(dat$family_work_hours~dat$income, data=dat)))