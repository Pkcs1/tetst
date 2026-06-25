number = int(input("How many tests did you take: "))
n = 0
lists = []
while n != number:
    Score = int(input("Whats ur score: "))
    lists.append(Score)
    n += 1
average = (sum(lists)) / len(lists)
print(f"Your average score is {average}")