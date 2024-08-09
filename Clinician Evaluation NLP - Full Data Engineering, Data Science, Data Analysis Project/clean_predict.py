import numpy as np
import pandas as pd

rng = np.random.default_rng()

def categorize_pain(num):
    if num < 4:
        return 'mild'
    elif num < 8:
        return 'moderate'
    else: return 'severe'


# Function to guess length of stay is based on fusion type, ambulation distance, pain, and number of falls in the last 6 months
def guess_los(fusion, pain, amb_distance, num_falls):
    los = 0

    if fusion == 'lumbar':
        if amb_distance >50:
            if pain < 7:
                if num_falls <=1:
                    while (los < 2.5):
                       los = np.random.normal(loc = 2., scale = 1, size = None)
                    return np.round(los,1)
                while (los < 3.5):
                    los = np.random.normal(loc = 4., scale = 1.5, size = None)
                return np.round(los,1)
            while (los < 4.5):
                los = np.random.normal(loc = 6., scale = 2, size = None)
            return np.round(los,1)
        while (los < 5.5):
            los = np.random.normal(loc = 9., scale = 2.5, size = None)
        return np.round(los,1)


    else:
        if amb_distance >50:
            if pain < 7:
                if num_falls <= 1:
                    while (los < 1.5):
                       los = np.random.normal(loc = 1.5, scale = 1, size = None)
                    return np.round(los,1)
                while (los < 2.5):
                    los = np.random.normal(loc = 2.5, scale = 1, size = None)
                return np.round(los,1)
            while (los < 3.5):
                los = np.random.normal(loc = 4.5, scale = 1.5, size = None)
            return np.round(los,1)
        while (los < 5.5):
            los = np.random.normal(loc = 5.5, scale = 2, size = None)
        return np.round(los,1)


def guess_dc_loc(prior_loc, fusion, pain, amb_distance, num_falls):
    ## If the patient is admitted from a SNF, IRH, LTC, we expect they will return to that location.
    if prior_loc in (5, 6, 7):
        return prior_loc
    ## Lumbar fusions
    if fusion == 'lumbar':
        if amb_distance >50:
            if pain < 8:
                if num_falls <=1:
                    loc = np.random.choice([prior_loc, 6, 5], p=[0.90, 0.08, 0.02], size = None)
                    return loc
                loc = np.random.choice([prior_loc, 6, 5], p=[0.80, 0.15, 0.05], size = None)
                return loc
            loc = np.random.choice([prior_loc, 6, 5], p=[0.50, 0.35, 0.15], size = None)
            return loc
        loc = np.random.choice([prior_loc, 6, 5], p=[0.15, 0.55, 0.30], size = None)
        return loc

    ## Cervical fusions
    else:
        if amb_distance >50:
            if pain < 8:
                if num_falls <= 1:
                    loc = np.random.choice([prior_loc, 6, 5], p=[0.95, 0.04, 0.01], size = None)
                    return loc
                loc = np.random.choice([prior_loc, 6, 5], p=[0.80, 0.15, 0.05], size = None)
                return loc
            loc = np.random.choice([prior_loc, 6, 5], p=[0.70, 0.15, 0.15], size = None)
            return loc
        loc = np.random.choice([prior_loc, 6, 5], p=[0.30, 0.55, 0.15], size = None)
        return loc

def calc_rehab(dc_loc):
    if dc_loc in (5,6):
        return 1
    else:
        return 0