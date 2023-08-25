from typing import List, Tuple
import requests
import json
import sys

from scapy.layers.inet import traceroute

"""
Usage: python3 traceroute.py <output_file>

Requires scapy to be installed
On Linux, needs to be run as root
    scapy: sudo pip3 install scapy
    run: sudo python3 traceroute.py <output_file>
"""

if len(sys.argv) != 2:
    print("Usage: python3 traceroute.py <output_file>")
    sys.exit(1)

endpoints = [
    "stanford.edu",
    # "ox.ac.uk",
    # "cam.ac.uk",
    # "berkeley.edu",
    # "ntu.edu.sg",
    # "www.tsinghua.edu.cn",
    # "ethz.ch",
    "uva.nl",
    # "utoronto.ca",
    "mcgill.ca",
    "www.tifr.res.in",
    "iitb.ac.in",
    # "iisc.ac.in",
    "iitd.ac.in",
    "iitkgp.ac.in",
    "www.iitm.ac.in",
    "iitk.ac.in",
    # "iith.ac.in",
    "uct.ac.za",
    "usp.br",
    # "u-paris.fr",
    # "www.u-tokyo.ac.jp",
    # "kyoto-u.ac.jp",
]
# endpoints = ['stanford.edu']
# (ttl, dst ip, rtt (s))
PktDetail = Tuple[int, str, float]

def trace(endpoint):
    traces = []
    TRACE_COUNT = 3
    for i in range(TRACE_COUNT):
        print(f"  Traceroute {i+1}/{TRACE_COUNT}...", end="", flush=True)
        times: List[PktDetail] = []
        ans, _ = traceroute(endpoint, verbose=0, maxttl=50)
        for packet_pair in ans:
            sent = packet_pair.query.getlayer("IP")
            recv = packet_pair.answer.getlayer("IP")
            rtt = recv.time - sent.sent_time
            times.append((sent.ttl, recv.src, rtt))

        times.sort()
        # distance = min(ttl for ttl, dst, _ in times if dst == endpoint)
        # times = list(filter(lambda x: x[0] <= distance, times))

        traces.append(times)

        print(" done")
    return traces

final = []

for i, endpoint in enumerate(endpoints):
    print(f"{endpoint} ({i+1}/{len(endpoints)})")
    traces = trace(endpoint)
    x = traces[0][len(traces[0]) - 1]
    xx = requests.get(f'https://freeapi.dnslytics.net/v1/ip2asn/{x[1]}')
    print(endpoint, xx.json()['shortname'])
    final.append({
        "endpoint": endpoint,
        "traces": traces,
    })

with open(sys.argv[1], "w") as f:
    f.write(json.dumps(final, indent=4))
