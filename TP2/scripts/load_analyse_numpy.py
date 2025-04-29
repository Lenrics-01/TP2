
import numpy as np
tab=np.loadtxt("tes.out", delimiter=",")
print(f"la moyenne est {np.mean(tab)}")
print(f"le minimun est {np.min(tab)}")
print(f"le maximum est {np.max(tab)}")
