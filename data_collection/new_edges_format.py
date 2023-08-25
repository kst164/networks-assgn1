import json

'''to make a map of cidr to as'''
# as_info = json.load(open('as_info.json'))

# cidr_to_as = {}

# for asn in as_info:
#     for cidr in as_info[asn]['cidr_list']:
#         cidr_to_as.update({cidr: asn})
# cidr_to_as.update({'pfft': '1'})
# with open('cidr_to_as.json', mode='w') as out_file:
#     json.dump(cidr_to_as, out_file, indent=4)

edges = []
from_to = []
cidr_to_as = json.load(open('cidr_to_as.json'))
curr_edges = json.load(open('edges.json'))

print(len(curr_edges))
for edge in curr_edges:
    if edge['from'] != edge['to'] and cidr_to_as[edge['from']] != cidr_to_as[edge['to']]:
        edges += [{
            "from": cidr_to_as[edge['from']],
            "to": cidr_to_as[edge['to']],
            "value": edge['value'],
            "color": edge['color'],
            "source": cidr_to_as[edge['source']],
            "sink": cidr_to_as[edge['sink']],
        }]
print(len(edges))
with open('new_edges.json', mode='w') as edge_file:
    json.dump(edges, edge_file, indent=4)