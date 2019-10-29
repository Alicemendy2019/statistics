
import random

filename = 'sampledata.csv'
text = ''
for i in range(0,10):
	text += str(random.randint(1,10))

with open(filename,'w')  as f:
	f.write(','.join(text))