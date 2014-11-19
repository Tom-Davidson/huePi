import requests

BRIDGE_IP = '192.168.10.14'
BRIDGE_USER = 'huepihuepi'

def createUser():
    # http://www.developers.meethue.com/documentation/configuration-api#71_create_user
    global BRIDGE_IP, BRIDGE_USER
    data = {
        "devicetype":"hue#pi",
        "username":BRIDGE_USER # Minimum 10 characters
    }
    r = requests.post(
        'http://%s/api' % (BRIDGE_IP),
        False,
        data
    )
    return r.json()


def getLights():
    # http://www.developers.meethue.com/documentation/lights-api#11_get_all_lights
    global BRIDGE_IP, BRIDGE_USER
    r = requests.get('http://%s/api/%s/lights' % (BRIDGE_IP, BRIDGE_USER))
    return r.json()

def main():
    print getLights()

if __name__ == '__main__':
    main()
