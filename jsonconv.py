import json

class MemType:
    type_byte = 0
    type_halfword = 1
    type_word = 2
    type_float = 3
    type_double = 4
    type_string = 5
    type_byteArray = 6
    type_num = 7

datatypes = ['DolphinByte', 'DolphinHalfword', 'DolphinWord', 'DolphinFloat']

# Read JSON data from a file
with open('MGTT_Addresses_latest.dmw', 'r') as file:
    json_data = file.read()

# Parse JSON data
data = json.loads(json_data)['watchList']

for i in data:
    for v in i.values():
        for dat in v:
            if type(dat) == dict:
                if dat.get('groupEntries'):
                    for ls in dat.values():
                        for ls_items in ls:
                            if type(ls_items) == dict:
                                if ls_items.get('groupEntries'):
                                    for listdat in ls_items.values():
                                        if type(listdat[0]) == dict:
                                            if listdat[0]['typeIndex'] in range(0, 4):
                                                # print(datatypes[listdat[0]['typeIndex']])
                                                print(listdat[0]['label'].strip().replace(' ', '_').replace('#',
                                                                                                            '').replace(
                                                    '(', '').replace(')', '').replace('/', 'or').lower() + ' = ' + datatypes[listdat[0]['typeIndex']] + '(' +
                                                      '0x' + str(listdat[0]['address']) + ')')

                                            # print(listdat[0]['label'].strip().replace(' ', '_').replace('#', '').replace('(', '').replace(')', '').replace('/', '').lower(), '0x' + str(listdat[0]['address']))
                else:
                    # print(dat['label'].strip().replace(' ', '_').replace('#', '').replace('(', '').replace(')', '').replace('/', '').lower(), '0x' + str(dat['address']))
                    print(dat['label'].strip().replace(' ', '_').replace('#',
                                                                                '').replace(
                        '(', '').replace(')', '').replace('/', 'or').lower() + ' = ' + datatypes[
                              dat['typeIndex']] + '(' +
                          '0x' + str(dat['address']) + ')')