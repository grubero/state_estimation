# state_estimation
Python script to calculate state estimation of a 3 bus network using Power Grid Model library. Node state values from the Power Grid Model library (https://power-grid-model.readthedocs.io/en/stable/examples/State%20Estimation%20Example.html)

By measuring power, voltage, and voltage angle at enough points on a network, all nodal and line currents can be calculated. Newton-Raphson convergence calculation method will solve partial differential equations in parallel to determine missing node values given sufficient known values are given. The real, reactive, and apparent power, and power-factor can then be calculated to give a state estimation of the network. 
![sdfdf](https://github.com/grubero/state_estimation/blob/main/3%20bus%20state%20estimation%20results.png)
