#!/usr/bin/env python

import sys
import json
import types
import re
import datetime
import psycopg2
import getopt
from pyeca import *

class EcaRec:

    def __init__(self,maxidx):
        self.ecaobj = ECA_CONTROL_INTERFACE()
        self.chnidx = 0
        self.fnbase = "defrec"
        self.carBitDepth = 24
        self.carOChanCt = 1
        self.carSampleRate = 48000
        self.recDuration = 30
        self.ecaobj.command("cs-add chainset")
        self.ecaobj.command("cs-set-length 30")
        self.setFormat(self.carBitDepth,4,self.carSampleRate)
        self.chanAdd("1,2,3,4")
        self.ecaobj.command("ai-add alsaplugin,1,0")

    def outchn(self,chnidx):

        self.chanSel(chnidx)
        self.carOutputFmt()
        ofn = "{}_{}.wav".format(self.fnbase,chnidx)
        self.ecaobj.command("ao-add {}".format(ofn))
        self.ecaobj.command("cop-add chcopy:{},1".format(chnidx))

    def carOutputFmt(self):
        self.setFormat(self.carBitDepth, self.carOChanCt, self.carSampleRate)

    def setFormat(self,bitdepth,chanct,samplerate):
        self.ecaobj.command("cs-set-audio-format {},{},{}".format(bitdepth,chanct,samplerate))

    def chanSel(self,chnlst):
        self.ecaobj.command("c-select {}".format(chnlst))

    def chanAdd(self,chnlst):
        self.ecaobj.command("c-add {}".format(chnlst))

    def startRec(self):
        self.ecaobj.command("start")

    def stopRec(self):
        self.ecaobj.command("stop")
    def ioStatus(self):
        self.ecaobj.command("aio-status")
        return(self.ecaobj.last_string())

    def engineStatus(self):
        self.ecaobj.command("engine-status")
        return(self.ecaobj.last_string())

    def disconnect(self):
        self.ecaobj.command("cs-disconnect")

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



        
def main(argv=None):

    chan_list = [1,2,3,4]
    ecarec = EcaRec(len(chan_list))
    for cl in chan_list:
        ecarec.outchn(cl)
    ecarec.startRec()
    
    while 1:
        print ecarec.engineStatus()

    ecarec.stopRec()

    ecarec.disconnect()

if __name__ == '__main__':
    main()



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
#
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
