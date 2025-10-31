pyscript:
  allow_all_imports: true
  hass_is_global: true

pyscript: !include pyscript/config.yaml

pyscript:
  allow_all_imports: true
  apps:
    my_app1:
      # any settings for my_app1 go here
    my_app2:
      # any settings for my_app2 go here

allow_all_imports: true
apps:
  my_app1:
    # any settings for my_app1 go here
  my_app2:
    # any settings for my_app2 go here

service.call("DOMAIN", "SERVICE", entity_id="DOMAIN.ENTITY", other_param=123)
DOMAIN.SERVICE(entity_id="DOMAIN.ENTITY", other_param=123)
DOMAIN.ENTITY.SERVICE(other_param=123)

DOMAIN.ENTITY.SERVICE(123)

service.call("input_number", "set_value", entity_id="input_number.test", value=13)
input_number.set_value(entity_id="input_number.test", value=13)
input_number.test.set_value(value=13)
input_number.test.set_value(13)

from datetime import datetime as dt
from datetime import timezone as timezone

num_seconds_ago = (dt.now(tz=timezone.utc) - binary_sensor.test1.last_changed).total_seconds()

@pyscript_compile
def incr(x):
    return x + 1

x = list(map(incr, [0, 5, 10]))

@pyscript_compile
def read_file(file_name):
    try:
        with open(file_name, encoding="utf-8") as file_desc:
           return file_desc.read(), None
    except Exception as exc:
        return None, exc

contents, exception = task.executor(read_file, "config/configuration.yaml")
if exception:
    raise exception
log.info(f"contents = {contents}")

@pyscript_executor
def read_file(file_name):
    try:
        with open(file_name, encoding="utf-8") as file_desc:
           return file_desc.read(), None
    except Exception as exc:
        return None, exc

contents, exception = read_file("config/configuration.yaml")
if exception:
    raise exception
log.info(f"contents = {contents}")

@service
def hello_world(action=None, id=None):
    """yaml
name: Service example
description: hello_world service example using pyscript.
fields:
  action:
     description: turn_on turns on the light, fire fires an event
     example: turn_on
     required: true
     selector:
       select:
         options:
           - turn_on
           - fire
  id:
     description: id of light, or name of event to fire
     example: kitchen.light
     required: true
     selector:
       text:
"""
    log.info(f"hello world: got action {action}")
    if action == "turn_on" and id is not None:
        light.turn_on(entity_id=id, brightness=255)
    elif action == "fire" and id is not None:
        event.fire(id)

@task_unique(task_name, kill_me=False)
Update 31.10.25 
