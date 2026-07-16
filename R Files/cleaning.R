#Name: Lucas Hasting
#Course: DA 380
#Instructor: Dr. Michael Floren
#Date: 4/9/2026
#Description: Clean the gss1_raw.csv file

#**NOTE**: Using R version 4.4.3

#needed for my machine since GNU make was on my system for another project (using rtools44):
#this was for installing packages using rtools  
  #new_path = "C:\\rtools44\\usr\\bin"
  #Sys.setenv(PATH = paste(new_path, Sys.getenv("PATH"), sep = ";"))

#load data
  #**NOTE**: do this before hand: setwd("C:/path/to/my/working_directory")
  #could also do session-> set working directory -> source file location
  #assuming the R file is in the same directory as the csv file
dat = read.csv("gss1_raw.csv")

#**IN CLASS VARIABLES**

#add sex categorical variable
sex_key = c("1" = "Male", 
            "2" = "Female")

dat$sex_cat = sex_key[dat$sex]

#add marital categorical variable
marital_key = c("1" = "married",
                "2" = "widowed",
                "3" = "divorced",
                "4" = "separated",
                "5" = "never married")
dat$marital_cat = marital_key[dat$marital]

#add a reverse code for health
dat$health_r = 5 - dat$health

#add a reverse code for happy
dat$happy_r = 4 - dat$happy

#add a variable for people of young, middle, and old ages
dat$age_ymo = cut(dat$age, 
                  breaks=c(-Inf, 34, 64, Inf),
                  label = c("Young", "Middle", "Old"))

#**HW Problems** (with some other in class cleaning)
#add education categorical variable
dat$educ_cat = cut(dat$educ,
    breaks=c(-Inf, 11, 12, 15, 16, Inf),
    label = c("< HS", "HS", "Some College", "College", "> College"))

#create/clean total work self
hrs1_0 = ifelse(is.na(dat$hrs1), 0, dat$hrs1)
hrs2_0 = ifelse(is.na(dat$hrs2), 0, dat$hrs2)
dat$tot_work_self = hrs1_0 + hrs2_0
dat$tot_work_self = ifelse(is.na(dat$hrs1) & is.na(dat$hrs2), NA, dat$tot_work_self)

#create work_full_self >=35 = 1, <35 = 0 based on tot_work_self
dat$work_full_self = ifelse(dat$tot_work_self >= 35, 1, 0)
dat$work_full_self = ifelse(is.na(dat$tot_work_self), NA, dat$work_full_self)

#create/clean total work self
sphrs1_0 = ifelse(is.na(dat$sphrs1), 0, dat$sphrs1)
sphrs2_0 = ifelse(is.na(dat$sphrs2), 0, dat$sphrs2)
dat$tot_work_spouse = sphrs1_0 + sphrs2_0
dat$tot_work_spouse = ifelse(is.na(dat$sphrs1) & is.na(dat$sphrs2), NA, dat$tot_work_spouse)

#create work_full_self >=35 = 1, <35 = 0 based on tot_work_self
dat$work_full_spouse = ifelse(dat$tot_work_spouse >= 35, 1, 0)
dat$work_full_spouse = ifelse(is.na(dat$work_full_spouse), NA, dat$work_full_spouse)

#create years to retirement variable
dat$years_to_retirement = ifelse(dat$age > 67, NA, 67 - dat$age)

#create family_work_hours based on cleaned hrs and sphrs
dat$family_work_hours = hrs1_0 + hrs2_0 + sphrs1_0 + sphrs2_0
dat$family_work_hours = ifelse(is.na(dat$hrs1) & is.na(dat$hrs2) & is.na(dat$sphrs1) & is.na(dat$sphrs2), NA, dat$family_work_hours)

#key for recoding wrkstat
wrkstat_key = c("1" = "working full time",
                "2" = "working part time",
                "3" = "with a job, but not at work because of temporary illness, vacation, strike",
                "4" = "unemployed, laid off, looking for work",
                "5" = "retired",
                "6" = "in school",
                "7" = "keeping house",
                "8" = "other")

#recode wrkstat
dat$wrkstat_cat = wrkstat_key[dat$wrkstat]

#happiness bin variable 1 = happy, 0 = not happy
dat$happy_bin  = ifelse(dat$happy < 3, 1, 0)

#convert realinc (low<13k, 13k<=medium<=40k, 40k<high)
dat$realinc_lmh = ifelse(dat$realinc < 13000, "Low", NA_character_)
dat$realinc_lmh = ifelse(dat$realinc >= 13000 & dat$realinc <= 40000, "Medium", dat$realinc_lmh)
dat$realinc_lmh = ifelse(dat$realinc > 40000, "High", dat$realinc_lmh)

#marital_bin variable 1 = married, 0 = not married
dat$marital_bin = ifelse(dat$marital == 1, 1, 0)

#clean generation
CURRENT_YEAR = 2026
DATA_YEAR = 2024
GAP = CURRENT_YEAR - DATA_YEAR
dat$generation = cut(dat$age,
                     breaks = c(-Inf, 13-GAP, 29-GAP, 45-GAP, 61-GAP, 71-GAP, 80-GAP, 98-GAP, Inf),
                     labels = c("Alpha", "Z", "Millenial", "X", "Jones", "Boomer", "Post War", "WWII"))

#add real_income variable (accounting for inflation) for 2024
dat$realinc_2024 = dat$realinc * 2.86191

#changes factors to characters, ran into a problem encoding NA as "" for some
#variables, but this fixed it, applies a lambda (anonymous) function to the data
#frame and converts frame types to character types
dat[] = lapply(dat, function(x) if(is.factor(x)) as.character(x) else x)

#saved clean file with NA replaced as blanks
dat[is.na(dat)] = ""
write.csv(dat, "gss1_cleaned.csv")