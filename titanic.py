# -*- coding: utf-8 -*-
"""
TITANIC DATASET
EXPLORATORY DATA ANALYSIS - 17/05/2021
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
IMPORT TITANIC DB USING SEABORN
"""

train = sns.load_dataset("titanic")
train.head()
pd.set_option('display.max_columns',100)  


"""
DATASET COLUMNS:
    
pclass - passgener class
sibsp - siblings or spouse 
parch - family aboard
fare - price
embarked - port of shipment - REMOVE COLUMN (duplicated column)
class - class - REMOVE COLUMN (duplicated column)
who - man, woman or child
adult_male - REMOVE COLUMN (duplicated column)
deck - ship compartment 
embark town - port of shipment
alive 
alone - REMOVE COLUMN (duplicated column)
"""

"""
DATA UNDERSTANDING
"""
train.shape
train.dtypes

"""
DATA CLEANSING - Drop "useless" columns
"""
train.info()
train = train.drop(columns=['embarked','class','adult_male','alone'])
train.shape

"""
MISSING VALUES
"""
train.info()

# There are missing values in column "age", "deck" and "embark town"

# DECK - there are many missing values (nearly 80%) therefore we should drop the column
train = train.drop(columns=['deck'])

# AGE - there are 177 missing values and we will replace those values by the mean w/ pclass variable
train.iloc[:,3] = train.iloc[:,3].replace('male',3)

train['age'] = train['age'].groupby([train['pclass'], train['sex']]).apply(lambda x: x.fillna(x.mean()))
train.info()

# EMBARK TOWN - there are only 2 missing therefore we will replace them by the mode
train.iloc[:,8] = train.iloc[:,8].fillna(0)
train.info()

"""
CLEANING THE REMAINING DATA
"""

#COLUMN SEX
train.iloc[:,2] = train.iloc[:,2].replace('male',0)
train.iloc[:,2] = train.iloc[:,2].replace('female',1)

#COLUMN WHO
train.iloc[:,7] = train.iloc[:,7].replace('man',0)
train.iloc[:,7] = train.iloc[:,7].replace('woman',1)
train.iloc[:,7] = train.iloc[:,7].replace('child',2)

#COLUMN EMBARK TOWN
train.iloc[:,8] = train.iloc[:,8].replace('Southampton',0)
train.iloc[:,8] = train.iloc[:,8].replace('Cherbourg',1)
train.iloc[:,8] = train.iloc[:,8].replace('Queenstown',2)

#COLUMN ALIVE
train.iloc[:,9] = train.iloc[:,9].replace('yes',1)
train.iloc[:,9] = train.iloc[:,9].replace('no',0)

"""
EXPLORATORY ANALYSIS
"""
train.describe()

"""
CORRELATION HEAT MAP
"""
corr = train.corr(method='pearson')
corr    

sns.heatmap(corr.round(2), annot=True) 

#Highest correlations = sex, class e who

"""
BOX PLOT
"""
ax = sns.boxplot(x="pclass", y="age", data=train)

#Conclusion = 1st class has older people

"""
AGE DISTRIBUTION
"""

with sns.plotting_context("notebook",font_scale=1.5):
    sns.set_style("whitegrid")
    sns.distplot(train["age"].dropna(),
                 bins=80,
                 kde=False,
                 color="red")
    sns.plt.title("Age Distribution")
    plt.ylabel("Count");

#Conclusion = most of the passengers age are between 20 and 40 years old

"""
BAR CHART
"""

sns.set(font_scale=1)

g = sns.factorplot(x="sex", y="survived", col="pclass",
                    data=train, saturation=.5,
                    kind="bar", ci=None, aspect=.6)
(g.set_axis_labels("", "Survival Rate")
    .set_xticklabels(["Men", "Women"])
    .set_titles("{col_name} {col_var}")
    .set(ylim=(0, 1))
    .despine(left=True))  
plt.subplots_adjust(top=0.8)
g.fig.suptitle('How many Men and Women Survived by Passenger Class');

#Conclusion: no matter in which class, woman tent to survive more than man

"""
SCATTER PLOT
"""
f, ax = plt.subplots(1,1, figsize=(10, 5))
sns.scatterplot(x="pclass", y="age", hue="survived", data=train, ax=ax);

#Conclusion: most passengers of 3rd class died as most of the passangers
# in the 1st class survided (only the elder ones in 1st class died)







