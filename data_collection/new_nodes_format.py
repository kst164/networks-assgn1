import json

as_info = json.load(open('as_info.json'))

nodes = []

for asn in as_info:
    q = {
        "id": asn, 
        "group": asn,
        "sname": as_info[asn]['shortname'],
        "country": as_info[asn]['country'],
        "cidr_list": as_info[asn]['cidr_list']
    }
    nodes += [q]
q = {
    "id": '1',
    "group": '1',
    "sname": 'blore',
    "country": 'IN',
    "cidr_list": ['pfft']
}
nodes += [q]
with open('new_nodes.json', mode='w') as node_file:
    json.dump(nodes, node_file, indent=4)
