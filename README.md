# 🕵️‍♂️ Simple Python Port Scanner (using Nmap)

A beginner-friendly Python project that uses the [`python-nmap`](https://pypi.org/project/python-nmap/) library to perform quick and informative port scans on any host. It’s a great way to understand how Nmap can be automated with Python for network analysis, system auditing, or learning purposes.

---

## 🚀 Features

* Scans a target host using Nmap directly from Python
* Displays:

  * Host IP and hostname
  * Protocols detected (TCP/UDP)
  * Port numbers, states (open/closed), and detected services
  * Product and version information (via `-sV`)
* Saves the results to a text file (`scan_results.txt`)
* Easy to modify for automation or batch scanning

---

## 🧰 Requirements

Make sure you have the following installed:

1. **Python 3.7+**
2. **Nmap**

   * [Download here](https://nmap.org/download.html)
   * Verify it works by running:

     ```bash
     nmap -v
     ```
3. **python-nmap** library
   Install it using pip:

   ```bash
   pip install python-nmap
   ```

> ⚠️ **Note:** Use a **Bash** or **Command Prompt** terminal to install packages and run the script. (If you encounter issues on PowerShell, try running the same commands in Bash or Command Prompt.)

---

## 💻 Usage

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/simple-port-scanner.git
cd simple-port-scanner
```

### 2. Run the script

```bash
python port_scanner.py
```

By default, it scans:

```python
ip = "45.33.32.156"  # Nmap test server
```

---

## 🧩 Example Output

```
Host: 45.33.32.156 (scanme.nmap.org)
State: up

Protocol: tcp
  Port: 22
    State:   open
    Service: ssh
    Product: OpenSSH
    Version: 6.6.1p1 Ubuntu

  Port: 80
    State:   open
    Service: http
    Product: Apache httpd
    Version: 2.4.7
```

After the scan finishes, results are saved to:

```
scan_results.txt
```

---

## 📄 Code Overview

```python
import nmap

nm = nmap.PortScanner()
ip = "45.33.32.156"

nm.scan(ip, arguments="-sC -sV")

for host in nm.all_hosts():
    print(f"\nHost: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")
    for proto in nm[host].all_protocols():
        print(f"\nProtocol: {proto}")
        ports = nm[host][proto]
        for port, info in ports.items():
            print(f"  Port: {port}")
            print(f"    State:   {info['state']}")
            print(f"    Service: {info.get('name', 'N/A')}")
            print(f"    Product: {info.get('product', 'N/A')}")
            print(f"    Version: {info.get('version', 'N/A')}")
```

---

## 🛡️ Safety & Legal Notice

This script is **for educational and authorized use only**.
Always ensure you have explicit permission before scanning any external network or host.

Scanning systems without consent can be illegal in many regions.

---

## 🧠 Future Improvements

* Add multiple IP / subnet scanning
* Include `rich` for colorized terminal output
* Add concurrent scanning for faster results
* Save outputs in JSON or CSV format

---

## 🏷️ License

This project is open-source under the **MIT License** — feel free to use and modify it.
