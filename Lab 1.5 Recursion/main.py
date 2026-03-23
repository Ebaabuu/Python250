from recursion import *

def main():
    print("***** TESTING POWER() *****")

    print(f"power(5, 0) = {power(5, 0)} [should be 1]")
    print(f"power(2, 9) = {power(2, 9)} [should be 512]")
    print(f"power(7, 6) = {power(7, 6)} [should be 117649]")
    print(f"power(0, 6) = {power(0, 6)} [should be 0]")
    print(f"power(10, -6) = {power(10, -6)} [should be 0]")

    print("\n***** TESTING SUM() *****")

    print(f"sum(0) = {sum(0)} [should be 0]")
    print(f"sum(17) = {sum(17)} [should be 153]")
    print(f"sum(100) = {sum(100)} [should be 5050]")
    print(f"sum(0) = {sum(0)} [should be 0]")
    print(f"sum(-2) = {sum(-2)} [should be 0]")

    print("\n***** TESTING DISPLAYSEQUENCE() *****")

    print("displaySequence(1, 1, 0):")
    displaySequence(1, 1, 0)
    print("\n[above should be blank]")

    print("\ndisplaySequence(1, 1, 15):")
    displaySequence(1, 1, 15)
    print("\n[above should be 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]")

    print("\ndisplaySequence(10, -2, 10):")
    displaySequence(10, -2, 10)
    print("\n[above should be 10 8 6 4 2 0 -2 -4 -6 -8]")
    
    print("\ndisplaySequence(-5, 1, 10):")
    displaySequence(-5, 1, 10)
    print("\n[above should be -5 -4 -3 -2 -1 0 1 2 3 4]")    

    print("\n***** TESTING SUMTHEDIGITS() *****")

    print(f"sumTheDigits(0) = {sumTheDigits(0)} [should be 0]")
    print(f"sumTheDigits(3) = {sumTheDigits(3)} [should be 3]")
    print(f"sumTheDigits(3201) = {sumTheDigits(3201)} [should be 6]")
    print(f"sumTheDigits(90160) = {sumTheDigits(90160)} [should be 16]")
    print(f"sumTheDigits(1122334455) = {sumTheDigits(1122334455)} [should be 30]")
    print(f"sumTheDigits(-5) = {sumTheDigits(-5)} [should be 0]")
    

if __name__ == "__main__":
    main()
