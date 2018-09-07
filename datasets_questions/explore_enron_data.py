#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# count=0
# for per in enron_data:
# 	if(enron_data[per]["poi"]==1):
# 		count += 1

# print count

# import sys
# sys.path.insert(0, '../final_project/')
# import poi_email_addresses
# print len(poi_email_addresses.poiEmails())

# print enron_data['PRENTICE JAMES']

count=0
for per in enron_data:
	if(enron_data[per]["salary"]=="NaN"):
		pass
	else:
		count += 1
 
print count

count1=0
for per in enron_data:
	if(enron_data[per]["email_address"]=="NaN"):
		pass
	else:
		count1 += 1
  
print count1
 