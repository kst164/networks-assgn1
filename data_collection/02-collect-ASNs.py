# iterate all json files in a directory

import os
import json
import ipaddress

import requests

directory = "raw_traces"

ip_set = set()
ip_set.add("16.10.16.9") # blore
ip_set.add("192.140.152.217") # blore2

# iterate all files in a directory
for filename in os.listdir(directory):
    # read json file
    file = os.path.join(directory, filename)
    with open(file) as f:
        data = json.load(f)

    for traceroute in data:
        for trace in traceroute["traces"]:
            for ttl, ip, rtt in trace:
                ip_set.add(ip)

# ip to asn
asn_dict = {}

# asn to cidr, shortname, country
asn_info = {}

# get ip's asn, and cache asn info
def get_asn(ip):
    ip = ipaddress.ip_address(ip)
    if ip.is_private:
        return None
    for asn, info in asn_info.items():
        for cidr in info["cidr_list"]:
            if ip in ipaddress.ip_network(cidr):
                return asn

    url = f"https://freeapi.dnslytics.net/v1/ip2asn/{ip}"

    r = requests.get(url)
    if r.status_code != 200:
        return None
    this_as = r.json()

    if not this_as["announced"]:
        print(f"ip {ip} not announced")
        return None
    if this_as["asn"] in asn_info:
        asn_info[this_as["asn"]]["cidr_list"].append(this_as["cidr"])
    else:
        asn_info[this_as["asn"]] = {
            "shortname": this_as["shortname"],
            "cidr_list": [
                this_as["cidr"],
            ],
            "country": this_as["country"],
        }
    return this_as["asn"]

for i, ip in enumerate(ip_set):
    print(f"{i+1}/{len(ip_set)}")
    asn = get_asn(ip)
    if asn is None:
        continue
    asn_dict[ip] = get_asn(ip)

with open("as_info.json", "w") as f:
    json.dump(asn_info, f, indent=4)

with open("ip_to_asn.json", "w") as f:
    json.dump(asn_dict, f, indent=4)
