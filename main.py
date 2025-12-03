

from gradient_descent import Solution


def main():
    print("Running problem :")
    solve = Solution()
    print(solve.get_minimizer(5, 0.001 , 3))

if __name__ == "__main__":
    main()