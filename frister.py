import sys
import datetime

fag = []
for line in sys.stdin:
    emne, tittel, frist = line.split(",")
    dag, mnd, aar = frist.split(".")
    dato = datetime.date(int(aar), int(mnd), int(dag)) 
    fag.append([dato, emne, tittel])
    fag.sort()

dagensdato = datetime.date.today()
for rad in fag:
    if dagensdato > rad[0]:
        continue
    if rad[0] - dagensdato > datetime.timedelta(weeks=2):
        break
    
    frist = ".".join([str(rad[0].day), str(rad[0].month)])
    print(frist, " - ", rad[1], rad[2])
    
