# read_met_example.py
import numpy as np

def read_met(path):
    with open(path, 'r') as f:
        txt = f.read().strip()
    if txt == '':
        return np.array([])
    nums = [float(x) for x in txt.split()]
    return np.array(nums)

if __name__ == "__main__":
    path = "S01N001.GFD"  # mets ici le nom de ton fichier MET
    v = read_met(path)
    print("Vecteur lu (taille={}):".format(v.size))
    print(v)
