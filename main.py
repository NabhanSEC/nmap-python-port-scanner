import nmap
#to install nmap need to run -- pip install python-nmap
#run this in bash terminal and not powershell or python
nm = nmap.PortScanner()
ip = "45.33.32.156" #THE DEFAULT NMAP LOCAL HOSTED WEBSITE when you install nmap

nm.scan(ip, arguments="-sC -sV")
for host in nm.all_hosts():
    print(f"\nHost: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")

    for protocol in nm[host].all_protocols():
        print(f"\nProtocol: {protocol}")
        ports = nm[host][protocol]
        for port, info in ports.items():
            print(f"  Port: {port}")
            print(f"    State:   {info['state']}")
            print(f"    Service: {info.get('name', 'N/A')}")
            print(f"    Product: {info.get('product', 'N/A')}")
            print(f"    Version: {info.get('version', 'N/A')}")
with open("scan_results.txt", "w") as f:
    for host in nm.all_hosts():
        f.write(f"Host: {host} ({nm[host].hostname()})\n")
        f.write(f"State: {nm[host].state()}\n")
        for protocol in nm[host].all_protocols():
            f.write(f"Protocol: {protocol}\n")
            ports = nm[host][protocol]
            for port, info in ports.items():
                f.write(f"  Port {port} ({info['state']}) {info.get('name', '')}\n")
        f.write("\n")
print("Results saved to scan_results.txt ✅")
