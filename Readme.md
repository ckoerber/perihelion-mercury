# A primer to numerical simulations: The perihelion motion of Mercury

This is the script repository for [this publication](https://arxiv.org/abs/1803.01678).

> **Abstract:** Numerical simulations are playing an increasingly important role in modern science.
In this work it is suggested to use a numerical study of the famous perihelion motion of the planet Mercury (one of the prime observables supporting Einsteins General Relativity) as a test case to teach numerical simulations to high school students.
The paper includes details about the development of the code as well as a discussion of the visualization of the results.
In addition a method is discussed how to estimate the size of the effect a priori. Which allows to double check the results found numerically.

In this repository, we provide example scripts and templates which can be used by teachers and students to simulate, visualize and extract the perihelion motion of Mercury caused by General Relativity.
The programs are available in two flavors, plain *Python* scripts in [py-scripts](py-scripts/)
and corresponding *Jupyter Notebooks* in [ipynb-scripts](ipynb-scripts/).

![Simulation screenshot: Mercury orbit](https://www.ckoerber.com/media/misc/perihelion.jpg "Simulation screenshot: Mercury orbit")


# Table of Contents

1. [Requirements](#requirements)
2. [Installation instructions](#install)
	* [Installation under Linux and MacOS](#install-unix)
	* [Installation under Windows](#install-windows)
3. [Running the scripts](#running)
3. [Credits](#credits)
4. [License](#license)


# <a name="requirements"></a> Requirements
- Python 3.5 or later
- [VPython](http://vpython.org/), version 7 or later (tested with 7.3.2)
- (*optional*) [Jupyter](http://jupyter.org/)


# <a name="install"></a> Installing and running VPython

Here, we explain how to install *Python* and *VPython* on different operating systems.

For users familiar with *Python*, we recommend to `pip install` the `vpython` package for *Python3* (*Python3* version number 3.5 or later).


## <a name="install-unix"></a> Linux and MacOS

### Installing a Python distribution
All *Unix* based system come with an installation of *Python*.
In case this is *Python 2*, a version of *Python 3* needs to be installed.
If you already have *Python 3* installed, you can skip to **Installing VPython**.

The best way to install *Python 3* is to use your distributions package manager,
e.g. **dpkg** or **apt-get** on *Linux*, or **Homebrew** or **MacPorts** on *MacOS*.
While *Linux* usually comes with a package manager preinstalled, *macOS* users must install them first.
For this we refer to [MacPorts](https://www.macports.org/install.php) or [Homebrew](https://brew.sh/).
As an alternative, one can also install [Anaconda](https://www.anaconda.com/download/#windows).
This is decribed in [Installation under Windows](#install-windows)

You can use the graphical interface of your package manager, if it has one, or use the terminal.
Here, we give instructions for installing *Python* via the terminal.
Depending on the installation, one usually needs superuser rights in order to update or install *Python*.
Therefore one has to use `sudo` in the following commands and confirm them by entering the superuser password.
The installations using a distribution manager are save and tested by vast communities.
In the following, the successive order of commands to update **Python** and install the *Python* package manager **Pip** is presented for *apt-get* (*Ubuntu*) and *MacPorts* (*MacOS*).
Other package managers use similar commands.

**Ubuntu**
```bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
```
**MacOS**
```bash
sudo port selfupdate
sudo port install python36
sudo port install py36-pip
```

Depending on the previously installed packages, further dependencies might be installed automatically (after confirmation).
One should test if the installation was successful by typing `python3 --version` or `python3.6 --version` (depending on the installation name of *Python3*). This prints out the version of the *Python* installation (and should be larger than 3.5).

Next one must update the package manager to get the newest versions of *Python* packages.
This is done by running
```bash
pip3 install --upgrade --user pip wheel
```
Depending on the installation name for *pip3*, one might have to exchange `pip3` &rarr; `pip3.6` (*MacPorts*).
This is best figured out by typing `pip` and pressing `tab`.
Note that this just upgrades the packages for the current *user*.
If you want the *systemwide* installation, prepend `sudo` and remove the `--user` flag (`sudo pip3 install --upgrade pip wheel`).

### Installing VPython
Finally, install **VPython** by running
```bash
pip3 install --user vpython
```
Again, leave our `--user` and add `sudo` to get a *systemwide* installation.

At this point, everything is installed and one can start the simulations.
To test the *VPython* installation, run `python3` or equivalent commands depending on the installation name (e.g., `python3.6` on *MacPorts*) to start an interactive *Python* console.

Next run
```python
from vpython import *
box()
```
in the *Python* console, which loads the *VPython* package and opens the default browser.
Running `box()` should generate a white box in the browser window, which can be rotated using the mouse.
Quit the program by running
```python
quit()
```
or pressing `Ctrl-c` in the terminal.


## <a name="install-windows"></a> Windows installation

### Summary
In order to install *VPython* on *Windows*, one has to execute the following three steps:
1. Install **Python3**, e.g., via [Anaconda](https://www.anaconda.com/download/#windows).
2. Start the *Anaconda Prompt* application and run the command `conda update conda`.
3. Install **VPython** by running `conda install -c vpython vpython` in the *Anaconda Prompt*.

### Installing a Python distribution
As the first step, one must install **Python**. There are several possibilities but we
suggest [Anaconda](https://www.anaconda.com/) for an intuitive installation.
There are two possible (free) options, [Anaconda](https://www.anaconda.com/download/#windows) and [Miniconda](https://conda.io/miniconda.html).
Both are equally sufficient and one can install further updates after the initial installation.
Download the newest *Python 3.x* (with *x* greater equal 5) installer for *Windows* and the right system type (32-bit or 64-bit).
The system type can be found by pressing `Windows+I`, navigating to **System &rarr; About** and looking at the **System type** entry.

Installing one of the two executables creates a new *Windows* application called **Anaconda Prompt**.
Starting this application opens a terminal which will be used to install the required *python* packages.
At first, one should test if the *Anaconda* installation was successful by running the command
```anconda_prompt
conda list
```
This command should print a list of already installed packages.
Also, run
```anconda_prompt
conda update conda
```
to make sure you have the most recent installation.

### Installing VPython
To install **VPython**, simply run
```anconda_prompt
conda install -c vpython vpython
```
in the *Anaconda Prompt*.
The additional flag `-c vpython` tells *Anaconda* the *channel* where the *VPython* package can be found.
Running this command prints out a list of dependencies which will be automatically installed in order for *VPython* to work.
The installation of any extra packages has to be confirmed.

To test the *VPython* installation, launch the **Anaconda Prompt**, enter `python3` to start
*Python* and enter
```python
from vpython import *
box()
```
This should open the default browser and render a white box on black background.
Using the mouse (right-click and drag), one should be able to rotate the box.
The *Internet Explorer* was found to not be able to properly render the animation.
You can use *Firefox* or any other modern browser of you choice.

### Additions
In principle this is already sufficient to run *VPython* scripts.
You could furthermore install *Anacondas* native navigator [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) by running
```anconda_prompt
conda install anaconda-navigator
```
This will install another application, *Anaconda Navigator*, which can be started from the Desktop and simplifies programming in *Python*.


# <a name="running"></a> Running the scripts

In general, there are multiple ways to run *Python* scripts.
We provide instructions for both *Python* script files and *Jupyter* notebooks.

## Linux and MacOS

#### Python files
The first scenario is to write a *Python* file, e.g., `test.py`, which can be edited
using any text editor of choice.
To run the *Python* script, navigate to the containing folder in the terminal using the
`cd` command and execute the script in the interpreter, e.g.,
```bash
cd ~/Desktop/
python3 test.py
```
Assuming the `test.py` is located in the directory `~/Desktop/`.
The command `cd` either takes relative paths (directories which are in the current
directory), e.g., `cd folder`, or absolute paths beginning with a `/`,
e.g., `cd /Users/name/Desktop/`.
Once in the folder which contains the *Python* file (e.g., the file name is listed
when typing `ls`), the file can be executed using the interpreter (command `python3 filename.py`).
Again, this script can be ended (if it does not end automatically) by pressing `Ctrl-c`.

#### Jupyter notebooks
The second scenario to run *Python* scripts is using the interactive **iPython** (or equivalently **Jupyter**) notebooks.
For this, you need to install the package first by running
```bash
pip3 install --user jupyter
```
in the console.
*Jupyter* notebooks are automatically installed when installing the newest version of *VPython*.

To start an interactive session, one has to run
```bash
jupyter notebook
```
in the console (or equivalent, depending on the installation name.
Again, this can be figured out by typing `jupyter` and pressing `tab`).

If succesfull, this command will print a link (containing "localhost")
in the terminal. Usually, this command will also automatically open the default
internet browser at the link-address. If not, one can simply copy and paste the
printed link in the address bar of the browser of choice. Within this browser window,
one can freely navigate to the directory of choice and create interactive *Python* and
*VPython* sessions by clicking on existing files or creating new ones
(upper right button **new &rarr; vpython**).


## Windows

There are several possibilities for running *Python* scripts on *Windows*.
Here we provide instructions based on an Anaconda installation.
* Create a file `test.py`, edit it with a text editor of choice and specify to open the file with *Python3*.
    To do so, `right-click` on  the file, select **open with** and locate the **Anaconda Python3** installation.
    Programs can be closed by closing the running window.
* Run `python3` in the **Anaconda Prompt** application to start an interactive session.
    Programs can be closed by closing the running window.
    This command executes the content of a *Python* file, if one appends the location of the file, e.g., `python3 test.py` (where the current working directory contains the file *test.py*).
* Start the **Anaconda Navigator** application, open an interactive **QT console** and program within the newly opened *QT* terminal.
    Programs can be closed by closing the running window.
* Start the **Anaconda Navigator** application and click on the **Jupyter Notebook** button.
    This opens an interactive *Python* session in the default web-browser.
    Here, one can open existing *notebooks* or create new files (upper right button **new &rarr; vpython**).


# <a name="credits"></a> Authors
* C. Körber
* I. Hammer
* J.-L. Wynen
* J. Heuer
* C. Müller
* C. Hanhart


# <a name="license"></a> License
MIT License

Copyright (c) 2018 Christopher Körber

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
