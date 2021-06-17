# Week 3: Useful Programs and Algorithms

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vR2cYPx1kRUlOpmEurSQeJJrEAdnUV6a4TQPDsdy4fjssnyRHViZqI2X5KSjPVVQRgZWWLr-DA_azJw/pubchart?oid=1583654128&amp;format=interactive" style="width: 610px; height: 380px; float: right; margin-left: 2em;"></iframe>

This is updated most days, so if you don't see your values changing, it's probably because you aren't `push`ing to GitHub.

It's important to note that this chart shows **un**weighted marks. I.e. it shows a longer bar for some parts than others. The mark you actually get is weighted, so don't get caught up in who's in what order, just use it to check that you're up to date.

What I _really_ want you to do with this graph is to use it as an opportunity to help people. You might be crushing this class, but you're going to spend 3 years with these people and sooner or later, you're going to need their help! Also, more than that, the better the average competence of your cohort is, the better you'll all do when you graduate. This is a _non zero sum game!_

This is the weighted graph, but it's not really worth looking at yet.

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vR2cYPx1kRUlOpmEurSQeJJrEAdnUV6a4TQPDsdy4fjssnyRHViZqI2X5KSjPVVQRgZWWLr-DA_azJw/pubchart?oid=17662914&amp;format=interactive" style="width: 610px; height: 380px; float: right; margin-left: 2em;"></iframe>

## Some dates:

| Week            | Activity                                             |
| --------------- | ---------------------------------------------------- |
| Weeks 1-5       | Exercises 👩🏾‍🏫📏📐                                     |
| Week 3          | (This week) Introduction to the data project. 📈📊📉 |
| Week 4          | Data project tutorial                                |
| Week 6          | Flex week 😴🌴🥥                                     |
| Week 7          | The Quiz 👩🏾‍💻                                          |
| Weeks 8, 9 & 10 | Data project tutorials                               |
| Week 11         | Data project presentations                           |
| Week 12         | Data project submission (by Monday 9pm)              |

## Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSox_vZU2xprGNVi-fi_3cwwkLvAo6qfuYhITdgSawNbQNI5ckW2G-CThN4Ew6XAmSnojYBMpAIr-Qz/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

### F-Strings

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6Xe8le9eVR0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

I mention a cheatsheet, it's [here](https://myshell.co.uk/blog/2018/11/python-f-string-formatting-cheatsheet/).
[This one was good too](https://zetcode.com/python/fstring/).

### Debugging and thinking about state

Several people said that they didn't _get_ exercise 2, the one where you step through a file with the debugger. I made this video in the hope that it'll make it a bit clearer.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/nfhNeIKGf2Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The idea is that each line in a program does something. In general it'll do one of two things, make something new, or modify something that exists. The skill here is learning to predict what those modifications will be, and not letting your imagination get carried away with you.

### New Syntax

#### `in`

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gv3bEgskOFY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

```python
for i in [1, 2, 3]:
    print(i * 2)

print(2 in [2, 3, 4])
print(8 in [2, 3, 4])
print("2" in [2, 3, 4])
print({} in [2, 3, 4])
print("car" in "carpet")

print(7 in {"key":7, "otherKey":5})
print("key" in {"key":7, "otherKey":5})

```

#### `try`/`except`

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/OxP4NOTxkUc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

```python
def be_silly(top_part, bottom_part):
    try:
        return top_part / bottom_part
    except TypeError as my_error:
        print(f"you are so silly! {my_error}")
    except ZeroDivisionError as my_error:
        print(
            f"you are so silly! Can't divide {top_part} by {bottom_part} "
            f"or we get infinity\n{my_error}"
        )
    except Exception as general_error:
        print(general_error)


print(be_silly(10, 2))
print(be_silly("cake", 2))
be_silly(10, 0)


```

## Exercise tips:

In set 3, exercise 1, this is how to solve the first question. There are a lot of ways to do it, but this is the one that will have the most applicability to the next question. If you want a challenge, try to solve it without using range at all, you'll need a while loop.

```python
def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    my_range = []
    for i in range(start, stop, step):
        my_range.append(i)
    return my_range
```

In `stubborn_asker` you're going to need a `while` loop, it's only going to be tested with integers.

In `not_number_rejector` you're going to need a `while` loop and a `try`/`catch` block, it's going to get thrown a bunch of inputs that are not a number, a string, a list, a dictionary, etc.

`exercise2.py` works, you're going to need to read the code, make notes, make diagrams etc. because you're going to make a more robust guessing game in the next exercise that uses your `super_asker` code to process the inputs to make sure they're really numbers. You _can_ import super_asker from ex1, but imports is a question for another day, so you can copy and paste it across, we'll do the penance later in our lives for this technical debt.

## The Open Data Project

This is the major project of this course. The first half of the course is about learning a skill, the second is about refining that skill by using it to explore the world.

> This assignment explores how to make data accessible to everyone. This is the capstone project for this course. You will take an open data set, from a collection such as the NSW government and build a way to represent it to others. You may use any available libraries or frameworks to do so, although matplotlib is recommended.

### Delivarables

### Presentation and code

The presentation will be in week 11 and your GitHub Repository will be marked at its state at 7pm Tuesday of week 12.

#### Git collaboration (due in week 11)

Working together to achieve greatness, through GitHub collaboration. One of the greatest things about being a student is having a cohort to go through the struggle of your courses with. One of the greatest things about open source culture is that there is a way for you to share the burden by helping each other out. This is a mark that is available to anyone who makes a Pull Request to anyone else’s repository during the Open Data Project and has it accepted.

**Deliverables:** Proof of an accepted pull request, in both directions, described in your lab book.

### What's the deal here then? What do I need to do?

The general model of this assignment is:

1. Pick a dataset
1. Document it, broadly
1. Describe it, broadly
1. Explore it
1. Find something that makes you say "_hmm, that's interesting_"
   1. Zoom in on that thing
   1. Visualise the data
   1. Investigate it a bit more
   1. Communicate the insights. Talk to your peers about it. They might see something that you've missed, or it might inspire them, and remember: you're all in this together!
   1. Find something that makes you say "_hmm, that's interesting_"
   1. Keep repeating this step until you've squeezed everything interesting out of it.
1. Communicate the insights. Make a presentation that is really clear and lets the graphs do most of the work.

You can do that either:

| Dataset first                                    | Question first                                             |
| ------------------------------------------------ | ---------------------------------------------------------- |
| Find an interesting dataset                      | Have a burning question you want to answer                 |
| And then find an interesting question to answer. | And then find the dataset[s] that will help you answer it. |
| Tell us what you found and how you got there.    | Tell us what you found and how you got there.              |

That recursive step of exploration is where the value in this assignment will be realised. I want you to be fascinated by your data, I want that fascination to come across in our discussions about your progress and I want it to come across in your final presentation too.

### What's the point of this assignment?

### What have people done before?

These videos are from the 2020 cohort. You can watch them to see the kinds of subjects people picked, and the depth of investigation they went into.

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLzHh2dYvM_HkpSmXqlDGIRLPr-a2BWksL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
### But where do you find data?

Governments are getting a lot better at collecting data about the world and then sharing it with their citizens. An early example of this is [Booth's Life and Labour Survey](https://www.bbc.co.uk/sounds/play/m000wsxf) from 1889 to 1903. More recently, we've been able to access data in much more productive ways, through computers, databases, spreadsheets, and most recently, APIs. Gone are the days of hand tabulating carefully, now we can query for anything we like.

You can go to [data.gov.au](https://data.gov.au/)🇦🇺, [data NSW](https://data.nsw.gov.au/), [data Victoria](https://data.melbourne.vic.gov.au/), [data.gov](https://www.data.gov/)🇺🇸, [data.gov.uk](https://data.gov.uk/), [the Australian Bureau of Statistics](https://www.abs.gov.au/), [Inside AirBnB](http://insideairbnb.com/), and a [whole bunch more](https://www.freecodecamp.org/news/https-medium-freecodecamp-org-best-free-open-data-sources-anyone-can-use-a65b514b0f2d/). Don't go to Kaggle, I'm really bored of people doing projects on who the best video game character is, that's not the point of this course!

Once you've found some, you'll need to do a data audit:

#### Data Audit

The file that I used to give the lecture is a template for how to do this chunk of the project. It shows you the techniques that you need to do preliminary exploration on your dataset. Here's some pseudo code for what you need to do:

- for your whole dataset:
  - How many rows and columns?
  - What does this dataset explain?


    **⏸️ Pause here**: There is a pretty good chance at this point that you'll find out that your data is garbage. Look for a file that's in one of these file formats: `.xls`, `.xlsx`, `.csv`, `.json`, `.tsv`. If it's not, run it past me or Alex.

    You'll want a file with at least 200 rows, ideally a thousand or more. Even more ideally, a dataset that has some geographic data, e.g. coordinates or suburb names, because we're going to be making some maps a bit later on.

- Why was it collected?
- Who paid for it?
- Where did you get it from?
- Does it have a geographical component?

* for each column in your dataset:

  - Describe it by recording/measuring/graphing:

    - Name
    - What the column describes
    - How that data was measured
    - Is it continuous or categorical data?

      - Continuous is `[1, 2, 4.6, -5]`
      - Categorical is `["cat", "dog", "mouse", "dog" , "dog"]`

      **🤓 Another Pause**: The rest of this is for next week, but I want you to read this anyway so that you can have these questions in your mind as you're picking a dataset.

    - If categorical:
      - do a `df["column_name"].value_counts()` and get an idea of the counts that you'll be working with.
      - do a `df["column_name"].value_counts().plot(kind="bar")` to get an idea of the distribution of the counts
      - Check for things that you might need to _fold_ into each other. Do you have entries for `sydney` and `Syd` and `Sydney` and `SYD` in your data? Should they really be the same thing?
      - What is the distribution shape of this graph?
    - If continuous:
      - do a `df["column_name"].hist()` to get an idea of what your numbers are and how they're distributed.
      - Is it a time series? A time series is data that changes over time, like the temperature at my desk, or the number of cookies I have left in the packet. If it _is_ a time series
        - do a `df["column_name"].plot()` to see the trends.
        - are there any periods of time that are missing data? E.g. did they turn it off over the weekends?
      - What's the biggest value (max)?
      - What's the smallest value (min)?
      - What's the mean value (mean)?
      - What's the median value (median)?
      - What's the most common value (mode)?
    - make some general comments about this column, based on what we see.

  - make some general comments about the dataframe, based on what we see.

That seems like quite a lot of work. It is, but it'll be very useful in exploring your dataset. It'll give you a strong sense of what you're dealing with.

All the way through, keep a keen eye out for moments where you say to yourself "Oh, that's interesting!". _That_ is the most important thing, and will be what forms the backbone of your data storytelling.

## Homework

Do these things in order, it'll be better that way, I promise.

1. Find a dataset and a question. Do the first part of the data audit on that dataset, up to 🤓.
1. Do the Khan Academy Algorithms Course: **Cormen, T. & Balkcom, D.**, [_Algorithms._](https://www.khanacademy.org/computing/computer-science/algorithms)

   Go through the Intro to algorithms, Binary search and Asymptotic notation sections, these guys have made it really simple to understand and it'll reinforce everything we've said in the lecture.

1. Complete the exercises in the week 3 folder.

   It looks like there's nothing to do to exercise 2, but actually that's a big deal! You need to work out a way to make a diagram of the code. It needs to be easy to understand, and help you keep track of what it's doing. There are lots of formal ways to diagram code ([UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language), flow charts) but don't let that constrain you. Think about what makes the most sense to _you_ and also about how you could use it to explain it to someone else. Make sure that your diagram goes into your lab book. It will really help you to do the same thing for exercise 3 and 4 too.

   To get a diagram into your lab book, you need an image that's online, you can use a hosting service or put the image file into your repo. Then you can make the image show with this markup: `![alt text](image url)`

1. listen to this podcast: **Galef, J.** (2016). [_Tom Griffiths and Brian Christian on "Algorithms to Live By"_. 🎧 Rationally Speaking](http://rationallyspeakingpodcast.org/show/rs-161-tom-griffiths-and-brian-christian-on-algorithms-to-li.html).

1. Read the _code reading experience_ section below. Write some thoughts in your lab book about why some of these solutions are better than others. Performance, readability, what else makes a function better.

This is a lot to do, so you've for this week and next to do it (including finishing the data audit that we'll cover how to do next week).

---

# A code reading experience!

<style>
  h3 img {
    width: 15vw;
    float: right;
  }
  .language-python {
    font-size: 140%;
  }
</style>

With that out of the way, [let's talk about](https://www.youtube.com/watch?v=ydrtF45-y-g) week 2 exercise 3 `loops_7`. You probably struggled a fair bit with this one. These are the instruction:

---

> ## Make a pyramid.
>
> Return this:

```python
[
    [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
    [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
    [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*']
]
```

> or in more simple terms:

```
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
```

> (this is what will print when you test from inside this file) This is a hard problem. Use lots of experimentation and draw lots of diagrams!

---

Below are some solutions from a previous year that passed the test. This function has a very strict test so that means that all these functions do _exactly the same thing!_

_Reading_ code is _at least_ as important as writing it, take the time to go through these examples of different ways of doing the same thing and think about which you like. Which is most readable? Which is most elegant? This is a great example of what we mean by choosing a good algorithm. There are almost always _many_ ways to do things, so you need to be able to make a call about which one to pick and why.

You should read these examples and try to make sense of them. Reading code is an aesthetic experience, you'll like some of these better than others. Some will _perform_ better than others in terms of algorithmic complexity, but usually a readable function is better than a fast one.

### Rizo007 ![](https://github.com/Rizo007/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    columns = []
    for x in range(5):
        rows = []
        for y in range(9):
            if abs(y-4) <= x:
                rows.append('*')
            else:
                rows.append(' ')
        columns.append(rows)

    print(columns)
    return columns
```

### pennypangCODE ![](https://github.com/pennypangCODE/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    columns = []
    for x in range(5):
        rows = []
        for y in range(9):
            if abs(y-4) <= x:
                rows.append('*')
            else:
                rows.append(' ')
        columns.append(rows)

    print (columns)
    return columns
    pass
```

### FlimEden ![](https://github.com/FlimEden/code1161base/raw/master/mugshot.png)

```python
def loops_7():

    baseLength = 9
    starting = int(baseLength / 2)  # Get middle index
    printNum = 1
    height = starting + 1
    pyramidArray = []

    for i in range(height):
        printIterator = printNum
        pyramidArray.append([])

        for j in range(baseLength):
            if j >= starting and printIterator != 0:
                pyramidArray[i].append("*")
                printIterator -= 1
            else:
                pyramidArray[i].append(" ")

        printNum += 2
        starting -= 1

    return pyramidArray
```

### sheldakristie ![](https://github.com/sheldakristie/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    ihatepyramids_box = []
    for i in range(5):
        ihatepyramids_inside = []
        for j in range(4-i):
            ihatepyramids_inside.append(" ")
        for j in range(1+i):
            ihatepyramids_inside.append("*")
        for j in range(0+i):
            ihatepyramids_inside.append("*")
        for j in range(4-i):
            ihatepyramids_inside.append(" ")
        ihatepyramids_box.append(ihatepyramids_inside)
    return ihatepyramids_box
```

### RangoRay ![](https://github.com/RangoRay/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    numberfield = []
    for i in range(5):
        number = []
        for j in range(9):
            if j < 5 + i and j > 3 - i:
                number.append('*')
            else:
                number.append(' ')
        numberfield.append(number)
    return numberfield
```

### lorniashi ![](https://github.com/lorniashi/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    pyramid = []
    for i in range(5):
        row = '{0}{1}{0}'.format(' '*(5-i-1), '*'*(i*2+1))
        pyramid.append(list(row))

    print (pyramid)
    return pyramid
```

### atiredturtle ![](https://github.com/atiredturtle/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    HEIGHT = 5
    WIDTH = 9
    arr = []
    num_blanks = 4

    for i in range(HEIGHT):
        row = []
        for i in range(WIDTH):
            if i < num_blanks:
                row.append(" ")
            elif WIDTH - i <= num_blanks:
                row.append(" ")
            else:
                row.append("*")
        num_blanks -= 1
        arr.append(row)
    return arr
```

### alanw410 ![](https://github.com/alanw410/code1161base/raw/master/mugshot.png)

```python
def loops_7():

    pyramid = [0] * 5
    sp = 4
    sp2 = 5

    def v(num):
        if(num < sp or num >= sp2):
            return True
            pass
        else:
            return False
            pass
    for x in range(0, 5):
        pyramid[x] = (map(lambda x: ' ' if(v(x)) else '*', range(0, 9)))
        sp = sp - 1
        sp2 = sp2 + 1

    return(pyramid)
    pass
```

### Matchalism ![](https://github.com/Matchalism/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    pyramidList = []
    for index in range(5):
        stacklist = []
        for j in range(9):
            if (5 - index - 2 < j and j < index + 5):
                stacklist.append("*")
            else:
                stacklist.append(" ")
        pyramidList.append(stacklist)
    return pyramidList
```

### TerryAg ![](https://github.com/TerryAg/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    returnedList = []
    for i in range(0, 5)[::-1]:
        temp = [' ' for _ in range(9)]
", "        temp[i:9-i] = '*'*(9-2*i)
        returnedList.append(temp)
    return returnedList
```

### sherry0303 ![](https://github.com/sherry0303/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    star_pyramid = []
    for i in range(5):
        row = list("*"*9)
        left_bound = int((9-1)/2 - i)
        right_bound = int((9+1)/2 + i)
        for j in range(0, left_bound):
            row[j] = " "
        for j in range(right_bound, 9):
            row[j] = " "
        star_pyramid.append(row)

    print(star_pyramid)
    return star_pyramid
```

### AkisukeY ![](https://github.com/AkisukeY/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    pyramid = []
    blank = 4
    dot = 1
    for i in range(5):
        plane = []
        for j in range(blank):
            plane.append(" ")
        for j in range(dot):
            plane.append("*")
        for j in range(blank):
            plane.append(" ")
        blank -= 1
        dot += 2
        pyramid.append(plane)
    return pyramid
```

### 872815554 ![](https://github.com/872815554/code1161base/raw/master/mugshot.png)

```python
def loops_7():

    baseLength = 9
    starting = int(baseLength / 2)  ### Get middle index
    printNum = 1
    height = starting + 1
    pyramidArray = []

    for i in range(height):
        printIterator = printNum
        pyramidArray.append([])

        for j in range(baseLength):
            if j >= starting and printIterator != 0:
                pyramidArray[i].append("*")
                printIterator -= 1
            else:
                pyramidArray[i].append(" ")

        printNum += 2
        starting -= 1

    return pyramidArray
```

### dbisazza ![](https://github.com/dbisazza/code1161base/raw/master/mugshot.png)

```python
def loops_7():

    def isPointOnPyramid(i, j):
        if j == 4:
            row.append('*')
        if (j > 4 - (i+1)) & (j < 4 + (i)):
            row.append('*')
        else:
            row.append(' ')

    column = []

    for i in range(5):
        row = []
        for j in range(8):
            isPointOnPyramid(i, j)
        column.append(row)

    print(column)
    return column
    pass
```

### timtamtinyman999 ![](https://github.com/timtamtinyman999/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    columns = []
    for x in range(5):
        rows = []
        for y in range(9):
            if abs(y-4) <= x:
                rows.append("*")
            else:
                rows.append(' ')
        columns.append(rows)

    return columns
```

### DarkPurple141 ![](https://github.com/DarkPurple141/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    temp = []
    for i in range(5):
        new = [' ']*9
        for j, _ in enumerate(new):
            if j >= 4-i and j <= 4+i:
                new[j] = '*'

        temp.append(new)
    return temp
```

### zingjanet ![](https://github.com/zingjanet/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    the_pyramid = []
    spine = ['*']
    for i in range(5):
        space = []
        tile = []
        for j in range(4-i):
            space.append(" ")
        for k in range(i):
            tile.append("*")
        the_pyramid.append(space + tile + spine + tile + space)

    return the_pyramid
```

### tomwyb ![](https://github.com/tomwyb/code1161base/raw/master/mugshot.png)

```python
def loops_7():

    pyr = []

    for i in range(5):
        row = []
        for x in range(9):
            if x < (4 - i) or x > (4 + i):
                row.append(" ")
            else:
                row.append("*")
        pyr.append(row)

    return pyr
```

### matthewpoytress ![](https://github.com/matthewpoytress/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    pyramid = []
    for i in range(5):
        row = '{0}{1}{0}'.format(' '*(5-i-1), '*'*(i*2+1))
        pyramid.append(list(row))

    print (pyramid)
    return pyramid
```

### BaptisteHiggs ![](https://github.com/BaptisteHiggs/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    pyramidList = []
    height = 5
    for y in range(height):
        tempLine = []
        for x in range(height*2-1):
            if x >= height - 1 - y and x <= height + y - 1:
                tempLine.append('*')
            else:
                tempLine.append(' ')
        pyramidList.append(tempLine)
    return pyramidList
```

### DanielHeh ![](https://github.com/DanielHeh/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    pyr = []
    blank = 4
    dot = 1
    for i in range(5):
        plane = []
        for ii in range(blank):
            plane.append(" ")
        for ii in range(dot):
            plane.append("*")
        for ii in range(blank):
            plane.append(" ")
        blank -= 1
        dot += 2
        pyr.append(plane)
    return pyr
```

### OneMoreN ![](https://github.com/OneMoreN/code1161base/raw/master/mugshot.png)

```python
def loops_7():
    pyramidList = []
    for index in range(5):
        stackList = []
        for x in range(9):
            if (5 - index - 2 < x and x < index + 5):
                stackList.append("*")
            else:
                stackList.append(" ")
        pyramidList.append(stackList)
    return pyramidList
    pass
```
