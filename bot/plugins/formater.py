
# GOAL:
# Convert to human readable information

def format_bytes(bytes):
    units = ['B', 'KB','MB','GB']
    for unit in units:
        out = f'{int(bytes)} {unit}'
        bytes = bytes / 1024
        if bytes < 1:
            break
    return out

def format_time(sec):
    units = [
        ['ms', 1000],
        ['s', 60],
        ['m', 60],
        ['h', 24],
        ['d', 0]
    ]
    out = ''
    qtime = int(sec * 1000)
    for unit in units:
        if unit[1] != 0:
            qtime, time = divmod(qtime, unit[1])
        else:
            time = qtime
        if time != 0:
            out = f"{time}{unit[0]} {out}"
        if qtime == 0:
            break
    return out