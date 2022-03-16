
one_dict = {}
two_dict = {}
macs = set()
result = []

with open('standards-oui.ieee.org.txt', 'r') as f:
    one = f.read().splitlines()
    for line in one:
        l = line.split('\t')
        one_dict[l[0]] = l[1]
        macs.add(l[0])

with open('macaddress.io-db.csv', 'r') as f:
    two = f.read().splitlines()
    for line in two:
        l = line.split('\t')
        two_dict[l[0]] = l[1] + '\t' + l[2]
        macs.add(l[0])


for mac in macs:
    result.append(['', '', ''])
    result[-1][0] = mac
    try:
        result[-1][1] = one_dict[mac]
    except KeyError:
        pass
    try:
        result[-1][2] = two_dict[mac]
    except KeyError:
        pass

with open('create_ouis.csv', 'w') as o:
    for line in result:
        o.write('\t'.join(line) + '\n')