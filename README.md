# Project 1: Wi-Fi Signal Mapper

## Proposal

### The Problem
In indoor environments, Wi-Fi coverage is frequently degraded by structural obstacles and poor router placement, making it hard to identify dead zones without expensive software.

### Why It Matters
A visual heatmap transforms raw numeric RSSI logs into an intuitive map, enabling instant identification of weak signal areas and optimized router placement.

### Team Members & Roles
* **Mohammad Itani** – Data Ingestion & Interpolation Logic (CSV parsing, SciPy/NumPy math)

### Tools Plan
* **Language:** Python 3.10+
* **Libraries:** pandas, matplotlib, scipy, numpy
* **Version Control:** Git & GitHub
* **AI Assistance:** Gemini for structuring specifications and plotting code optimization.

## Milestone 2 Prototype
- **Requirement Met:** R1 (CSV data loading and validation) & R5 (minimum 20 spatial points).
- **How to Run:**
  ```bash
  python src/mapper.py