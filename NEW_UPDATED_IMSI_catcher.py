import serial
import pyshark
import subprocess
import threading
from pydub import AudioSegment
from pydub.playback import play

class SerialConnection:

    def __init__(self, path, baud_rate, timeout):
        self.conn = serial.Serial(path, baud_rate, timeout=timeout)

    def write(self, channel):
        self.conn.write(bytes(f'AT+SQNSCFG= "BandMasks","{channel}",3,8000000,0,1,0\r\n', 'utf-8'))
        self.conn.write(b'AT+CGSN\r\n')

    def get_response(self):
        response = self.conn.readline()
        return response.strip() if response else "unknown"

class TrafficSniffer:
    def __init__(self, interface, output, filter_expression):
        self.command = ["tshark", "-i", interface, "-w", output, "-f", filter_expression]

    def start_sniffing(self):
        self.process = subprocess.Popen(self.command)

    def stop_sniffing(self):
        self.process.terminate()

class DecodeTraffic:
    def __init__(self, file):
        self.capture = pyshark.FileCapture(file)

    def decode_traffic_to_audio(self):
        decoded_result = []
        audio_format = 'gsm'
        for packet in self.capture:
            if packet.highest_layer == 'gsm_a.dtap':
                if packet.get_field('user_data'):
                    decoded_data = packet.user_data.getvalue().decode('utf-8')
                    audio_data = AudioSegment.from_file(decoded_data, format=audio_format)
                    decoded_result.append(audio_data)
        return decoded_result

def start_decoding():
    decoder = DecodeTraffic('capture.pcap')
    while True:
        audio_segments = decoder.decode_traffic_to_audio()
        for audio_segment in audio_segments:
            play(audio_segment)

def main():
    channels = ['890', '891', '892']
    conn = SerialConnection(path='/dev/ttyACM0', baud_rate=115200, timeout=1)

    for channel in channels:
        conn.write(channel)
        print("IMSI:", conn.get_response())

    sniffer = TrafficSniffer(interface="usb0", output="capture.pcap", filter_expression="tcp")
    sniffer.start_sniffing()

    decoding_thread = threading.Thread(target=start_decoding)
    decoding_thread.start()

    try:
        decoding_thread.join()
    except KeyboardInterrupt:
        sniffer.stop_sniffing()
        decoding_thread.join()

if __name__ == "__main__":
    main()
