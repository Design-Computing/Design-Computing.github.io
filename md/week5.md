### Week 5 History and I/O

## Lecture

### History

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQkRONPNEDyj3YpSf7LMfGflYj4mnwJJGOllSvPrvXp6xUP8jbGm8gLzugVdwQBWz0cXGFLAXKWO30W/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true">Should be a video here</iframe>

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQkRONPNEDyj3YpSf7LMfGflYj4mnwJJGOllSvPrvXp6xUP8jbGm8gLzugVdwQBWz0cXGFLAXKWO30W/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true">Should be a video here</iframe>

## Lab

1. There are some running examples in `IOexamples.py`, read them, step through them, and you should have a pretty good idea of what to do in `exercise1.py`. You should be feeling pretty comfortable with how this process works by now.

1. Talk to a tutor about your open data project idea. Get started on the data audit process described below.

Here's the example from the lecture if you want to try it out:

```python

import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

r = requests.get(url)
if r.status_code is 200:
    the_json = json.loads(r.text)
    print(the_json)
    print(json.dumps(the_json, indent=4))
```

## Lab

1. There are some running examples in `IOexamples.py`, read them, step through them, and you should have a pretty good idea of what to do in `exercise1.py`. You should be feeling pretty comfortable with how this process works by now.

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSxdowE5V8LmQtbDO8iXKPh9BuNUzPwiqYN7ytxbYuQsXGc1lbt-EJGTkX9CoYdhKg06CpEToLQ8wnz/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Jobs

What to do this week:

### Exercises

There's a break in the weekly exercises this week for you to get moving on your data project. That means that you have _more time_ to catch up. So if you're not right up to date, don't stop! [link](https://docs.google.com/spreadsheets/d/e/2PACX-1vRpx7SE6am9_uszUVCzGmBfKWshvtcTYZp9oilhlKht2-r2YY9wgt-MmIja_20igkoEkeowzuaNQmap/pubhtml?gid=1672893348&single=true)

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRpx7SE6am9_uszUVCzGmBfKWshvtcTYZp9oilhlKht2-r2YY9wgt-MmIja_20igkoEkeowzuaNQmap/pubhtml?gid=1672893348&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="700px" frameless></iframe>

(I've been working on this a bit so there are a couple of things that need a tweak.)

Now that you know how to do shared sessions, practice pair programming to work together on your exercises.

## Data Project

If you don't have a dataset, get in touch as soon as you can!

If you do, work through the example file with it to get a feel for the data. Start to think about what you could do with it.

What are the columns like? What _type_ of data are they? `int`s or dates? or strings?

What opportunities for grouping are there? Categories? Group by day, month, year, day of week, time of day?

If you had infinite time, what else could you join to this dataset to make it even more interesting?

#### Example file

[This file](https://github.com/Design-Computing/course/blob/master/week7/basic_pandas.ipynb) should get you up and running with exploring your data.

Just point the file path in the cell that loads the data to your data and start working through it. It's not going to work straight out of the box. It'll need to be modified a lot, but it's the bones of a good set up.

<iframe src="https://github.com/Design-Computing/course/blob/master/week7/basic_pandas.ipynb" width="960" height="569">

[The iframe isn't working, just go to the link](https://github.com/Design-Computing/course/blob/master/week7/basic_pandas.ipynb)

</iframe>

I'd like you to present your data to at least 1, ideally 2 of your peers before Wednesday. I'm going to ask them what your data is about and what was interesting about it to them.
