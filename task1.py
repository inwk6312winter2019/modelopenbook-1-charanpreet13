def list_ifname_ip():
        list=[]
        file=open("running-config.cfg","r")
        for word in file:
                list.append(word)
        interface=[]
        vlan=[]
        name=[]
        ip_address=[]
        for j in list:
                x=""
                y=""
                z=j.split()
