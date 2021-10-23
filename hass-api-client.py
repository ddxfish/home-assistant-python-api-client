
from requests import get, post
import json

class HassRestAPIClient:
    def __init__(self):
        #Change to your Home Assistant API URL (ex. http://192.168.1.100:8123/api )
        self.hassurl = "http://192.168.1.100:8123/api"
        #Make sure you enter your own Long Time Access token (Bearer token) from Home Assistant
        self.headers = {
            "Authorization": "Bearer BEARERTOKENGOESHERE",
            "content-type": "application/json",
        }

    #Get information from home assistant states
    def getHassStates(self, entitysearch="", key="all", exactmatch=0):
        url = self.hassurl + "/states"
        response = get(url, headers=self.headers)
        entities = response.json()
        result = []
        for entity in entities:
            if exactmatch == 0:
                if entitysearch.lower() in entity['entity_id'].lower() or entitysearch.lower() in entity['attributes']['friendly_name'].lower():
                    if key == "all":
                        result.append(entity)
                    if key == "basic":
                        result.append([entity['entity_id'],entity['attributes']['friendly_name'],entity['state']])
                    else:
                        try:
                            result.append(entity[key])
                        except KeyError:
                            try:
                                result.append(entity['attributes'][key])
                            except KeyError:
                                result.append("no key named " + key)
            if exactmatch == 1:
                if entitysearch.lower() == entity['entity_id'].lower() or entitysearch.lower() == entity['attributes']['friendly_name'].lower():
                    if key == "all":
                        return entity
                    if key == "basic":
                        return [entity['entity_id'],entity['attributes']['friendly_name'],entity['state']]
                    else:
                        try:
                            return entity[key]
                        except KeyError:
                            try:
                                return entity['attributes'][key]
                            except KeyError:
                                return "no key named " + key
        return result

    #Custom service call
    def callHassService(self, entity_id, service, action):
        payload = json.dumps({"entity_id": entity_id})
        entityurl = self.hassurl + "/services/" + service + "/" + action
        result = post(entityurl, headers=self.headers, data=payload)
        return result
