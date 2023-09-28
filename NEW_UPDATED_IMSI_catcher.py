import serial
import subprocess
import pyshark

class SerialConnection:
    def __init__(self,path,baud_rate,timeout):
        self.conn = serial.Serial(path, baud_rate, timeout=timeout)

    def write(self,channel):
        self.conn.write(bytes('AT+SQNSCFG= "BandMasks","' + channel + '",3,8000000,0,1,0\r\n', 'utf-8'))
        self.conn.write(b'AT+CGSN\r\n')

    def get_response(self):
        response = self.conn.readline()
        return response.strip() if response else "unknown"


class TrafficSniffer:
    def __init__(self,interface,output,filter):
        self.command = ["tshark", "-i", interface, "-w", output, "-f", filter]
    
    def start_sniffing(self):
        self.process = subprocess.Popen(self.command)
        
    def stop_sniffing(self):
        self.process.terminate()


class DecodeTraffic:
    def __init__(self,file):
        self.capture = pyshark.FileCapture(file)
        
    def decode_traffic(self):
        decoded_result = []
        for packet in self.capture:
            if packet.highest_layer == 'gsm_a.dtap':
                if packet.user_data:
                    decoded_data = packet.user_data.getvalue().decode('utf-8')
                    decoded_result.append(decoded_data)
        return decoded_result


if __name__ == "__main__":
    channels = ['890', '891', '892'] 
    conn = SerialConnection(path='/dev/ttyACM0',baud_rate=115200,timeout=1)
    for channel in channels:
        conn.write(channel)
        print("IMSI:",conn.get_response())
    
    sniffer = TrafficSniffer(interface="usb0",output="capture.pcap",filter="port 80")
    sniffer.start_sniffing()
    
    decoder = DecodeTraffic('capture.pcap')
    print(decoder.decode_traffic())
    
    try:
        while True:
            continue
    except KeyboardInterrupt:
        sniffer.stop_sniffing()
