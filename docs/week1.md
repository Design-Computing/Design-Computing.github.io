# Week 1 Lab: Python and Your Dev Environment

## Introduction

This week's lab is in two parts. One's administrative and the other's creative. But don't let that lull you into thinking that the first part is boring! Managing your dev environment is something you'll keep doing for your whole career. (_dev_ is short for _development_.) You can think of it like a chef choosing and sharpening their knives&mdash;it's a never ending process.

Part one will involve a lot of doing things without really knowing why. It'll be confusing, but it will get you going, then you can look back and understand.

Part two is a low-barrier-to-entry way to start flexing your computational thinking.

## Your dev environment

Part of your dev environment is going to be on your computer, and some of it will be in the cloud.

You'll year us use the word _local_ to mean _on your computer_ and _remote_ to mean _in the cloud_.

### Cloud environment

**But first:** You might have an email address that's like `unicorn.sparkles@gmail.com` or `i_am_so_cool03@hotmail.com`. If you do, think about writing that on your CV. Do you want Norman Foster to read that?

Your email address, for better or worse, is your central identity. Don't use your university or work email address to sign up for things, you'll still be using your GitHub account long after you've severed ties with that organisation. Get a good personal email address, and look after it.

#### Get a GitHub account!

1. Go to [github.com](https://github.com/) and **Sign Up**.
2. Fill in your real name
3. Upload a photo of your face as your profile picture. We need this so that we can work out who you are.

Once you've done those steps, you can refresh this page and you should see yourself at the bottom!

#### Get a StackOverflow account!

### Steps to set up your dev environment

We'll go through this together, but if you need to setup a new dev environment then these are the steps:

1.  Go to https://git-scm.com/downloads and download the latest git
1.  Install git with all the default values, except make vs code be the default editor
1.  Download anaconda from https://www.anaconda.com/distribution/#download-section get the Python 3.7 version
1.  install it with default values _except_ tick the option to **Add Anaconda to my PATH**, tick that and the text will go red.
1.  Be patient
1.  Open anaconda navigator
1.  Click install on the VS Code box, be patient again
1.  Open VS Code, bask in its glory
1.  inside VS Code, type [ctrl]+[`] that's a backtick, it's to the left of 1 on most keyboards
1.  Your prompt should say something like:

    `C:\Users\ben>` except where mine says `ben` yours will say something else, maybe it'll be your name, maybe it'll be something boring?

1.  type `mkdir 1161`
1.  then `cd 1161`
1.  then `git clone https://github.com/Design-Computing/CODE1161-2019 course`
1.  Go to https://github.com/Design-Computing/me and fork yourself a copy of the _me_ repo
1.  then `git clone https://github.com/`_your name_`/me.git` We talked about it in the presentation.
1.  now type `dir` you should get something that looks like:

    ```
    C:\Users\ben\1161>dir

    01/06/2019  16:20    <DIR>          .
    01/06/2019  16:20    <DIR>          ..
    01/06/2019  16:20    <DIR>          course
    01/06/2019  16:20    <DIR>          org
    01/06/2019  16:20    <DIR>          me
                0 File(s)              0 bytes
                5 Dir(s)  308,818,493,440 bytes free

    C:\Users\ben\1161>
    ```

1.  Last thing: type `cd course` and then `./startup.bat` and press [enter] this will install some libraries and extensions that will make your life easier/more fun. If you've got a mac, call someone over to help.

1.  Now you're ready to start the lab for real!

In the last hour we will familiarise ourselves with each bit of software we have installed and what purpose it serves in the course. After that we will cover how to write your lab books and push them to GitHub.

### Then

Computing is mainly a mindset, not a typing skill. That mindset trinket.io if you have finished.

### Homework

- Ensure you have your dev environment set up.

- In the week1 folder, complete: - exercise1.py

- write your journal in README.md

  Check out [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) for an intro to how formatting works in markdown (`.md`) files.

- That means that if you kept up in class, no homework this week! It's a great chance to read some of the articles below. They won't teach you python, but they _will_ broaden your mind.

### Readings

<dd>
<p class="reference"><strong>Graham, P.</strong> (2009). <a href="http://paulgraham.com/makersschedule.html"><em>Maker’s Schedule, Manager’s Schedule.</em></a></p>
<p class="reference"><strong>Case, N.</strong> (2016). <a href="http://ncase.me/simulating/"><em>Simulating The World (In Emoji 😘).</em></a></p>
<p class="reference"><strong>Davis, D.</strong> (2015). <a href="http://www.architectmagazine.com/technology/why-architects-cant-be-automated_o"><em>Why Architects Can’t Be Automated.</em></a></p>
<p class="reference"><strong>Doherty, B.</strong> (2015). <a href="https://notionparallax.co.uk/2015/architects-getting-automated"><em>Architects getting automated?</em></a></p>
<p class="reference"><strong>Noll, A. M.</strong> (1967). <a href="http://noll.uscannenberg.org/Art%20Papers/Creative%20Medium.pdf">The digital computer as a creative medium</a>. IEEE Spectrum, 4(10), 89–95.</p>
</dd>
