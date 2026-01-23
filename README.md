# 🚖 Uber Analytics Executive Dashboard (2024)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end Data Analytics & Executive Dashboard project analyzing **148,000+ Uber ride bookings** in the NCR region for the year 2024. This project provides actionable insights into ride completion rates, revenue drivers, and cancellation patterns through advanced visualizations and interactive mapping.

![Dashboard Preview](dashboard_preview.png)

## 🚀 Interactive Dashboard Features

- **Executive KPI Tracking**: Real-time monitoring of Gross Revenue, Completion Rates, and Customer Satisfaction (CSAT).
- **GitHub-Inspired UI**: Clean, light-themed interface with custom CSS for a professional enterprise look.
- **Root Cause Analysis**: Sunburst visualizations for hierarchical cancellation data attribution.
- **Temporal Deep-Dives**: Performance analysis by Time of Day, Day Type (Weekday vs. Weekend), and Month.
- **Strategic Geospatial Mapping**: Heatmaps identifying high-demand clusters and cancellation hotspots in the NCR region.
- **Dynamic Filtering**: Global sidebar filters for Vehicle Category, Payment Method, and Date Range.

## 🛠️ Project Architecture

1. **Jupyter Notebook (`uber_analysis.ipynb`)**: Detailed end-to-end analysis including:
   - Data Cleaning (Handling 148k+ records, nulls, and format standardization).
   - Exploratory Data Analysis (EDA).
   - Revenue density mapping (Revenue per KM).
   - Strategic Recommendations based on data trends.
2. **Streamlit Application (`dashboard.py`)**: An interactive, production-ready dashboard served via Streamlit.
3. **Configuration (`.streamlit/config.toml`)**: Custom theme configuration for forced light mode and branding.

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Divyadhole/Uber-Analytics-Executive-Dashboard.git
   cd Uber-Analytics-Executive-Dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

## 📊 Key Insights

- **Revenue Drivers**: Premier Sedans and Go Sedans contribute over 60% of total revenue despite making up only 40% of ride volume.
- **Cancellation Paradox**: The primary cause of churn is "Driver not moving towards pickup," peaking during evening rush hours (6 PM - 9 PM).
- **Geospatial Hotspots**: High demand is concentrated in Saket, AIIMS, and Khandsa, presenting opportunities for dynamic incentive programs.

## 🛠️ Tech Stack

- **Language**: Python 3.12
- **Data Handling**: Pandas, NumPy
- **Visuals**: Plotly, Seaborn, Matplotlib
- **Geospatial**: Folium, Streamlit-Folium
- **UI Framework**: Streamlit (with custom CSS injection)

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
**Author**: [Divya Dhole](https://github.com/Divyadhole)
