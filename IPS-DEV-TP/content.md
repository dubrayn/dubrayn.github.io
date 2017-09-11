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

# IPS-DEV-TP - Week #1

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

## Initialization
 * initialize a `git` project
 * structure the project
 * prepare the compilation chain
 * prepare the documentation generation
 * prepare the unit tests

:arrow_right: write a dummy program which only parses the CLI flags.

.center[:warning: Do not forget to push your commits ! :warning:]

---
# IPS-DEV-TP - Week #2

<div class="mermaid">
    graph LR
    A["Week #1<br/>Initialization"] --> B
    B["Week #2<br/>Project"] --> C
    C["Week #3<br/>Project"] --> D
    D["Week #4<br/>Project"] --> E
    E["Week #5<br/>Project"] --> F["Week #6<br/>Presentation"]
    style B fill:#9f9
    style F fill:#f9f
</div>

## Quantum Harmonic Oscillator
`$$\hat{H}_{(z)}\psi_n(z) = E_n\psi_n(z)$$`
with
`$$\hat{H}_{(z)}\equiv \frac{\hat{p_{(z)}}^2}{2m} + \frac{1}{2}m\omega^2\hat{z}^2$$`
and
`$$\hat{p}_{(z)}\equiv -i\hbar\frac{\partial}{\partial z}$$`

---
# Quantum Harmonic Oscillator
`$$\left(\frac{\hat{p}_{(z)}^2}{2m} + \frac{1}{2}m\omega^2\hat{z}^2\right)\psi_n = E_n\psi_n$$`

## Solutions:
`$$\psi_n(z) = \frac{1}{\sqrt{2^n n!}}\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-\frac{m\omega z^2}{2\hbar}}H_n\left(\sqrt{\frac{m\omega}{\hbar}} . z\right)$$`
with the usual Hermite polynomials (physicist version)
`$$H_n(z)\equiv (-1)^n e^{z^2} \frac{d^n}{dz^n}\left( e^{-z^2} \right).$$`

---
 * calculate HO 1D solutions (z-axis)
 * calculate HO 2D solutions (polar coordinates)
 * check `\(H|i\rangle=E_i|i\rangle\)`
 * numerically check `\(\langle i|j\rangle = \delta_{ij}\)`
 * calculate a cylindrical local density
 * calculate the Gauss-Hermite coefs.
 * calculate the Gauss-Laguerre coefs.
 * calculate some cylindrical multipole moments `\(\langle\psi|\hat{Q}_{\lambda 0}|\psi\rangle\)`
 * prepare presentation

---

## Week #6 - Evaluation
 * presentation [~15min] + questions [~10min]

---
# Evaluation




