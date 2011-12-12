import survey

table = survey.Pregnancies()
table.ReadRecords()
firsts = survey.Pregnancies()

for p in table.records:
    if p.outcome == 1:
        firsts.AddRecord(p)

print 'Number of live birth', len(firsts.records)
