import nmap

def scan_target(ip):
    nm = nmap.PortScanner()
    print(f"[+] Scanning target: {ip}")
    nm.scan(ip, arguments='-A -sV -p- --script vulners -T4')

    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                service = nm[host][proto][port]
                risk = "Low"
                if service.get('script', {}).get('vulners'):
                    risk = "High"
                elif service.get('version') or service.get('product'):
                    risk = "Medium"

                results.append({
                    'ip': ip,
                    'port': port,
                    'name': service.get('name'),
                    'version': service.get('version'),
                    'product': service.get('product'),
                    'cves': service.get('script', {}).get('vulners', ''),
                    'risk': risk
                })

    return results

if __name__ == '__main__':
    target_ip = input("Enter target IP: ")
    result = scan_target(target_ip)
    for r in result:
        print(r)
