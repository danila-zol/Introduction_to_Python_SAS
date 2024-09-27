def outer(text):
 
    def inner():
        print(text)

    return inner
    
 
 
f = outer("Hello, Closures!")
f()