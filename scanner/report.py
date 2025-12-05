# scanner/report.py
"""
Report generation for simulated scans.
Generates JSON and Markdown reports that are safe and non-actionable.
"""

import json
from datetime import datetime
from pathlib import Path

def _now_str():
    return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def save_json_report(results, out_dir="reports", name_prefix="stealthsim"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    filename = f"{name_prefix}_{_now_str()}.json"
    fp = Path(out_dir) / filename
    with fp.open("w", encoding="utf-8") as f:
        json.dump({"generated_at": datetime.utcnow().isoformat() + "Z", "results": results}, f, indent=2)
    return str(fp)

def make_markdown_summary(results):
    """
    Create a readable markdown summary suitable for sharing in training materials.
    This intentionally avoids giving exploit paths or actionable commands.
    """
    lines = []
    lines.append("# StealthScan-Sim Report (simulated)\n")
    lines.append(f"Generated: {datetime.utcnow().isoformat()}Z\n")
    for host in results:
        lines.append(f"## Host: {host['hostname']}\n")
        lines.append(f"- Aggregate simulated risk: **{host['aggregate_risk']}**")
        lines.append(f"- Evasion score (simulated): **{host['evasion']['evasion_score']}**")
        lines.append("\n### Services discovered (simulated):\n")
        for s in host["services"]:
            lines.append(f"- `{s['service']}` on port {s['port']} — simulated banner: `{s['banner']}`; simulated vuln score: {s['simulated_vuln_score']}")
        lines.append("\n> Note: simulated results only — for lab/training use.\n")
    return "\n".join(lines)

def save_markdown_report(md_text, out_dir="reports", name_prefix="stealthsim"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    filename = f"{name_prefix}_{_now_str()}.md"
    fp = Path(out_dir) / filename
    fp.write_text(md_text, encoding="utf-8")
    return str(fp)
class ReportGenerator:
    def generate(self, summary, evasion_data, out_dir="reports"):
        """
        Generate both JSON and Markdown reports from the scan summary and evasion data.
        Returns the JSON report content as a string.
        """
        results = {
            "summary": summary,
            "evasion_analysis": evasion_data,
        }
        json_path = save_json_report(results, out_dir=out_dir)
        md_text = make_markdown_summary(summary.get("hosts", []))
        md_path = save_markdown_report(md_text, out_dir=out_dir)

        print(f"Reports generated:\n- JSON: {json_path}\n- Markdown: {md_path}")
        with open(json_path, "r", encoding="utf-8") as f:
            return f.read()
        
# Example usage:
# reporter = ReportGenerator()
# report_file = reporter.generate(summary={}, evasion_data={})