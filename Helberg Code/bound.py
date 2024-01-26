d = 2
q = 2 

for n in range(3,15):
    lower = round(d*d*pow(q,n+d)/(pow(q-1,2*d)*pow(n,2*d)), 3)
    upper = round(d*pow(q,n)/(pow(q-1,d)*pow(n,d)), 3)
    print("lower= ", lower, " upper= " , upper)
