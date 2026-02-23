# Real-Time SSH Attack Detection & Active Response System

##  Overview

This project implements a real-time SSH brute force detection system with automated incident response using Linux firewall rules.

The system continuously monitors `/var/log/auth.log`, detects repeated failed login attempts from the same IP address within a defined time window, and automatically blocks malicious sources using `iptables`.

The project was developed in a virtualized Ubuntu Server environment to simulate real-world attack scenarios and demonstrate practical defensive security implementation.

---

##  Key Features

- Real-time monitoring of SSH authentication logs  
- Detection of repeated failed login attempts  
- Sliding time window algorithm (5 attempts within 2 minutes)  
- Automated IP blocking via `iptables`  
- Modular and extensible architecture  
- Designed for future expansion to detect additional attack types  

---

##  Technologies Used

- Python  
- Ubuntu Server  
- iptables  
- VMware Workstation Pro (virtualized lab environment)  
- Regex-based log parsing  

---


### Module Responsibilities

- **log_watcher.py** → Monitors `/var/log/auth.log` in real time  
- **failed_login_detector.py** → Applies regex parsing and sliding window logic  
- **iptables_manager.py** → Handles automated firewall rule insertion  
- **main.py** → Orchestrates system flow  

This separation improves maintainability, clarity, and scalability.

---

##  Detection Logic

1. Continuously monitor `/var/log/auth.log`  
2. Identify entries containing `"Failed password"`  
3. Extract source IP address using regex  
4. Store timestamps of attempts per IP  
5. Remove outdated attempts outside a 2-minute window  
6. Block IP when 5 or more attempts are detected within the window  

---

## 🧪 Lab Environment

- Windows host machine  
- VMware Workstation Pro  
- Ubuntu Server virtual machine  
- OpenSSH service enabled  
- Simulated brute force attempts for validation  

---

##  Future Improvements

- Support for additional attack patterns (port scans, HTTP abuse, etc.)
- Automatic unblocking after configurable timeout
- Alerting system (email / webhook)
- Configuration via external `config.json`
- Log rotation handling
- Web-based monitoring dashboard

---

##  Inspiration

Inspired by defensive tools such as Fail2Ban, this project demonstrates understanding of:

- Log-based intrusion detection  
- Behavioral pattern analysis  
- Sliding window rate limiting  
- Automated incident response  
- Linux system security  

---

##  Purpose

This project was created to demonstrate practical cybersecurity skills including:

- Real-time log analysis  
- Threat detection logic  
- Firewall automation  
- Linux administration  
- Modular software architecture  

---

##  Disclaimer

This project is intended for educational and defensive security purposes only.  
All testing was performed in a controlled lab environment.
