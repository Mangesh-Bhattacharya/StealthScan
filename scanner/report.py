import json
from datetime import datetime

class ReportGenerator:
    def generate(self, summary, evasion_results):
        report_data = {
            "scan_summary": summary,
            "evasion_analysis": evasion_results,
            "generated_on": datetime.now().isoformat()
        }
        report_path = "stealthscan_report.json"
        with open(report_path, "w") as f:
            json.dump(report_data, f, indent=4)
        return report_path
    