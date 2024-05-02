import numpy as np
import np.linalg.cholesky as cholesky

class ModelBase(object):
    def __init__(self, file):
        self._project_base(file)

    def _project_base(self, file):
        pzs = file['pzs']
        self.z = file['z']
        self.pz_mean = np.mean(pzs, axis=0)

    def get_parametrisation(self):
        raise NotImplementedError

    def evaluate_model(self, *args):
        raise NotImplementedError

    def save_parametrization(self):
        raise NotImplementedError

class ModelMoments(ModelBase):
    def __init__(self, file):
        self._project(file)

    def _project(self, file):
        self._project_base(file)
        self.pz_cov = np.cov(file['pzs'], rowvar=False)

    def evaluate_model(self, alpha):
        pz = self.pz_mean + cholesky(self.pz_cov) @ alpha
        return [self.z, pz]
    
    def get_parametrisation(self):
        return [self.pz_mean, self.pz_cov]

    def save_parametrization(self):
        raise NotImplementedError

class ModelShifts(ModelBase):
    def __init__(self, file):
        self._project(file)

    def _project(self, file):
        self._project_base(file)
        pzs = file['pzs']
        self.shifts = [self._find_shift(self.pz_mean, pz) for pz in pzs]
        self.shift_mean = np.mean(shifts)
        self.shift_std = np.std(shifts)

    def get_parametrisation(self):
        return [self.shift_mean, self.shift_std]

    def evaluate_model(self, shift):
        zs = self.z + shift
        return [zs, self.pz_mean]

    def _find_shift(self, mean_pz, pz):
        raise NotImplementedError

    def save_parametrization(self):
        raise NotImplementedError
