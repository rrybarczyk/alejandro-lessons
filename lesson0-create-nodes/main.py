import nuke

# Create a Blur node
nuke.createNode("Blur")

# Create another Blue node
nuke.createNode("Blur")

# Create a third Blue node
nuke.createNode("Blur")

# Now this is getting really repetitive....
# So we use a `for loop` instead

# This will create 10 Blur nodes and print out the value of `x` in every loop
for x in range(0,10):
    nuke.createNode("Blur" + str(1))
    print x

