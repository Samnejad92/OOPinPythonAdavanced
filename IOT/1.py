class Device:
    count=0
    def __init__(self,ip,mac,name):
        self.ip=ip
        self.mac_address=mac
        self.name=name
        Device.count+=1
        # result =ping the device
        if result:
            self.status="active"
        else:
            self.status='unknown'

class TV(Device):
    def turn_on(self):
        #connect to self.ip and turn on
        pass
    def turn_off(self):
        #connect to self.ip and turn off
        pass

class Thermo(Device):
    def get_degree(self):
        #connect to self.ip and get the temprature and return the result
        return result

class SmartTV(TV):
    def turn_on(self):
        #turn on the smart tv by self.ip
