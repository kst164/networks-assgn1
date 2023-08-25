import json
# {"id": "shit", group: shit}
# {"from": "shit", "to": "shit", "value": shit, "color": shit, "label": "shit", "origin": "shit", "sink": "shit"}


# {
#   'endpoint': "shit",
#   "some shit": [
#       three more shits
#   ]
# goes
# }
f = open('pfft.json')
q = json.load(f)

print(q['shits'])
