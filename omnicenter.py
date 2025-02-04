import subprocess
import psutil
import socket
import os

class OmniCenter:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.local_ip = socket.gethostbyname(self.hostname)

    def display_network_info(self):
        print(f"Hostname: {self.hostname}")
        print(f"Local IP: {self.local_ip}")

    def list_network_adapters(self):
        adapters = psutil.net_if_addrs()
        print("Network Adapters and their IPs:")
        for adapter, addresses in adapters.items():
            for address in addresses:
                if address.family == socket.AF_INET:
                    print(f"{adapter}: {address.address}")

    def ping_test(self, host='8.8.8.8'):
        print(f"Pinging {host}...")
        response = os.system(f"ping -n 4 {host}")
        if response == 0:
            print(f"{host} is reachable")
        else:
            print(f"{host} is not reachable")

    def run_speed_test(self):
        try:
            import speedtest
        except ImportError:
            print("Speedtest module not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])
            import speedtest

        st = speedtest.Speedtest()
        print("Running speed test...")
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")

    def optimize_network(self):
        print("Optimizing network settings...")
        # Placeholder for network optimization logic

if __name__ == "__main__":
    omni = OmniCenter()
    omni.display_network_info()
    omni.list_network_adapters()
    omni.ping_test()
    omni.run_speed_test()
    omni.optimize_network()