import streamlit as st
from utils.validators import validate_pcap_file
from utils.visualization import render_summary, render_chart
from scanner.stealth_scan import StealthScanner
from scanner.evasion import EvasionEngine
from scanner.report import ReportGenerator

def main():
    st.set_page_config(page_title="StealthScan", layout="wide")
    st.title("🕵️ StealthScan - Advanced Red Team Reconnaissance Tool")

    st.markdown("Upload any **Wireshark PCAP** file below and let StealthScan automatically analyze, scan, and generate a dynamic security report.")

    uploaded_file = st.file_uploader("Upload PCAP:", type=["pcap", "pcapng"])

    if uploaded_file:
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        if not validate_pcap_file(file_path):
            st.error("Invalid PCAP file. Please ensure it’s captured using a supported Wireshark format.")
            return

        st.success("File validated successfully. Starting reconnaissance...")

        scanner = StealthScanner(file_path)
        summary = scanner.analyze_pcap()
        render_summary(summary)

        evasion = EvasionEngine()
        stealth_result = evasion.apply_stealth_modes(summary)
        render_chart(stealth_result)

        reporter = ReportGenerator()
        report_file = reporter.generate(summary, stealth_result)
        st.download_button("Download Recon Report (JSON)", report_file, file_name="stealthscan_report.json")

if __name__ == "__main__":
    main()
