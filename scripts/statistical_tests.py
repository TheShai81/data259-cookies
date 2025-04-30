'''This file contains methods to execute pairwise statistical tests between proportions and means.
There are also options for Bonferroni correction.
All tests for pairwise have the following hypotheses:
$H_0$: $\mu_1 = \mu_2$ or $p_1 = p2$ <br/> 
$H_1$: $\mu_1 != \mu_2$ or $p_1 != p2$
'''

import scipy.stats as st

def p_value_Z(z_score: float, tails: int=2):
    '''
    Calculates the p-value from a z-score.

    Parameters:
        z_score (float): The calculated z-score.
        tails (int): The number of tails for the test (1 or 2, default is 2).

    Returns:
        float: The p-value.
    '''
    if tails == 1:
        p = st.norm.cdf(z_score)  # For one-tailed test
    elif tails == 2:
         p = 2 * (1 - st.norm.cdf(abs(z_score))) # For two-tailed test
    else:
        raise ValueError("tails must be 1 or 2")
    return p


def p_value_T(t_score: float, degrees_of_freedom: int, tails: int=2):
    '''
    Calculates the p-value from a t-score.

    Args:
        t_score (float): The calculated t-score.
        degrees_of_freedom (int): The degrees of freedom.
        tails (int, optional): Type of test, either 1 or 2. Defaults to 2.

    Returns:
        float: The p-value.
    '''
    if tails == 1:
        p = st.t.cdf(t_score, degrees_of_freedom)
    elif tails == 2:
        p = 2 * (1 - st.t.cdf(abs(t_score), degrees_of_freedom))
    else:
        raise ValueError("tails must be 1 or 2")
    return p


def two_prop_z_test(prop1: float, prop2: float, n1: int, n2: int, 
                    alpha: float = .05, bonferroni: int = 1):
    '''
    Executes a two-proportion z test on two proportions with optional Bonferroni correction.

    Parameters:
        prop1 (float): Proportion from sample 1.
        prop2 (float): Proportion from sample 2.
        n1 (int): Sample size for sample 1.
        n2 (int): Sample size for sample 2.
        alpha (float, optional): Significance level. Defaults to 0.05.
        bonferroni (int, optional): Number of comparisons for Bonferroni correction. 
                                    Defaults to 1 (no correction).

    Returns:
        tuple: z-score (float), p-value (float), result (str: 'reject' or 'fail to reject')
    '''
    corrected_alpha = alpha / bonferroni
    p_pool = (prop1 * n1 + prop2 * n2) / (n1 + n2)
    se = (p_pool * (1 - p_pool) * (1 / n1 + 1 / n2)) ** 0.5
    z = (prop1 - prop2) / se
    p = p_value_Z(z)
    result = 'reject' if p < corrected_alpha else 'fail to reject'
    return z, p, result


def two_sample_t_test(mean1: float, mean2: float, std1: float, std2: float,
                      n1: int, n2: int, alpha: float = .05, bonferroni: int = 1):
    '''
    Executes a two-sample t test on two means assuming unequal variances 
    (Welch's t-test), with optional Bonferroni correction.

    Parameters:
        mean1 (float): Mean of sample 1.
        mean2 (float): Mean of sample 2.
        std1 (float): Standard deviation of sample 1.
        std2 (float): Standard deviation of sample 2.
        n1 (int): Sample size of sample 1.
        n2 (int): Sample size of sample 2.
        alpha (float, optional): Significance level. Defaults to 0.05.
        bonferroni (int, optional): Number of comparisons for Bonferroni correction.
                                    Defaults to 1 (no correction).

    Returns:
        tuple: t-score (float), p-value (float), result (str: 'reject' or 'fail to reject')
    '''
    corrected_alpha = alpha / bonferroni
    se = ((std1 ** 2) / n1 + (std2 ** 2) / n2) ** 0.5
    t = (mean1 - mean2) / se

    df_num = ((std1**2) / n1 + (std2**2) / n2) ** 2
    df_denom = ((std1**2 / n1) ** 2) / (n1 - 1) + ((std2**2 / n2) ** 2) / (n2 - 1)
    df = df_num / df_denom

    p = p_value_T(t, df)
    result = 'reject' if p < corrected_alpha else 'fail to reject'
    return t, p, result
