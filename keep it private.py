class myclass:
    __privatevar = 27;
    def __privmeth(self):
        print("im inside my class myclass")
    def hellow(self):
        print("private variable value", myclass.__privatevar)
foo = myclass()
foo.hellow()
foo.__privmeth
        