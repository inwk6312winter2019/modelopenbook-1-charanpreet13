l1=[]
l2=[]
l3=[]
fin=open("running-config.cfg")
def list_ifname_ip(fin):
	for line in fin:
		line=line.strip()
		if "access-list" in line:
			if "transit_access_in" in line:
				l1.append(line)
			elif "fw-management_access_in" in line:
				l2.append(line)
			elif "global_access" in line:
				l3.append(line)
print(list_ifname_ip(fin))
print(l1)
print(l2)
print(l3)
