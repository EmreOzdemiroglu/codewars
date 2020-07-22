def get_planet_name(id):
    switcher={
            1:"Mercury",
            2:"Venus",
            3:"Earth",
            4:"Mars",
            5:"Jupiter",
            6:"Saturn",
            7:"Uranus",
            8:"Neptune"}
    return switcher.get(id)
"""
def get_planet_name(id):
    return{
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id)
    
def get_planet_name(id):
    return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]
    
def get_planet_name(id):
    name=""
    return{
        1:"Mercury",
        2:"Venus",
        3:"Earth",
        4:"Mars",
        5:"Jupiter",
        6:"Saturn",
        7:"Uranus" , 
        8:"Neptune"
       }[id]
       
      
get_planet_name=lambda id: ["Kypton","Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id]


get_planet_name = (None, "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune").__getitem__
get_planet_name = lambda i: ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"].__getitem__(i-1)
def get_planet_name(id):
    solar_system = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    return solar_system[id - 1]
def get_planet_name(id):
    return "Sun Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune".split()[id]
"""
