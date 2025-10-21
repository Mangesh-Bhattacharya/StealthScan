from scapy.all import rdpcap
from collections import Counter

class StealthScanner:
    def __init__(self, pcap_path):
        self.pcap_path = pcap_path

    def analyze_pcap(self):
        packets = rdpcap(self.pcap_path)
        protocols = Counter()
        endpoints = Counter()

        for pkt in packets:
            proto = getattr(pkt, 'proto', None)
            src = getattr(pkt, 'src', None)
            dst = getattr(pkt, 'dst', None)
            if proto is not None:
                protocols[proto] += 1
            if src and dst:
                endpoints[src] += 1
                endpoints[dst] += 1

        return {
            "file": self.pcap_path,
            "total_packets": len(packets),
            "protocol_distribution": dict(protocols),
            "top_endpoints": endpoints.most_common(10)
        }
