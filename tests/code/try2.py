sys.path.inser(0, '../../../protocol/snmpc.py')
from snmpc import Snmp

oid = '.1.3.6.1.2.1.1.3.0'
oid2 = '.1.3.6.1.2.1.31.1.1.1.1'

D = Snmp('10.56.1.142','SquidT3l3c0m',2)

#DD = D.Get(oid)
DDD = D.Walk(oid2)
for DD in list(DDD.keys()):
    print(DDD[DD])   
