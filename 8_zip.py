#----------------------zipping----------------

#----zip----

keys = ["a", "b", "c"]
vals = [1,2,3]

zipped = zip(keys,vals)
zipped = list(zipped)

print(zipped)

#--unzip-----

k,v = zip(*zipped)
print(k,v)
