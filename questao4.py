sp = 67836.43
rj=36678.66
mg=29229.88
es=27165.48
outros=19849.53

total = sp+rj+mg+es+outros

def percentualSP():
    return (sp/total)*100

def percentualRJ():
    return (rj/total)*100

def percentualMG():
    return (mg/total)*100

def percentualES():
    return (es/total)*100

def percentualOutros():
    return (outros/total)*100


print(percentualSP())
print(percentualRJ())
print(percentualMG())
print(percentualES())
print(percentualOutros())