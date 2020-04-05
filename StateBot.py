import os
import botRuntime

# Returns the bot parameters
def getConfiguration():
    # Get the collectd server address
    collectdAddress = os.getenv("collectdAddress")

    # Check if the `collectdAddress` environment variable
    # exists.
    if collectdAddress == None:
        print("Missing collectd server address")
        return None

    # Get the collectd server port and check if the
    # `collectdPort` environment variable exists
    # and that it is an integer.
    try:
        collectdPort = os.getenv("collectdPort")
        if collectdPort == None:
            print("Missing collectd server port")
            return None
        collectdPort = int(collectdPort)
    except ValueError:
        print("An integer for the collectd server port is needed")
        return None
    
    
    return {"address" : collectdAddress, "port" : collectdPort}

# Initializes the bot and starts it
def init():
    # Get the configuration and check if it is valid
    configuration = getConfiguration()

    if configuration == None:
        print("Exiting, invalid configuration...")
        exit()
    else:
        botRuntime.botStart()

init()