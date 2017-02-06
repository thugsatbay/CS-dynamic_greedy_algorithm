def calculateDynamicHP(dungeon):
	r = len(dungeon)
	c = len(dungeon[0])#column

	#Declaring the hp dp table, hp at given cell before encountering daemons or magic orbs
	hp=[[0 for x in xrange(c)] for x in xrange(r)]

	#initialize the hp value when knight reaches prince cell.
	hp[r - 1][c - 1] = max(1 - dungeon[r - 1][c - 1], 1)

	#last column
	for i in range(r-2,-1,-1):
		hp[i][c - 1] = max(hp[i + 1][c - 1] - dungeon[i][c - 1], 1)

	#last row
	for j in range(c-2,-1,-1):
		hp[r - 1][j] = max(hp[r - 1][j + 1] - dungeon[r - 1][j], 1)

	#calculate dynamic hp table
	for i in range(r-2,-1,-1):
		for j in range(c-2,-1,-1):
			down = max(hp[i + 1][j] - dungeon[i][j], 1)
			right = max(hp[i][j + 1] - dungeon[i][j], 1)
			hp[i][j] = min(right, down)

	
	pr,pc=0,0
	moves=[]
	for x in xrange(r+c-2):
		if pr!=r-1 and pc!=c-1:
			if hp[pr+1][pc]<hp[pr][pc+1]:
				pr=pr+1
				moves.append("down")
			else:
				pc=pc+1
				moves.append("right")
		else:
			if pr==r-1:
				pc=pc+1
				moves.append("right")
			else:
				pr=pr+1
				moves.append("down")
	print "Steps Taken :",list(moves)
	return hp[0][0]


def calculateGreedyHP(dungeon):
	r = len(dungeon)
	c = len(dungeon[0])#column

	originalHP=1

	currentHP = max(1,originalHP + dungeon[0][0])
	originalHP = originalHP - min(0,dungeon[0][0])
	
	moves=[]
	pr,pc=0,0
	for i in xrange(r+c-2):
		if pr!=r-1 and pc!=c-1:
			#print dungeon[pr+1][pc],dungeon[pr][pc+1]
			if dungeon[pr+1][pc]>dungeon[pr][pc+1]:
				pr=pr+1
				moves.append("down")
			else:
				pc=pc+1
				moves.append("right")
		else:
			if pr==r-1:
				pc=pc+1
				moves.append("right")
			else:
				pr=pr+1
				moves.append("down")
		currentHP = currentHP + dungeon[pr][pc]
		if currentHP<=0:
			originalHP = originalHP + 1 - currentHP
			currentHP = 1

	print "Steps Taken :",list(moves)
	return originalHP


dungeon1=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon2=[[-2,-3,3],[-2,-10,1],[10,30,-5]]
dungeon3=[[-2,-3,5],[3,-10,3],[-10,2,2]]

print "***=====Dungeon Game=====***"
print ""
print "Dungeon :",dungeon1
print ""
print "---Dynamic Approach---"
answer=calculateDynamicHP(dungeon1)
print "Minimum HP Required :",answer
print ""
print "---Greedy Approach---"
answer=calculateGreedyHP(dungeon1)
print "Minimum HP Required :",answer
print "\n"
print "Dungeon :",dungeon2
print ""
print "---Dynamic Approach---"
answer=calculateDynamicHP(dungeon2)
print "Minimum HP Required :",answer
print ""
print "---Greedy Approach---"
answer=calculateGreedyHP(dungeon2)
print "Minimum HP Required :",answer
print "\n"
print "Dungeon :",dungeon3
print ""
print "---Dynamic Approach---"
answer=calculateDynamicHP(dungeon3)
print "Minimum HP Required :",answer
print ""
print "---Greedy Approach---"
answer=calculateGreedyHP(dungeon3)
print "Minimum HP Required :",answer
print ""