#!/usr/bin/python

import json

class CarAudConfig:
    def __init__(self,cfgfile,branch='defaults'):
        jsonstr = ''
        self.branch = branch

        with open(cfgfile) as ifil:
            for ifa in ifil:
                jsonstr += ifa

        self.config = json.loads(jsonstr)
        self.chanCtOpts = { 'both'   : (lambda: self.config['chanCt']),
                            'input'  : (lambda: self.config['chanCt']['input']),
                            'output' : (lambda: self.config['chanCt']['output']) }
        self.deviceOpts = { 'both'   : (lambda: [ self.config['inputDevice'], self.config['outputDevice'] ]),
                            'input'  : (lambda: self.config['inputDevice']),
                            'output' : (lambda: self.config['outputDevice']) }

    def default(self):
        return(self.config['defaults'])
    def branch(self):
        return(self.config[self.branch])
    def duration(self):
        return(self.config[self.branch]['duration'])
    def fnbase(self):
        return(self.config[self.branch]['fnbase'])
    def chanCt(self,mode='both'):
        return self.chanCtOpts[mode]()
    def sampleRate(self):
        return self.config['sampleRate']
    def bitDepth(self):
        return self.config['bitDepth']
    def inputDevice(self):
        return self.config['inputDevice']
    def outputDevice(self):
        return self.config['outputDevice']
    def device(self,mode='both'):
        return self.deviceOpts[mode]()

if __name__ == '__main__':
    cac = CarAudConfig("../etc/caraudcoll_config.json")
    print cac.duration()
    print cac.chanCt()
    print cac.inputDevice()
    print cac.device()
