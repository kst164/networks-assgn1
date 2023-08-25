import json

nodes = json.load(open('nodes.json'))
curr_edges = json.load(open('edges.json'))
print(len(curr_edges))
edges = []

all_jsons = [
    {
        "origin": "blore",
        "cidr": "pfft",
        "data": json.load(open('clean_traces/blore.json'))
    },
    {
        "origin": "www.iitb.ac.in",
        "cidr": "103.21.124.0/24",
        "data": json.load(open('clean_traces/iitb.json'))
    },
    {
        "origin": "www.iitd.ac.in",
        "cidr": "103.27.9.0/24",
        "data": json.load(open('clean_traces/iitd.json'))
    },
    {
        "origin": "www.iith.ac.in",
        "cidr": "103.232.241.0/24",
        "data": json.load(open('clean_traces/iith.json'))
    },
]

de = json.load(open('destin.json'))
def de_search(s):
    for d in de:
        if d['node'] == s:
            return d['cidr']
    return 'pfft'

for source in all_jsons:
    x = 0
    for dest in source['data']:
        tr = dest['traces'][0]
        for i in range(len(tr) - 1):
            temp = {
                "from": source['cidr'],
                "to": tr[i]['cidr'],
                "value": abs(0.01 / (tr[i]['rtt'])),
                "color": x,
                "source": de_search(source['origin']),
                "sink": de_search(dest['endpoint'])
            }
            edges += [temp]
        x+=1
        for tr in dest['traces']:
            for i in range(len(tr) - 1):
                q = {
                    "from": tr[i]['cidr'],
                    "to": tr[i + 1]['cidr'],
                    "value": abs(0.01 / (tr[i + 1]['rtt'] - tr[i]['rtt'])),
                    "color": x,
                    "source": de_search(source['origin']),
                    "sink": de_search(dest['endpoint'])
                }
                if q not in edges:
                    edges += [q]
        x += 1

# print('[', file=edge_file)
# for n in edges:
#     print(f'\t{n},', file=edge_file)
# print(']', file=edge_file)

print(len(edges))
with open('edges.json', mode='w') as edge_file:
    json.dump(edges, edge_file, indent=4)