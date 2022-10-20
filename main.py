import mido, keyboard
notes = {
        20: "ctrl + 0",
        21: "ctrl + 1",
        22: "ctrl + 2",
        23: "ctrl + 3",
        24: "ctrl + 4",
        25: "ctrl + 5",
        26: "ctrl + 6",
        27: "ctrl + 7",
        28: "ctrl + 8",
        29: "ctrl + 9",
        30: "ctrl + 0",
        31: "ctrl + q",
        32: "ctrl + w",
        33: "ctrl + e",
        34: "ctrl + r",
        35: "ctrl + t",
        36: "1",
        37: "shift + 1",
        38: "2",
        39: "shift + 2",
        40: "3",
        41: "4",
        42: "shift + 4",
        43: "5",
        44: "shift + 5",
        45: "6",
        46: "shift + 6",
        47: "7",
        48: "8",
        49: "shift + 8",
        50: "9",
        51: "shift + 9",
        52: "0",
        53: "q",
        54: "shift + q",
        55: "w",
        56: "shift + w",
        57: "e",
        58: "shift + e",
        59: "r",
        60: "t",
        61: "shift + t",
        62: "y",
        63: "shift + y",
        64: "u",
        65: "i",
        66: "shift + i",
        67: "o",
        68: "shift + o",
        69: "p",# nice
        70: "shift + P",
        71: "a",
        72: "s", 
        73: "shift + s",
        74: "d",
        75: "shift + d",
        76: "f",
        77: "g",
        78: "shift + g",
        79: "h",
        80: "shift + h",
        81: "j",
        82: "shift + j",
        83: "k",
        84: "l",
        85: "shift + l",
        86: "z",
        87: "shift + z",
        88: "x",
        89: "c",
        90: "shift + c",
        91: "v",
        92: "shift + v",
        93: "b",
        94: "shift + b",
        95: "n",
        96: "m",
        97: "ctrl + y",   
        98: "ctrl + u",        
        99: "ctrl + i",
        100: "ctrl + o",
        101: "ctrl + p",
        102: "ctrl + a",
        103: "ctrl + s",
        104: "ctrl + d",
        105: "ctrl + f",
        106: "ctrl + g",
        107: "ctrl + h",
        108: "ctrl + j"
}

        
        
def midiToQwerty():

    with mido.open_input() as port:            
        for m in port:                           
            if m.type == 'note_on':               
                try:
                    keyboard.press(notes[m.note + 12])
                    keyboard.release('shift')
                except: 
                    pass
            elif m.type == 'note_off':               
                try:
                    keyboard.release(notes[m.note + 12])
                except: 
                    pass
        
if __name__ == '__main__':
    midiToQwerty()
    
