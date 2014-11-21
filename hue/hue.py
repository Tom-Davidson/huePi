import requests
from .light import Light

class Hue():
    container = False
    lights = False
    lightIDs = {}
    lightNames = {}
    def __init__(self, container):
        self.container = container
        lights = self.getLights()
    def getLights(self):
        if self.lights == False:
            # http://www.developers.meethue.com/documentation/lights-api#11_get_all_lights
            r = requests.get(
                'http://%s/api/%s/lights' % (
                    self.container['config'].get('hue', 'address'),
                    self.container['config'].get('hue', 'user')
                )
            )
            lights = r.json()
            self.lights = {}
            for lightNo in lights:
                self.lightIDs[lightNo] = lights[lightNo]['name']
                self.lightNames[lights[lightNo]['name']] = lightNo
                lights[lightNo]['id'] = lightNo
                self.lights[lightNo] = Light(lights[lightNo], self.container)
        return self.lights
    def getLightById(self, id):
        id = str(id)
        if id in self.lights:
            return self.lights[id]
        else:
            raise IndexError('There is no light with id: '+id)
    def getLightByName(self, name):
        id = str(name)
        if name in self.lightNames:
            return self.getLightById(self.lightNames[name])
        else:
            raise IndexError('There is no light with name: '+name)
