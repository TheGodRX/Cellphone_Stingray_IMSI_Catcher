# Cellphone_Stingray_IMSI_Catcher

# GSM Network Capture

This is a Python script that captures IMSI numbers and decodes calls and messages transmitted over GSM networks using a cellphone connected by USB. 

## Requirements

To use this script, you will need:

- A cellphone that supports a serial connection, such as an Android phone.
- A computer with Python installed.
- A USB cable to connect the cellphone to the computer.

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/codercoins/Cellphone_Stringray_Catcher.git
   ```

2. Open `gsm-network-capture.py` in a Python editor.

3. Connect the cellphone to the computer via USB.

4. Modify the necessary variables:
   
   - `channels`: update to include the channels used in your local GSM network.
   - `port`: update with the correct port for your device.

5. Run the script in the terminal:

   ```
   $ python3 IMSICATCHER.py
   ```

   The script will capture IMSI numbers and network traffic, including calls and messages transmitted over GSM networks. Those data will output to your console.

6. Stop capturing by pressing `CTRL + C`.

Please note that unauthorized interception and recording of telephone conversations and text messages is illegal and violates personal privacy. Use this code only for authorized and legal purposes. 
