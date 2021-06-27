from .instructions import ScriptInstruction, ScriptMsg, ScriptSelectCommand
import struct

class DecompilationException(Exception):
    pass

class OffsetSizeMismatchError(DecompilationException):
    def __init__(self, offset, size, script):
        self.offset = offset
        self.size = size
        self.script = script

    def __str__(self):
        return f'offset ({self.offset})/size ({self.size}) mismatch during decompilation'

class Script:
    @staticmethod
    def decompile(buffer):
        count, = struct.unpack_from('<H', buffer, 0)
        offset = 2
        script = Script()
        for _ in range(count):
            instruction = ScriptInstruction.from_opcode(buffer[offset])
            start_offset = offset
            offset += 1
            offset = instruction.decode(buffer, offset)
            instruction._offset = start_offset
            script.append(instruction)
        if offset != len(buffer):
            raise OffsetSizeMismatchError(offset, len(buffer), script)
        return script

    def __init__(self):
        self.instructions = []
    
    def append(self, instruction):
        self.instructions.append(instruction)

    def collect_texts(self):
        texts = {}
        for i, instruction in enumerate(self.instructions):
            if isinstance(instruction, ScriptMsg):
                texts[f'{i}'] = instruction.text
            elif isinstance(instruction, ScriptSelectCommand):
                for j, command in enumerate(instruction.commands):
                    texts[f'{i}/{j}'] = command

        return texts
    
    def dump(self, f):
        for i, instruction in enumerate(self.instructions):
            f.write(f'[{i:3}:{instruction._offset:04X}] 0x{instruction.opcode:02X} ')
            f.write(instruction.pretty_print())
            f.write('\n')
