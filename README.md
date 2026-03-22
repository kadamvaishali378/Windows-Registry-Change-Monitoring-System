# 🛡️ Windows Registry Change Monitoring System

### Cybersecurity Monitoring Tool for Detecting Persistence & Policy Tampering

🔗 **Project Repository:** [https://github.com/your-username/windows-registry-monitor](https://github.com/your-username/windows-registry-monitor)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Security](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Overview

The **Windows Registry Change Monitoring System** is a cybersecurity tool developed as part of an internship project to detect suspicious changes in the Windows Registry.

It focuses on identifying common attack techniques such as:

* Malware persistence via autorun registry entries
* Security policy tampering (e.g., disabling Windows Defender)

The system compares current registry values with a stored **baseline snapshot**, allowing detection of unauthorized additions and configuration changes.

---

## 🚀 Key Features

✔ Autorun registry monitoring
✔ Detection of unauthorized registry changes
✔ Windows Defender tampering detection
✔ JSON-based baseline snapshot
✔ Real-time alert generation
✔ Timestamp-based logging
✔ Lightweight and easy to run

---

## 🛠️ Tech Stack

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Core logic              |
| winreg     | Access Windows Registry |
| json       | Store baseline snapshot |
| datetime   | Generate timestamps     |

---

## 🐍 Python Version

Python 3.x (Recommended: Python 3.8 or above)

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/your-username/windows-registry-monitor.git

# Navigate to project
cd windows-registry-monitor

# Run application
python monitor.py
```

---

## 🧪 Usage

1. Run the monitoring script
2. System scans registry keys
3. Alerts are generated if suspicious changes are detected

---

## 🔍 Test Scenario (Detection)

1. Open Registry Editor (`regedit`)
2. Navigate to:

```
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

3. Add a new String Value:

```
Name: TestMalwareEntry
Value: C:\\test.exe
```

4. Run the script again

---

## 🧠 Detection Techniques

### 🔹 Autorun Monitoring

* Tracks startup registry entries
* Detects newly added programs

### 🔹 Baseline Comparison

* Uses `baseline.json`
* Compares current vs original state

### 🔹 Security Policy Check

* Monitors Windows Defender settings
* Detects disabling attempts

### 🔹 Logging Mechanism

* Records alerts with timestamps
* Stores events in `logs.txt`

---

## 🏗️ System Architecture

```
Windows Registry → Python Script → winreg Module
                  → Baseline Comparison (JSON)
                  → Change Detection
                  → Security Policy Check
                  → Alert System → Logging Module
```

---

## 🔄 Workflow

1. Load baseline snapshot
2. Read current registry values
3. Compare with baseline
4. Detect new entries
5. Check Defender policy
6. Generate alerts
7. Log events

---

## 📊 Output

* Alerts displayed in terminal
* Logs stored in `logs.txt`

### Example Output

```
[AUTORUN] New startup entry detected: TestMalwareEntry -> C:\\test.exe
[SECURITY] Suspicious Defender policy detected
```

---

## 📁 Project Structure

```
windows-registry-monitor/
│── monitor.py
│── baseline.json
│── logs.txt
│── README.md
```

---

## ✅ Advantages

* Detects persistence mechanisms
* Helps identify security tampering
* Simple and lightweight tool
* Useful for learning cybersecurity concepts
* Supports forensic analysis through logs

---

## ⚠️ Limitations

* Monitors only one autorun key
* Detects only new entries
* No real-time monitoring
* Limited registry coverage

---

## 🚀 Future Improvements

* Real-time registry monitoring
* Multiple registry path coverage
* Detection of modified/deleted entries
* GUI dashboard
* SIEM integration

---

## 📚 Learning Outcomes

* Understanding Windows Registry
* Detecting persistence techniques
* Python-based monitoring systems
* Log analysis
* Security event detection

---

## 🏁 Conclusion

This project demonstrates how registry monitoring can detect suspicious system changes and potential security threats. It provides practical exposure to real-world cybersecurity monitoring techniques.

---

## 📦 Deliverables

* Python script (`monitor.py`)
* Baseline file (`baseline.json`)
* Log file (`logs.txt`)
* Documentation
* Screenshots

---

## 👩‍💻 Author

**Vaishali Vasant Kadam**
Cyber Security Internship Project
📅 22 March 2026

---

⭐ *If you like this project, consider giving it a star!*
