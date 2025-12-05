# scanner/ai_agent.py
"""
AI Agent wrapper.
- If OPENAI_API_KEY environment variable is set and openai package is available, it will attempt to use it.
- Otherwise falls back to a deterministic, local rule-based analyzer suitable for training/education.
This module never produces exploit code; it provides recommendations for detection and mitigation only.
"""

import os
import openai
import json
from typing import List, Dict

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

class AIAgent:
    def __init__(self, use_openai: bool = False):
        self.use_openai = use_openai and (OPENAI_KEY is not None)
        if self.use_openai:
            try:
                openai.api_key = OPENAI_KEY
                self._openai = openai
            except Exception:
                self.use_openai = False
                self._openai = None
        else:
            self._openai = None

    def analyze(self, sim_results: List[Dict], prompt: str = "", model: str = "default"):
        """
        Return a recommendations dict.
        If OpenAI is available and enabled, a safe, high-level prompt is sent.
        Otherwise a deterministic rule-based analysis is returned.
        """
        if self.use_openai and self._openai:
            # Very high-level safe prompt. No request for exploit steps.
            messages = [
                {"role": "system", "content": "You are an assistant that provides high-level defensive recommendations based on simulated cybersecurity scan outputs. Do not provide exploit code or offensive steps."},
                {"role": "user", "content": f"{prompt}\n\nSimulated results (JSON):\n{json.dumps(sim_results, indent=2)[:8000]}"}
            ]
            try:
                resp = self._openai.ChatCompletion.create(
                    model="gpt-4o-mini", messages=messages, max_tokens=600
                )
                text = resp["choices"][0]["message"]["content"].strip()
                return {"source": "openai", "analysis": text}
            except Exception as e:
                # fallback
                pass

        # Deterministic fallback:
        return {"source": "local_rule_based", "analysis": self._local_analyze(sim_results)}

    def _local_analyze(self, sim_results):
        """
        Produce safe, human-readable recommendations based on simulated results.
        """
        recs = []
        # Prioritize hosts with higher aggregate_risk
        sorted_hosts = sorted(sim_results, key=lambda h: h.get("aggregate_risk", 0), reverse=True)
        for host in sorted_hosts:
            hr = host.get("aggregate_risk", 0)
            esc = host.get("evasion", {}).get("evasion_score", 0)
            host_name = host.get("hostname")
            if hr >= 0.7:
                recs.append({
                    "hostname": host_name,
                    "priority": "high",
                    "recommendation": "Investigate service configurations, check patch levels, and verify only authorized services are running. Increase logging for these hosts."
                })
            elif hr >= 0.4:
                recs.append({
                    "hostname": host_name,
                    "priority": "medium",
                    "recommendation": "Review exposed services and consider network segmentation or firewall rules to reduce exposure."
                })
            else:
                recs.append({
                    "hostname": host_name,
                    "priority": "low",
                    "recommendation": "Baseline the host and continue monitoring; ensure host inventory is up to date."
                })
            # Evasion-specific guidance
            if esc >= 0.6:
                recs[-1]["evasion_note"] = "Simulated evasion seems high — recommend tuning IDS/endpoint heuristics and adding anomaly-based detection rules."
        # Summarize
        summary = {
            "summary": f"Analyzed {len(sim_results)} simulated hosts. Highest risk host: {sorted_hosts[0]['hostname'] if sorted_hosts else 'n/a'}",
            "recommendations": recs
        }
        return summary
# Example usage:
# agent = AIAgent(use_openai=True)
# analysis = agent.analyze(sim_results=summary["hosts"], prompt="Provide defensive recommendations based on the simulated scan results.")
# print(analysis)