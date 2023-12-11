

#handles calculation for Starters - asks user for variables "eaves" and "rakes"
#adds these values and divides them by a constant 120 giving the starter value
def starter_calc():
    eaves = int(input("Enter the Eave value "))
    rakes = int(input("Enter the Rake value "))
    print("The amount of Starter needed: ", eaves + rakes/120)

#handles Ridge calculations - variables: "ridge" and "hips" adds them and divides
#by constant
def ridge_calc():
    ridge = int(input("Enter the ridge value "))
    hips = int(input("Enter the hips value "))
    print("Materials needed for the Ridge: ", ridge + hips/33)

def ice_water_calc():
    valleys = int(input("Enter the valleys value "))
    print("The amount of Ice & Water needed: ", valleys/66)

    #think of adding global variable 4 rakes and eaves since they are already specified in
    #earlier calcs - could automate this calc
def drip_edge_calc():
    rakes = int(input("Enter Ridge value "))
    eaves = int(input("Enter eave value "))
    print("The amount of Drip edge Needed: ", rakes + eaves/9)

def coils_nails_calc():
    nailBoxes = int(input("Enter amount of nail boxes "))
    print("The amount of boxes in squares is: ", nailBoxes*14)

def plastic_cap_calc():
    plasticCaps = int(input("enter amount of Plastic Caps "))
    print("The amount of Plastic Caps in squares is: ", plasticCaps*20)

starter_calc()
ridge_calc()
ice_water_calc()
drip_edge_calc()
coils_nails_calc()
plastic_cap_calc
