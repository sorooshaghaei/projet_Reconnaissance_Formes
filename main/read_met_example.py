# read_met_example.py
import numpy as np


# Generic Fourier Descriptor --> GFD
def read_met(path):
    with open(path, "r") as f:
        txt = f.read().strip()
    if txt == "":
        return np.array([])
    nums = [float(x) for x in txt.split()]
    return np.array(nums)


if __name__ == "__main__":
    path = "/Users/sorooshaghaei/Desktop/Cours_ParisCite_2025/master-1-vmi-main/S1/Introduction Reconnaissance des Formes/prj/projet_Reconnaissance_Formes/GFD/s01n001.GFD"  # mets ici le nom de ton fichier MET
    v = read_met(path)
    print("Read Vecteur (size={}):".format(v.size)) # These numbers are usually normalized, meaning they don’t depend on the size or position of the object — only on its shape.
    print(v)
