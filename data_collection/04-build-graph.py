import json
import os
import math

directory = "clean_traces"

source_asns = {
    "blore": "60140",
    "blore2": "133982",
    "hyd": "24560",
    "iitb": "132423",
    "iitd": "132780",
    "iitg": "55847",
    "iith": "59193",
    "iitm": "141340",
}

def get_nodes():
    with open('as_info.json') as f:
        as_info = json.load(f)
    nodes = []
    for asn, info in as_info.items():
        nodes.append({
            "id": asn,
            "sname": info['shortname'],
            "country": info['country'],
            "cidr_list": info['cidr_list']
        })
    return nodes

def time_transform(t):
    return -math.log2(t + 0.1)

def get_edges():
    edges = []

    for filename in os.listdir(directory):
        if not filename.endswith(".json"):
            continue
        origin = filename.rstrip(".json")

        file = os.path.join(directory, filename)
        with open(file) as f:
            data = json.load(f)

        for endp_idx, dest in enumerate(data):

            if len(dest["traces"][0]) == 0:
                print(f"{origin} -> {dest['endpoint']}")
                continue
            dest_asn = dest["traces"][0][-1]["asn"]
            for trace in dest["traces"]:
                if source_asns[origin] != trace[0]["asn"]:
                    edges.append({
                        "from": source_asns[origin],
                        "to": trace[0]["asn"],
                        "value": time_transform(trace[0]["rtt"]),
                        "color": endp_idx,
                        "origin": source_asns[origin],
                        "sink": dest_asn,
                    })

                for i in range(len(trace) - 1):
                    time = trace[i+1]["rtt"] - trace[i]["rtt"]
                    edges.append({
                        "from": trace[i]["asn"],
                        "to": trace[i + 1]["asn"],
                        "value": time_transform(time),
                        "color": endp_idx,
                        "origin": source_asns[origin],
                        "sink": dest_asn,
                    })
    return edges

graph = {
    "nodes": get_nodes(),
    "edges": get_edges(),
}

with open('graph.json', mode='w') as out_file:
    json.dump(graph, out_file, indent=4)
