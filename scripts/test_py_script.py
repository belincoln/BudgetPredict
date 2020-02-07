import pandas as pd
import argparse
from sklearn import svm

#parser = argparse.ArgumentParser()
#parser.add_argument('--input', default = None)
#parser.add_argument('--header', default = True)
#args = parser.parse_args()
#
#print(args)

filename = '../data/FY2019_070_Contracts_Full_20200110_1.csv'

data = pd.read_csv(filename)

def over_thresh(fao):
    if fao < -7000:
        return 1
    else:
        return 0

data['signif_deob'] = data.apply(lambda x : over_thresh(x['federal_action_obligation']), axis = 1)

data['potential_pct'] = data['total_dollars_obligated']/ data['potential_total_value_of_award']

data['current_pct'] = data['total_dollars_obligated']/data['current_total_value_of_award']

data['pct_of_totals'] = data['current_total_value_of_award']/data['potential_total_value_of_award']


print(data.columns)

data1 = data[['signif_deob' , 'potential_pct', 'current_pct', 'pct_of_totals', 'total_dollars_obligated', 'current_total_value_of_award', 'potential_total_value_of_award']]

X = data1[['potential_pct', 'current_pct', 'pct_of_totals', 'total_dollars_obligated', 'current_total_value_of_award', 'potential_total_value_of_award']]
Y = data1[['signif_deob']]

print(data1.shape)
print(X.shape)
print(Y.shape)

classifier = svm.SVC

classifier.fit(X,Y)



