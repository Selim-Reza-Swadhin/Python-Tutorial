roll = [101, 102, 103, 104, 105, 106]
name = ["Anisul Islam", "Selim", "Reza", "Swadhin", "Ridoy", "Pinkey"]

zipfnc = zip(roll, name)
print(list(zipfnc))

# add section
zipfnc = zip(roll, name, "ABCDEF")
print(list(zipfnc))
