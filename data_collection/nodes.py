import json
# node_file = open('nodes.json', mode='w')
# asn = json.load(open('ip_to_asn.json'))
asn = json.load(open('as_info.json'))

nodes = []

all_jsons = [
    {
        "origin": "blore",
        "data": json.load(open('clean_traces/blore.json'))
    },
    {
        "origin": "iitb",
        "data": json.load(open('clean_traces/iitb.json'))
    },
    {
        "origin": "iitd",
        "data": json.load(open('clean_traces/iitd.json'))
    },
    {
        "origin": "iith",
        "data": json.load(open('clean_traces/iith.json'))
    },
    {
        "origin": "iitm",
        "data": json.load(open('clean_traces/iitm.json'))
    },
    {
        "origin": "iitg",
        "data": json.load(open('clean_traces/iitg.json'))
    },
]
rep = 0
for source in all_jsons:
    for dest in source['data']:
        for tr in dest['traces']:
            for node in tr:
                q = {
                    "id": node['cidr'], 
                    "group": node['asn'],
                    "sname": asn[node['asn']]['shortname']
                }
                if q not in nodes:
                    nodes += [q]
                else:
                    rep += 1

# print(nodes, file=node_file)
with open('nodes.json', mode='w') as node_file:
    json.dump(nodes, node_file, indent=4)
# print(blore[0])
print(rep)