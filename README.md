# Traffic Sniffer and Decoder

This Python-based project contains a script crafted to analyze and decode network traffic coming from a cellphone connected via a serial connection (USB). It employs Pyshark, a Python interface for network packet analyzers such as Wireshark, to decode captured network traffic and return valuable information. 

Besides, the `TrafficSniffer` class is used to capture network traffic through the subprocess module and stop the capture when a keyboard interrupt signal is detected. 

## Prerequisites

The project relies on the following Python libraries:

* Pyshark
* subprocess
* serial

You can install these libraries using pip:
```
pip install pyshark pyserial subprocess
```

Also, please install Tshark (Wireshark's network protocol analyzer) on your machine.

## Usage

The main script requires no command-line arguments to run. You may need to modify some variables in the script based on your requirements.

1. Modify `channels` based on the GSM networks you wish to capture.
2. Feel free to change the serial connection parameters in the `SerialConnection` instance according to your device.
3. Set your specific sniffing parameters in the `TrafficSniffer` instance.

You can then execute the script using the following command:

```
python main.py
```

During execution, the script will output IMSI (International Mobile Subscriber Identity) numbers it captures from the defined channels.

Finally, the script prints packets related to DTAP (Direct Transfer Application Part) provided any user data is available, after decoding.

## Result Interpretation

The result you are receiving is the decoded traffic from the connected device. It represents the list of all the user data related to 'gsm_a.dtap' present in the captured network traffic.

These packets contain signaling (non-user) data, which are used to set up and tear down calls, and for other explicit signaling purposes like maintaining communication between the mobile station and the base station subsystem.

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Support

If you have any issues or enhancement proposals, feel free to open a new issue. Your feedback is always welcome!
