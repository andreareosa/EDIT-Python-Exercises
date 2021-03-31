# -*- coding: utf-8 -*-
"""
DATA UNDERSTANDING AND DATA PREPARATION EXERCISE
"""

import pandas as pd


"""
FROM THE .CSV FILE TO A PANDAS DATAFRAME
"""

# 1 - READ CSV FILE ON PYTHON

myfile = r'C:\Users\andre\OneDrive\Ambiente de Trabalho\EDIT\PROGRAMA\01. Data Science Fundamental\Exercicios\Data Cleansing exercise\pima-indians-diabetes.csv'

data = pd.read_csv(myfile, header=None)
data_top = data.head()
data_top

data.columns 

# Currently there are no column names on our dataset

# 2 - CREATE A LIST OF VARIABLE NAMES FOR COLUMN NAMES
column_names = ['NPG','PGC','DBP','TST','SIC','BMI','DPF','AGE','DIA']

# 3 -READ CSV WITH THE NEW LIST AS THE COLUMN NAMES
data = pd.read_csv(myfile, names=column_names)
data.head()

# 4 - PRINT THE FIRST 10 ROWS OF THE DATASET
data_top10 = data.head(10)
data_top10

# 5 - PRINT A SUMMARY OF THE DATA (HINT: use pandas describe)
data_summary = data.describe()
data_summary

# 6 - IDENTIFY THE NUMBER OF ROWS AND COLUMNS OF THE DATAFRAME
len(data)
len(data.columns)

#OR
data.shape

# 7 - IDENTIFY THE DATATYPES OF EACH COLUMN
data.dtypes


# 8 - CHECK IF THE DATASET IS WELL BALANCED (diabetic vs non-diabetic)
balance = data.groupby('DIA').size()
balance

# 0 - (Non-diabetic) = 500
# 1 - (Diabetic) = 268


"""
DATA CLEANSING
"""

# CHECK FOR POSSIBLE NULL VALUES OR MISSING VALUES
data.info()

# There are no null values. But what about missing values?
# They can be "disguised"!
# For example columns 2 through 6 should not have zeros:
    # for example DBP: Blood pressure can't be 0 or the person is dead...

# 1 - REPLACE ZEROS BY NAN(Not a number) ON COLUMNS 2 THROUGH 6
import numpy as np

# iloc[rows,columns]
# utilizamos : para selecionar todas as linhas
data.iloc[:,1:7] = data.iloc[:,1:7].replace(0,np.NaN)

# 2 - PRINT A SUMMARY OF THE DATE - missing values have been removed
data.describe()


"""
PLOTTING - visualize the information
"""

# 1 - CREATE A BOX PLOT AND SAVE IT INTO A FILE
# Hint: Data frame has plot.xxx functions to create the box
# Import matplotlib.pyplot as plt to save the file

import matplotlib.pyplot as plt

data.plot.box(figsize=(6,6)) # tuple with dimensions of the figure
plt.savefig('box_plot.png',dpi=300,bbox_inches='tight')

# dpi = resolution
# 'tight' = no border

plt.close()

# A imagem foi salva no seguinte diretorio 
os.getcwd() # as "box_plot.png"

"""
TÉCNICAS DE RESCALING - ajustar as escalas do gráfico
"""

# 1 - NORMALIZATION 
# Não é possivel perceber a distribuição das variáveis
# Fórmula de normalização

norm_data = (data - data.min()) / (data.max() - data.min())
#NOTA: O pandas faz estas operações coluna a coluna

norm_data.plot.box(figsize=(6,6))
plt.savefig('norm_box_plot.png',dpi=300,bbox_inches='tight')
plt.close()

# 2 - STANDARDIZATION 

standard_data = (data - data.mean()) / (data.std())

standard_data.plot.box(figsize=(6,6))
plt.savefig('standard_box_plot.png',dpi=300,bbox_inches='tight')
plt.close() 



"""
SCATTERPLOT MATRIX - matrix of pairwise scatterplots

Para identificar correlações:
Diagonal - distribuição da própria variável
Fora da diagonal - distribuição com outras variáveis

É possivel desenhar uma reta que una os pontos? Sim? Correlação
Pontos disporsos? Não há correlação
"""

from pandas.plotting import scatter_matrix

# Normal Scatter plot
scatter_matrix(data,figsize=(12,12))
plt.savefig('scatter_plot.png',dpi=300,bbox_inches='tight')

# KDE Scatter plot
scatter_matrix(data,figsize=(12,12), diagonal='kde')
plt.savefig('kde_scatter_plot.png',dpi=300,bbox_inches='tight')


"""
Pearson correlation coefficient

r varia entre -1 e 1:
    r mais próximo de 1 = correlação positiva forte
    4 mais perto de -1 = correlação negativa forte
"""

# 1 - Implement a correlation matrix for this dataframe
    
corr = data.corr(method='pearson')
corr    

# Dataframe opções de visualização para mostrar até 100 colunas de 1 dataframe
pd.set_option('display.max_columns',100)  

# 2 - # Draw a correletion heat map with values

import seaborn as sns

sns.heatmap(corr.round(2), annot=True) #annot = True para aparecerem os valores



