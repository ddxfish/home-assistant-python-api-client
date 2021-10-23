This script allows you to interact with Home Assistant servers through python. It interacts with the RESTful API documented here: https://developers.home-assistant.io/docs/api/rest/

# Examples

## Get information from Home Assistant
* Get all states from Home Assistant, 1 item list containing JSON
print(server.getHassStates())
* Search states for id or friendly name containing phrase, returns 1 item list with JSON
print(server.getHassStates("light."))
* Search states for id or friendly, return only their state in a list
print(server.getHassStates("sensor.", "state"))
* Search states for id or friendly, return only basic list of info
print(server.getHassStates("sensor.", "basic"))
* Find every entity containing temperature and list their entity_ids
print(server.getHassStates("temperature", "entity_id"))
* Exact match a single device entity_id or friendly name.
print(server.getHassStates("switch.main_desk_lamp_on_off", "all", 1))
* Exact match a single device and return the state, returns string
print(server.getHassStates("switch.main_desk_lamp_on_off", "state", 1))
* Get the entity_id from a friendly name, exact match, return string
print(server.getHassStates("main desk lamp", "entity_id", 1))
 
## POST to the Home Assistant API
This simply takes 3 arguments, entity_id, service prefix and service suffix. You can call any service you want here. Services can be found in **Developer Tools > Services**. switch.toggle is a service and is how we get the info for this.

* Toggle switch
server.callHassService("switch.main_desk_lamp_on_off", "switch", "toggle")
* activate a scene in Home assistant
server.callHassService("scene.full_bright", "scene", "turn_on")
* trigger automation event
server.callHassService("automation.cube_changed_face", "automation", "trigger")
* Custom stuff - Any HA service like media_player.volume_up would be
server.callHassService("media_player.smart-tv-1", "media_player", "volume_up")

# Advanced
* Use the switch.toggle service, get the entity_id by searching for friendly name
server.callHassService(server.getHassStates("main desk lamp", "entity_id", 1), "switch", "toggle")
