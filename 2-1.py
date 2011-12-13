import thinkstats
import math

pumpkin = [1,1,1,3,3,591]
meanvar=thinkstats.MeanVar(pumpkin)
print 'mean is', meanvar[0]
print 'variance is', meanvar[1]
print 'standard deviation is', math.sqrt(meanvar[1])
