location = input ("Enter City:")
mbra = "Mbarara"
Kla = "Kampala"
sp = "Space"
gh = "Mbale"
ks = "Kasese"
ar = "Arua"
try:
    if location == "Mbarara":
        pa = input ("Pay:")
        p = int (pa)
        if p >= 4000000:
            print ("Decision: I'll take the Mbarara job")
        else:
            print ("No thanks, I can find something better in kla")
    elif location == "Kampala" :
        pa = input ("Pay:")
        p = int (pa)
        if p >= 10000000:
            print ("Decision: I'll take the Kampala job")
        else:
            print ("Get serious")
    elif location == "Space":
        pa = input ("Pay:")
        p = int (pa)
        if p >= 100:
            print ("Decision: I will definately take the job")
        else:
            print ("I,ll still take the job bro.")
    elif location == gh :
        pa = input ("Pay:")
        p = int (pa)
        if p >= 6000000:
            print ("Decision: I'll take the job outside Mbarara")
        else:
            print ("No thanks, I can find something better abroad")
except:
    print ("Try major cities")