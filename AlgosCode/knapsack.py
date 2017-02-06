def kanpsack01Dynamic(weights,values,maxwght):

	maxV = [[0 for x in xrange(maxwght+1)] for x in xrange(len(weights))]

	#First Row with value of corresponding weight
	for i in xrange(maxwght+1):
		if weights[0]<=i:
			maxV[0][i]=values[0]

	for i in range(1,len(weights),1):
		for j in range(1,maxwght+1,1):
			if j==0:
				#First Column to be 0
				maxV[i][j] = 0.0
			elif weights[i] <= j:
				#max of (value when item(ith) not included and value of when item(ith) included with value of remaining weight)
				maxV[i][j] = max(maxV[i-1][j] , values[i] + maxV[i-1][j-weights[i]])
			else:
				#if weight is bigger than knapsack just forget about adding it
				maxV[i][j] = maxV[i-1][j]

	
	pr,pc=len(weights)-1,maxwght
	items=[]
	#Finding which items to include
	while pr!=0 and pc!=0:
		if maxV[pr][pc]!=maxV[pr-1][pc]:
			items.append(weights[pr])
			pc=pc-weights[pr]
		else:
			pr=pr-1
		if pc>0 and pr==0:
			items.append(weights[pr])
			break

	print "Items Included in knapsack :",list(reversed(items))
	return maxV[len(weights)-1][maxwght]


def knapsack01Greedy(weights,values,maxwght):
	items = []
	maxValue = 0
	
	#Greedy approach of selecting the item with max value first
	while len(values)>0:
		maxV = max(values)
		indexV = values.index(maxV)
		if weights[indexV] < maxwght:
			maxwght = maxwght - weights[indexV]
			items.append(weights[indexV])
			maxValue = maxV + maxValue
		del values[indexV]
		del weights[indexV]

	print "Items Included in knapsack :",list(reversed(items))
	return maxValue


def fractionalKnapsackGreedy(weights,values,maxwght):
	items = []
	maxValue = 0.0

	density=[float(values[x])/float(weights[x]) for x in xrange(len(weights))]
	while maxwght>0:
		maxD = max(density)
		indexD = density.index(maxD)
		if weights[indexD] < maxwght:
			maxwght = maxwght - weights[indexD]
			items.append(weights[indexD])
			maxValue = values[indexD] + maxValue
		else:
			items.append(weights[indexD])
			maxValue = float(maxD*maxwght) + maxValue
			maxwght = 0
		del values[indexD]
		del weights[indexD]
		del density[indexD]

	print "Items Included in knapsack :",list(reversed(items))
	return maxValue


def fractionalKnapsackDynamic(weights,values,maxwght):

	maxV = [[0.0 for x in xrange(maxwght+1)] for x in xrange(len(weights))]

	#First Row with value of corresponding weight
	for i in xrange(maxwght+1):
		if weights[0]<=i:
			maxV[0][i]=values[0]

	for i in range(1,len(weights),1):
		for j in range(1,maxwght+1,1):
			if j==0:
				#First Column to be 0
				maxV[i][j] = 0.0
			elif weights[i] <= j:
				#max of (value when item(ith) not included and value of when item(ith) included with value of remaining weight)
				maxV[i][j] = max(maxV[i-1][j] , values[i] + maxV[i-1][j-weights[i]])
			else:
				#if weight is bigger than knapsack just forget about adding it
				maxV[i][j] = max(maxV[i-1][j] , float(values[i])/weights[i]*j)

	return maxV[len(weights)-1][maxwght]


weights=[1,3,4,5]
values=[1,4,5,7]
maxwght=7
print "***=====0/1 Knapsack=====***"
print ""
print "Weights :",weights,"Corresponding Values :",values
print "Maximum weight of knapsack :",maxwght
print ""
print "---Dynamic Approach---"
answer=kanpsack01Dynamic(weights,values,maxwght)
print "Max Value :",answer
print ""
weights=[1,3,4,5]
values=[1,4,5,7]
maxwght=7
print "---Greedy Approach---"
answer=knapsack01Greedy(weights,values,maxwght)
print "Max Value :",answer
print ""
print ""
weights=[1,3,4,5]
values=[1,4,5,7]
maxwght=7
print "***=====Fractional Knapsack=====***"
print ""
print "Weights :",weights,"Corresponding Values :",values
print "Maximum weight of knapsack :",maxwght
print ""
print "---Greedy Approach---"
answer=fractionalKnapsackGreedy(weights,values,maxwght)
print "Max Value :",answer
print ""
weights=[1,3,4,5]
values=[1,4,5,7]
maxwght=7
print "---Dynamic Approach---"
answer=fractionalKnapsackDynamic(weights,values,maxwght)
print "Max Value :",answer
print ""