import json

nodes = json.load(open('nodes.json'))

edges = []

all_jsons: list[dict[str, list[dict[str, list[list[dict[int, str, str]]]]]]] = [
    {
        "origin": "blore",
        "data": json.load(open('clean_traces/blore.json'))
    },
    {
        "origin": "www.iitb.ac.in",
        "data": json.load(open('clean_traces/iitb.json'))
    },
    {
        "origin": "www.iitd.ac.in",
        "data": json.load(open('clean_traces/iitd.json'))
    },
    {
        "origin": "www.iith.ac.in",
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

with open('edges.json', mode='w') as edge_file:
    json.dump(edges, edge_file, indent=4)