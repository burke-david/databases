import sys

def decode_j1939_id(arb_id):
    """Decodes a J1939 arbitration ID and prints the details."""
    # Ensure it's a valid 29-bit ID
    if arb_id > 0x1FFFFFFF:
        print(f"Error: Invalid J1939 Arbitration ID {hex(arb_id)} (must be 29-bit).")
        return

    # Extract fields
    priority = (arb_id >> 26) & 0x07
    reserved = (arb_id >> 25) & 0x01
    data_page = (arb_id >> 24) & 0x01
    pdu_format = (arb_id >> 16) & 0xFF
    pdu_specific = (arb_id >> 8) & 0xFF
    source_address = arb_id & 0xFF

    # Determine PGN
    if pdu_format >= 240:  # Broadcast PGN
        pgn = (data_page << 16) | (pdu_format << 8) | pdu_specific
        destination = "Broadcast"
    else:  # Destination-specific PGN
        pgn = (data_page << 16) | (pdu_format << 8)
        destination = f"0x{pdu_specific:02X}"

    # Print results
    print(f"Decoded J1939 Arbitration ID: 0x{arb_id:08X}")
    print(f"  Priority:        {priority}")
    print(f"  Reserved Bit:    {reserved}")
    print(f"  Data Page:       {data_page}")
    print(f"  PDU Format:      0x{pdu_format:02X} ({pdu_format})")
    print(f"  PDU Specific:    0x{pdu_specific:02X} ({pdu_specific})")
    print(f"  PGN:             0x{pgn:04X} ({pgn})")
    print(f"  Destination:     {destination}")
    print(f"  Source Address:  0x{source_address:02X} ({source_address})")
    print("-" * 50)

def process_file(filename):
    """Reads arbitration IDs from a file and decodes each."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            try:
                # Convert to integer, stripping '0x' if present
                arb_id = int(line, 16)
                decode_j1939_id(arb_id)
            except ValueError:
                print(f"Skipping invalid hex ID: {line}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python batch_decode_j1939.py <file_with_arbitration_ids>")
        print("Example: python batch_decode_j1939.py arb_ids.txt")
        return

    filename = sys.argv[1]
    process_file(filename)

if __name__ == "__main__":
    main()
