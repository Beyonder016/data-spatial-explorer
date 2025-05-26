# app/main1.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
from app.spatial_logic import Device, check_connections
from app.ui_utils import generate_plot
from app.config import DEFAULT_SIGNAL_RADIUS
import time
import random

st.set_page_config(page_title="DataSpatial Explorer", layout="wide")
st.title("🧠 DataSpatial Explorer — Signal Mesh Simulation")
st.markdown("Place and simulate devices that broadcast signals in a 2D space.")

# Initialize device list
if "device_list" not in st.session_state:
    st.session_state.device_list = []

# ───── Sidebar ─────
with st.sidebar:
    st.header("📟 Add Device")
    new_id = st.text_input("Device ID", value=f"D{len(st.session_state.device_list) + 1}")
    x = st.slider("X Position", 0, 100, 50)
    y = st.slider("Y Position", 0, 100, 50)
    r = st.slider("Signal Radius", 5, 50, int(DEFAULT_SIGNAL_RADIUS))
    if st.button("➕ Add Device"):
        if all(d.id != new_id for d in st.session_state.device_list):
            st.session_state.device_list.append(Device(new_id, x, y, r))
            st.success(f"Device {new_id} added.")

    st.markdown("---")

    st.header("🛠 Edit Device")
    if st.session_state.device_list:
        selected_id = st.selectbox("Choose a Device", [d.id for d in st.session_state.device_list])
        selected_device = next(d for d in st.session_state.device_list if d.id == selected_id)

        new_x = st.slider("New X", 0, 100, int(selected_device.x), key="edit_x")
        new_y = st.slider("New Y", 0, 100, int(selected_device.y), key="edit_y")
        new_r = st.slider("New Radius", 5, 50, int(selected_device.signal_radius), key="edit_r")

        if st.button("🔁 Update Device"):
            for idx, d in enumerate(st.session_state.device_list):
                if d.id == selected_id:
                    st.session_state.device_list[idx] = Device(selected_id, new_x, new_y, new_r)
                    break
            st.success(f"{selected_id} updated.")

# ───── Main View ─────
if st.session_state.device_list:
    connections = check_connections(st.session_state.device_list)
    fig = generate_plot(st.session_state.device_list, connections)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔍 Connection Status")
    if connections:
        for d1, d2, status in connections:
            st.markdown(f"**{d1}** ↔ **{d2}** : `{status}`")
    else:
        st.info("No connections found.")
else:
    st.warning("Add at least one device to begin simulation.")

# ───── Simulation Drift ─────
st.markdown("---")
st.header("🌀 Simulate Movement")
if st.button("▶️ Run Device Drift"):
    steps = 10
    for _ in range(steps):
        for idx, device in enumerate(st.session_state.device_list):
            new_x = min(100, max(0, device.x + random.uniform(-3, 3)))
            new_y = min(100, max(0, device.y + random.uniform(-3, 3)))
            st.session_state.device_list[idx] = Device(device.id, new_x, new_y, device.signal_radius)

        fig = generate_plot(st.session_state.device_list, check_connections(st.session_state.device_list))
        st.plotly_chart(fig, use_container_width=True)
        time.sleep(0.5)
