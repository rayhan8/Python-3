# float formatting follows "{value:width.precision f}"

result = 100/700

print("The result was {}".format(result))
print("The result was {r}".format(r=result))

# r is value:1 is width.3f is precision f
print("The result was {r:1.3f}".format(r=result))

# "{value:gap10.5 precision f}"
print("The result was {r:10.5f}".format(r=result))
