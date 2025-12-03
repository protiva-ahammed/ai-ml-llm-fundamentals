

import numpy as np
from gradient_descent import Solution1
from linear_regression import Solution2


def main():
    print("Running problem :")
    solve = Solution2()
    print(solve.get_model_prediction (np.array([[0.37454012], [0.95071431], [0.73199394]]), 
                                      
                                      np.array([[0.59865848]])))

if __name__ == "__main__":
    main()