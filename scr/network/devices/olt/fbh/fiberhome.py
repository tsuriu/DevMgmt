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
                                     'unauthOnuListMac':'1.3.6.1.4.1.5875.800.3.11.1.1.7',
                                     'unauthOnuListSlot':'1.3.6.1.4.1.5875.800.3.11.1.1.2',
                                     'unauthOnuListPon':'1.3.6.1.4.1.5875.800.3.11.1.1.3'
                                    },
                        'OnuCfg':   {
                                    'authOnyListMac':'1.3.6.1.4.1.5875.800.3.10.1.1.10',
                                    'authOnuListSlot':'1.3.6.1.4.1.5875.800.3.10.1.1.2',
                                    'authOnuListPon':'1.3.6.1.4.1.5875.800.3.10.1.1.3',
                                    'authOnuListOnuid':'1.3.6.1.4.1.5875.800.3.10.1.1.4',
                                    'authOnuListOnuType':'1.3.6.1.4.1.5875.800.3.10.1.1.5',
                                    'authOnuListOnuName':'1.3.6.1.4.1.5875.800.3.10.1.1.7',
                                    'authOnuStatus':'1.3.6.1.4.1.5875.800.3.10.1.1.11',
                                    'authOnuSoftwareVersion':'1.3.6.1.4.1.5875.800.3.10.1.1.12',
                                    'authOnuHardwareVersion':'1.3.6.1.4.1.5875.800.3.10.1.1.13',
                                    'authOnuFirmwareVersion':'1.3.6.1.4.1.5875.800.3.10.1.1.14',
                                    'authOnuPonRxOpticalPower':'1.3.6.1.4.1.5875.800.3.9.3.3.1.6',
                                    'authOnuPonTxOpticalPower':'1.3.6.1.4.1.5875.800.3.9.3.3.1.7',
                                    'authOnuPonOpticalTemperature':'1.3.6.1.4.1.5875.800.3.9.3.3.1.10'
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
