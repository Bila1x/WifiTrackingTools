import csv
import time


def rows(input, minLength):
    lines = [x.strip() for x in input if x != '\n' and len(x) >= minLength]

    lastline = lines[0]
    c = 0
    result = []
    before = time.time()
    for line in sorted(lines):
        if not line or line == 'bil': c = 0; continue
        c += 1
        # print(line)
        if lastline != line:
            result.append([c, lastline, '%{}'.format(round(c / len(lines) * 100, 1))])
            lastline = line
            c = 0
            continue
    return result

def cells():
    print('By cell:')
    with open(r'C:\Users\Bilal\Desktop\whereabouts\\%s' %filename, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        dd = list(reader)
        s = []
        for row in dd:
            for cell in row:
                if cell and len(cell) >= minLength: s.append(cell.strip())
        return s

def mentions():
    print('mentions:')
    with open(r'C:\Users\Bilal\Desktop\whereabouts\\%s' % filename, 'r') as f:
        whole = f.read()
        diccount = 0
        for item in keys:
            ccount = whole.count(item)
            keys[item] = ccount
            diccount += ccount
        if not diccount:
            print('Nothing found!'); quit()
        for item in reversed(sorted(keys.items(), key= lambda x: x[1])):
            print([item[1], item[0], '{}%'.format(int(item[1]/diccount*100))])
        print(diccount)


if __name__ == '__main__':

    filename = 'scripts\\allprobed.csv'
    bycell = 1
    resultcount = 20 # specify result count (0 for all)

    keys = {'Freewave': 0,'AndroidAP': 0,'eduroam': 0, 'OEBB': 0, 'OEBB-station': 0, '.wienatPublicWLAN': 0, 'Wiener Linien Free WiFi': 0, 'Austrian Free Wifi': 0, 'UPC Wi-Free': 0}


    f = open(r'C:\Users\Bilal\Desktop\whereabouts\\%s' %filename, 'r')

    if bycell == 2:
        lines = cells()
    elif bycell == 1:
        print('By row:')
        lines = rows(f.readlines(), 1)
    else:
        mentions()
    f.close()

def rest():
    if bycell == 1 or bycell == 2:
        lastline = lines[0]
        c = 0
        result = []
        before = time.time()
        for line in sorted(lines):
            if not line or line == 'bil': c=0; continue
            c += 1
            #print(line)
            if lastline != line:
                result.append([c, lastline, '%{}'.format(round(c/len(lines)*100, 1))])
                lastline = line
                c = 0
                continue

        result.append([c, lastline, '%{}'.format(round(c/len(lines)*100, 1))])
        for line in reversed(sorted(result)[-resultcount:]):
            print(line)
        print('runtime: {}'.format(time.time() - before))
        print(len(lines))
    # for key in sorted(keys):
    #     print(keys[key])
