# Merchant Category Recommendation
# Flexibility, boy, and action.

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

import os
print(os.listdir("../input"))

train = pd.read_csv('../input/train.csv', parse_dates=['first_active_month'])
test = pd.read_csv('../input/test.csv', parse_dates=['first_active_month'])

data_dictionary = pd.read_excel('../input/Data_Dictionary.xlsx', sheet_name='train')

train['feature_1'] = train['feature_1'].astype('category')
train['feature_2'] = train['feature_2'].astype('category')
train['feature_3'] = train['feature_3'].astype('category')

train.info()

fig, ax = plt.subplots(1, 3, figsize=(16,6))
train['feature_1'].value_counts().sort_index().plot(kind='bar', ax=ax[0], color='teal', title='feature_1');
train['feature_2'].value_counts().sort_index().plot(kind='bar', ax=ax[1], color='brown', title='feature_2');
train['feature_3'].value_counts().sort_index().plot(kind='bar', ax=ax[2], color='gold', title='feature_3')

test['feature_1'] = test['feature_1'].astype('category')
test['feature_2'] = test['feature_2'].astype('category')
test['feature_3'] = test['feature_3'].astype('category')

test.loc[test['first_active_month'].isna(), 'first_active_month'] = test.loc[(test['feature_1'] == 5) & (test['feature_2'] == 2) & (test['feature_3'] == 1), 'first_active_month'].min()

plt.hist(train['target'])
plt.title('Target distribution')

print('There are {0} samples with target lower than -20.'.format(train.loc[train['target'] < -20].shape[0]))

historical_transactions = pd.read_csv('../input/historical_transactions.csv')
history = pd.read_excel('../input/Data_Dictionary.xlsx', sheet_name='history')
