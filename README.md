<p align="center">
  <img src="https://img.shields.io/badge/Live%20App-Click%20to%20Launch-blueviolet?style=for-the-badge&logo=streamlit" alt="Live App Badge"/>
  <br>
  <a href="https://beyonder016-data-spatial-explorer.streamlit.app/">
    👉 <strong>Launch DataSpatial Explorer Now</strong>
  </a>
</p>

<h1 align="center">🧠 DataSpatial Explorer – Signal Mesh Simulation</h1>

<p align="center">
  A futuristic simulation that brings signal-emitting devices to life in a 2D space.<br>
  Built with <strong>Streamlit</strong>, <strong>Plotly</strong>, and <strong>Python</strong>.
</p>

---

## 🎥 Demo Preview

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmNjcTljZXB2dW55cjdvNXQxYWJoa2lpZ3FuOWp1bWd1MGp3bGgyaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o6ZsXK9gbFstpH2Vi/giphy.gif" alt="demo gif" width="75%">
</p>

> ⚠️ Don't see anything? Replace this link with your own GIF for better showcasing.

---

## 🚀 What is DataSpatial Explorer?

**DataSpatial Explorer** is a signal simulation and visualization tool where "data objects" behave like real-world devices in space.

Instead of traditional CRUD logic, this app **models behavior based on distance, overlap, and interference**, making it ideal for:

- 🛰 Wireless sensor network modeling
- 📶 Wi-Fi/IoT signal placement testing
- 🤖 Agent-based systems
- 🎓 Education in spatial computing or data visualization

---

## 🌟 Features at a Glance

🔧 **Interactive Device Setup**
- Add devices with custom IDs, positions, and signal ranges
- Modify existing devices instantly with live feedback

📊 **Dynamic Visualization**
- Visual 2D grid powered by Plotly
- Devices and signal radii rendered as interactive nodes
- Connections auto-highlighted by signal logic

🎨 **Color-Coded Signal Logic**
| Status         | Meaning                                       | Color   |
|----------------|-----------------------------------------------|---------|
| 🟢 Connected    | Signal reaches another device's center        | Green   |
| 🟡 Overlapping  | Signals overlap but not fully connected       | Yellow  |
| 🔴 Interfering  | Both signals overlap each other's centers     | Red     |
| ⚫ Isolated     | Device stands alone, no connections           | Gray    |

🌀 **Simulate Movement**
- Devices drift randomly to simulate mobility
- Triggers real-time connection updates

📘 **Live Connection Status**
- Textual log of current connection states below the grid
- Auto-refreshes with every move or edit

---

## 📌 Use Cases

- **IoT Planning**: Test ideal sensor placements
- **Mesh Network Design**: Simulate signal spread and loss
- **Emergency Scenarios**: Visualize coverage gaps
- **Teaching Aid**: Explain proximity, distance, and network theory

---

## 📦 Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Frontend  | Streamlit          |
| Plotting  | Plotly             |
| Backend   | Python (custom logic) |
| Hosting   | Streamlit Cloud    |

---

## 💻 Run It Locally

```bash
# 1. Clone the repo
git clone https://github.com/Beyonder016/data-spatial-explorer.git
cd data-spatial-explorer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app/main.py
