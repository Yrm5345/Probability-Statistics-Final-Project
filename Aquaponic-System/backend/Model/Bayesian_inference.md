# Intelligent Plants Watering System Mathematical Framework Documentation - Bayesian Inference

## Introduction

- We use Bayesian Inference (BI) in our Intelligent Plants Watering System to set hypothesis (Prior) probabilities for the Soil Moisture Level.
- It allows us to update the prior probability based on new information.

## Brief Background on Bayesian Statistical Inference

- Bayesian inferences about a parameter \(\theta\) or unobserved data \(\hat{y}\) are made in the form of probability statements conditioned on the observed data \(y\).

## Formulating Probability Statements

- To create probability statements about the parameter, we define the joint probability distribution of the parameter \(\theta\) and \(y\).

## Identifying the Sample Space

- Before determining the joint probability mass distribution, we need to first identify the type of sample space in the model. Since the probability of Soil Moisture Level could be any number within a range of infinite sample points, indicating a continuous space.

- Given the continuous space, the joint probability density function is expressed as the product of two densities:
  - The prior distribution (\(p(\theta)\))
  - The sampling distribution (\(p(y | \theta)\)):

  \[ P(\theta , y) = p(\theta) \cdot p(y | \theta) \]

Now we can condition the known value of the data \(y\) using the basic property of conditional probability. The conditional probability formula is given by:

\[ P(\theta | y) = \frac{P(y | \theta) \cdot P(\theta)}{P(y)} \]

In our case:


\[ P(\text{SML}_{\text{new}} | \text{data}) = \frac{P(\text{data} | \text{SML}_{\text{new}}) \cdot P(\text{SML}_{\text{new}})}{P(\text{data})} \]


**Components:**
- \(P(\text{SML}_{\text{new}} | \text{data})\): Posterior probability of soil moisture given new data.
- \(P(\text{data} | \text{SML}_{\text{new}})\): Likelihood of observing the data given the soil moisture.
- \(P(\text{SML}_{\text{new}})\): Prior probability of the soil moisture.
- \(P(\text{data})\): Probability of observing the data.


```python
import pymc3 as pm
import numpy as np

# Define the model
with pm.Model() as model:
    # Prior distribution for theta
    theta = pm.Uniform('theta', lower=0, upper=1)
    
    # Likelihood for observed data y
    y_observed = pm.Bernoulli('y_observed', p=theta, observed=data)
    
    # Sample from the posterior distribution
    trace = pm.sample(1000)

# Plot the posterior distribution
pm.plot_posterior(trace)
```

### Sources:

1. **Bayesian Data Analysis, Third Edition**
   
   - https://www.google.com/books/edition/Bayesian_Data_Analysis_Third_Edition/ZXL6AQAAQBAJ?hl=en&gbpv=1&printsec=frontcover

2. **PyMC3 Official Documentation:**
   - https://docs.pymc.io/

3. **Bayesian Methods for Hackers - Chapter 1 - Introduction to Bayesian Methods:**
   - https://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter1_Introduction/Ch1_Introduction_PyMC3.ipynb


4. **PyMC3 GitHub Repository:**
   - https://github.com/pymc-devs/pymc3


