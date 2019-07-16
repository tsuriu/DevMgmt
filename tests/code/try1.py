from easysnmp import Session as S

s = S(hostname='10.56.1.142',community='SquidT3l3c0m',version=2)

items = s.walk('.1.3.6.1.4.1.3902.1015.2.1.1.3.1.4.1.1')
items2 = s.walk('.1.3.6.1.2.1.31.1.1.1.1')


print(type(items))

print("##############")

for item in items2:
    print(item.oid,item.oid_index,item.value)
