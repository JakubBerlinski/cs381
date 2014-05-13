#!/usr/bin/python
# create, initialize, and run the 381 engine

from engine import Engine

try:
    engine = Engine()
    engine.init()
    engine.run()

except Exception, e:
    # prevent system from losing buffered keys on program crash
    try:
        if engine.inputMgr is not None:
            engine.inputMgr.stop()
            
    except:
        pass

    raise e
