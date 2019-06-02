# Week 1:

##Welcome to CODE1161 and Your dev environment

#### Introduction

- **An introduction to the world of computing** as it is in 2018. This should provide some context to what this course aims to teach and why.

- **Learning the 3 step** process that will help to start your journey as a problem solver.

- Setting up your development environment.

#### Requirements

- Please bring a portable computer to the lab as you will be setting up your dev environment.
- An open mind and a willingness to trade some privacy for automation of boring tasks and quicker processes.

#### Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTH0wxz0Vy61NXaS6g2Nmot2w0qhhOkz1km_2g2TnrLGRyB0OBOlELz6uQ6_Sh5FYWkffY_KKECBpgF/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Lab

Instructions:

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQED50HjjGZhZ8Nv_9m8dSij1-eVpzuT3jBh3Djd6axm6guCc0H9gWpk9OJwfSIfbIiwGOSPDDz75qG/embed?start=false&loop=false&delayms=60000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

Attempt exercises in trinket.io if you have finished.

In the last hour we will familiarise ourselves with each bit of software we have installed and what purpose it serves in the course. After that we will cover how to write your lab books and push them to GitHub.

1.  Download anaconda from https://www.anaconda.com/distribution/#download-section get the Python 3.7 version
1.  install it with default values _except_ tick the option to **Add Anaconda to my PATH**, tick that and the text will go red.
1.  Be patient
1.  Open anaconda navigator
1.  Click install on the VS Code box, be patient again
1.  Go to https://git-scm.com/downloads and download the latest git
1.  Install git with all the default values, except make vs code be the default editor
1.  restart vs code
1.  type [ctrl]+[`] that's a backtick, it's to the left of 1 on most keyboards
1.  Your prompt should say something like:
1.  `C:\Users\ben>` except where mine says `ben` yours will say something else, maybe it'll be your name, maybe it'll be something boring?
1.  type `mkdir 1161`
1.  then `cd 1161`
1.  then `git clone https://github.com/Design-Computing/CODE1161-2019 course`
1.  then `https://github.com/Design-Computing/courseOrg.git org`
1.  Go to https://github.com/Design-Computing/me and fork yourself a copy of the _me_ repo
1.  then `git clone https://github.com/`_your name_`/me.git`
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

1.  Last thing: type `cd course` and then `./startup.bat` and press [enter] this will install some libraries and extensions that will make your life easier/more fun

1.  Now you're ready to start the lab for real!

#### Homework

- Ensure you have your dev environment set up.
- In the week1 folder, complete: - exercise1.py - write your journal in README.md

#### Readings

<dd>
<p class="reference"><strong>Graham, P.</strong> (2009). <a href="http://paulgraham.com/makersschedule.html"><em>Maker’s Schedule, Manager’s Schedule.</em></a></p>
<p class="reference"><strong>Case, N.</strong> (2016). <a href="http://ncase.me/simulating/"><em>Simulating The World (In Emoji 😘).</em></a></p>
<p class="reference"><strong>Davis, D.</strong> (2015). <a href="http://www.architectmagazine.com/technology/why-architects-cant-be-automated_o"><em>Why Architects Can’t Be Automated.</em></a></p>
<p class="reference"><strong>Doherty, B.</strong> (2015). <a href="https://notionparallax.co.uk/2015/architects-getting-automated"><em>Architects getting automated?</em></a></p>
<p class="reference"><strong>Noll, A. M.</strong> (1967). <a href="http://noll.uscannenberg.org/Art%20Papers/Creative%20Medium.pdf">The digital computer as a creative medium</a>. IEEE Spectrum, 4(10), 89–95.</p>
</dd>

### Week 2: All of Python in three hours

#### Introduction

- This week we will get an overview of all the components of the Python syntax. Theoretically, you will be able to do **any** programming task after this week ;-).

- More details about the development environment.

- How to ask questions and the three step process to general problem solving.

#### Requirements

- A portable computer.
- List of questions from last week's lab
- Maybe some snacks for the lab. Keep it low GI if you can.

#### Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSJzgHnvLKcSJPt5nfXaz314GprB-fnuoHpLDdafF5Mn4STjs370X7lMdDhn0fZClijt9tDG_lBVOI1/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Lab

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR17tPHvj11C7pOFkuTTxZ_2rcepz0PHUOa8h_wnzTHTRPBoTBBCrgrZVjn5V3NcYDM-s-kmaVOLfzf/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Homework

- The first two readings
- homework exercises in week2 folder

#### Readings

https://automatetheboringstuff.com/#toc: chapters 1-5 Really awesome book
https://programminghistorian.org/lessons/getting-started-with-github-desktop: Clarification for the GitHub stuff

### Week 3: Useful Programs and Algorithms

#### Introduction

This week in the lecture we will cover loops, collections and functions and taking user input by building a hangman game.

#### Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQQvpQvKiZyXyKCck-vJxxY2N7ONCfv08Yy5AtpxSu_8zG47yVlDwAfkk1LbAWvanX2NKJV1e7KEGWt/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Lab

Instructions for week3:

- _pull from upstream/master_
- run _week3/setup.py_ to install required libraries
- start working through the lab exercises

#### Homework

- Khan Academy Algorithms Course: [https://www.khanacademy.org/computing/computer-science/algorithms](https://www.khanacademy.org/computing/computer-science/algorithms). 'Intro to Algorithms' and 'Binary Search' sections
- Lab book for week3x
- homework exercises in week3 folder

### Week 4: Dictionaries and File I/O

#### Introduction

This week in the lecture we will build on our hangman game by saving the highest scores and introducing a leader board.

#### Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ8BkNrDW08ySOr44rQSxrAeht7Avm6PXHclCuAdzUtLn1SMNO8oywMFJI4dKIN3k_rPKbXy0keXUVc/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Lab

Instructions:

- _pull from upstream/master_

#### Homework

- ensure you have completed all labs from week 1, 2, 3
- run through the hangman.py and understand what each line does.

### Week 5: More File I/O and the Internet

#### Introduction

This week we will extend on our hangman game by getting the word to guess from the internet.

#### Lecture

- go over saving and reading from file again
- what is JSON?
- reading stuff from the internet with programs
- recursion
- [add video link if we successfully manage to record it]

#### Lab

Instructions:

- _pull from upstream/master_
- run week4/setup.py
- complete week 4 file I/O exercises - run through the `hangman_leaderboard_word_from_internet.py` for some hints.
- complete week 5 refactoring and recursion exercises - You may need to look at other examples of recursion to develop a fuller understanding of how it works.

#### Homework Due 10/04/2018 @ 12pm

- ensure you have completed all labs from weeks 4 and 5
- lab books for both weeks
- Prepare for the programming exam on 17/04/2018 at 3pm.

### Week 6: Non-teaching week

### Week 7: Also non-teaching week

### Week 8: Exam

In the lectures we will revise what so far in preparation for the exam in the labs. After the exam we will start looking at the software project due in

#### Lab (exam)

Instructions:

- Promptly fire up your laptops
- At ~15:15, the exam will be pushed
- You will have 90 minutes to complete the exam, commit it and push it to your repository.

### Week 9: Machine Learning

#### Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRLNFC0gxS4xh2wztQmuwmPQkNmrNe4YLlYeoPOyGaTPc1sZIFL7PxSuJadvM4Cn1RyLRsEf2EgFNbV/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Lab

Machine learning assignment to be demonstrated on 1 May 2018 in the labs.

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQTErz4xhwXpQFJ9808NHSZZKrc3Rf_g_P8yXMdMkOSmzfUHeZdFGU5hzlcQ4e_F5tADRRn5ClyAldY/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

### Week 10: OpenData Introduction

#### Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTXNkJCGDstDeRNc_jbHt7Y-TO1-Fj_oB1taSWwtrksUfr1RhRYwK5RmrcueLtly4EFFjoZSc9s0faB/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Lab

While we are marking the projects:

- Create a Kaggle account - Fork this: https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners - Run: - up to the start of 2. Python Data Science Toolbox - 3.Cleaning Data - 4.Pandas Foundation. - 5.Manipulating Data Frames with Pandas. - Absorb all the possibilities of these tools
- Start looking for data and thinking about a question you want to answer
- Get first hand experience using pandas and visualisation skills.
  https://www.kaggle.com/residentmario/welcome-to-data-visualization

#### Homework

- Pull from upstream to get the latest lab books
- Complete the lab book in the week10 folder
- Get acquainted with pandas and matPlotLib
- Research what questions you would like to answer and datasets.

### Week 11: OpenData: Deciding on a dataset and topic

#### Lecture

Guest Lecture: Rachel Bunder, Data Scientist at Solar Analytics

#### Lab

- Decide on a dataset or question. Might be worthwhile doing some quick exploratory data analyses.
- Going deeper with pandas and matPlotLib

#### Homework

- Complete this form by next Tuesday 15 May @ 12pm. These results will be used in the marking sheet. <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeG8uQ6mCdnHlZcxFKL8--oLQrL35L-nFRwH5EbswPRZ-tmhw/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
- lab book in week11 folder

### Week 13: Final Week–Review

#### Lecture

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTc32kGt2vOuBBrpFEnwyaQHruLYWBeTCXfpvtlK0HjrGT7ndC8RGlRp8e1PsJA-MecHa6GGuJoZfUz/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

#### Lab

- OpenData Project

#### Homework

- None, you're free now.
