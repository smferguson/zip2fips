import datetime
import json
import re

from os import listdir


today = datetime.datetime.now().strftime('%Y%m%d')
statecodes = json.load(open('state_fips.json'))
zipmap = {}

for f in listdir('zipctys'):
    print(f'processing file {f}')
    with open(f'zipctys/{f}', 'r') as zfile:
      zfile.readline() # skip first line
      for l in zfile:
          m = re.match(r"(?P<zip>.{5}).{18}(?P<state>..)(?P<fips>...)", l)
          if m:
              r = m.groupdict()
              zipmap[r['zip']] = statecodes[r['state']] + r['fips']

with open(f'zip_to_fips_{today}.json', 'w') as ztf:
    ztf.write(json.dumps(zipmap))

