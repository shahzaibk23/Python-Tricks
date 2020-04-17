#----------------------------map------------------------

#----lambda---

g = lambda x: x*x*x
#lambda argument: expressions

print(g(5))

#---map--

x = [1,2,3]

y = map(lambda x: x+2,x)
print(list(y))