#!/usr/bin/python

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

sume=0

for counter in enron_data["SKILLING JEFFREY K"]:
	sume=sume+1

print(sume)

counter=0

for person_name in enron_data:
	if enron_data[person_name]["poi"]==1:
		counter = counter+1

print(counter)


print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
