import re

def decode_control_code(text, i):
    code = ord(text[i + 1])
    if code == 0x01:
        arg = ord(text[i + 3])
        if arg == 0x03:
            return '{emph}', i + 4
        elif arg == 0x04:
            return '{regular}', i + 4
        else:
            return '{01}', i + 2        
    elif code == 0x02:
        index = ord(text[i + 3]) + (ord(text[i + 4]) << 8)
        return f'{{item:{index:04X}}}', i + 5
    elif code == 0x03:
        index = ord(text[i + 3]) + (ord(text[i + 4]) << 8)
        return f'{{unknown03:{index:04X}}}', i + 5
    elif code == 0x04:
        index = ord(text[i + 3]) + (ord(text[i + 4]) << 8)
        return f'{{number:{index:04X}}}', i + 5
    elif code == 0x05:
        arg = ord(text[i + 3])
        if arg == 0x01:
            return '{variable}', i + 4
        elif arg == 0x02:
            return '{fixed}', i + 4
        else:
            return '{05}', i + 2
    elif code == 0x40:
        index = ord(text[i + 3]) + (ord(text[i + 4]) << 8)
        return f'{{button:{index:04X}}}', i + 5
    elif code == 0x42:
        return '{unknown42}', i + 2
    else:
        return f'{{{code:02X}}}', i + 2

_PUNCTUATION = r'…\u3000、？！!《》○―＝\n♪【】「｢｣」』）～〜・々)'
_REDUNDANT_FIXED = re.compile(f'{{fixed}}(?P<chars>[{_PUNCTUATION}]+)({{variable}}|$)')
_REDUNDANT_VARIABLE = re.compile(f'^{{variable}}[^{_PUNCTUATION}]')

def _remove_spacing_cc(match):
    return match.group('chars')

def _remove_variable_cc(match):
    return match.group(0).replace('{variable}', '')

def remove_redundant_cc(text):
    removed = re.sub(_REDUNDANT_FIXED, _remove_spacing_cc, text)
    return re.sub(_REDUNDANT_VARIABLE, _remove_variable_cc, removed)

def _decode_text(buffer):
    text = buffer.decode('utf-8')
    text_cc = ''
    last = 0
    i = text.find('@')
    while i != -1:
        text_cc += text[last:i]
        if i != -1:
            cc, i = decode_control_code(text, i)
            text_cc += cc
            last = i
        i = text.find('@', i)
    text_cc += text[last:]
    return text_cc.replace('\r', '')

def decode_text(buffer, offset):
    for i in range(offset, len(buffer)):
        if buffer[i] == 0:
            subbuffer = buffer[offset:i]
            return _decode_text(subbuffer)

def decode_text_fixed(buffer, offset, length):
    return _decode_text(buffer[offset:offset+length])

def encode_text(string):
    return string.encode('utf-8') + b'\0'