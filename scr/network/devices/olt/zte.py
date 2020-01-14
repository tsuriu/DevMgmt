import sys
sys.path.insert(0, '../../../protocol/snmpc.py')

from snmpc import Snmp
import binascii

class ZTE(Snmp):

    ZteOids = {
            'Crd': {
                    'CrdType':'.1.3.6.1.4.1.3902.1015.2.1.1.3.1.4.1.1',
                    'CrdPortsNum':'.1.3.6.1.4.1.3902.1015.2.1.1.3.1.7.1.1',
                    'CrdCPULoad':'.1.3.6.1.4.1.3902.1015.2.1.1.3.1.9.1.1',
                    'CrdMenUsage':'.1.3.6.1.4.1.3902.1015.2.1.1.3.1.11.1.1'
                   },
            'Pon': {
                    'PonName':'.1.3.6.1.2.1.31.1.1.1.1',
                    'PonModuleTemperature':'.1.3.6.1.4.1.3902.1015.3.1.13.1.12',
                    'PonTxPower':'.1.3.6.1.4.1.3902.1015.3.1.13.1.4'
                   },
            'Onu': {
                        
                        'OnuUnCfg': {
                                    'OnuSN':'.1.3.6.1.4.1.3902.1012.3.13.3.1.2'
                                    },
                        'OnuCfg': {
                                  'OnuSN':'.1.3.6.1.4.1.3902.1012.3.28.1.1.5',
                                  'OnuSysUptime':'.1.3.6.1.4.1.3902.1012.3.50.11.2.1.20',
                                  'OnuRxOptLvl':'.1.3.6.1.4.1.3902.1012.3.50.12.1.1.10', #Need a custom equation to validate value, it's (OnuRxOptLvl * 0.002) - 30
                                  'OnuTxOptLvl':'.1.3.6.1.4.1.3902.1012.3.50.12.1.1.14', #Need a custom equation to validate value, it's (OnuTxOptLvl * 0.002) - 30
                                  'OnuState':'.1.3.6.1.4.1.3902.1012.3.28.2.1.4',
                                  'OnuModel':'.1.3.6.1.4.1.3902.1012.3.50.11.2.1.9',
                                  'OnuVlan':'.1.3.6.1.4.1.3902.1012.3.11.4.1.2'
                                  }
                  }
             }

    def __init__(self,host,snmpword,ver):
        Snmp.__init__(self,host,snmpword,ver)

    def sn2Str(self,sn):
        sn2d = ':'.join('{:02x}'.format(ord(x)) for x in sn)
        snlist = sn2d.split(":")
        sn1p = snlist[:4]
        sn1p_str  = (binascii.unhexlify(''.join(sn1p))).decode("utf-8")
        sn2p = (''.join(snlist[4:])).lower()

        snStr = sn1p_str + sn2p

        return snStr

    def disc_card(self):
        card = {}

        oid = self.ZteOids['Crd']['CrdType']

        crd_dt = self.Walk(oid)
        for dctid in list(crd_dt.keys()):
            crd = crd_dt[dctid]
            idx = crd['oidx']
            ctype = crd['value']
            PortNum = self.Get(self.ZteOids['Crd']['CrdPortsNum']+"."+idx)
            CPULoad = self.Get(self.ZteOids['Crd']['CrdCPULoad']+"."+idx)
            MenUsage = self.Get(self.ZteOids['Crd']['CrdMenUsage']+"."+idx)
            
            card.update({idx:{'type':ctype,'PortsNum':PortNum,'CPULoad':CPULoad,'MenUsage':MenUsage}})

        return card
    
    def disc_pon(self):
        pon = {}

        oid = self.ZteOids['Pon']['PonName']

        pon_dt = self.Walk(oid)
        for dctid in list(pon_dt.keys()):
            pn = pon_dt[dctid]
            idx = pn['oidx']
            descr = pn['value']
            shell,card,ponid = (descr.split("_")[1]).split("/")
            txpower = self.Get(self.ZteOids['Pon']['PonTxPower']+"."+idx)
            temperature = (self.Get(self.ZteOids['Pon']['PonModuleTemperature']+"."+idx))['value']
        
            pon.update({idx:{'descr':descr,'shelf':shell,'card':card,'ponid':ponid,'txpower':txpower,'temperature':temperature}})
            
        return pon        

    def disc_onu(self, ponid, dtype):

        onu_dt = {}

        w_oid = '.'.join([self.ZteOids['Onu'][dtype]['OnuSN'],ponid])

        ONUs = self.Walk(w_oid)

        for onuid in list(ONUs.keys()):
            onu_tmp = {}
            
            onu = ONUs[onuid]
            idx = onu['oidx']
            if idx == ponid: idx = '1'
            sn = self.sn2Str(onu['value'])

            tmp_dt = {'onuid':idx}
            onu_tmp.update(tmp_dt)

            for key in list(self.ZteOids['Onu'][dtype]):
                oid_base = self.ZteOids['Onu'][dtype][key]
                g_oid = "%s.%s.%s.1.0" %(oid_base,ponid,idx)
                gdt = self.Get(g_oid)

                onu_tmp.update({key:gdt['value']})

            onu_dt.update({sn:onu_tmp})
        return onu_dt
