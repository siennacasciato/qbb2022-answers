#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

#exercise 2 question 1
df = np.genfromtxt("joined_final", delimiter = ",", dtype = None, encoding = None, names = True)

#exercise 2 question 2
mdnm = df["mother_dnm"]
mage = df["mother_age"]

fig, ax = plt.subplots()
ax.scatter(mage,mdnm)
plt.xlabel("Mother Age")
plt.ylabel("Number of Maternal De Novo Mutations")
plt.title("Relationship Between Maternal Age and Number of De Novo Mutations")
#plt.show()
#plt.savefig("ex2_a.png")


fdnm = df["father_dnm"]
fage = df["father_age"]

fig, ax = plt.subplots()
ax.scatter(fage,fdnm)
plt.xlabel("Father Age")
plt.ylabel("Number of Paternal De Novo Mutations")
plt.title("Relationship Between Paternal Age and Number of De Novo Mutations")
#plt.show()
#plt.savefig("ex2_b.png")


#exercise 2 question 3
full_model = smf.ols(formula= "mother_dnm ~ 1 + mother_age", data = df).fit()
print(full_model.summary())
print(full_model.pvalues)

#exercise 2 question 4
full_model = smf.ols(formula= "father_dnm ~ 1 + father_age", data = df).fit()
print(full_model.summary())
print(full_model.pvalues)


#exercise 2 question 5
fig, ax = plt.subplots()
ax.hist(df["mother_dnm"], label = "Mother")
ax.hist(df["father_dnm"], label = "Father")
ax.set_xlabel("Number of De Novo Mutations")
ax.set_ylabel("Frequency of De Novo Mutations")
ax.legend()
#plt.show()
plt.savefig("ex2_c.png")


#exercise 2 question 6
full_model2 = smf.ols(formula= "father_dnm ~ 1 + mother_dnm", data = df).fit()
print(full_model2.summary())
print(full_model2.pvalues)

#exercise 2 question 7
full_model3 = smf.ols(formula= "father_dnm ~ 1 + father_age", data = df).fit()
print(full_model3.summary())
print(full_model3.pvalues)

y=1.3538 
b = 10.3263
m = 1.3538
y = number of mutations
x = age (50.5)
