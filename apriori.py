import collections
import copy

"""Reads file and put it on an array of arrays structure"""
def loadFile(filename):
  f = open(filename, "r")
  data = []
  # Discard first line
  f.readline()
  # Append each line to array, splitting the line by comma
  for line in f:
    data.append(line.strip().split(','))
  # Close file and return data structure
  f.close()
  return data

"""Apply the apriori algorithm to a supplied dataset with the given support and confidence"""
def apriori(data, sup, conf):
  # Generating all itemsets of size 1
  frequencies = firstItemset(data)
  # Deleting not frequent items based on the support
  for item in frequencies.keys():
    if frequencies[item]/float(len(data)) < sup:
      del frequencies[item]

  # generating candidate set of size k+1
  k = 2
  itemset = generateItemset(frequencies)
  frequencies = {} 
  for item in itemset:
    for transaction in data:
      if in_transaction(transaction, item):
        if item in frequencies.keys():
          frequencies[item] += 1
        else:
          # initialize if item wasn't already in the dict
          frequencies[item] = 1
  
  return frequencies

def in_transaction(transaction, item):
  return all(x in transaction for x in item)


"""Generate first itemset of size 1 and the frequencies for each item"""
def firstItemset(data):
  # Store the item and its frequency in an ordered dict structure
  frequencies = collections.OrderedDict()
  # Count for each item in a transaction its frequency
  for transaction in data:
    for item in transaction:
	  # a list of one element is used because it will be better 
	  # when dealing with itemsets of a larger size
      if (item,) in frequencies:
        frequencies[(item,)] += 1
      else:
	    # initialize if item wasn't already in the dict
        frequencies[(item,)] = 1
  return frequencies


"""Generate a new itemset based on a previous itemset where the 
new itemset has size of the previous + 1 and the items are 
combinations of frequent items in the previous itemset"""
def generateItemset(frequencies):
  # Get the ordered keys from the frequencies dictionary
  itemset = frequencies.keys()
  new_itemset = []
  for i in xrange(len(itemset)):
    for j in xrange(i + 1, len(itemset)):
      if itemset[i][:-1] == itemset[j][:-1] and itemset[i][-1] < itemset[j][-1]:
	    candidate = itemset[i] + (itemset[j][-1],)
	    new_itemset.append(candidate)
      else:
        next
  return new_itemset

data = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
#loadFile("exemplo.csv")
print apriori(data, 0.5, 0.5)  
