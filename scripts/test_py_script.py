import pandas as pd
import argparse
from sklearn import svm
import random

#parser = argparse.ArgumentParser()
#parser.add_argument('--input', default = None)
#parser.add_argument('--header', default = True)
#args = parser.parse_args()
#
#print(args)

filename = '../data/FY2019_070_Contracts_Full_20200110_1.csv'

data = pd.read_csv(filename)

def over_thresh(fao):
    if fao < -1000:
        return 1
    else:
        return 0

data['signif_deob'] = data.apply(lambda x : over_thresh(x['federal_action_obligation']), axis = 1)

data['potential_pct'] = data['total_dollars_obligated']/ data['potential_total_value_of_award']

data['current_pct'] = data['total_dollars_obligated']/data['current_total_value_of_award']

data['pct_of_totals'] = data['current_total_value_of_award']/data['potential_total_value_of_award']


print(data.columns)


#todo impute missing data
data1 = data[['signif_deob' , 'potential_pct', 'current_pct', 'pct_of_totals', 'total_dollars_obligated', 'current_total_value_of_award', 'potential_total_value_of_award','base_and_exercised_options_value','base_and_all_options_value']].dropna()

X = data1[['potential_pct', 'current_pct', 'pct_of_totals', 'total_dollars_obligated', 'current_total_value_of_award', 'potential_total_value_of_award','base_and_exercised_options_value','base_and_all_options_value']]
Y = data1[['signif_deob']]

print(data1.shape)
print(X.shape)
print(Y.shape)

row_ct = data1.shape[0]

train_ct = round(row_ct * 0.8)

train_rows_idx = random.sample(range(0,row_ct), train_ct)
test_rows_idx = [i for i in range(0,row_ct) if i not in train_rows_idx]

print(len(train_rows_idx))
print(len(test_rows_idx))

train_X = X.iloc[train_rows_idx]
train_Y = Y.iloc[train_rows_idx]

test_X = X.iloc[test_rows_idx]
test_Y = Y.iloc[test_rows_idx]

classifier = svm.SVC(kernel='linear', C=1.0)

#DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
#  y = column_or_1d(y, warn=True)
#
classifier.fit(train_X,train_Y)

classifier.predict(test_X, test_Y)




