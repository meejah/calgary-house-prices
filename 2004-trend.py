#!/usr/bin/env python

values = [198000,
          202500,
          202000,
          203000,
          203000,
          205500,
          200000,
          201000,
          202500,
          204000,
          205000,
          206000,
          
          215000,
          214900,
          220000,
          221500,
          222000,
          220000,
          221000,
          219303,
          223500,
          223000,
          230500,
          238000]

deltas = []
for i in range(1,len(values)):
    delta = values[i] - values[i-1]
    deltas.append(delta)
#print deltas

yearly_diff = []
for i in range(12):
    yearly_diff.append(values[i+12] - values[i])
##print yearly_diff

avg = reduce(lambda x,y: x+y, values) / float(len(values))
##print "average:",avg

avgdelta = reduce(lambda x,y: x+y, deltas) / float(len(deltas))
##print "average monthly change",avgdelta

avgyd = reduce(lambda x,y: x+y, yearly_diff) / float(len(yearly_diff))
##print "average yearly diff",avgyd

first = None
second = None
for line in open('real-estate-prices','r').readlines():
    line = line.strip()
    if len(line) == 0 or line[0] == '#':
        continue

    if first is None:
        first = line
    second = line

value = 198000
month = int(first[:2])
last_month = int(second[:2])
year = int(first[3:7])

trend = open('2004-05-trend', 'w')
while True:
    line = "%02d/%04d %d" % (month, year, int(value))
    trend.write(line + '\n')
    
    value += avgdelta

    if year == 2011 and month == last_month:
        break
    month += 1
    if month > 12:
        month = 1
        year += 1

trend.close()
print 'wrote "2004-05-trend"'
