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
                if(z[0]=="interface"):
                        interface.append(z[1])
                if(z[0]=="vlan"):
                        vlan.append(z[1])
                if(z[0]=="nameif"):
                        name.append(z[1])
                if(z[0]=="ip"):
                        ip_address.append(z[2])
                
        print("Interface:",interface)
        print("Vlan:",vlan)
        print("Name:",name)
        print("Ip address:",ip_address)

list_ifname_ip()
