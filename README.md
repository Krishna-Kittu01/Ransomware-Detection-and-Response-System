# 🛡️ Ransomware Detection and Response System (RDRS)

## 📌 Overview

The Ransomware Detection and Response System (RDRS) is a Python-based cybersecurity project that monitors file system activity in real time, detects suspicious file modifications using entropy analysis, stores security events in a SQLite database, quarantines suspicious files, and generates security reports through a graphical dashboard.

---

## 🚀 Features

- Real-time file monitoring using Watchdog
- Shannon entropy-based ransomware detection
- SQLite database logging
- Automatic ransomware alerts
- File quarantine mechanism
- Security report generation
- GUI dashboard built with Tkinter
- Configurable detection thresholds

---

## 🛠️ Technologies Used

- Python
- Watchdog
- SQLite
- Tkinter
- Loguru
- PyYAML

---

## 📂 Project Structure

```
rdrs/
│
├── app/
│   ├── core/
│   ├── database/
│   ├── detectors/
│   ├── dashboard/
│   ├── reports/
│   └── response/
│
├── data/
├── logs/
├── reports/
├── config.yaml
├── main.py
└── README.md
```

---

## ▶️ How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start monitoring

```bash
python main.py
```

### Launch Dashboard

```bash
python app/dashboard/dashboard.py
```

### Generate Security Report

```bash
python app/reports/generate_report.py
```

---

## 🔄 Project Workflow

1. Monitor selected folders.
2. Detect file creation and modification.
3. Calculate Shannon entropy.
4. Compare entropy with the configured threshold.
5. Log events into SQLite.
6. Generate alerts for suspicious files.
7. Move suspicious files to quarantine.
8. Generate security reports.
9. Display statistics in the GUI dashboard.

---

## 🔮 Future Improvements

- Machine learning-based ransomware detection
- Email alert notifications
- Web dashboard
- Multi-folder monitoring
- Cloud log storage
- Real-time analytics

---

## 👨‍💻 Author

**Krishna Bhukya**

B.Tech Final Year Student

Cybersecurity & Python Developer


