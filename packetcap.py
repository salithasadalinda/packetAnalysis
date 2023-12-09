import pyshark
import matplotlib

def packet_capturing(interface, file_name):
    capture = pyshark.LiveCapture(interface=interface, output_file=file_name)
    capture.sniff(packet_count=10)
    capture.close()

if __name__ == "__main__":
    packet_capturing('eth0', 'output.pcap')  # replace 'eth0' with your network interface



