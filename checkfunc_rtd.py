import pyvisa

# Function to connect to the Rigol instrument
def connect_rigol(ip_address):
    rm = pyvisa.ResourceManager('@py')
    instrument = rm.open_resource(f'TCPIP::{ip_address}::INSTR')
    return instrument

# Function to configure channels for temperature measurement
def configure_temperature_measurement(instrument, probe_type, type_, scan_list):
    command = f"CONFigure:TEMPerature {probe_type},{type_},1,DEF,({scan_list})"
    send_command(instrument, command)

# Function to send commands to the instrument
def send_command(instrument, command):
    try:
        instrument.write(command)
        print(f"Command sent: {command}")
    except pyvisa.VisaIOError as e:
        print("An error occurred while sending command:", e)

# Function to read temperature from a specific channel
def read_temperature(instrument, channel):
    try:
        command = f"MEASure:TEMPerature? (@{channel})"
        temperature = instrument.query(command)
        print(f"Temperature on channel {channel}: {temperature} °C")
    except pyvisa.VisaIOError as e:
        print("An error occurred while reading temperature:", e)

# Replace '192.168.0.106' with the IP address of your Rigol instrument
ip_address = '192.168.0.106'

# Connect to the instrument
rigol_instrument = connect_rigol(ip_address)

if rigol_instrument:
    # Configure channels for RTD temperature measurement
    probe_type = 'RTD'  # Set probe type to RTD
    type_ = '85'  # Example type for RTD (adjust as needed)
    scan_list = '201'  # Channel to read temperature from
    configure_temperature_measurement(rigol_instrument, probe_type, type_, scan_list)
    
    # Read temperature from channel 201
    read_temperature(rigol_instrument, '201')

    # Remember to close the connection when done
    rigol_instrument.close()