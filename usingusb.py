import pyvisa

def connect_rigol():
    rm = pyvisa.ResourceManager('@py')
    resources = rm.list_resources()
    usb_resources = [resource for resource in resources if 'USB' in resource]
    
    if not usb_resources:
        print("No USB-connected instruments found.")
        return None
    
    print("USB-connected instruments:")
    for index, resource in enumerate(usb_resources, start=1):
        print(f"{index}. {resource}")
    
    selection = int(input("Enter the index of the instrument you want to connect to: "))
    selected_resource = usb_resources[selection - 1]
    instrument = rm.open_resource(selected_resource)
    
    return instrument

# Connect to the instrument
rigol_instrument = connect_rigol()

if rigol_instrument:
    # Now you can communicate with the instrument using rigol_instrument
    # For example, to query the identification string of the instrument:
    identification = rigol_instrument.query('*IDN?')
    print("Instrument Identification:", identification)
    
    # Remember to close the connection when done
    rigol_instrument.close()