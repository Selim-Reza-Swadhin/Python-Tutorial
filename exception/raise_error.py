print("Voter check")

n = int(input("Enter your age : "))


def voter(n):
    if n <= 18:
        raise ValueError("Invalid voter")
    return "You are allowed to vote"


# print(voter(n))

try:
    print(voter(n))
except ValueError as e:
    print(e)
