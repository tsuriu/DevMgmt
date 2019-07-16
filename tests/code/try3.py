from snmpgetdt import Snmp, ZTE

hst = ZTE('10.56.1.142','SquidT3l3c0m',2)

D = hst.disc_onu_cfg()


for i in list(D.keys()): print(D[i])

#print(D)
