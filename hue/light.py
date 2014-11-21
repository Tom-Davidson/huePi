import json
import requests

class Light():
    container = False
    state = False
    def __init__(self, state, container):
        self.state = state
        self.container = container
    def getState(self):
        return self.state['state']
    def setState(self, state):
        # http://www.developers.meethue.com/documentation/lights-api#16_set_light_state
        r = requests.put(
            'http://%s/api/%s/lights/%s/state' % (
                self.container['config'].get('hue', 'address'),
                self.container['config'].get('hue', 'user'),
                self.state['id']
            ),
            json.dumps(state)
        )
        result = r.json()
        # TODO: check each result instead of just the first
        if 'success' in result[0]:
            for stateItem in state:
                self.state['state'][stateItem] = state[stateItem]
            return True
        else:
            print json.dumps(state)
            print result
            return False
    def setOn(self):
        return self.setState({'on':True})
    def setOff(self):
        return self.setState({'on':False})
    def setBrightness(self, intensity):
        try:
            if intensity < 1:
                print 'Minimum intensity is 1%'
                intensity = 1
            if intensity > 100:
                print 'Maximum intensity is 100%'
                intensity = 100
            return self.setState({'bri':intensity*255/100})
        except TypeError:
            print 'Bad intensity value '+str(intensity)+' should be an integer'
            return False
