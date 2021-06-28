import json
from time import sleep

def ParseConfig_v0(filename):
    j = json.load(open(filename, "r"))
    
    c_type  = j['type']
    c_time  = j['time']
    
    try:
        c_first = int(j['first'])
    except ValueError:
        c_first = None
    
    try:
        c_last = int(j['last'])
    except ValueError:
        c_last = None
    
    return (c_type, c_time, c_first, c_last);
def ParseConfig(filename):
    j = json.load(open(filename, "r"))
    
    d = {}
    
    d['type'] = j['type']
    d['time'] = j['time']
    
    try:
        d['start'] = int(j['start'])
    except ValueError:
        d['start'] = None
    
    try:
        d['stop'] = int(j['stop'])
    except ValueError:
        d['stop'] = None
    
    try:
        d['step'] = int(j['step'])
    except ValueError:
        d['step'] = None
    
    return d

if __name__ == "__main__":
    d = ParseConfig("test.json")
    
    l = list(range(10))
    # print("{:s}, {:s}".format(control_type, control_time))
    # print(l[control_first:control_last])
    print("{:s}, {:s}".format(d['type'], d['time']))
    print(l[d['start']:d['stop']])
    
    sleep(10)