# scanner/stealth_scan.py
"""
Safe, simulated "stealth scanning" module.
NO real network calls. All data is synthetic and intended for lab/simulation use only.
"""

import random
import time
from datetime import datetime
from .evasion import compute_evasion_metrics
from .ai_agent import AIAgent

DEFAULT_SERVICES = [
    ("http", 80),
    ("https", 443),
    ("ssh", 22),
    ("rdp", 3389),
    ("smtp", 25),
    ("dns", 53),
    ("mysql", 3306),
    ("postgres", 5432),
]

def simulate_host(hostname: str, depth: int = 3, seed: int | None = None):
    """
    Simulate a host scan. Returns dict with services, simulated banners, and meta.
    """
    rng = random.Random(seed if seed is not None else (hash(hostname) & 0xffffffff))
    num_services = rng.randint(1, min(depth + 1, len(DEFAULT_SERVICES)))
    chosen = rng.sample(DEFAULT_SERVICES, num_services)

    services = []
    base_time = datetime.utcnow().isoformat() + "Z"
    for svc, port in chosen:
        banner = f"{svc.upper()}/{rng.choice(['1.0', '1.1', '2.0'])} - simulated"
        vuln_score = round(rng.uniform(0.0, 1.0), 2)  # 0 = low, 1 = severe (simulated)
        services.append({
            "service": svc,
            "port": port,
            "banner": banner,
            "simulated_vuln_score": vuln_score,
            "added_at": base_time
        })

    # Simulate evasion metrics using compute_evasion_metrics
    evasion = compute_evasion_metrics({
        "noise_level": rng.choice(["low", "medium", "high"]),
        "delay_ms": rng.randint(50, 1500),
        "technique": rng.choice(["timing", "packet_size_mod", "randomized_order"])
    })

    aggregate_risk = round(sum(s["simulated_vuln_score"] for s in services) / max(1, len(services)), 2)

    return {
        "hostname": hostname,
        "started_at": base_time,
        "services": services,
        "evasion": evasion,
        "aggregate_risk": aggregate_risk,
        "note": "This is a simulated result for lab/education only."
    }

def run_simulation(targets, depth=3, throttle_seconds=0.2, verbose=False, seed=None):
    """
    Simulate scanning multiple hosts. Yields results (list) for each target.
    """
    results = []
    for t in targets:
        if verbose:
            print(f"[sim] scanning {t} (depth={depth})")
        # Respect throttle_seconds purely as simulation pacing
        time.sleep(throttle_seconds)
        res = simulate_host(t, depth=depth, seed=seed)
        results.append(res)
    return results

def analyze_with_ai(results, model="default"):
    """
    Run the safe AI assistant (rule-based or via OpenAI if configured).
    Returns the agent's recommendations.
    """
    agent = AIAgent()
    prompt_text = "Analyze these simulated host results and produce prioritized action items for defenders."
    return agent.analyze(sim_results=results, prompt=prompt_text, model=model)
class StealthScanner:
    def __init__(self, pcap_file: str):
        self.pcap_file = pcap_file

    def analyze_pcap(self):
        """
        Analyze the PCAP file and return a summary of findings.
        This is a simulated analysis for demonstration purposes.
        """
        # In a real implementation, parse the PCAP and extract hosts
        simulated_hosts = ["host1.example.com", "host2.example.com", "host3.example.com"]
        results = run_simulation(simulated_hosts, depth=3, verbose=True)

        total_packets = 1500  # Simulated packet count
        top_endpoints = [(host, random.randint(10, 100)) for host in simulated_hosts]

        summary = {
            "total_packets": total_packets,
            "top_endpoints": top_endpoints,
            "detailed_results": results
        }
        return summary
    def generate_ai_report(self, results, model="default"):
        """
        Generate a report using AI analysis on the scan results.
        """
        ai_analysis = analyze_with_ai(results, model=model)
        return ai_analysis
    def perform_full_scan(self, depth=3, throttle_seconds=0.2, verbose=False, seed=None, ai_model="default"):
        """
        Perform the full simulated scan and return summary, evasion results, and AI report.
        """
        simulated_hosts = ["host1.example.com", "host2.example.com", "host3.example.com"]
        results = run_simulation(simulated_hosts, depth=depth, throttle_seconds=throttle_seconds, verbose=verbose, seed=seed)

        total_packets = 1500  # Simulated packet count
        top_endpoints = [(host, random.randint(10, 100)) for host in simulated_hosts]

        summary = {
            "total_packets": total_packets,
            "top_endpoints": top_endpoints,
            "detailed_results": results
        }

        evasion_results = {res["hostname"]: res["evasion"] for res in results}

        ai_report = self.generate_ai_report(results, model=ai_model)

        return summary, evasion_results, ai_report