# GitHub Codespaces

My computer is my favourite place to run code, but somebody else's computer is also great. GitHub has a thing called a codespace, that's a programming environment that they host. You can use it in your browser, which looks exactly like the VS Code on your computer, or you can use it _actually in_ your own VS Code on your computer.

We're going to switch to codespaces for the presentation becasue it's proving too dificult at the moment to get the presentations working on everyone's computer.

https://youtu.be/RwLpFlYQdOc

## Steps to get set up on a codespace

These are all in this video, I'l try to refer to the numbers below as I'm talking.

1. Make sure your project is _fully_ commited and pushed. The best way to do that is to check on the command line with `git status` and if it says anything other than

    ```
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

    Then you need to **commit** if you've got red or green text, and you need to **push** if it doesn't.

1. Once you've done that, go to github.com/\<your name>/\<your data project>, you can work that out! Then check that the last commit message is actually your last commit message.

1. Are you _absolutely_ sure that your repo is up to date on github?

1. You make a codespace by pressing the green **\[\<Code>▼\]** button, then..

1. Go to the _Codespaces_ tab. It'll say:

    No codespaces

    You don't have any codespaces with this repository checked out

    **Create codespace on main**

    Learn more about codespaces...

1. Click the green button that says **Create codespace on main**

1. Now we wait, sometimes for quite a long time (in the 5 minutes range)

1. Once your terminal has settles and it looks something like

    `@notionparallax ➜ /workspaces/DATAproject (main) $ `

    (that's mine, yours will look different because we have different names, of course!)

    _Take a deep breath_

1. ok, now we start doing things

1. The codespace comes with a lot of things already, like magic. So we don't need to install anything just now. We do need to do some maintainance. so run:

    `jupyter lab build`

    This will take another 5 minutes. Take this time to drink your tea.

1. Once it's finished, you can open jupyter lab, by running:

    `jupyter lab`

    A bunch of stuff will happen, then it'll get confused, and if you click around a bit, the screen will re-load. That's fine, just go with it.

1. A bunch more text will scroll past, what you need is these lines:

    ```
    [I 2023-08-09 16:47:59.582 ServerApp] Jupyter Server 2.6.0 is running at:
    [I 2023-08-09 16:47:59.582 ServerApp] http://localhost:8888/lab?token=3b1916738269224356b0a13467b130864f531896376ac892
    [I 2023-08-09 16:47:59.582 ServerApp]     http://127.0.0.1:8888/lab?token=3b1916738269224356b0a13467b130864f531896376ac892
    [I 2023-08-09 16:47:59.582 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 2023-08-09 16:47:59.619 ServerApp]

    To access the server, open this file in a browser:
        file:///home/codespace/.local/share/jupyter/runtime/jpserver-13143-open.html
    Or copy and paste one of these URLs:
        👉http://localhost:8888/lab?token=3b1916738269224356b0a13467b130864f531896376ac892 👈
        http://127.0.0.1:8888/lab?token=3b1916738269224356b0a13467b130864f531896376ac892
    ```

    You need to look out for the line that I've marked with the finger 👈

1. This is a link, but don't click it yet. You're going to need the token the first time you run a jupyter lab. The link looks like:
    ```
    http://localhost:8888/lab?token=3b1916738269224356b0a13467b130864f531896376ac892
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ```
    And the part above the ^^^s is the token. Highlight it and copy it (ctrl + c). This might sound obvious, but in case it doesn't, don't copy this one ☝, yours will be different.

1. Now click it. Except you can't just click, you need to crtl + click it. It will open a new tab. You might need to click a few times, it's temperamental.

1. Put the token into the box at the top of the screen

1. Now you're in jupyter lab!! _wheeee!_ Open your data file and check it out. Make sure it still runs. _But_ don't make any edits yet, you won't be able to save yet.

1. We need to add an extension to make it do presentations. It's called RISE, but there's a special once for jupyter lab, called _jupyterlab-rise_

1. But first we need to tell jupyter that we're ok with loading extensions. On the far left of the screen there's a jigsaw piece. Click it, then click the red **\[Yes\]** button.

1. In the search box at the top of that column, type `rise` and press enter. Only one option will come up, _jupyterlab-rise_. Click _install_

1. Once it says "Information: You will need to refresh the web page to apply the changes." you might actually going to have to go a lot further than that! Let's check. So click ok then refresh the page. If a little tiny icon that looks like an easel appears next to the tiny icon that looks like a bug, up in the top right corner, you're all good!

1. If you don't get that icon, get in touch with Ben and talk it through.

1. Open _another_ terminal. Type `jupyter trust <your_filename>.ipynb`

1. Close that terminal. You can now save your file.

1. On the far right, there is a pair of cogs and a bug. We need the cogs, then _COMMON TOOLS_. That'll give you some options for the type of cell you want to use.

1. When you click the little presentation icon to fire up the presentaiton, you'll get a `404 : Not Found` message. This is _annoying_. You need to close the tab. Then go back to your terminal and press \[ctrl + c] twice. That will stop the server. Then you need to restart it and get back to where you were. Then the presentation should work.

1. Each cell can either be a Slide, Sub-Slide, Fragment, Skip, or Notes. The easiest is slide, but look at the [RISE docs](https://rise.readthedocs.io/en/stable/usage.html#creating-a-slideshow) for an explanation.

1. You can tick _Render on Save_ and it'll update your changes when you save.
