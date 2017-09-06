
import numpy as np

import pandas as pd
import operator



df_train = pd.read_csv('C:/Users/Tonk/Desktop/empcount2.csv', header=0, low_memory=False, dtype='object')



train_array = df_train.iloc[0:,0:].values
print (train_array)

m = ['01','02','03','04','05','06','07','08','09','10','11','12']


count = 0
for i in range(2004,2018):
    for j in m:
        print (i,j)
        count += 1

print (count)

d_i = train_array.shape[0]
d_j = train_array.shape[1]

print ("d & j")
print (d_i, d_j)

s = set(train_array[:,7])
print (s) # Creat the set of team.
print (len(s))

hire_output = np.zeros(shape=(count+1,len(s)+1), dtype=object)

caset = 1
for i in range(2004,2018):
    for j in m:
        hire_output[caset,0] = str(str(i)+str(j))
        caset +=1

index = 1
for j in s:
    hire_output[0,index] = str(j)
    index += 1
print (hire_output[:,0])

print (hire_output[0,:])

print (np.where(hire_output[:,0]=='200512')[0])
# for ii in range(train_array.shape[0]):

ind_m = np.where(hire_output[:,0]=='200512')[0]
ind_dep = np.where(hire_output[0,:]=='ACCOUNTING')[0]
print (hire_output[ind_m,0])

print (hire_output[0,ind_dep])

#
for i in range(d_i):
#for i in range(3):
    print (train_array[i,:])
    print (train_array[i,4][-2:])
    start_y = train_array[i,4][-2:]
    check = 0
    if int(start_y) >= 80 or int(start_y) < 4 :
        start_y = str(2004)
        check = 1
        #train_array[i, 4][:2] = '01'
    else:
        start_y = int(start_y) +  2000
        start_y = str(start_y)
    print ("test",start_y)

    start_m = (train_array[i,4][:2])
    print (start_m)
    if check == 1:
        start_wm = str(start_y) + str('01')
    else:
        start_wm = str(start_y) + str(start_m)
    print (start_wm)

    end_y = train_array[i, 6][-2:]
    if int(end_y) >= 80 or int(end_y) < 4:
        end_y = str(2004)
    else:
        end_y = int(end_y) + 2000
        end_y = str(end_y)
    print(end_y)
    print(end_y)
    end_m = (train_array[i, 6][:2])
    print(end_m)
    #print(str(end_y) + str(end_m))
    end_wm = str(end_y) + str(end_m)
    print(end_wm)

    ind_sm = np.where(hire_output[:,0]==start_wm)[0]
    ind_em = np.where(hire_output[:,0]==end_wm)[0]
    ind_dep = np.where(hire_output[0,:]== str(train_array[i, 7]))[0]

    print (ind_sm,' ', ind_em,' ',ind_dep)

    ii = 0
    kk = 0

    for ii in range(int(ind_sm),int(ind_em)+1):
        #print (ii)
        hire_output[ii,ind_dep] = int(hire_output[ii,ind_dep]) + 1

        #kk = 1

np.savetxt("C:/Users/Tonk/Desktop/empcount_outv2.csv", hire_output, delimiter=",", fmt='%s', header='')
#


#
# print()
# print("# Jaccard index calculation ----------")
# # Jaccard code start
#
# cust_i = cust_ind.shape[0]
# cust_j = cust_ind.shape[0]
# jaccard_output = np.zeros(shape=(cust_i,cust_j), dtype=float)
#
# # for i in range(0,100):              # try running 100 customers
# # ***  Uncomment if you wanna run all the jaccard again for all customers
# for i in range(0,cust_i):
#      try:
#          for j in range(0+i,cust_j):
#             # print (jaccard_similarity_score(np.array([train_array[1016]]), np.array([train_array[1016]])))
#             jaccard_output[j,i] = jaccard_similarity_score(np.array([train_array[i]]), np.array([train_array[j]]))
#
#      except ValueError:
#          print ('error on line :', i)
#
# # ***************************
#
# print (jaccard_output)
#
# import csv
# #
# # # Create the csv file for the train_input
# #
# fl = open('C:/Users/Tonk/Desktop/empcount_out.csv', 'w')
#
# writer = csv.writer(fl)
#
# #cust_ind_t = np.transpose(cust_ind)         # Transpose the customer array to concat as a header.
# # writer.writerow(cust_ind_t)
# #jaccard_output = np.vstack([cust_ind_t,jaccard_output])         # concat the header
#
#
#
#
#
# for values in hire_output:
#     writer.writerow(values)
#
# fl.close()



