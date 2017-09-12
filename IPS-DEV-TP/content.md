class: titlepage leftm

.title[Introduction to Scientific Programming - TP :notebook: ]

.subtitle[IPS-DEV-TP - N. Dubray - ENSIIE - 2017]

`$$\int_{-\infty}^\infty f(x)e^{-x^2} dx \simeq \sum_{i=0}^{n-1}w_if(x_i)$$`

---
layout: true
class: top animated fadeIn

.footnote[IPS-DEV-TP - N. Dubray - ENSIIE - 2017]

---
# Project rules

<div class="mermaid">
    graph LR
    A["Week #1<br/>Initialization"] --> B
    B["Week #2<br/>Project"] --> C
    C["Week #3<br/>Project"] --> D
    D["Week #4<br/>Project"] --> E
    E["Week #5<br/>Project"] --> F["Week #6<br/>Presentation"]
    style F fill:#f9f
</div>

## Rules:
* the source **must be** written in `C++11` and / or `Python2`
* the source **must be** documented with `Doxygen`
* the compilation chain **must use** `GNU Make`
* presentation **must be** in the repository
* branches are OK but **only master will be checked**
* `phyton2` bindings can be used, but are **not mandatory**
* the presentation **must use** `remark.js`

## :moneybag: Bonuses:
* no warning at {compilation, bindings, tests, doc}
* project is implementing other methods
* source code is well written (comments, easy to read, etc...)
* commits are small and explicit
* unit tests pass

---

# IPS-DEV-TP - Initialization

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

## Start your project from scratch
 * create a **bare `git` project** on the remote server
 * clone this project locally
 * structure the project
 * prepare the compilation chain
 * prepare the documentation generation
 * prepare the unit tests

:arrow_right: write a dummy program which only parses the CLI flags.

.center[:warning: Do not forget to push your commits ! :warning:]

---
# IPS-DEV-TP - Project description

<div class="mermaid">
    graph LR
    A["Week #1<br/>Initialization"] --> B
    B["Week #2<br/>Project"] --> C
    C["Week #3<br/>Project"] --> D
    D["Week #4<br/>Project"] --> E
    E["Week #5<br/>Project"] --> F["Week #6<br/>Presentation"]
    style B fill:#9f9
    style C fill:#9f9
    style D fill:#9f9
    style E fill:#9f9
    style F fill:#f9f
</div>

## Summary
During this 5-week long project, solutions to the **1D quantum harmonic oscillator** will be calculated and some of their properties will be checked.

## Quantum Harmonic Oscillator
Schrödinger equation:
`$$\hat{H}_{(z)}\psi_n(z) = E_n\psi_n(z)$$`
with the 1D-Hamiltonian and 1D-momentum operator defined as
`$$\hat{H}_{(z)}\equiv \frac{\hat{p}_{(z)}^2}{2m} + \frac{1}{2}m\omega^2\hat{z}^2, \hspace{5mm}\hat{p}_{(z)}\equiv -i\hbar\frac{\partial}{\partial z}.$$`

---
# Quantum Harmonic Oscillator

## Resulting 1D-HO Schrödinger equation
`$$\left(\frac{\hat{p}_{(z)}^2}{2m} + \frac{1}{2}m\omega^2\hat{z}^2\right)\psi_n = E_n\psi_n.$$`

## Solutions:
The analytic solutions take the form
`$$\psi_n(z) = \frac{1}{\sqrt{2^n n!}}\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-\frac{m\omega z^2}{2\hbar}}H_n\left(\sqrt{\frac{m\omega}{\hbar}} . z\right).$$`

## Orthonormality
One has
`$$\forall (m,n), \int \psi^*_m(z)\psi_n(z) dz = \delta_{mn}.$$`

---
# Hermite polynomials

## Definition (physicists' version)

`$$\forall n\ge 0, H_n(z)\equiv (-1)^n e^{z^2} \frac{d^n}{dz^n}\left( e^{-z^2} \right).$$`

## Recurrence relation

One has
`$$H_0(z) = 1$$`
`$$H_1(z) = 2z$$`
`$$\forall n\ge 1, H_{n+1}(z) = 2zH_n(z)-2nH_{n-1}(z).$$`

---
# Project instructions

## Work to be done
 * implement the calculation of the 1D-HO solutions (along the z-axis, using recurrence formula)
 * evaluate and plot the first 1D-HO solutions (using xmgrace, matplotlib...)
 * numerically check the energy of the 1D-HO solutions (estimate the derivatives)
 * numerically check the orthonormality of the 1D-HO solutions (use a quadrature)
 * prepare a presentation using `remark.js`

## Presentation content
 * the structure of the project (choice of classes, files hierarchy, etc...)
 * the compilation chain (content of the Makefile)
 * the generated documentation
 * some code samples
 * the git history, and some commit messages
 * **the calculation results**

## :moneybag: Bonus
 * do the same for the 2D-HO solutions (polar coordinates)

---

## Week #6 - Evaluation
 * presentation [~15min] + questions [~10min]

---
# Evaluation




