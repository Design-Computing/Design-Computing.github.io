# Week 1 Lab: Python and Your Dev Environment

## Introduction

This week's lab is in two parts. One's administrative and the other's creative. But don't let that lull you into thinking that the first part is boring! Managing your dev environment is something you'll keep doing for your whole career. (_dev_ is short for _development_.) You can think of it like a chef choosing and sharpening their knives&mdash;it's a never ending process.

Part one will involve a lot of doing things without really knowing why. It'll be confusing, but it will get you going, then you can look back and understand.

Part two is a low-barrier-to-entry way to start flexing your computational thinking.

## Your dev environment

Part of your dev environment is going to be on your computer, and some of it will be in the cloud.

You'll hear us use the word _local_ to mean _on your computer_ and _remote_ to mean _in the cloud_.

### Cloud environment

**But first:** You might have an email address that's like `unicorn.sparkles@gmail.com` or `i_am_so_cool03@hotmail.com`. If you do, think about writing that on your CV. Do you want Norman Foster to read that?

Your email address, for better or worse, is your central identity. Don't use your university or work email address to sign up for things, you'll still be using your GitHub account long after you've severed ties with that organisation. Get a good personal email address, and look after it.

#### Get a GitHub account!

1. Go to [github.com](https://github.com/) and **Sign Up**.
2. Fill in your real name
3. Upload a photo of your face as your profile picture. We need this so that we can work out who you are.

Once you've done those steps, you can refresh this page and you should see yourself at the bottom!

#### Get a StackOverflow account!

1. Go to [stackoverflow.com](https://stackoverflow.com/) and **Sign Up**.

You'll need this to help you out. As a way of 'paying' for that help, it's good manners to upvote the questions and answers that you find useful. Being a programmer without SO is unthinkable!

### Steps to set up your dev environment

We'll go through this together, but if you need to setup a new dev environment then these are the steps:

1. Anaconda:

   1. Download anaconda from https://www.anaconda.com/distribution/#download-section get the Python 3.7 version
   1. Install it with default values _except_ tick the option to **Add Anaconda to my PATH**, tick that and the text will go red.
   1. Be patient
   1. Open anaconda navigator
   1. Click install on the VS Code box, be patient again

1. Git:

   1. Go to https://git-scm.com/downloads and download the latest git
   1. Install git with all the default values, except make vs code be the default editor

1. VS Code

   1. Open VS Code, bask in its glory
   1. Inside VS Code, type [ctrl]+[`] that's a backtick, it's to the left of 1 on most keyboards. That will pop up a section at the bottom of the screen. We'll call that your _terminal_.
   1. Your prompt should say something like:

      `C:\Users\ben>` except where mine says `ben` yours will say something else, maybe it'll be your name, maybe it'll be something boring?

      Whatever it is, now we need to write some magic spells.

1. Getting your content
   1. Type `mkdir 1161`
   1. Then `cd 1161`
   1. Then `git clone https://github.com/Design-Computing/CODE1161-2019 course`
1. Clone

   1. Go to https://github.com/Design-Computing/me and [fork](https://help.github.com/en/articles/fork-a-repo) yourself a copy of the _me_ repo
   1. Then, back in the terminal `git clone https://github.com/`_your name_`/me.git` We talked about it in the presentation.
   1. Now type `dir` you should get something that looks like:

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

   1. Now use cd (change directory) to move into the 'me' repo - type `cd me`
   1. Last thing here: Associate your fork with it's upstream version; that's the one you forked from. This means that if we make a change, you can pull it into your repo.

      ```
      git remote add upstream https://github.com/Design-Computing/me.git

      ```

      Now you've done that, you can do a `git pull upstream master` to get the latest changes. If you need to do this, we'll tell you about it.

1. Finish up

   1. Last thing: type `cd course` and then `./startup.bat` and press [enter] this will install some libraries and extensions that will make your life easier/more fun. If you've got a mac, call someone over to help.

1. Prepare your workspace.

   1. Get out a pen and notebook
   1. Take a deep breath
   1. Say "You've got this" to yourself
   1. Smile
   1. Go to `File`&rarr;`Open Folder` and then choose `me`
   1. Look at all those neat folder ready for you to work on!

1. Now you're ready to start the lab for real!

## My first programming

In this task you're going to do a full cycle of work.

1. Think
1. Test
1. Do
1. Save
1. Test
1. Commit
1. Push
1. Test

That's a lot to think about but it'll become easy soon. If we break that down individually:

![my dev environment setup](../pictures/vs_code_week_1.png)

This is how I set up my workspace for doing this kind of work. To split the screen, drag the tab all the way across to the right side of the screen.

#### Think

This is the _most_ important thing. Spending a long time doing the wrong thing is painful. So thinking means discussing with your peers, drawing diagrams, closing your eyes and dancing out the steps, whatever helps you understand.

Each week has a folder. It'll show up in the tree view on the left. We're in week 1, so look in the folder `week1`.

We're interested in `exercise1.py` and `readme.md` I like to have them both open at the same time.

In `exercise1.py` look at the instructions in the _doc-string_. That's the bit at the top of the file.

```
"""Your very first python program!

TODO: write a python script that first prints "Hello world!"
"""
```

Now do some thinking.

#### Test

In this course, at least to begin with, the tests are already written for you. They check if your code does what it's supposed to do. To run the tests, you write, at the terminal:

> `python ../course/week1/tests.py`

Then press enter.

Resist the urge to copy and paste this, you're going to be doing it a lot, and it'll be much better if you just learn to type it.

The test produce a lot of output, so you'll want to pull up your terminal; there's an up arrow (**^**) on the right that makes it get much bigger.

Most of your tests will fail. This is good because you haven't done any work yet!

#### Do

Now you do the work! This is going to be a back and forth with google, What we tell you in the lab, and conversations with yourself and your notebook.

#### Save

Save your work, it won't do anything otherwise.

#### Test

Again, write, at the terminal:

> `python ../course/week1/tests.py`

Then press enter.

What did the tests say? What passed? What didn't?

The last two tests this week can't pass until you've pushed.

#### Commit

TODO: get some screenshots in here

#### Push

TODO: get some screenshots in here

#### Test

Hopefully, for the last time, write, at the terminal:

> `python ../course/week1/tests.py`

Then press enter.

What happens? Do you need to go back a few steps and have another go? If you can get a full suite of green ticks, then move onto Trinket

## Then: Trinket

Computing is mainly a mindset, not a typing skill. That mindset doesn't really care about languages. Programmers love to argue about which language is better, but in reality they have more in common than you'd think. The ideas cross boundaries.

Syntax, the way we type letters to make words and symbols, easy to get wrong. Let's start with an environment that makes the syntax easier.

Have a play with [trinket.io](https://hourofpython.trinket.io/from-blocks-to-code-with-trinket#/blocks/dragging-and-dropping) , follow the tutorial, or just try making the first letter of your name with a turtle, or even both!

Put a link to your trinket results into your lab book (readme.md file).

### Homework

- Make sure that you have your dev environment set up.

- In the week1 folder, complete: - exercise1.py

- write your journal in README.md

  Check out [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) for an intro to how formatting works in markdown (`.md`) files.

- That means that if you kept up in class, no homework this week! It's a great chance to read some of the articles below. They won't teach you python, but they _will_ broaden your mind.

In theory, you can't get a full set of green ticks without everything going right. If you get all the ticks, then you have finished your homework. _Don't_ leave class if you don't have a full set of green ticks

### Readings

- **Graham, P.** (2009). _[Maker’s Schedule, Manager’s Schedule.](http://paulgraham.com/makersschedule.html)_
- **Case, N.** (2016). _[Simulating The World (In Emoji 😘).](http://ncase.me/simulating/)_
- **Davis, D.** (2015). _[Why Architects Can’t Be Automated.](http://www.architectmagazine.com/technology/why-architects-cant-be-automated_o)_
- **Doherty, B.** (2015). _[Architects getting automated?](https://notionparallax.co.uk/2015/architects-getting-automated)_
- **Noll, A. M.** (1967). _[The digital computer as a creative medium](http://noll.uscannenberg.org/Art%20Papers/Creative%20Medium.pdf)_. IEEE Spectrum, 4(10), 89–95.

# Slides

## Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRdspBdIJjboJldPB4KTL-HtZ6sCtNkBvgfuUsd0d50ZNb7fheGMSuTAZ8MGVeMi3QDbXEvWa5troYh/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Lab

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQFMw9WsAuZ43GoF3OGs1pCJq1NzEEgpp1GknWwRrFq1_qizdkPGAPZ-5Ar2mkDwkpflIWv0n2n6KLj/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

# Are you a Mac user?

Some things are different for you. Here's what to do:

### First, get some things working

Make sure you have VS Code, Git and Anaconda installed and working. You probably do already or you wouldn't know that things are astray.

You need to get a grasp of your file system. [This might be helpful to read](https://www.dummies.com/computers/macs/mac-operating-systems/basics-of-the-os-x-folder-structure/). I'll ask some mac people for advice on where to keep your `1161` folder.

To open a folder in Mac VS Code, there isn't a separate menu option, you just click _Open_ and then choose a folder instead of a file. This will make your version control work properly.

### The steps

1. You need to make VS Code be able to run as a command in your terminal.

   ![terminal access](../pictures/macShellAccess.png)

   To do this, type [cmd]+[shift]+[p]. This will open the command pallet. Then type `shell` which will narrow the commands down to three or four. Then pick **Terminal: Allow Workspace Shell Configuration**. This now means that you can launch VS Code from inside the folder that you want it to launch in. E.g. if I'm inside my `Me` folder, then you can type `code .` and it'll launch, all ready to work.

1. You can't run `startup.bat` because `bat`s are only for Windows; you need a `.sh`. There's a file called `startup.sh` all ready for you to use. It should install a bunch of things, and set some aliases so that when you type `python` it knows what you mean. To get it:

   - Open the `course` folder in VS Code. For Macs, there isn't an _open folder_ option, the OS doesn't force a distinction between files and folders, so go to _open_, click _course_ and then don't click a file. This feels tricky so it might take you a couple of goes.
   - Open your terminal by typing [ctrl]+[`] (that's a backtick, it's to the left of 1 on most keyboards). That will pop up the section at the bottom of the screen.

     Your prompt should say something like: `C:\Users\ben\course>`

   - type `git pull` and press enter
   - A little bit of text will scroll past, it will tell you about what's changed in the repo since you were there last.
   - type `bash startup.sh` and press enter
   - A _lot_ of text will start scrolling past.
   - When it has finished, type `python --version` it should say `Python 3.7.3` or at least `3.`.
   - If it does say that, then you are set!

1. run your tests by opening the `me` folder and typing `python ../course/week1/tests.py` in the terminal.

# General trouble shooting

## Git

To get a good grasp of how to use version control in VS Code, [this is a pretty good place to start](https://code.visualstudio.com/docs/editor/versioncontrol).

If your version control tab isn't showing a provider, check that you have your `Me` folder open.

![highlighting the me title](../pictures/meFolderOpen.png)

This means that the `me` folder is the active environment. There are fancy ways around this, but this is the easiest way to make it work.

If your git still seems to be totally broken, even if you're doing this, then you can try Zack's fix:

> The fix for the git problem on VSCode (windows only, haven’t checked if there’s a solution for it on Mac but Mac people had the same problem) was to get into the settings.json file (File&rarr;Preferences&rarr;Settings then scroll down until it says ‘edit settings.json’) and add:
>
> `"git.enabled": true;`
>
> `"git.path": "C:\\path\\to\\git.exe"`

I don't really know how this works yet because I haven't tried it myself.
