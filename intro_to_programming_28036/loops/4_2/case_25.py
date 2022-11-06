from math import gcd

def main():
    number = int(input("Enter a number: "))

    if number <= 0:
        print("Error: number has to be > 0.")
        return main()

    print(factorization(number))
    return 1

def factorization(n: int) -> list[int]:

    """
        Pollard's rho algorithm
        https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
    """

    factors = []

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors

if __name__ == '__main__':
    main()