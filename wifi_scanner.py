import subprocess

# scan all wifi signals
def scan_wifi(interface="wlp8s0"):
    result = subprocess.check_output(["sudo", "iw", "dev", interface, "scan"]).decode()
    signals = {}
    for line in result.split("\n"):
        if "signal:" in line:
            rssi = float(line.strip().split(":")[1].split()[0])
        if "SSID" in line:
            ssid = line.strip().split(":")[1][1:]
            signals[ssid] = rssi
    return signals
