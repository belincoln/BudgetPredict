import pandas as pd
import argparse
from sklearn import svm


#parser = argparse.ArgumentParser()
#parser.add_argument('--input', default = None)
#parser.add_argument('--header', default = True)
#args = parser.parse_args()

print('Loading data...')

filename = '../data/FY2019_070_Contracts_Full_20200110_1.csv'

data = pd.read_csv(filename)
print(data.shape)

def over_thresh(fao):
    if fao < -1000:
        return True
    else:
        return False

data['signif_deob'] = data.apply(lambda x : over_thresh(x['federal_action_obligation']), axis = 1)
data['action_date'] = pd.to_datetime(data['action_date'])
data['period_of_performance_start_date'] = pd.to_datetime(data['period_of_performance_start_date'])
data['period_of_performance_current_end_date'] = pd.to_datetime(data['period_of_performance_current_end_date'])
print(data.info(verbose = True))


print('Creating classification model...')
classifier = svm.SVC()

X = data.drop(['signif_deob'], axis = 1)
Y = data['signif_deob']

classifier.fit(X,Y)

print(classifier)
print(type(classifier))


