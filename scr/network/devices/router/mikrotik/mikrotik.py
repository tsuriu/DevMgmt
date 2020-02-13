import sys, re
sys.path.append('../../../protocols/')

from protocols.sshc import ssh

class mkt:
    CmdL = {
            'getPPPoEiface':'/interface pppoe-server server print terse',
            'usrONiface':'/interface pppoe-server print count-only where service=%s',
            }

    def __init__(self,host,usr,passwd):
        self.host = host
        self.usr = usr 
        self.passwd = passwd 
        self.session = ssh(self.host,self.usr,self.passwd)

    def parsedt(lst):
        lstret = {}

        lst = lst.splitlines()

        for line in lst:
            line = re.sub(' +',',',line)
            line = line.split(" ")
            line_id = line[0]

            dt = {}

            for dt in line[1:]:
                key,value = dt.split("=")
                dt.uptade({str(key):str(value)})

            lstret.update({line_id:dt})

        return lstret


    def usr_oniface(self):
        actusr = {}
        s = self.session

        ifaceL = s.execute(CmdL['getPPPoEiface'])
        ifaceL = self.parsedt(ifaceL)

        for ifid in list(ifaceL.keys()):
            ifn = ifaceL[ifid]['interface']

            usrs = s.execute(CmdL['usrONiface']%ifn)
            usrs = self.parsedt(usrs)
            usrcnt = len(usrs.keys())

            actusr.update({ifn:usrcnt})

        return actusr
