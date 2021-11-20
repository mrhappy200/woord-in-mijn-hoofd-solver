def computer_guess():
    low = 0
    high = 25
    guess = (low+high)//2
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while 1 == 1:
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        a = input(f"is your letter between {abc[low]} and {abc[guess]}")
        if a == "Y":
            high = guess
            low1 = low + 1
            if guess == low1:
                print(f"the answer is {abc[guess]}")
                raise SystemExit()
        elif a == "N":
            if guess == low:
                print(f"the answer is {abc[guess]}")
                raise SystemExit()
            low = guess + 1



def main():
     computer_guess()

if __name__ == '__main__':
    main()