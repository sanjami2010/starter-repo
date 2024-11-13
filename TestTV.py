from Tv import Tv

def main():
    tv1=Tv()
    tv1.turnOff()
    tv1.turnOn()
    tv1.channelUp()
    tv1.setVolume(9)
    print("volume here is ",tv1.getVolume())
main()