# Ultraplace

## Code Structure
![Ultraplace drawio](https://github.com/JaimeRZP/ultraplace/assets/39957598/35e41ed8-7c7f-42b2-a4ce-618a1f19bd1b)

## Goal
The goal of this project is two fold:
- On the one hand, we want to study the how different models for photometric uncertainty propagates to our theory predictions. 
- On the other hand, we want to study if the method used to marginalise over said uncertainties matters; i.e. can we get away with analytical marginalisation.
## Motivation

One of the leading contributions to the error budgets of cosmological analysis is the uncertainty in apparent redshifts of galaxies (also known as the radial galaxy distribution). This is particularly important when photometric catalogues, with course SED estimates, are used. Thus propagating said uncertainties to the final products of the analysis (cosmological constraints, ... etc) is paramount. 

The uncertainties in the radial distribution of galaxies is naturally expressed in the form of a statistical process. However, due the finite number of galaxies at a given position, the process is often discretised as a histogram with finite bins and an associated covariance matrix. The number of discrete bins is normally of order 10^2. This large number of parameters makes propagating their impact computationally prohibitive for traditional inference methods. Thus, cosmological analysis have so attempted to summarise the radial distribution in terms of far lower number of parameters (10^1). 
## Literature review
### Papers
- Analytic marginalization over CMB calibration and beam uncertainty *by Bridle et al* (0112114) - 2001
- Analytic Methods for Cosmological Likelihoods *by Taylor & Kitchin* (1003.1136) - 2011
- Self-calibration and robust propagation of photometric redshift distribution uncertainties in weak gravitational lensing *by Stölzner et al* (2012.07707) - 2021
- Analytical marginalisation over photometric redshift uncertainties in cosmic shear analyses *by Ruiz-Zapatero et al* (2301.11978) - 2023
### Photo-z Models
* **Shifts**: $$p(z + \Delta z)$$
* **Shifts & widths**: $$p(z_c + w_{z}(z-z_c) + \Delta z)$$
* **Eigen-functions**: $$p(z) = \sum_i^n \lambda_i \phi_i(z)$$
* **Comb**:  $$p(z) = \sum_i^{N_z} A_i \, \mathcal{N}(z; z_i, \sigma^2)$$
* **Full Histogram**: $$p(z) = \boldsymbol{n}$$
* **Neuronal Network**: $$p(z) = NN(\boldsymbol{\alpha})$$ 

### Stölzner vs Ruiz-Zapatero
|                  | Stölzner                                                            | Ruiz-Zapatero                                                                                                                                                           |  
| ---------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | 
| Photo-z model    | Comb                                                                | No model (full histogram)                                                                                                                                               |  
| Marginalisation  | Laplace Approximation                                               | Laplace approximation and HMC                                                                                                                                           |   
| Assumptions      | Nuisance posteriors are somewhat Gaussian (base Laplace assumption) | Nuisance posteriors are somewhat Gaussian (base Laplace assumption)                                                                                                     |   
|                  |                                                                     | Gaussian Likelihood                                                                                                                                                     |  
|                  |                                                                     | Photo-z's are tightly constraint such that their impact of the theory can be linearized                                                                                 |   
|                  |                                                                     | Gaussian priors for the Photo-z's                                                                                                                                       |    
| Final expression | $P(\Omega \| d) = P(d \| \Omega, n^*) + \ln(Det(F_{n^*}))$          | $P(\Omega \| d) = (d - t^*)^T \tilde{C}^{-1} (d-t^*) - 2 \ln P(\Omega) + \ln(Det(T^T C^{-1}T+C_n^{-1}))$ where $\tilde{C} = C + TC_nT^T$ and $T= \partial t/\partial n$ |    
| Advantages       | More general                                                        | Best-fit nuisance parameters can be found analytically                                                                                                                  |   
|                  |                                                                     | Laplace term simplifies to $\ln(Det(C_n^{-1}))$                                                                                                                         |    
|                  |                                                                     | Profile term amounts to including an extra contribution to the covariance.                                                                                                      |    
|                  |                                                                     | Faster                                                                                                                                                             |    
