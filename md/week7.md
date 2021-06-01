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

