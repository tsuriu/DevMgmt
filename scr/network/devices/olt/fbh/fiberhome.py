import sys
sys.path.inser(0,'../../../protocol/snmpc.py')

from snmpc import Snmp

class Fiberhome(Snmp):

    FbhOids = {
            'Crd': {

                   },
            'Pon': {

                   },
            'Onu': {
                        'OnuUncfg': {

                                    },
                        'OnuCfg':   {

                                    }
                   }    
                }

    def __init__(self,host,snmpword,ver):
        Snmp.__init__(self,host,snmpword,ver)

    def disc_card(self):
        card = {}

        return card

    def disc_pon(self):
        pon = {}

        return pon

    def disc_onu(self, ponid, dtype):
        onu_dt = {}
        
        return onu_dt
