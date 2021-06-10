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
