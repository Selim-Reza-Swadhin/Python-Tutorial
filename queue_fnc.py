# FIFO -> first in first out

# bank = ["Selim","Reza","Swadhin","Anisul"]

from collections import deque

bank = deque(["Selim", "Reza", "Swadhin", "Anisul"])
print(bank)
bank.popleft()
print(bank)
bank.appendleft("Islam")
print(bank)

"""
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")
"""

