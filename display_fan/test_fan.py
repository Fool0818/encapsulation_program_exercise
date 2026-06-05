from fan import Fan

fan1 = Fan()
fan1.setSpeed(Fan.FAST)
fan1.setRadius(10)
fan1.setColor("yellow")
fan1.setOn(True)

fan2 = Fan()
fan2.setSpeed(Fan.MEDIUM)
fan2.setRadius(5)
fan2.setColor("blue")
fan2.setOn(False)

print("First Fan Object:")
print("Speed:", fan1.getSpeed())
print("Radius:", fan1.getRadius())
print("Color:", fan1.getColor())
print("On:", fan1.getOn())

print()

print("Second Fan Object:")
print("Speed:", fan2.getSpeed())
print("Radius:", fan2.getRadius())
print("Color:", fan2.getColor())
print("On:", fan2.getOn())