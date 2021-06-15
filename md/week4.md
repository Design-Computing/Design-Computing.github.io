# Week 4: 🐼 Pandas 🐼 and starting the data project for real!

## Lecture

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

## Homework

# This week's optional reading 📚

Although this reading is optional, it'll make a you a way better CoDe person! Maybe re-read the early readings, they might make more sense now.

**[Coates, P.](https://generativedesign.wordpress.com/2010/08/04/book-review-programming-architecture/)** (2010). [Programming.Architecture](https://www.amazon.com/Programming-Architecture-Paul-Coates/dp/0415451884) 📖

**Victor, B.** (2013). [_The Future of Programming._](http://worrydream.com/dbx)

**Polich, K.** (2016). [_Potholes._](http://dataskeptic.com/blog/episodes/2016/potholes) 🎧

**Polich, K.** (2015). [_NYC Speed Camera Analysis._](http://dataskeptic.com/blog/episodes/2015/nyc-speed-camera-analysis) 🎧

# This week's homework

1. Finish this week's exercises

1. Redo as many of the exercises as you feel you need to until you feel fluent with them.

1. Take a look at these. Watch this one:

   <iframe width="560" height="315" src="https://www.youtube.com/embed/495nCzxM9PI" frameborder="0" allowfullscreen>Should be a video here</iframe>

   You might want to find out more about Alan Kay, he's an interesting character in his own right.

   Don't watch all of this, but flick through it. Almost everything demoed here is new in this demo.

   <iframe width="560" height="315" src="https://www.youtube.com/embed/yJDv-zdhzMY" frameborder="0" allowfullscreen>Should be a video here</iframe>

# How to do...

<iframe width="560" height="315" src="https://www.youtube.com/embed/y6gGuLbfMLk" frameborder="0" allowfullscreen>Should be a video here</iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/3YHXf8dmoiA" frameborder="0" allowfullscreen>Should be a video here</iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/2FlCOC2QK4k" frameborder="0" allowfullscreen>Should be a video here</iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/9U94fy1bQgg" frameborder="0" allowfullscreen>Should be a video here</iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/BsJwH-CiOrM" frameborder="0" allowfullscreen>Should be a video here</iframe>

<iframe width="560" src="https://www.youtube-nocookie.com/embed/9U94fy1bQgg?rel=0" frameborder="0" allowfullscreen>Should be a video here</iframe>
