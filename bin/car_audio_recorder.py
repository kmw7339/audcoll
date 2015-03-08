#!/usr/bin/env python

import sys
import json
import types
import getopt
import re
import datetime
import psycopg2
import getopt
from CarAudConfig import *
from pyeca import *

class EcaRec:

    cacConfigFile = '../etc/caraudcoll_config.json'
    def __init__(self,DEBUG=None):

        self.debugmode = DEBUG
        self.cfgObj        = CarAudConfig(EcaRec.cacConfigFile)
        self.chnStartIdx   = 1
        self.currChain     = "LDC123"
        self.fnbase        = self.cfgObj.fnbase()
        self.inputDevice   = self.cfgObj.inputDevice()
        self.carBitDepth   = self.cfgObj.bitDepth()
        self.carOChanCt    = int(self.cfgObj.chanCt('output'))
        self.carOChanArry  = range(self.chnStartIdx, self.carOChanCt)
        self.carIChanCt    = self.cfgObj.chanCt('input')
        self.carSampleRate = int(self.cfgObj.sampleRate())
        self.recDuration   = int(self.cfgObj.duration())
        self.ecaobj        = ECA_CONTROL_INTERFACE(0)

    def createChanset(self,chnLabel=None):
        if chnLabel:
            self.currChain = label
        self.ecaobj.command("cs-add {}".format(self.currChain))

    def setOutFile(self,ofil=None):
        if ofil:
            self.fnbase = ofil

    def setDuration(self,duration=None):
        if duration:
            self.recDuration = duration
        self.ecaobj.command("cs-set-length {}".format(self.recDuration))

    def setSource(self):
        self.ecaobj.command("ai-add {}".format(self.inputDevice))

    def dump(self):
        print self.ecaobj.command("cs-status")

    def outchn(self,chnidx):
        self.chanSel(chnidx)
        self.carOutputFmt()
        ofn = "{}_{}.wav".format(self.fnbase,chnidx)
        self.ecaobj.command("ao-add {}".format(ofn))
        self.ecaobj.command("cop-add chcopy:{},1".format(chnidx))

    def carOutputFmt(self):
        self.setFormat(self.carBitDepth, self.carOChanCt, self.carSampleRate)

    def setFormat(self,bd,ct,sr):
        if self.debugmode > 0:
            print "{} {} {}".format(bd, ct, sr)
        self.ecaobj.command("cs-set-audio-format {},{},{}".format(bd, ct, sr))


    def chanSel(self,chnlst):
        self.ecaobj.command("c-select {}".format(chnlst))

    def ochanAdd(self,chnlst):
        for cl in chnlst:            
            self.outchn(int(cl))

    def ichanAdd(self,chnlst):
        chnstr = "{}".format(",".join(map(str,chnlst)))
        self.ecaobj.command("c-add {}".format(chnstr))
        self.ecaobj.command("c-select {}".format(chnstr))
        self.ecaobj.command("ai-add {}".format(self.inputDevice))

    def startRec(self):
        self.ecaobj.command("start")

    def stopRec(self):
        self.ecaobj.command("stop")

    def ioStatus(self):
        self.ecaobj.command("aio-status")
        return(self.ecaobj.last_string())

    def isRunning(self):
        if self.engineStatus() == "running":
            return(True)
        else:
            return(None)

    def engineStatus(self):
        self.ecaobj.command("engine-status")
        return(self.ecaobj.last_string())

    def disconnect(self):
        self.ecaobj.command("cs-disconnect")

def usage():
    print "car_audio_recorder.py"

def main(argv=None):
    try:                                
        opts, args = getopt(argv, "f:") 
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)                     

    ecarec = EcaRec()
    ecarec.createChanset()
    ecarec.setDuration(5)
    ecarec.setOutFile("kevinstest")

    ecarec.ichanAdd([1,2,3,4])
    ecarec.ochanAdd([1,2,3,4])

    print ecarec.engineStatus()
    ecarec.startRec()
    
    while 1:
        if ecarec.engineStatus() == "running": 
            break 

    while ecarec.isRunning():
        print "OK"

    ecarec.stopRec()

    ecarec.disconnect()

if __name__ == '__main__':
    main(sys.argv[1:])



##!/usr/bin/env python
#from pyeca import *
#e = ECA_CONTROL_INTERFACE(0)
#
#e.command("cs-add chainset")
#
#e.command("cs-set-length 360")
#e.command("cs-set-audio-format 24,4,48000")
#
#e.command("c-add 1,2,3,4")
#e.command("c-select 1,2,3,4")
#e.command("ai-add alsaplugin,1,0")
#
#e.command("c-select 1")
#e.command("cs-set-audio-format 24,1,48000")
#e.command("ao-add foobarX.wav")
#e.command("cop-add chcopy:1,1")
#
#e.command("c-select 2")
#e.command("cs-set-audio-format 24,1,48000")
#e.command("ao-add foobarY.wav")
#e.command("cop-add chcopy:2,1")
#
#e.command("c-select 3")
#e.command("cs-set-audio-format 24,1,48000")
#e.command("ao-add foobarZ.wav")
#e.command("cop-add chcopy:3,1")
#
#e.command("c-select 4")
#e.command("cs-set-audio-format 24,1,48000")
#e.command("ao-add foobarA.wav")
#e.command("cop-add chcopy:4,1")
#e.command("start")
#
#ctr = 360;
#while ctr > 0:
#    time.sleep(1)
#    #e.command("cop-status")
#    #print e.last_string()
#    ctr = ctr - 1
#    print ctr
#
#e.command("stop")
#e.command("cs-disconnect")
