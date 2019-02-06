fin=open("Street_Centrelines.csv","r")
def easy(fin):
	list1=[]
	for line in fin:
		line=line.split(",")
		list1.append((line[2],line[4],line[6],line[7]))
	return list1

print(easy(fin))

fin=open("Street_Centrelines.csv","r")
def histogram(fin):
	d=dict()
	for line in fin:
		line=line.split(",")
		if line[12] not in d:
			d[line[12]]=1
		else:
			d[line[12]]+=1
	return d	
print(histogram(fin))
