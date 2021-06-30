import re

def decode_control_code(text, i):
    try:
        code = text[i + 1]
        if code == 0x01:
            arg = text[i + 3]
            if arg == 0x03:
                return '{emph}', i + 4
            elif arg == 0x04:
                return '{regular}', i + 4
            else:
                return '{01}', i + 2        
        elif code == 0x02:
            index = text[i + 3] + (text[i + 4] << 8)
            return f'{{item:{index:04X}}}', i + 5
        elif code == 0x03:
            index = text[i + 3] + (text[i + 4] << 8)
            return f'{{unknown03:{index:04X}}}', i + 5
        elif code == 0x04:
            index = text[i + 3] + (text[i + 4] << 8)
            return f'{{number:{index:04X}}}', i + 5
        elif code == 0x05:
            arg = text[i + 3]
            if arg == 0x01:
                return '{variable}', i + 4
            elif arg == 0x02:
                return '{fixed}', i + 4
            else:
                return '{05}', i + 2
        elif code == 0x40:
            index = text[i + 3] + ((text[i + 4]) << 8)
            return f'{{button:{index:04X}}}', i + 5
        elif code == 0x41:
            index = text[i + 3]
            return f'{{unknown41:{index:02X}}}', i + 4
        elif code == 0x42:
            return '{triverse}', i + 2
        else:
            return f'{{{code:02X}}}', i + 2
    except Exception as e:
        raise ValueError(str(e) + f' ("{text}")')

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

def get_next_end(buffer, offset, end):
    i = buffer.find(b'\x00', offset)
    if i == -1:
        return end
    else:
        return min(i, end)

def decode_text(buffer, offset, max_len=0):
    if not max_len:
        end = len(buffer)
    else:
        end = offset + max_len

    next_at = buffer.find(b'@', offset)
    next_end = get_next_end(buffer, offset, end)
    last = offset
    text = ''
    while next_at != -1 and next_at < next_end:
        text += buffer[last:next_at].decode('utf-8')
        cc, last = decode_control_code(buffer, next_at)
        text += cc
        next_at = buffer.find(b'@', last)
        next_end = get_next_end(buffer, last, end)
    text += buffer[last:next_end].decode('utf-8')
    return text.replace('\r', '')

def decode_text_fixed(buffer, offset, length):
    return decode_text(buffer, offset, length)

def encode_text(string):
    return string.encode('utf-8') + b'\0'