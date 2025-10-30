h = int(input("enter classes held:"))
a = int(input("enter classes attended"))
p = (h/a)*100
s="Eligible" if p >=75 else "Not eligible"
print(f"Attendance:{p}  Staus:{s}")