import csv
import numpy as np # type: ignore
with open("data/fibonacci.csv", "w", encoding="utf-8") as f:
    tab=[1, 2, 3, 5, 8] 
    np.savetxt(tab)
    f.writerow(tab)
