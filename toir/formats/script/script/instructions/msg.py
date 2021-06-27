from . import ScriptInstruction, ScriptInstructionWithArgs
from .....text import decode_text_fixed, remove_redundant_cc
import struct

def _transform_codes(text):
    i = 0
    occurences = []
    while i != -1:
        i = text.find('@', i)
        if i != -1:
            i += 1
            occurences.append(i)
    for i in reversed(occurences):
        text = text[:i] + f'{{{ord(text[i]):02X}}}' + text[i+1:]
    return text    

class ScriptMsg(ScriptInstruction):
    def decode(self, buffer, offset):
        self.arg1, length = struct.unpack_from('<BH', buffer, offset)
        #self.text = decode_text(buffer[offset+3:offset+length+3], 0)
        self.text = decode_text_fixed(buffer, offset+3, length)
        self.text = remove_redundant_cc(self.text)
        return offset + length + 3
 
    def pretty_print(self):
        return f'ScriptMsg({self.arg1}, "{self.text}")'

class ScriptSelectCommand(ScriptInstruction):
    def decode(self, buffer, offset):
        count = buffer[offset]
        self.commands_arg = buffer[offset+1:offset+count+1]
        offset += count + 1
        self.commands = []
        for _ in range(count):
            length = buffer[offset]
            offset += 1
            text = buffer[offset:offset+length].decode('utf-8')
            offset += length
            text = _transform_codes(text)
            self.commands.append(text)
        return offset

class ScriptSelectCancel(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<B', opcode)

class ScriptMsgWait(ScriptInstruction):
    def decode(self, buffer, offset):
        return offset

class ScriptMsgWindowSet(ScriptInstruction):
    def decode(self, buffer, offset):
        self.arg = buffer[offset]
        return offset + 1

    def pretty_print(self):
        return f'ScriptMsgWindowSet({self.arg})'

class ScriptChoice(ScriptSelectCommand):
    pass
