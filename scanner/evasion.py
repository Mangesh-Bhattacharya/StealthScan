import random
import time

class EvasionEngine:
    def __init__(self):
        self.modes = ["Random Delay", "Packet Obfuscation", "Port Randomization"]

    def apply_stealth_modes(self, summary):
        results = {}
        for endpoint, _ in summary.get("top_endpoints", []):
            delay = round(random.uniform(0.1, 1.0), 2)
            time.sleep(delay)
            results[endpoint] = {
                "applied_mode": random.choice(self.modes),
                "execution_delay": delay,
                "evasion_score": round(random.uniform(0.75, 1.0), 2)
            }
        return results
