
class Hello(object):

    def __init__(self,args,**kwargs):

        self.Names=args
        self.Greetings=[kwargs['Greetings'] + "-" + i  if 'Greetings' in kwargs else 'Hello -' + i for i in args]

    def say_hi(self):
        [print(x) for x in self.Greetings]
