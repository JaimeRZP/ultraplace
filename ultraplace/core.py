import numpy as np


def _TPT(J, P):
    return np.dot(np.dot(J, P), np.transpose(P))


def covmod(cov, bins):
    """
    Computes the modification to the data covariance matrix
    necessary to marginalise over photometric uncertainties.

    Parameters
    ----------
    dict : dict
        A dictionary containing the Jacobian and prior
        covariance matrix of each tomographic bin.

    Returns
    -------
    numpy.ndarray
        The modified data covariance matrix.
    """
    tpt = np.zeros(cov.shape)
    bin_keys = list(bins.keys())
    for bin in bin_keys:
        J = bins[bin]['J']
        P = bins[bin]['P']
        tpt += _TPT(J, P)
    return cov + tpt
