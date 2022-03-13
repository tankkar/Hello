import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = [numpy.mean(speed), numpy.median(speed)]
print(x)

from scipy import stats
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 5)

#x = numpy.std(speed)
#x = numpy.var(speed)
#x = numpy.percentile(speed, 75)

print(x)

