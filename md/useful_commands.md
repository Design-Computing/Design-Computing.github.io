# Useful Commands

To get from your `me` directory into the course directory:

```
cd ..\course
```

To get from the course directory back into your `me` directory:

```
cd ..\me
```

To run the tests this week:

```
python ..\course\set1\tests.py
```

To update the course to the latest version:

```
cd ..\course
git pull
pip install -r .\requirements.txt
cd ..\me
python ..\course\set1\tests.py
```

To check the state of your git commits:

```
git status
```

To push to github with some useful feedback:

```
git push
```


# Important words

Think of this as a collaborative notebook. When you come across a word that you think should be in here, contribute it.

* **call**: when we _call_ a function, we make it happen. E.g. when we call the function `one_the_gate()` the gate will open. If we call the function `add(4, 6)` it will _return_ 10, because we called it with the _arguments_ 4 and 6.
