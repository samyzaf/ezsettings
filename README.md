# ezsettings

* Simplest settings manager class.

* Look at the file "tests.py" for simple usage examples.

* The standard usage is explained in the file "tests.py" that comes with the package.

* The only deficiency is that you are not allowed to use the Settings class attributes
  as keys in your settings object:  
      delete, get, keys, pop, set, update,
      __class__, __delattr__, __dict__, __dir__, __doc__, __eq__, __format__, __ge__,
      __getattribute__, __getitem__, __gt__, __hash__, __init__, __init_subclass__,
      __iter__, __le__, __lt__, __module__, __ne__, __new__, __reduce__, __reduce_ex__,
      __repr__, __setattr__, __setitem__, __sizeof__, __str__, __subclasshook__, __weakref__

* There are only 6 real keys that you need to give up for enjoying the convenience and
  simplicity of this data structure: "delete", "get", "keys", "pop", "set", and "update".
  The others are dunder keys that are rarely used and usually are excluded by design.
  If you absolutely need to use such keys, they can be substituted with an upper case version,
  or with a preceding underscore.

* An attempt to use one of these keys will raise an Exception,
  so a simple test of your code can protect you from using these reserved keys.
