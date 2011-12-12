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

print 'Number of first babies', len(firsts.records)
print 'Number of other babies', len(others.records)
