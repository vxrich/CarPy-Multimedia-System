import obd


class Obd():

    SPEED = obd.commands.SPEED
    RPM = obd.commands.RPM
    FUEL_LEVEL = obd.commands.FUEL_LEVEL
    THROTTLE = obd.commands.THROTTLE_POS

    def __init__ (self):

        self.connection = obd.OBD() # auto-connects to USB or RF port


    def getSpeed(self):
        return self.connection.query(SPEED) #kph

    def getRpm(self)
        return self.connection.query(RPM) #rpm

    def getFuel(self):
        return self.connection.query(FUEL_LEVEL) #percent


obd = Obd()
obd.getValue()
#print(self.response.value) # returns unit-bearing values thanks to Pint
#print(self.response.value.to("kmh")) # user-friendly unit conversions