#pre install pyvisa and pyvisa-pi
#for ethernet based connectivity

import pyvisa

def connect_rigol(ip_address):
    rm = pyvisa.ResourceManager('@py')
    instrument = rm.open_resource(f'TCPIP::{ip_address}::INSTR')
    return instrument

# Replace '192.168.0.102' with the IP address of your Rigol instrument
ip_address = '192.168.0.106'
rigol_instrument = connect_rigol(ip_address)

# Now you can communicate with the instrument using rigol_instrument
# For example, to query the identification string of the instrument:
identification = rigol_instrument.query('*IDN?')
print("Instrument Identification:", identification)

# Remember to close the connection when done
rigol_instrument.close()