from . import ScriptInstruction, ScriptInstructionWithArgs
import struct

class ScriptObjectDirPlayer(ScriptInstruction):
    def __init__(self, opcode):
        self.opcode = opcode

    def decode(self, buffer, offset):
        self.arg1, self.arg2, self.arg3 = struct.unpack_from('<BBH', buffer, offset)
        return offset + 4

    def pretty_print(self):
        return f'ScriptObjectDirPlayer({self.arg1}, {self.arg2}, {self.arg3})'

class ScriptObjectDirDefault(ScriptInstruction):
    def __init__(self, opcode):
        self.opcode = opcode

    def decode(self, buffer, offset):
        self.arg1, self.arg2, self.arg3 = struct.unpack_from('<BBH', buffer, offset)
        return offset + 4

    def pretty_print(self):
        return f'ScriptObjectDirDefault({self.arg1}, {self.arg2}, {self.arg3})'

class ScriptObjectVisible(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BB', opcode)

class ScriptObjectMotionChange(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BHBL', opcode)
class ScriptObjectMovePointFrame(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBHHB', opcode)

class ScriptObjectMovePointSpeed(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBHBfB', opcode)

class ScriptObjectMoveWait(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<B', opcode)

class ScriptObjectMouseAction(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<B', opcode)

class ScriptObjectModelLoad(ScriptInstruction):
    pass

class ScriptObjectDirPoint(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBBH', opcode)

class ScriptObjectDirWait(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<B', opcode)

class ScriptObjectDirObject(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBBH', opcode)

class ScriptObjectDirMoveAbs(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BHBH', opcode)

class ScriptObjectCostumeSet(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BH', opcode)

class ScriptObjectEyeAnime(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BB', opcode)

class ScriptObjectMotionWait(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<B', opcode)

class ScriptObjectMotionFrameSet(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BL', opcode)

class ScriptObjectNeckRel(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BHHBH', opcode)

class ScriptObjectNeckDefault(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBH', opcode)

class ScriptObjectDirMoveRel(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BHBH', opcode)

class ScriptObjectNeckWait(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<B', opcode)

class ScriptObjectWeaponVisible(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BB', opcode)

class ScriptObjectEyeChange(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BB', opcode)

class ScriptObjectShadowDisp(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBH', opcode)

class ScriptObjectNeckPlayer(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBH', opcode)

class ScriptObjectNeckObject(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBBH', opcode)

class ScriptObjectMotionLoop(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBLL', opcode)

class ScriptObjectCollisionSet(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BB', opcode)

class ScriptObjectAlphaMove(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBH', opcode)

class ScriptObjectMoveDirAbs(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BHHHBLB', opcode)

class ScriptObjectAlphaWait(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<B', opcode)

class ScriptObjectMotionSpeedSet(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BL', opcode)

class ScriptObjectNeckPoint(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BBBH', opcode)

class ScriptObjectMoveDirRel(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BHHHBLB', opcode)

class ScriptObjectActive(ScriptInstructionWithArgs):
    def __init__(self, opcode):
        super().__init__('<BB', opcode)
        