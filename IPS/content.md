class: titlepage leftm

.title[Introduction to Scientific Programming]

.subtitle[N. Dubray - ENSIIE - 2017]

`$$\int_{-\infty}^\infty f(x)e^{-x^2} dx \simeq \sum_{i=0}^{n-1}w_if(x_i)$$`

---
layout: true
class: middle animated fadeIn

.footnote[Introduction to Scientific Programming - N. Dubray - ENSIIE - 2017]

---
# Lecturer

## N. Dubray - `noel.dubray@cea.fr`
* *job:* researcher at the CEA (french nuclear agency)
* *field:* theoretical nuclear physics
* *research subject:* microscopic description of the fission process
* *skills:* scientist / developer / HPC user / sysadmin

.center.shadow.w50[![]($HOME$/images/density.png)]

---
# Modules

## :arrow_right: IPS: Introduction to Scientific Programming (S3)
* *IPS.DEV:* Scientific application development
* *IPS.PROD:* Scientific data production, post-processing and visualization

## :arrow_right: PSA: Advanced Scientific Programming (S4)
* *PSA.???:* TBA
* *PSA.???:* TBA

## Evaluation
* project report
* project presentation

## TPs timeline
<div class="mermaid">
    graph LR
    A["Week #1<br/>Initialization"] --> B
    B["Week #2<br/>Project"] --> C
    C["Week #3<br/>Project"] --> D
    D["Week #4<br/>Project"] --> E
    E["Week #5<br/>Project"] --> F["Week #6<br/>Presentation"]
    style A fill:#9f9
    style F fill:#f9f
</div>

---
# IPS.DEV - Project timeline

## Week #1 - Initialization
 * initialize a `git` project
 * prepare the compilation chain
 * prepare the documentation generation
 * prepare the unit tests
 * write an empty prog which only parses the CLI flags

## Weeks #2, #3, #4 ( :warning: overly optimistic schedule :warning: )
 * calculate HO cylindrical solutions
 * check `\(H|i\rangle=E_i|i\rangle\)`
 * numerically check `\(\langle i|j\rangle = \delta_{ij}\)`
 * calculate a cylindrical local density
 * calculate the Gauss-Hermite coefs.
 * calculate the Gauss-Laguerre coefs.
 * calculate some cylindrical multipole moments `\(\langle\psi|\hat{Q}_{\lambda 0}|\psi\rangle\)`

## Week #5
 * prepare report
 * prepare presentation

---
# Project rules

## Mandatory rules:
* the source must be in `C++11` and/or `Python`
* the source must be documented with `Doxygen`
* the compilation chain must be using `make`
* some unit tests will be imposed
* the project must be clean at each commit
* branches are OK but only master will be checked
* `phyton` bindings can be used, but are not mandatory
* presentation must be in the repository
* report must be in the repository

## :moneybag: Bonuses:
* no warning at {compilation, bindings, tests, doc}
* project is implementing other methods
* source code is easy to read
* commits are small and explicit
* unit tests pass
* report is written in `markdown` (cf. `pandoc`)
* presentation is written in `markdown` (cf. `remark.js`)
---
# Scientific method

.right-column.w20[![]($HOME$/images/wikipedia_logo.png)]

1. Define a question
2. Gather information and resources (observe)
3. Form an explanatory hypothesis
4. Test the hypothesis by *performing an experiment* and collecting data in a **reproducible manner**
5. Analyze the data
6. Interpret the data and draw conclusions that serve as a starting point for new hypothesis
7. **Publish results**
8. Retest (frequently done **by other scientists**)

:arrow_right: The scientific code must be shared with **HPC staff and other scientists**.

---
# Good development practices

## Make the code **easy to use**
 * Documentation
 * Compilation chain
 * Dependencies
 * Examples
 * Unit tests
 * Efficient code
 * Bindings

## Make the code **easy to read / extend**
 * Documentation (again)
 * Coding style guidelines
 * Well structured source / project
 * Useful comments
 * Versioning

---
# Good development practices

## Make the code **easy to use**
 * Documentation - *documentation generator*
 * Compilation chain - *build system*
 * Dependencies - *build system*
 * Examples - *no tool ?*
 * Unit tests - *unit testing framework*
 * Efficient code - *performance analysis tools*
 * Bindings - *binding generator*

## Make the code **easy to read / extend**
 * Documentation (again) - *documentation generator*
 * Coding style guidelines - *code formatting tool*
 * Well structured source / project - *UML design ?*
 * Useful comments - *commenting conventions*
 * Versioning - *version control system*

---
class: top

# Development tools

## Tools presented in this course
* version control system

--
  * `subversion`, `mercurial`, `CVS`, `SVN`, `Bazaar`, **`git`**

--
* build system

--
  * `Distutils`, `CMake`, `Autotools`, `qmake`, **`GNU Make`**

--
* documentation generator

--
  * `Sphinx`, `Docutils`, **`Doxygen`**

--
* unit testing framework

--
  * `*test*`, **`CxxTest`**

--
* code formatting tool

--
  * **`astyle`**, **`indent`**

--
* commenting conventions
  * various guidelines

--
* performance analysis tools
  * will be presented in PSA (S4)

--
* binding generator
  * will be presented in PSA (S4)

---
# Version control system: `git`

.center.w20[![]($HOME$/images/git_logo.png)]

## History
 * distributed version control system
 * created by **Linus Torvalds** in 2005 as free software (GPL v2)
 * initial goal: become the main VCS (Version Control System) of the **Linux kernel**
 * today: **#1 VCS** :v:

## Characteristics
 * strong support for non-linear development
 * distributed development
 * compatibility with existant systems and protocols
 * efficient handling of large projects
 * cryptographic authentication of history
 * toolkit-based design
 * pluggable merge strategies
 * garbage accumulates until collected
 * periodic explicit object packing

---
# `git` workflow

<div class="mermaid">
    sequenceDiagram
        Remote-->>+Local repo: git clone/pull
        Note over Staged: Empty
        Local repo->>Files: git checkout
        Note over Files: Code...
        Files->>+Staged: git add/rm
        Staged->>-Local repo: git commit
        Note over Files: Code...
        Files->>+Staged: git add/rm
        Staged->>-Local repo: git commit
        Local repo-->>-Remote: git push
</div>

---
# Creation of a `git` repo from scratch

.center[
<div data-dir='$HOME$/scripts/toto4' class='cinescript'></div>
]

---
# Main `git` commands

## Configure `git` (should be done once)
```shell
$ git config --global user.name "Your Name"
$ git config --global user.email you@yourdomain.example.com
```

## Create a local repo
```shell
$ git init
```

## Clone a remote repo (and create a local repo)
```shell
$ git clone http://some.domain.com/path/to/repo.git
```

## Get documentation
```shell
$ # Example: documentation for command 'git clone'
$ man git-clone
```
---
class: top
# Typical `git` workflow

## 1. clone or create repo
```shell
$ git clone http://some.domain.com/path/to/repo.git
```
--

## 2. make some changes
```shell
$ vim README.md # create new file
$ vim main.cpp  # edit existing file
$ rm toto.h     # remove existing file
```
--

## 3. **stage** changes
```shell
$ git add main.cpp README.md
$ git rm toto.h
```
--

## 4. check staged changes
```shell
$ git diff
$ git status
```
--

## 5. commit staged changes
```shell
$ git commit  # will open an editor to enter the commit message
$ git commit -m "Commit message"
```
---
# `git` history

## View project history (CLI)
```shell
$ git log
$ git log --draw --oneline --color
```

.center[
<div data-dir='$HOME$/scripts/toto5' class='cinescript'></div>
]

## View project history (GUI)
```shell
$ gitk
$ gitg
```
---
# GUI tool `gitk`

.shadow.center[
![]($HOME$/images/gitk_00.png)
]

---
# `git` branches

.right-column.w55[
 <canvas id='gitExample0'></canvas>
]

.left-column.w40[
## List branches
```shell
$ git branch
  dev
* main
```

## Create a branch
```shell
$ git branch dev
```

## Switch to a branch
```shell
$ git checkout dev
```

## Create + switch to a branch
```shell
$ git checkout -b dev
```

## Merge a branch
```shell
$ git merge dev
```

## Delete a branch
```shell
$ git branch -d dev
```
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto0'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.0**
* you start working on a new functionnality by creating a branch and commiting on it
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto1'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.0**
* you start working on a new functionnality by creating a branch and commiting on it
```shell
$ git checkout -b newfunc
$ # some work
$ git commit -m "Commit D"
...
$ # some work
$ git commit -m "Commit F"
```
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto2'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.0**
* you start working on a new functionnality by creating a branch and commiting on it
```shell
$ git checkout -b newfunc
$ # some work
$ git commit -m "Commit D"
...
$ # some work
$ git commit -m "Commit F"
```
* :warning: **issue #627 needs to be fixed**
* you create a branch to fix the issue
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto3'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.0**
* you start working on a new functionnality by creating a branch and commiting on it
```shell
$ git checkout -b newfunc
$ # some work
$ git commit -m "Commit D"
...
$ # some work
$ git commit -m "Commit F"
```
* :warning: **issue #627 needs to be fixed**
* you create a branch to fix the issue
```shell
$ git checkout master
$ git checkout -b fixit
$ # some work
$ git commit -m "Commit G"
...
$ # some work
$ git commit -m "Fixed issue #627"
```
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto4'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.0**
* you start working on a new functionnality by creating a branch and commiting on it
```shell
$ git checkout -b newfunc
$ # some work
$ git commit -m "Commit D"
...
$ # some work
$ git commit -m "Commit F"
```
* :warning: **issue #627 needs to be fixed**
* you create a branch to fix the issue
```shell
$ git checkout master
$ git checkout -b fixit
$ # some work
$ git commit -m "Commit G"
...
$ # some work
$ git commit -m "Fixed issue #627"
```
* you merge your fix in `master`
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto5'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.0**
* you start working on a new functionnality by creating a branch and commiting on it
```shell
$ git checkout -b newfunc
$ # some work
$ git commit -m "Commit D"
...
$ # some work
$ git commit -m "Commit F"
```
* :warning: **issue #627 needs to be fixed**
* you create a branch to fix the issue
```shell
$ git checkout master
$ git checkout -b fixit
$ # some work
$ git commit -m "Commit G"
...
$ # some work
$ git commit -m "Fixed issue #627"
```
* you merge your fix in `master`
```shell
$ git checkout master
$ git merge fixit
$ git tag v0.2.1 # lightweight tag
```
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto6'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.1**
* you can resume working on the new functionnality
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto7'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.1**
* you can resume working on the new functionnality
```shell
$ git checkout newfunc
$ # some work
$ git commit -m "Commit J"
```
* when you are ready, merge the new functionnality in the `master` branch
]

---
class: top
# How to use `git` branches

.right-column.w50[
 <canvas id='branchHowto8'></canvas>
]

.left-column.w45[
* SuperProg :copyright: is in state **v0.2.1**
* you can resume working on the new functionnality
```shell
$ git checkout newfunc
$ # some work
$ git commit -m "Commit J"
```
* when you are ready, merge the new functionnality in the `master` branch
```shell
$ git checkout master
$ git merge newfunc
$ git tag v0.3.0
```
]

---
# Remote repositories

<div class="mermaid">
    sequenceDiagram
        Remote-->>+Local repo: git clone/pull
        Local repo->>Files: git checkout
        Note over Files: Code...
        Files->>+Staged: git add/rm
        Staged->>-Local repo: git commit
        Local repo-->>-Remote: git push
</div>

## Declare a remote repo
```shell
$ git remote add farAway http://some.domain.com/path/to/repo.git
```

## Sync from remote repo
```shell
$ git fetch farAway && git merge
$ git pull farAway
```

---
# Conclusions on `git`

.right-column.w55[
 <canvas id='gitExample1'></canvas>
]

.left-column.w40[
## To sum up...
* very powerful tool, can be complex sometimes
* **can work offline !**
* rock-solid, very efficient
* **decentralized !**
* several source forges are using it (`github`, `bitbucket`, `gitlab`, etc...)
* learn a few commands and start using it !
* several ways to use it, *follow the guidelines*
* the de-facto standard CVS

.center.w50[![]($HOME$/images/git_logo.png)]
]

---
class: top

# Development tools

## Tools presented in this course
* version control system
  * `subversion`, `mercurial`, `CVS`, `SVN`, `Bazaar`, **`git`** :+:
* build system
  * `Distutils`, `CMake`, `Autotools`, `qmake`, **`GNU Make`**
* documentation generator
  * `Sphinx`, `Docutils`, **`Doxygen`**
* unit testing framework
  * `*test*`, **`CxxTest`**
* code formatting tool
  * **`astyle`**, **`indent`**
* commenting conventions
  * various guidelines
* performance analysis tools
  * will be presented in PSA (S4)
* binding generator
  * will be presented in PSA (S4)

---
# Build system: `GNU Make`

.center.w20[![]($HOME$/images/gnu_logo.png)]

## Key facts
* originally created by *Stuart Feldman* in April 1976 at Bell Labs
* part of the `GNU Autotools`
* allows to recompile **only the necessary files**
* has its own language to describe dependencies / actions
* allows a user to build a package **without knowing how it should be done**
* not limited to any particular language
* not limited to building packages
* required for compiling `gcc` since version 3.4.
* required for building the **Linux kernel**, Apache OpenOffice and LibreOffice, Mozilla Firefox...

---
# `GNU Make` workflow

## as a user
```shell
$ make
$ make install
```

## as a dev
```shell
$ # tweak the Makefile...
$ make clean
$ make docs
$ make tests
$ make debug
...
```
---
# Using `GNU Make`

## Makefile
```Makefile
target0: dep0 dep1 dep2
    command0
    command1
```
* a `Makefile` contains a set of rules
* a rule consists of a target, its dependencies, and the commands used to update it
* if not specified, `GNU Make` tries to update the first target of the default file `Makefile`
* for a given target to be updated, `GNU Make` checks which of its dependencies must be updated by checking their modification time
* if a target **does not exist or is older than some of its dependencies**, `GNU Make` tries to update it

## Example
<div class="mermaid">
    graph TD
    A[main.c]
    B[test.c]
    C[test.h]
    D[Makefile]
</div>

## Makefile
```makefile
main: main.c main.h
    gcc -o main main.c
```

---
# Writing clean Makefiles 

## Try to...
* use standard variable names (`CC`, `CFLAGS`, `LDFLAGS`, `PREFIX`, `TARGET`...)
* use standard target names (`all`, `install`, `clean`...)
* use generic rules (wildcards)

.left-column.w45[
## .center[Makefile]
```Makefile
CC = gcc
CFLAGS = -Wall
TARGET = main
OBJS = main.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $< -o $@

%.o: %.c %.h
	$(CC) $(CFLAGS) $< -c -o $@

.PHONY: clean

clean:
	rm -f $(OBJS)
	rm -f $(TARGET)
```
]

.right-column.w45[

## .center[Shell session]
```shell
$ make
gcc -Wall main.c -c -o main.o
gcc -Wall main.o -o main
$ make
make: Nothing to be done for `all'.
$ touch main.c
$ make
gcc -Wall main.c -c -o main.o
gcc -Wall main.o -o main
$ touch main.o
$ make
gcc -Wall main.o -o main
$ make clean
rm -f main.o
rm -f main
$ ls
main.c  main.h  Makefile
$
```
]

---
# Makefile wizardry


.left-column.w35[
## .center[Makefile]
```Makefile
CC = gcc
CFLAGS = -Wall
TARGET = main
OBJS = main.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $< -o $@

%.o: %.c %.h
	$(CC) $(CFLAGS) $< -c -o $@

.PHONY: clean

clean:
	rm -f $(OBJS)
	rm -f $(TARGET)
```
]

.right-column.w60[
## .center[Magic spell]
* replace by internal variable: `$(VAR)`
* replace by env. variable: `${VAR}`
* replace by target: `$@`
* replace by first dependency: `$<`
* target must always be updated: `.PHONY: target`

.center.w50[![]($HOME$/images/wizard.png)]
]

---
# Remaining tools










 * Makefile
 * doxygen
 * LaTeX
 * unit tests
* HPC project
 * overview (from idea to results)
 * applying
  * identify target supercomp
  * dimension the project
  * test the code 1 (scalability, benchmarks...)
  * example of an application
 * porting the code
  * supercomp overview (file system, modules, libs, compilers...)
  * preparatory access
   * test the code 2 (scalability, benchmarks...)
  * queues
  * restart mechanism
* scientific libraries
 * lapack
 * MKL
 * armadillo
* programming techniques
 * mix languages
 * python as a glue
  * bindings
 * quadratures
 * vectorization
 * loops optimization
* debug / profiling
 * gdb
 * valgrind
 * DIY timers
* data storage
 * mongoDB
 * MPI-IO
* post-processing
 * python + mongoDB
* data visualization
 * matplotlib
 * paraview
 * blender
 * POVRay

==== PSA ====

* IPS summary
* development tools
* scientific libraries
 * scalapack
 * magma
 * eigen
* programming techniques
 * errors / exceptions
 * OpenMP
 * MPI master / slaves
 * threads
 * live monitoring
  * API
	* JSON
* data visualization
 * VTK
 * paraview plugin
 * blender plugin

IPS project goals:

* initialize project (hierarchy of files, of classes, doxygen, Makefile, clean, git, cxxtest, data, bindings, README, LICENSE)
* derivate cylindrical HO solutions (LaTeX in doxygen), implement them, check H|p>=E|p>
* write C++ msgpack importer
* calculate the local density from a msgpack
* monitor the code performances with at least a simple timer
* num. calculate some <Q0m> values
* ana. calculate some <Q0m> values
* visualize local density in paraview, blender, povray, etc...
* use bindings in a MPI4py python script to calculate from mongoDB to ana. and num. <Q0m> values
* implement a transparent restart mechanism in the python script
* make a scalability benchmark, identify IO and CPU times
* write monitor server
* write monitor client

PSA project goals:

* initialize project (hierarchy of files, of classes, doxygen, Makefile, clean, git, cxxtest, data, bindings, README, LICENSE)
* derivate cylindrical HO solutions (LaTeX in doxygen), implement them, check H|p>=E|p>
* write C++ msgpack importer
* calculate the local density from a msgpack
* monitor the code performances with at least a simple timer
* calculate the local density from a msgpack
* num. calculate some <Q0m> values
* ana. calculate some <Q0m> values
* visualize local density in paraview, blender, povray, etc...
* use bindings in a MPI4py python script to calculate from mongoDB to ana. and num. <Q0m> values
* implement a transparent restart mechanism in the python script
* make a scalability benchmark, identify IO and CPU times

project rules:


