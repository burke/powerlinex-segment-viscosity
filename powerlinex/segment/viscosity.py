from __future__ import absolute_import
import os

def playing(pl):
    data = os.popen("osascript /Users/burke/Library/viscosity.script").read().rstrip()
    if data == "Connected":
        return "☗:"
    elif data == "Connecting":
        return "☖ "
    else:
        return "☖ "
