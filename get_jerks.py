#!/bin/python

import os
import re
# for csv writing
import csv

ips = []
auditdir = '/var/log/audit'
for log in os.listdir(auditdir):
  file = open(os.path.join(auditdir, log), 'r')
  for line in file:
    if re.search("terminal=ssh res=failed", line):
      addr = re.search("addr=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group(0)
      ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", addr).group(0)
      ips.append(ip)
  file.close()

print "making IP dictionary"

ipdict = {x:ips.count(x) for x in ips}
print "Done!"
jerkdict = {}
print "Making jerk dictionary."
print "Getting countries."
for ip in ipdict:
  jerkcountry = os.popen("geoiplookup {0}".format(ip)).read()
  jerkcountry = jerkcountry.split(':')[1].strip()
  if "," in jerkcountry:
    jerkcountry = jerkcountry.split(',')[1].strip()
  jerktries = ipdict[ip]
  if jerkcountry in jerkdict:
    jerkdict[jerkcountry] += jerktries
  else:
    jerkdict[jerkcountry] = jerktries

#print stuff
for jerk in jerkdict:
  print "{0}\t\t\t\t{1}".format(jerk, jerkdict[jerk])
# write to csv
with open('jerks.csv', 'wb') as file:
  writer = csv.writer(file, delimiter=',')
  for jerk in jerkdict:
    writer.writerow([jerk, str(jerkdict[jerk])])
