from functools import wraps

Y = lambda f :\
        wraps (f)\
              ((lambda x : f (lambda *v, **gv : x (x) (*v, **gv)))
               (lambda x : f (lambda *v, **gv : x (x) (*v, **gv))))

