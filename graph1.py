# this code is written for submission of assignment 1
# graphs replicated from https://www.cse.iitb.ac.in/~br/webpage/covid19/u5india/images/germany-birth-rate-drop.mp4 and
# https://www.dropbox.com/s/rrv0swipiroz3c2/u5news.pdf?dl=0
# graph of Birth Rate decline in germany quarterwise and yearwise-quarterwise

# Mohammed Azmat Khan
# python 3.9.6, Pandas, Matplotlib and attached file required


import pandas as pd
import matplotlib.pyplot as mt



path = 'D:/codes/py/iit_a1/12612-0002_$F.xlsx'
data = pd.read_excel(path)

df = pd.DataFrame(data)

months = df["months"].to_list()
year = df["year"].unique()

# setting year and month as index for navigation
df.set_index(['year','months'])
df.sort_index()


# removing extra values present
x = df.loc[57, 'in Total']
df['in Total'].replace(x, 0, inplace=True)

qs = []    
for i in range(0, 59, 3):
    qs.append( sum (df.loc[i:i+2, 'in Total']))

q_name = []


q_name = []
for a in year:
    for q in range (1, 5):
        q_name += ['Q' + str(q)+'-'+str(a)]


# plotting on graph year-wise results
y_pos = range(len(q_name))
mt.figure(figsize=(40, 10))
barplot = mt.bar (q_name, qs, width=0.75)
mt.xticks(y_pos, q_name, rotation=90)
mt.bar_label(barplot, labels=qs, label_type= 'edge', rotation=0)
mt.xlabel('Quarters')
mt.ylabel('Number of Births In Germany')
mt.title('German Birth Rate Decline Year-wise per Quarter', pad=20)
mt.show()

# make a dict
q_w = {'quarter': q_name, 'births' : qs}
q_wise = pd.DataFrame(q_w)

# set quarter as new index and sort to get a new dataframe
q_wise.set_index('quarter')
qw2 = q_wise.sort_values(by=['quarter'])

# plot quarter-wise results
qtr = qw2['quarter'].to_list()
brt = qw2['births'].to_list()

y_pos = range(len(qtr))
mt.figure(figsize=(40, 10))
bar2 = mt.bar (qtr, brt, width=0.75, color=(0.9, 0.7, 0.1, 0.5), edgecolor='green')
mt.bar_label(bar2, labels=qs, label_type= 'edge', rotation=0)
mt.xlabel('Quarters')
mt.ylabel('Number of Births In Germany')
mt.title('German Birth Rate Decline Quarter-wise', pad=20)
mt.xticks(y_pos, qtr, rotation=90)
mt.show()