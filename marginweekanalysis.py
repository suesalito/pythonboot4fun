import numpy as np

import pandas as pd
import operator



df_train = pd.read_csv('/Users/suesalito/Desktop/Python/datatest.csv', header=0, low_memory=False, dtype='object')



train_array = df_train.iloc[0:,0:].values
print (train_array)



s = set(train_array[:,9])

print (s)

hire_output = np.zeros(shape=(len(s)+1,4), dtype=object)

print(hire_output)

hire_output[0,0] = 'WeekNo.'
hire_output[0,1] = 'Sales'
hire_output[0,2] = 'Cost'
hire_output[0,3] = 'Margin'

ii = 0
for o in s:
    hire_output[1+ii:,0] = o
    ii += 1

print (hire_output[1:,0])

print(hire_output)

for i in range(train_array.shape[0]):
    start_m = (train_array[i, 9])
    #print (start_m)
    ind_sm = np.where(hire_output[:, 0] == start_m)[0]
    #Sales = 6, Cost =7, Margin = 8

    hire_output[ind_sm,1] +=  float(train_array[i, 6])
    hire_output[ind_sm, 2] += float(train_array[i, 7])
    hire_output[ind_sm, 3] += float(train_array[i, 8])



    #print (ind_sm)
    #print (i)
print (hire_output)

np.savetxt("/Users/suesalito/Desktop/Python/datatest_out.csv", hire_output, delimiter=",", fmt='%s', header='')
