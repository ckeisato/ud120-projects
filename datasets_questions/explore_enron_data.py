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

def printNumEntries(data):
  num_entries = len(enron_data)
  print "number of entries", num_entries
# printNumEntries(enron_data)

def printNumFeatures(data):
  keys = list(enron_data.keys())
  features = enron_data[keys[0]]
  num_features = len(features)
  print "number of features", num_features
# printNumFeatures(enron_data)

def printNumPois(data):
  accum = 0
  for person in data:
    if data[person]["poi"] == True:
      accum = accum + 1
  print "number of pois", accum
# printNumPois(enron_data)

def getFeature(data, name, feature):
  return data[name][feature]

def printTotalStockValue(data, name):
  print "total stock value for ", name, ": ", getFeature(data, name, "total_stock_value")
# printTotalStockValue(enron_data, "PRENTICE JAMES")

def printEmailsToPOI(data, name):
  print "number of emails from ", name, " to POI: ", getFeature(data, name, "from_this_person_to_poi")
# printEmailsToPOI(enron_data, "COLWELL WESLEY")

def printExercisedStockOptions(data, name):
  print "exercised stock options of ", name, ":" , getFeature(data, name, "exercised_stock_options")
# printExercisedStockOptions(enron_data, "SKILLING JEFFREY K")

def getTotalPayments(data):
  skilling = "SKILLING JEFFREY K"
  fastow = "FASTOW ANDREW S"
  lay = "LAY KENNETH L"
  print skilling, data[skilling]["total_payments"]
  print fastow, data[fastow]["total_payments"]
  print lay, data[lay]["total_payments"]
# getTotalPayments(enron_data)

def getFeatures(data):
  print "MCMAHON JEFFREY", data["MCMAHON JEFFREY"]
# getFeatures(enron_data)

def getNumKnownFeature(data, feature):
  accum = 0
  for person in data:
    if data[person][feature] != "NaN":
      accum = accum + 1
  print accum, "number of people have a known ", feature
getNumKnownFeature(enron_data, "salary")
getNumKnownFeature(enron_data, "email_address")
