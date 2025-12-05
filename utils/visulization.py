# utils/visualization.py
"""
Visualization helpers using matplotlib.
Streamlit will render the returned figure.
"""

import matplotlib.pyplot as plt
from typing import List

def plot_risk_chart(hosts: List[str], risks: List[float]):
    fig, ax = plt.subplots(figsize=(8, 3.5))
    y_pos = range(len(hosts))
    ax.barh(y_pos, risks, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(hosts)
    ax.invert_yaxis()
    ax.set_xlabel("Aggregate simulated risk")
    ax.set_title("Simulated host risk overview")
    ax.set_xlim(0, 1)
    plt.tight_layout()
    return fig
# --- end of visualization.py ---