# A primer to numerical simulations: The perihelion motion of Mercury
This is the script repository for an upcoming publication.

> **Abstract:** Numerical simulations are playing an increasingly important role in modern science.
In the [work](link) it is suggested to use a numerical study of the famous perihelion motion of the planet Mercury (one of the prime observables supporting Einsteins General Relativity) as a test case to teach numerical simulations to high school students.
The paper includes details about the development of the code as well as a discussion of the visualization of the results.
In addition a method is discussed how to estimate the size of the effect a priori that at the same time also can be employed to double check the results found numerically.

In this repository, we provide example scripts and templates which can be used by teachers and students to simulate, visualize and extract the perihelion motion of mercury caused by General Relativity.
The script files make use of the *Python* package [VPython](http://vpython.org/).

# Table of Contents

1. [Scripts](#scripts)
2. [Installation instructions and usage](#install)
	* [Installation instruction for Linux based systems and MacOS](#install-linux)
	* [Installation instruction for Windows systems](#install-windows)
4. [Credits](#credits)
5. [License](#license)

# <a name="scripts"></a> Scripts
The *Python* scripts can be found in directory [py-scripts](py-scripts/) and the *Jupyter Notebook* scripts in the directory [ipynb-scripts](ipynb-scripts/).

# <a name="install"></a> Installing and running VPython

Here, we briefly explain how to install *Python* and *VPython* on different operating systems.

For users familiar to *Python*, we recommend to `pip` install the `vpython` package for *Python3* (version number 3.5 or later).

## <a name="install-linux"></a> MacOS and other Linux systems

### Installing a Python distribution
All *Linux* based system come with an installation of *Python*.
Thus, if not already at the newest version, one just has to update existing installations.
This is best done by using a distribution manager.
Native to *Linux* based systems is for example **dpkg** and **apt-get**, or **Homebrew** and **MacPorts** for *MacOS*.
While *dpkg* and *apt-get* usually come with the *Linux* installations, *macOS* user must install such distribution managers at first.
For this we refer to [MacPorts](https://www.macports.org/install.php) or [Homebrew](https://brew.sh/).
As an alternative, one can also install [Anaconda](https://www.anaconda.com/download/#windows).
For this we refer to the [Windows installation](#install-windows)

As the start one should open a *terminal/console* (bash).
Depending on the installation, one usually needs superuser rights in order to update *Python*.
Therefore one has to prepend `sudo` to the following commands and confirm them by entering the superuser password.
The installations using a distribution manager are save and tested by the vast community.
In the following, the successive order of commands to update **Python** and install the *Python* package manager **Pip** is presented for *apt-get* (*Linux*) and *MacPorts* (*MacOS*), but are most similar for other distribution managers.

**Linux**
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

Depending on the previously installed packages, this command might install further dependencies automatically (after confirmation).
One should test if the installation was successful by typing `python3 --version` or `python3.6 --version` (depending on the installation name of *Python3*). This prints out the version of the *Python* installation (and should be larger than 3.5).

Next one must update the package manager to get the newest versions for *python* packages.
This is done by running
```bash
pip3 install --upgrade --user pip wheel
```
Depending on the installation name for *pip3*, one might has to exchange `pip3` &rarr; `pip3.6` (*MacPorts*).
This is best figured out by typing `pip` and pressing `tab`.
Note that this just upgrades the packages for the current *user*.
If one wants the *systemwide* installation, one again has to prepend `sudo` and can ignore the `--user` flag (`sudo pip3 install --upgrade pip wheel`).
Furthermore, depending on the installed version of \code{pip}, it could have a different name.

### Installing VPython
Finally, one can install **VPython** by running
```bash
pip3 install --user vpython
```

At this point, everything is installed and one can start the simulations.
To test the *VPython* installation one should run `python3` or equivalent commands depending on the installation name (e.g., `python3.6` on *MacPorts*) which starts an interactive *Python* console.

Next, one shall run 
```python
from vpython import *
box()
```
in the python console, which loads the *VPython* package and opens the default browser.
Running `box()` should generate a white box in the browser window, which can be rotated using the mouse.
The program is quit by running
```python
quit()
```
or pressing `Ctrl-c`.

### Running Python scripts
In general, there are multiple ways to run *Python* scripts.
For the sake of these simulations, we suggest two scenarios:

#### Python files
The first scenario to run *Python* scripts is that one writes and saves a *Python* file, e.g., `test.py`, which can be edited using any texteditor of choice.
	To run the *Python* script one must navigate the terminal to the containing folder using the `cd` command, e.g.,
```bash
cd ~/Desktop/
python3 test.py
```
Assuming the *Python* `test.py` is located in the directory `~/Desktop/`.
The command `cd` either takes relative paths (directories which are in the current directory), e.g., `cd folder`, or absolute paths beginning with a `/`, e.g., `cd /Users/name/Desktop/`.
Once one has navigated to folder which contains the `python` file (e.g., the file name is listed when typing `ls`), than one can type  execute the script.
Again, this script can be ended (if it does not end automatically) by pressing `Ctrl-c`.

#### Jupyter notebooks
The second scenario to run *Python* scripts is given by the interactive **iPython** or equivalently **Jupyter** notebooks.
To do so, one needs to install the package by running
```bash
pip3 install --user jupyter
```
in the console.
*Jupyter* notebooks are automatically installed when installing the newest version of *VPython*.

To start an interactive session, one has to run
```bash
jupyter notebook
```
in the console (or equivalent, depending on the installation name. Again, this can be figured out by typing `jupyter` and pressing `tab`).

If succesfull, this command will print a link (containing the name `localhost`) in the terminal.
Usually, this command will also automatically open the default internet browser at the link-address.
If not, one can simply copy and paste the printed name in the address bar of the browser of choice.
Within this browser window, one can freely navigate to the directory of choice and create interactive *Python* and *VPython* sessions by clicking on existing files or creating new ones (upper right button **new &rarr; vpython**).




## <a name="install-windows"></a> Windows installation

### Summary
In order to install *VPython* on *Windows*, one has to execute the following three steps:
1. Install **Python3**, e.g., via [Anaconda](https://www.anaconda.com/download/#windows).
2. Start the *Anaconda Prompt* application and run the command `conda update conda`.
3. Install **VPython** by running `conda install -c vpython vpython` in the *Anaconda Prompt*.

### Installing a Python distribution
As the first step, one must install **Python**, again there are several possibilities but we suggest [Anaconda](https://www.anaconda.com/) for an intuitive installation.
One has two possible (free) options, [Anaconda](https://www.anaconda.com/download/#windows) and [Miniconda](https://conda.io/miniconda.html).
Both are equally sufficient and one can install further updates after the initial installation.
One shall download the newest *Python 3.x* (with *x* greater equal 5) installer for *Windows* and the right system type (32-bit or 64-bit).
The system type can be found by pressing `Windows+I`, navigating to **System &rarr; About** and looking at the **System type** entry.

Installing one of the two executables creates a new *Windows* application called **Anaconda Prompt**.
Starting this application opens a terminal which will be used to install the required *python* packages.
At first, one should test if the *Anaconda* installation was successful by running the command 
```anconda prompt
conda list
```
This command should print a list of already installed packages.
Also, one should run
```anconda prompt
conda update conda
```
to make sure one has the most recent installation.

### Installing VPython
To install **VPython** one simply has to run
```anconda prompt
conda install -c vpython vpython
```
in the *Anaconda Prompt*.
The additional flag `-c vpython` tells *Anaconda* the *channel* where the *VPython* package can be found.
Running this command prints out a list of dependencies which will be automatically installed in order for *VPython* to work.
This must be confirmed.

### Additions
In principle this is already sufficient to run *VPython* scripts.
One could furthermore install *Anacondas* native navigator [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) by running 
```anconda prompt
conda install anaconda-navigator
```
This will install another application, *Anaconda Navigator*, which can be started from the Desktop and simplifies programming in *Python*.


### Running Python scripts
Again, there are several possibilities for running *Python* files on *Windows*.
* One could create a file `test.py`, edit it with an *Texteditor* of choice and specify to open the file with *Python3*.
	To do so, `right-click` on  the file, select **open with** and locate the **Anaconda Python3** installation.
	Programs can be closed by closing the running window.
*  One can run `python3` in the **Anaconda Prompt** application to start an interactive session.
	Programs can be closed by closing the running window.
	This commands executes the content of a *Python* file, if one appends the location of the file, e.g., `python3 test.py` (where the current working directory contains the file *test.py*).
* Start the **Anaconda Navigator** application, open an interactive **QT console** and program within the newly opened *QT* terminal.
	Programs can be closed by closing the running window.
*  Start the **Anaconda Navigator** application and click on the **Jupyter Notebook** button.
	This opens an interactive *Python* session in the default web-browser.
	Here, one can open existing *notebooks* or create new files (upper right button **new &rarr; vpython**).


To start and test the *VPython* installation one should pick any out of these options and execute the code
```python
from vpython import *
box()
```
Running this code should open the default browser and render a white box on black background.
Using the mouse (`right-click and drag`), one should be able to rotate the box.
It was found that the *Internet Explorer* is not able to properly render the animation.
Here, we suggest to use the, e.g., the *Firefox* web-browser as the default choice.

Once this test case works, one can start to test the Mercury orbit simulations.
We provide example files for both *Juypter Notebooks* and regular *Python* files.


# <a name="credits"></a> Credits
Authors:
* C. Körber
* I. Hammer
* J.-L. Wynen
* J. Heuer
* C. Müller
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
