This package seems to be a Python wrapper around a Java program.
Thus, if your machine has not yet had Java installed, you'd probably
meet with problems warning , e.g., that

```python
File ~/.config/miniconda3/envs/py3.10/lib/python3.10/site-packages/jnius/env.py:332, in get_jdk_home(platform)
    328             jdk_home = realpath(
    329                 which('javac')
    330             ).replace('bin/javac', '')
    331         except TypeError:
--> 332             raise Exception('Unable to find javac')
    334 if not jdk_home or not exists(jdk_home):
    335     return None

Exception: Unable to find javac
```

I am no Java programmer, but on one machine I happened to have Scala installed, which
turned out to be one way to install the above-mentioned `javac`:

1. Install sdkman: <https://sdkman.io/>  
   As of 2022, install via the command `curl -s "https://get.sdkman.io" | bash`
1. Use sdkman to install Java: `sdk install java`
1. Then you're good to go. (To double-check, you can type `which javac` in the terminal to see where it is installed)


