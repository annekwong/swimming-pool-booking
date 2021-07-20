
from datetime import datetime
from datetime import timedelta


def SuffixedDate(s):
    if(s[-1] == '1'):
        return 'st'
    elif(s[-1] == '2'):
        return 'nd'
    elif(s[-1] == '3'):
        return 'rd'
    else:
        return 'th'

def NextMonday(d):
    offset = 0
    for i in range(1,8):
        if((d+timedelta(i)).strftime("%a") == 'Mon'):
            offset = i
    
    # day = (d+timedelta(offset)).strftime("%a %b %d")
    day = (d+timedelta(offset))
    # print(day.strftime("%a %b %d"))
    
    return day

# let's find the offset by formatting next Monday's date, then getting index of that in the list of dates

def FormatDate(d):
    s = d.strftime("%a %b %d")
    
    _, m, n = s.split(' ')
    n = str(int(n))
    num = SuffixedDate(n)
    return "{:s} {:s}{:s}".format(m, n, num)

# FormatDate(MondayNextWeek())

# ! had a variable named 'd', made a list 'days' from it, by adding timedelta; printing `for d in days` changed d. Spooky.


# dates  = [x['date'] for x in slot_nodes]
# nextm  = FormatDate(NextMonday(today))
# offset = daystamps.index(nextm)
# daystamps[off:off+7]

# - later down the line:
# days = [x['link'] for x in slot_nodes[off:off+7]]

