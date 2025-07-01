# ezsettings

* Simplest settings manager class.

* Look at the file "tests.py" for simple usage examples.

* The standard usage is explained in the file "tests.py" that comes with the package.

* The only deficiency is that you are not allowed to use the Settings class attributes
  as keys in your settings object:  
      delete, get, keys, pop, set, update,
      and the other dunder keys.

* There are only 6 real keys that you need to give up for enjoying the convenience and
  simplicity of this data structure: "delete", "get", "keys", "pop", "set", and "update".
  The others are dunder keys that are rarely used and usually are excluded by design.
  If you absolutely need to use such keys, they can be substituted with an upper case version,
  or with a preceding underscore.

* An attempt to use one of these keys will raise an Exception,
  so a simple test of your code can protect you from using these reserved keys.
