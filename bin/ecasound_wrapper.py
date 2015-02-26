#!/usr/bin/env python
from pyeca import *
e = ECA_CONTROL_INTERFACE(0)

e.command("cs-add chainset")

e.command("cs-set-length 360")
e.command("cs-set-audio-format 24,4,48000")

e.command("c-add 1,2,3,4")

e.command("c-select 1,2,3,4")
e.command("ai-add alsaplugin,1,0")

e.command("c-select 1")
e.command("cs-set-audio-format 24,1,48000")
e.command("ao-add foobarX.wav")
e.command("cop-add chcopy:1,1")

e.command("c-select 2")
e.command("cs-set-audio-format 24,1,48000")
e.command("ao-add foobarY.wav")
e.command("cop-add chcopy:2,1")

e.command("c-select 3")
e.command("cs-set-audio-format 24,1,48000")
e.command("ao-add foobarZ.wav")
e.command("cop-add chcopy:3,1")

e.command("c-select 4")
e.command("cs-set-audio-format 24,1,48000")
e.command("ao-add foobarA.wav")
e.command("cop-add chcopy:4,1")
e.command("start")

ctr = 360; 
while ctr > 0:
    time.sleep(1)
    #e.command("cop-status")
    #print e.last_string()
    ctr = ctr - 1
    print ctr

e.command("stop")
e.command("cs-disconnect")
