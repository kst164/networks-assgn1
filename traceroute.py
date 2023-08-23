from typing import List, Tuple
import subprocess
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
    "www.ox.ac.uk",
    "www.cam.ac.uk",
    "www.berkeley.edu",
    "www.ntu.edu.sg",
    "www.tsinghua.edu.cn",
    "www.ethz.ch",
    "www.uva.nl",
    "www.utoronto.ca",
    "www.mcgill.ca",
    "www.tifr.res.in",
    "www.iitb.ac.in",
    "www.iisc.ac.in",
    "www.iitd.ac.in",
    "www.iitkgp.ac.in",
    "www.iitm.ac.in",
    "www.iitk.ac.in",
    "www.iith.ac.in",
    "www.uct.ac.za",
    "www5.usp.br",
    "www.u-paris.fr",
    "www.u-tokyo.ac.jp",
    "www.kyoto-u.ac.jp",
]

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
    final.append({
        "endpoint": endpoint,
        "traces": traces,
    })

with open(sys.argv[1], "w") as f:
    f.write(json.dumps(final, indent=4))
