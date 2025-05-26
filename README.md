<p align="center">
  <img src="https://img.shields.io/badge/Live%20Demo-Streamlit-blueviolet?logo=streamlit" />
</p>

<h1 align="center">🧠 DataSpatial Explorer</h1>

<p align="center">
  <strong>A futuristic 2D signal mesh simulator powered by Python + Streamlit</strong>  
</p>

<p align="center">
  <a href="https://beyonder016-data-spatial-explorer.streamlit.app/" target="_blank">
    👉 <strong>Try the Live Demo Now</strong>
  </a>
</p>

---

## 🎬 Preview

> Here’s how the simulation looks in action 👇

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmNjcTljZXB2dW55cjdvNXQxYWJoa2lpZ3FuOWp1bWd1MGp3bGgyaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o6ZsXK9gbFstpH2Vi/giphy.gif" alt="demo-gif" width="80%" />
</p>

---

## 🚀 About the Project

**DataSpatial Explorer** is an interactive signal simulation that models devices in a 2D grid — each broadcasting a signal radius. The project is inspired by **spatial programming** concepts and explores dynamic, reactive behaviors based on proximity and signal overlap.

---

## 🧠 Core Features

- 🎯 **Add & edit devices**: Set unique IDs, position, and signal radius
- 🧩 **Real-time grid visualization** using Plotly
- 🌐 **Connection logic**:
  - Green = Connected (signal reaches center)
  - Yellow = Overlapping (edges touch)
  - Red = Interfering (bi-directional overlap)
- 🌀 **Live drift simulation**: Devices move randomly in space
- 📡 **Dynamic status updates**: Visual & text-based relationship feedback

---

## 💻 Built With

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [Python 3](https://www.python.org/)

---

## 📦 Folder Structure

```bash
data-spatial-explorer/
│
├── app/
│   ├── main.py              # Streamlit app entry point
│   ├── spatial_logic.py     # Device behavior & signal logic
│   ├── ui_utils.py          # Plotting logic
│   ├── config.py            # Constants (colors, defaults)
│   └── __init__.py
│
├── .gitignore
├── requirements.txt
├── README.md
