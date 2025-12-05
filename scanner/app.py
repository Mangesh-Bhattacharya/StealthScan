# scanner/app.py
"""
Streamlit UI that ties the simulated scanner together.
Run with: streamlit run scanner/app.py
"""

import streamlit as st
from .stealth_scan import run_simulation, analyze_with_ai
from .report import save_json_report, make_markdown_summary, save_markdown_report
from ..utils.validators import validate_targets
from ..utils.visualization import plot_risk_chart
import json
import io

st.set_page_config(page_title="StealthScan-Sim", layout="wide")

st.title("StealthScan-Sim — safe simulated reconnaissance for labs & training")
st.markdown(
    """
**Important:** This tool runs *simulations only* and does not perform network scanning. Use for training and lab exercises.
"""
)

with st.sidebar:
    st.header("Scan options")
    targets_input = st.text_area("Targets (comma-separated hostnames for simulation)", value="lab-host-1, lab-host-2, localhost")
    depth = st.slider("Depth (simulated)", 1, 6, 3)
    throttle = st.slider("Throttle (seconds between simulated hosts)", 0.0, 2.0, 0.2, step=0.1)
    run_ai = st.checkbox("Run AI analysis (safe)", value=True)
    seed = st.text_input("Random seed (optional for reproducibility)", value="")
    seed_val = int(seed) if seed.strip().isdigit() else None
    if st.button("Run Simulation"):
        # validate input
        targets = [t.strip() for t in targets_input.split(",") if t.strip()]
        invalid = validate_targets(targets)
        if invalid:
            st.error(f"Invalid targets: {invalid}")
        else:
            with st.spinner("Running simulated scan..."):
                results = run_simulation(targets, depth=depth, throttle_seconds=throttle, verbose=False, seed=seed_val)
            st.success("Simulation complete")
            st.session_state["last_results"] = results

if "last_results" in st.session_state:
    results = st.session_state["last_results"]
    # show summary table
    st.subheader("Summary")
    try:
        import pandas as pd
        rows = []
        for r in results:
            rows.append({
                "hostname": r["hostname"],
                "services_count": len(r["services"]),
                "aggregate_risk": r["aggregate_risk"],
                "evasion_score": r["evasion"]["evasion_score"]
            })
        df = pd.DataFrame(rows)
        st.dataframe(df)
        # visualization
        st.pyplot(plot_risk_chart(df["hostname"].tolist(), df["aggregate_risk"].tolist()))
    except Exception as e:
        st.write("Unable to render table/chart:", e)

    st.subheader("Host details (simulated)")
    for host in results:
        with st.expander(f"{host['hostname']} — risk {host['aggregate_risk']}"):
            st.json(host)

    if run_ai:
        with st.spinner("Running safe AI analysis..."):
            ai_out = analyze_with_ai(results)
        st.subheader("AI analysis (safe)")
        st.write(ai_out)

    st.subheader("Reports")
    md = make_markdown_summary(results)
    json_path = save_json_report(results)
    md_path = save_markdown_report(md)
    st.markdown(f"- JSON report saved to `{json_path}`")
    st.markdown(f"- Markdown report saved to `{md_path}`")

    # allow downloads in memory
    buf = io.BytesIO(json.dumps({"results": results}, indent=2).encode("utf-8"))
    st.download_button(label="Download JSON", data=buf, file_name="stealthsim_results.json", mime="application/json")

    st.download_button(label="Download Markdown", data=md.encode("utf-8"), file_name="stealthsim_report.md", mime="text/markdown")
else:
    st.info("Run a simulation from the sidebar to get started.")
    