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

### Data Audit

The file that I used to give the lecture is a template for how to do this chunk of the project. It shows you the techniques that you need to do preliminary exploration on your dataset. Here's some pseudo code for what you need to do:

* for your whole dataset:
    * How many rows and columns? `df.shape` will tell you that.
    * What does this dataset explain?
    * Why was it collected?
    * Who paid for it?
    * Where did you get it from?
* for each column in your dataset:
    * Describe it by recording/measuring/graphing:
        * Name
        * What the column describes
        * How that data was measured
        * Is it continuous or categorical data? Continuous is `[1, 2, 4.6, -5]` and categorical is `["cat", "dog", "mouse", "dog" , "dog"]`
        * If categorical:
            * do a `df["column_name"].value_counts()` and get an idea of the counts that you'll be working with.
            * do a `df["column_name"].value_counts().plot(kind="bar")` to get an idea of the distribution of the counts
            * Check for things that you might need to _fold_ into each other. Do you have entries for `sydney` and `Syd` and `Sydney` and `SYD` in your data? Should they really be the same thing?
            * What is the distribution shape of this graph?
        * If continuous:
            * do a `df["column_name"].hist()` to get an idea of what your numbers are and how they're distributed.
            * Is it a time series? A time series is data that changes over time, like the temperature at my desk, or the number of cookies I have left in the packet. If it _is_ a time series
                * do a `df["column_name"].plot()` to see the trends.
                * are there any periods of time that are missing data? E.g. did they turn it off over the weekends?
            * What's the biggest value (max)?
            * What's the smallest value (min)?
            * What's the mean value (mean)?
            * What's the median value (median)?
            * What's the most common value (mode)?
        * make some general comments about this column, based on what we see.
    * make some general comments about the dataframe, based on what we see.

That seems like quite a lot of work. It is, but it'll be very useful in exploring your dataset. It'll give you a strong sense of what you're dealing with.

All the way through, keep a keen eye out for moments where you say to yourself "Oh, that's interesting!". _That_ is the most important thing, and will be what forms the backbone of your data storytelling.

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
