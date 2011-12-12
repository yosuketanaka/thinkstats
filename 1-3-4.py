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

sum1=0
num1=0
sum2=0
num2=0

for q in firsts.records:
    sum1+=q.prglength
    num1+=1
print 'average pregnancy length for first babies is', float(sum1)/num1, 'weeks'

for q in others.records:
    sum2 += q.prglength
    num2 += 1
print 'average pregnancy length for other babies is', float(sum2)/num2, 'weeks'
print 'difference is', (float(sum1)/num1-float(sum2)/num2)*7, 'days'
