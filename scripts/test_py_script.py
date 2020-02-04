import pandas as pd
import argparse
from sklearn import svm

parser = argparse.ArgumentParser()
parser.add_argument('--input', default = None)
parser.add_argument('--header', default = True)
args = parser.parse_args()

print(args)

filename = args.input

data = pd.read_csv(filename)
print(data.shape)

def over_thresh(fao):
    if fao < -7000:
        return 1
    else:
        return 0

data['signif_deob'] = data.apply(lambda x : over_thresh(x['federal_action_obligation']), axis = 1)



