import thinkstats
import math
import survey

table = survey.Pregnancies()
table.ReadRecords()
firsts = survey.Pregnancies()
others = survey.Pregnancies()

for p in table.records:
    if p.outcome != 1:continue
    else:
        if p.birthord ==1:
            firsts.AddRecord(p)
        else:
            others.AddRecord(p)
fprg=[]
oprg=[]
for q in firsts.records:
    fprg.append(q.prglength)
for q in others.records:
    oprg.append(q.prglength)

fmeanvar=thinkstats.MeanVar(fprg)
omeanvar=thinkstats.MeanVar(oprg)
print 'mean of first babies is', fmeanvar[0], 'weeks'
print 'mean of other babies is', omeanvar[0], 'weeks'
print 'standard deviation of first babies is', math.sqrt(fmeanvar[1])
print 'standard deviation of other babies is', math.sqrt(omeanvar[1])
