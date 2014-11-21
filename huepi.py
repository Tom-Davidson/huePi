import ConfigParser
import requests
from hue.hue import Hue

def main():
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    container = {
        'config': Config
    }
    hue = Hue(container)
    light = hue.getLightByName('Sitting room lamp')
    #print light.setOn()
    #print light.setOff()
    print light.setBrightness(90)
    print light.getState()

if __name__ == '__main__':
    main()
