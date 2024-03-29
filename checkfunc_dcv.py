import pyvisa

# Function to connect to the Rigol instrument
def connect_rigol(ip_address):
    try:
        rm = pyvisa.ResourceManager('@py')
        instrument = rm.open_resource(f'TCPIP::{ip_address}::INSTR')
        return instrument
    except pyvisa.VisaIOError as e:
        print("An error occurred while connecting to the instrument:", e)
        return None

# Function to send commands to the instrument
def send_command(instrument, command):
    try:
        instrument.write(command)
        print(f"Command sent: {command}")
    except pyvisa.VisaIOError as e:
        print("An error occurred while sending command:", e)

# Function to measure DC voltage on a specific channel
def measure_dc_voltage(instrument, channel):
    try:
        command = f":MEASure:VOLTage:DC? (@{channel})"
        instrument.write(command)
        measured_voltage = instrument.read()
        print(f"Voltage on channel {channel}: {measured_voltage} V")
    except pyvisa.VisaIOError as e:
        print("An error occurred while measuring voltage:", e)

# Replace '192.168.0.106' with the IP address of your Rigol instrument
ip_address = '192.168.0.106'

# Connect to the instrument
rigol_instrument = connect_rigol(ip_address)

if rigol_instrument:
    try:
        # Query the identification string of the instrument
        identification = rigol_instrument.query('*IDN?')
        print("Instrument Identification:", identification)
        
        # Measure DC voltage on channel 201
        measure_dc_voltage(rigol_instrument, 201)
    finally:
        # Remember to close the connection when done
        rigol_instrument.close()