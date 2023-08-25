import json
# edge_file = open('edges.json', mode='w')
# nodes = json.load(open('nodes.json'))
out_file = open('destin.json', mode='w')
# edges = []

all_jsons: list[dict[str, list[dict[str, list[list[dict[int, str, str]]]]]]] = [
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
]

out = []
for source in all_jsons:
    for dest in source['data']:
        tr = dest['traces'][0]
        # print(tr)
        if len(tr) == 0:
            continue
        q = {
            "node": dest['endpoint'],
            "cidr": tr[len(tr) - 1]['cidr']
        }
        if q not in out:
            out += [q]
        

with open('destin.json', mode='w') as out_file:
    json.dump(out, out_file, indent=4)