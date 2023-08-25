import os
import json
import ipaddress

import requests

input_directory = "raw_traces"
output_directory = "clean_traces"

# create output directory if not exists
os.makedirs(output_directory, exist_ok=True)

with open("as_info.json") as f:
    as_info = json.load(f)

# convert each cidr to ipaddress.ip_network
for asn in as_info:
    info = as_info[asn]
    for i in range(len(info["cidr_list"])):
        info["cidr_list"][i] = ipaddress.ip_network(info["cidr_list"][i])

with open("ip_to_asn.json") as f:
    ip_to_asn = json.load(f)

def get_as_info(ip):
    ip_obj = ipaddress.ip_address(ip)
    if ip_obj.is_private:
        return None

    if ip not in ip_to_asn:
        print(f"ip {ip} not in ip_to_asn")
        return None
    asn = str(ip_to_asn[ip])

    if asn not in as_info:
        print(f"asn {asn} not in as_info")
        return None

    info = as_info[asn]

    cidr = None
    for this_cidr in info["cidr_list"]:
        if ip_obj in this_cidr:
            cidr = this_cidr
            break
    if cidr is None:
        print(f"ip {ip} not in cidr_list of asn {asn}")
        return None

    return asn, info, cidr

def clean_trace(trace):
    cleaned_trace = []
    for hop in trace:
        _, ip, rtt = hop
        as_info = get_as_info(ip)
        if as_info is None:
            continue
        asn, _, cidr = as_info

        if len(cleaned_trace) > 0 and cleaned_trace[-1]["cidr"] == cidr:
            cleaned_trace[-1]["rtt"] = rtt

        cleaned_trace.append({
            "rtt": rtt,
            "asn": asn,
            "cidr": str(cidr),
        })
        if ip == trace[-1][1]:
            break
    return cleaned_trace

# iterate all files in a directory
for filename in os.listdir(input_directory):
    # read json file
    file = os.path.join(input_directory, filename)
    with open(file) as f:
        data = json.load(f)

    cleaned = []
    for traceroute in data:
        cleaned_traces = []
        for trace in traceroute["traces"]:
            cleaned_trace = clean_trace(trace)
            cleaned_traces.append(cleaned_trace)
        cleaned.append({
            "endpoint": traceroute["endpoint"],
            "traces": cleaned_traces,
        })

    # write json file
    file = os.path.join(output_directory, filename)
    with open(file, "w") as f:
        json.dump(cleaned, f, indent=4)
