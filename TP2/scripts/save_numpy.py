import csv
import numpy as np
tab=[1, 2, 3, 5, 8]
with open("data/fibonacci.csv", "w", encoding="utf-8", newline="") as f:
    writer=csv.writer(f,delimiter=",")
    writer.writerow(tab)
    np.savetxt("tes.out", tab, delimiter=",")
    
