def maxDynamicProfit(k,prices):
	days = len(prices)
 	
 	#No need to solve in given situation
	if days < 2 or k <= 0:
		return 0

	#The problem is broken as we try solve with increasing transactions with all days till we reach k transactions
	llV = [[0 for x in xrange(k+1)] for x in xrange(days)]
	#Contains Solutions for k=i transactions for each day as last element in each row, contains the profit amount
	glV = [[0 for x in xrange(k+1)] for x in xrange(days)]
 
 	#Calculates the dynamic solution
 	#Used https://www.youtube.com/watch?v=oDhu5uGq_ic for reference
	for i in range(1,days,1):
		diff = prices[i] - prices[i - 1]
		for j in range(1,k+1,1):
			llV[i][j] = max(glV[i - 1][j - 1] + max(diff, 0) , (llV[i - 1][j] + diff))
			glV[i][j] = max(glV[i - 1][j], llV[i][j])

	return glV[days-1][k]


def maxGreedyProfit(k,prices):
	currentPrice=prices[0]
	profit=0
	transactions=0
	x=1
	while x<len(prices):
		if prices[x]-currentPrice>0:
			transactions=transactions+1
			profit=profit+prices[x]-currentPrice
			currentPrice=prices[x]
			#Select the lowest stock price in the future days greedy approach so to maximize profit
			for k in range(x+1,len(prices)-1,1):
				if prices[k]<currentPrice:
					currentPrice=prices[k]
					x=k
		if transactions==k:
			break
		#Stock If bought must be sold
		if x==len(prices)-1:
			profit=profit+prices[x]-currentPrice
		x=x+1
	return profit


price=[2,5,7,1,4,3,1,3]
transactions=3
print "***=====Best Time To Sell And buy Stock=====***"
print ""
print "Price List :",price
print "Max Transactions :",transactions
print ""
print "---Dynamic Approach---"
answer=maxDynamicProfit(transactions,price)
print "Max Profit :",answer
print ""
print "---Greedy Approach---"
answer=maxGreedyProfit(transactions,price)
print "Max Profit :",answer
print ""