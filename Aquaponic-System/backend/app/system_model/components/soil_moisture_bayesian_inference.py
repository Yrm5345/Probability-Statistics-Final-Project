import pymc3 as pm
import numpy as np

class BayesianInference:
    """
    BayesianInference class for performing Bayesian inference on soil moisture data.

    Parameters:
    - data (numpy.ndarray): An array of observed soil moisture data (0 or 1).

    Attributes:
    - data (numpy.ndarray): The observed soil moisture data.
    - model (pymc3.Model): The PyMC3 Bayesian model.
    """

    def __init__(self, data):
        """
        Initialize the BayesianInference class.

        Parameters:
        - data (numpy.ndarray): An array of observed soil moisture data (0 or 1).
        """
        self.data = data
        self.model = self.create_bayesian_model()

    def create_bayesian_model(self):
        """
        Create the PyMC3 Bayesian model.

        Returns:
        - pymc3.Model: The PyMC3 Bayesian model.
        """
        with pm.Model() as model:
            """
            Prior Distribution: The prior distribution, or prior belief, is the hypothetical probability distribution assigned to a parameter 
            before observing any data. In our Bayesian model, we initially considered using a beta distribution, which is continuous.

            However, we opted for a uniform prior because we lacked prior information suggesting that certain values were more likely than others 
            within the parameter's range (0 to 1). The uniform distribution assumes that, before observing any data, all values of the parameter are equally likely.

            Resources: 
                - https://bayesiancomputationbook.com/markdown/chp_01.html
                - http://www.stat.columbia.edu/~gelman/book/
                
            """
            SML_prior = pm.Uniform('SML_prior', lower=0, upper=1)

            """
            The observed data represents the probability of SML_prior being 1 for wet and 0 for dry.
            We chose Bernoulli over binomial because the outcome of the event is required for only one time.

            Resources: 
                - https://medium.com/swlh/binomial-vs-bernoulli-distribution-dd9197c418d
            """

            data_likelihood = pm.Bernoulli('data_likelihood', p=SML_prior, observed=self.data)

        return model

    def sample_posterior(self, num_samples=1000, tune=1000, chains=2):
        """
        Sample from the posterior distribution.

        Parameters:
        - num_samples (int): The number of times to imagine a new reality.
        - tune (int): Adjustments made at the start to make the sampler perform better.
        - chains (int): The number of parallel universes to explore.

        Returns:
        - pymc3.backends.base.MultiTrace: A record of all the imagined realities.
        """
        with self.model:
            trace = pm.sample(num_samples, tune=tune, chains=chains)

        return trace

    def calculate_posterior_mean(self, trace):
        """
        Calculate the average belief about soil moisture.

        Parameters:
        - trace (pymc3.backends.base.MultiTrace): A record of all the imagined realities.

        Returns:
        - float: The average belief about soil moisture.
        """
        posterior_samples = trace['SML_prior']
        posterior_mean = np.mean(posterior_samples)
        return posterior_mean

    def run_inference(self):
        """
        Run Bayesian inference and find out the average belief about soil moisture.

        Returns:
        - float: The average belief about soil moisture.
        """
        trace = self.sample_posterior()
        posterior_mean = self.calculate_posterior_mean(trace)
        return posterior_mean



