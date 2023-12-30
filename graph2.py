# this code is written for submission of assignment 1
# graphs replicated from https://www.dropbox.com/s/3umwd17xi4e0kh0/age-wise-excess-deaths.pdf?dl=0 article
# graph of deaths due to natural cause for each age group from 2019-2021


# Mohammed Azmat Khan
# python 3.9.6, Pandas, Matplotlib and attached file required


import pandas as pd 
import matplotlib.pyplot as plt



path = 'D:/codes/py/iit_a1/AH_Monthly_Provisional_Counts_of_Deaths_by_Age_Group_and_HHS_region_for_Select_Causes_of_Death__2019-2021.csv'
data = pd.read_csv(path)
df = pd.DataFrame(data)

# setting index for sorting/grouping in future
df.set_index(['Date Of Death Year', 'Date Of Death Month', 'NaturalCause', 'AgeGroup'])
df.groupby(by=[ 'Date Of Death Year', 'Date Of Death Month'])

# extract values for agegroup for iteration
grps = df['AgeGroup'].unique()
grps = list(grps)


# for 15-24 years not necessary just for extracting  years and month as list and can be removed
mask15_24 = df['AgeGroup'] == '15-24 years' #& df['Date Of Death Month'] == '2019'
df15_24  = pd.DataFrame(df[mask15_24])
df15_24.set_index(['Date Of Death Year', 'Date Of Death Month', 'NaturalCause'])
df15_24.groupby(by=['Date Of Death Year', 'Date Of Death Month'])


yrs = df15_24['Date Of Death Year'].unique()
yrs = list(yrs)
mnth = df15_24['Date Of Death Month'].unique()
mnth = list(mnth)


#newdf =  df.loc[(df['AgeGroup'] == '15-24 years') & (df['Date Of Death Year'] == 2019)].sort_values(by='Date Of Death Month')
#newdf.set_index('Date Of Death Month')

for grp in grps:
    g = []
    for y in yrs:
        newdf =  (df.loc[(df['AgeGroup'] == grp) & 
                         (df['Date Of Death Year'] == y)].sort_values(by='Date Of Death Month'))
        newdf.set_index('Date Of Death Month')
        g.append(newdf.groupby(by='Date Of Death Month').sum().loc[: , 'NaturalCause'].to_list())

    #plotting for current age group
    plt.plot (mnth, g[0])
    plt.plot (mnth, g[1])
    plt.plot (mnth[0:7], g[2])
    plt.xticks(mnth)
    plt.xlabel('Months')
    plt.ylabel('Natural Cause Death ('+grp+')')
    plt.legend(['2019', '2020', '2021'])
    plt.show ()


# --------------------------- end ---------------------------------