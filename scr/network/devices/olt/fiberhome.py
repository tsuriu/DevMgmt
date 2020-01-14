import sys
sys.path.insert(0,'../../../protocol/snmpc.py')

from snmpc import Snmp

class Fiberhome(Snmp):

    FbhOids = {
            'Crd': {
                        'CrdPon':{
                                    'cardType':'1.3.6.1.4.1.5875.800.3.9.2.1.1.2',
                                    'cardHardwareVersion':'1.3.6.1.4.1.5875.800.3.9.2.1.1.3',
                                    'cardSoftwareVersion':'1.3.6.1.4.1.5875.800.3.9.2.1.1.4',
                                    'cardStatus':'1.3.6.1.4.1.5875.800.3.9.2.1.1.5',
                                    'cardNumOfPorts':'1.3.6.1.4.1.5875.800.3.9.2.1.1.6',
                                    'cardAvailablePorts':'1.3.6.1.4.1.5875.800.3.9.2.1.1.7',
                                    'cardCpuUtil':'1.3.6.1.4.1.5875.800.3.9.2.1.1.8',
                                    'cardMenUtil':'1.3.6.1.4.1.5875.800.3.9.2.1.1.9'
                                 },
                        'CrdMgr':{
                                    'mgrCardType':'1.3.6.1.4.1.5875.800.3.9.8.1.1.1',
                                    'mgrCardHardwareVersion':'1.3.6.1.4.1.5875.800.3.9.8.1.1.2',
                                    'mgrCardSoftwareVersion':'1.3.6.1.4.1.5875.800.3.9.8.1.1.3',
                                    'mgrCardWorkStatus':'1.3.6.1.4.1.5875.800.3.9.8.1.1.4',
                                    'mgrCardCpuUtil':'1.3.6.1.4.1.5875.800.3.9.8.1.1.5',
                                    'mgrCardMemUtil':'1.3.6.1.4.1.5875.800.3.9.8.1.1.6'                                    
                                 }
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
