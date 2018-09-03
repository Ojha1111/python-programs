import functools

 memoize = functools.lru_cache
 print(memoize)
<function lru_cache at 0x7fb2a6b42f28>
 

 class MyClass:
...     pass
...
 give_me_more = MyClass()
 print(give_me_more)
<__main__.MyClass object at 0x7f512e65bfd0>

