import ConfigParser
import requests

def getLights(container):
    # http://www.developers.meethue.com/documentation/lights-api#11_get_all_lights
    r = requests.get(
        'http://%s/api/%s/lights' % (
            container['config'].get('hue', 'address'),
            container['config'].get('hue', 'user')
        )
    )
    return r.json()

def main():
    Config = ConfigParser.ConfigParser()
    Config.read('config.ini')
    container = {
        'config': Config
    }
    print getLights(container)

if __name__ == '__main__':
    main()
