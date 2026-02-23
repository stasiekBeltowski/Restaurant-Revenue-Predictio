#Zamiana lokalizacji
def location(l):
    if l == "Downtown":
        return "Good_loc"
    elif l == "Suburban":
        return "Medium_loc"
    elif l == 'Rural':
        return "Bad_loc" 
    
#Istnienie parkingu  
def parking(p):
    if p == "Yes":
        return 1
    elif p == "No":
        return 0
    
# Zamiana typu kuchni na Popularny(1) i Normalny(0) (poprawia model)
def cuisine(c):
    if c in ['American', 'Italian']:
        return 1
    else:
        return 0