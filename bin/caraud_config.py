#!/usr/bin/python

import json

class CarAudConfig:
    def __init__(self,cfgfile):
        with open(cfgfile) as ifil:
            for ifa in ifil:
                self.ifa_jsn = json.loads(ifa)


if __name__ == '__main__':
    cac = CarAudConfig("../etc/caraudcoll_config.json")
