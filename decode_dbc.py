import cantools
import sys

def decode_dbc(dbc_file_path):
    try:
        # Load the DBC file
        db = cantools.database.load_file(dbc_file_path)

        # Print CAN messages and signals
        for message in db.messages:
            print(f"Message: {message.name}, ID: {hex(message.frame_id)}, DLC: {message.length}")
            for signal in message.signals:
                print(f"  Signal: {signal.name}, Start Bit: {signal.start}, Length: {signal.length}, "
                      f"Endianess: {'Big Endian' if signal.byte_order == 'big_endian' else 'Little Endian'}, "
                      f"Factor: {signal.scale}, Offset: {signal.offset}, Min: {signal.minimum}, Max: {signal.maximum}, "
                      f"Unit: {signal.unit}")

    except Exception as e:
        print(f"Error decoding DBC file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python decode_dbc.py <dbc_file>")
    else:
        dbc_file = sys.argv[1]
        decode_dbc(dbc_file)
