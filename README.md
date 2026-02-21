# 🌊 AquaSwarm (Project UH-SWARM)
**Dual-Use Autonomous Amphibious Micro-Swarm Robotics System**

![Status: Active](https://img.shields.io/badge/Status-Active_Development-brightgreen)
![Tech: Edge AI](https://img.shields.io/badge/Tech-Edge_AI_%7C_ROS2-blue)
![Domain: Defense Tech](https://img.shields.io/badge/Domain-Dual--Use_Defense_Tech-red)

> **"We don't need to sink the ship; we just need to stop it."** > An autonomous, RF-silent, amphibious crawler swarm designed to transition seamlessly from a commercial aquatic maintenance MVP to a tactical asymmetric warfare asset.

---

## 🚀 Project Overview

AquaSwarm is a low-cost, decentralized swarm robotics platform. It tackles two distinct domains using the exact same core architecture:
1. **Commercial MVP:** Autonomous pool maintenance eliminating manual labor and docking infrastructure via amphibious self-recovery.
2. **Defense Tactical (USMC EABO):** A communication-independent (EMCON) micro-submarine swarm capable of underwater ISR, Surf Zone (Pipeline) transit, and amphibious seawall assaults for "Mobility Kill" operations.

## 🧠 Core Technologies & Capabilities

* **Decentralized Flocking (Swarm Intelligence):** Multi-agent coordination using Cohesion, Separation, and Alignment. No central server required.
* **Absolute Radio Silence (EMCON):** Zero reliance on GPS, Wi-Fi, or RF. Navigates using onboard IMU (Dead Reckoning) and Acoustic Sonar. Zero OPSEC risk (No cameras).
* **Amphibious Track System (ATS):** Utilizes hydrodynamic downforce and silicon-rubber tracks to scale 90-degree vertical walls, completely eliminating the need for recovery cranes or docks.
* **Deck Ops & Wireless Charge:** Autonomously navigates to a passive RFID-enabled Qi-charging mat on the deck after exfiltration.

---

## 🛠️ System Architecture

### 1. Hardware (BOM < $450 / unit)
The system prioritizes COTS (Commercial Off-The-Shelf) parts for attritability and rapid scaling:
* **Compute:** Raspberry Pi Zero 2W / ESP32-S3 (Edge AI)
* **Navigation:** MPU-9250 (9-DOF IMU), MS5837-30BA (Depth), JSN-SR04T (Sonar)
* **Propulsion:** Twin Brushless Thrusters + 1 Vertical Downforce Thruster
* **Mobility:** Shore 40A Silicon-rubber continuous tracks
* **Chassis:** 3D Printed PETG (Wedge-shaped for coping clearance)

### 2. Software Stack
* **Simulation:** HTML5 / Three.js (Boids Algorithm & Collision Avoidance)
* **Control Systems:** ROS 2 (Robot Operating System), C++, Python
* **Filtering:** Extended Kalman Filter (EKF) for underwater dead reckoning

---

## 🎮 Interactive Simulation & 3D Design

This repository includes a fully functional 3D simulation of the flocking algorithm and the interactive robot CAD design.

### How to Run:
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/AquaSwarm.git](https://github.com/yourusername/AquaSwarm.git)
