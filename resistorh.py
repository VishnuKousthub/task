colors = {"black":0,"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,"green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
tolerance = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10}
multiplier = { "black":1,"brown":10 , "red":100 , "orange": 1000 , "blue": 1000000}
tol=''

def resistor_tolerance(bands):
    if len(bands) == 1:
        value = colors[bands[0]]
        return value
    elif len(bands) == 4:
        tol=tolerance[bands[3]]
        value = (colors[bands[0]] * 10  + colors[bands[1]]) * multiplier[bands[2]]
        return value,tol
    elif len(bands) == 5:
        tol=tolerance[bands[4]]
        value = (colors[bands[0]] * 100 + colors[bands[1]] * 10 + colors[bands[2]]) * multiplier[bands[3]]
        return value,tol
    else:
        print("not a valid input")
def tolerance_value(value,tol):
    if value is not None:
        if value >= 1000000:
            return f"{value//1000000} megaohms ±{tol}%"
        elif value >= 1000:
            return f"{value//1000} kiloohms ±{tol}%"
        else:
            return f"{value} ohms ±{tol}%"
    else:
        return "Not a valid input"
bands=("orange","orange","blue","red")
res_value,tol_value=resistor_tolerance(bands)
res=tolerance_value(res_value,tol_value)
print(res)


    
    