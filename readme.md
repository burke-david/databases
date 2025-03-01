# Database stuff

Create python venv
```
python -m venv .venv
```

Activate
```
source .venv/vin/activate
```

Install cantools
```
pip install cantools
```

Convert database (`.dbc`) to human-readable format
```
python decode_dbc.py result.dbc
```

Example result
```
Message: AuxControls, ID: 0x18ff35e4, DLC: 8
  Signal: btn_LHJoystick_LH, Start Bit: 20, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: -
  Signal: btn_LHJoystick_RH, Start Bit: 22, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: -
  Signal: btn_LHJoystick_Dw, Start Bit: 24, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: -
  Signal: btn_LHJoystick_Up, Start Bit: 25, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: -
  Signal: btn_RHJoystick_Up, Start Bit: 26, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: -
  Signal: btn_RHJoystick_Dw, Start Bit: 27, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: -
  Signal: btn_RHJoystick_Trigger, Start Bit: 28, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: -
  Signal: sld01, Start Bit: 32, Length: 8, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: btn_RHJoystick_Speed, Start Bit: 59, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: -
Message: LegacyMessaggesPrior6, ID: 0x18ffffe4, DLC: 8
  Signal: CANLegacyFunctionsSelector, Start Bit: 0, Length: 16, Endianess: Little Endian, Factor: 1, Offset: 0, Min: 0, Max: 65535, Unit: None
  Signal: btn_07, Start Bit: 16, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: btn_05, Start Bit: 16, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: btn_03, Start Bit: 16, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: btn_01, Start Bit: 16, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: btn_08, Start Bit: 17, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: btn_06, Start Bit: 17, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: btn_04, Start Bit: 17, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: btn_02, Start Bit: 17, Length: 1, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
Message: AuxControlsTX, ID: 0x18ff53e4, DLC: 8
Message: TestMsg_0000, ID: 0x14ffffb0, DLC: 8
  Signal: DWORD, Start Bit: 0, Length: 32, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
  Signal: DWORD1, Start Bit: 32, Length: 32, Endianess: Little Endian, Factor: 1, Offset: 0, Min: None, Max: None, Unit: None
```