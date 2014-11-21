import ConfigParser
import requests

def createUser(container):
    # http://www.developers.meethue.com/documentation/configuration-api#71_create_user
    data = {
        "devicetype":"hue#pi",
        "username": container['config'].get('hue', 'user') # Minimum 10 characters
    }
    r = requests.post(
        'http://%s/api' % (container['config'].get('hue', 'address')),
        False,
        data
    )
    return r.json()

def main():
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    container = {
        'config': Config
    }
    print createUser(container)

if __name__ == '__main__':
    main()
