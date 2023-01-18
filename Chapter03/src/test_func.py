def function(argm):
    argm += " in function"
    print(argm)


immutable = "hello"
function(immutable)
print(immutable)


mutable = list("hello")
function(mutable)
print(mutable)
