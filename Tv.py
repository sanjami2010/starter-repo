class Tv:
    def __init__(self):
        self.channel=1 #defaults to 1 as soon as constructor ,this object is instantiated
        self.volumeLevel= 1
        self.on=True
    def turnOn(self):
        self.on=True
    def turnOff(self):
        self.off=False
    def getChannel(self):
        return self.channel
    def setChannel(self,channel):
        if self.on and 1 <= channel <=120:
            self.channel=channel
    def getVolume(self):
        return self.volumeLevel
    def setVolume(self,volumeLevel):
        if self.on and 1<=volumeLevel <=7:
            self.volumeLevel =volumeLevel
    def channelUp(self):
        if self.on and self.channel<120:
            self.channel+=1
    def channelDown(self):
        if self.on and self.channel>1:
            self.channel-=1
    def volumeUp(self):
        if self.on and self.volumeLevel<7:
            self.volumeLevel+=1
    def volumeDown(self):
        if self.on and self.volumeLevel>1:
            self.volumeLevel-=1
    

        
        

        
        