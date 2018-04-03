import functools

def doublewrap(f):
    @wraps(f)
    def new_dec(*args,**kwargs):
        if len(args)== 1 and len(kwargs) and calleble(args[0]):
            return f[args[0]]
        else:
            return lambda realf: f(realf,*args,**kwargs)
    return new_dec

@doublewrap
def mult(f, factor=2):
    def wrap(*args,**kwargs):
        return