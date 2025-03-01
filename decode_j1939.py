import sys

def decode_j1939_id(arb_id):
    # Ensure it's a valid 29-bit ID
    if arb_id > 0x1FFFFFFF:
        print("Error: Invalid J1939 Arbitration ID (must be 29-bit).")
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

def main():
    if len(sys.argv) != 2:
        print("Usage: python decode_j1939.py <Arbitration ID in hex>")
        print("Example: python decode_j1939.py 0x18FEE400")
        return
    
    try:
        # Parse input (strip '0x' if present and convert from hex)
        arb_id = int(sys.argv[1], 16)
        decode_j1939_id(arb_id)
    except ValueError:
        print("Error: Invalid input. Provide a valid hex arbitration ID.")
        return

if __name__ == "__main__":
    main()
