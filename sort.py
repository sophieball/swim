#The original log file is achronical, so I wrote this file to sort the logs into different files based on their end_time

f = open('2013-02-27', 'r')
files = {} 

f.readline()#header
for i in xrange(1, 1000):
  line = f.readline()
  line_array = line.split(',')

  end_time = line_array[1]
  end_time = end_time.split('.')[0]

  if not (end_time in list(files)):
    files[end_time] = open(end_time, 'w') 
  files[end_time].write(line)

f.close()
for i in list(files):
  files[i].close()
