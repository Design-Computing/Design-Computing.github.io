### Week 5 I/O

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/yx8qy-BseQg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. There are some running examples in `IOexamples.py`, read them, step through them, and you should have a pretty good idea of what to do in `exercise1.py`. You should be feeling pretty comfortable with how this process works by now.

1. Talk to a tutor about your open data project idea. Get started on the data audit process described below.

Here's an example of getting some json from the internet if you want to try it out:

```python

import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

r = requests.get(url)
if r.status_code is 200:
    the_json = json.loads(r.text)
    print(the_json)
    print(json.dumps(the_json, indent=4))
else:
  print(r)
```

## Jobs

What to do this week:

### Exercises

Do set 4 of the exercises.

It'd be really good to practice pair programming to work together on your exercises.
