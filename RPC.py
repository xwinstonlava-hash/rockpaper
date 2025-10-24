import random
print("----Welcome to the game Rock Paper and Scissor----")

choices = ["Rock","Paper","Scissor"]
a = int(input("Enter the number of rounds you want to play:-"))

points = 0
for i in range(a):
    b = input("pick up Rock , Paper or Scissor")
    c= random.choice(choices)
    print(f"computer choices :{c}")

    if b==c:
        print("oh! it's a Tie.")
    elif(b == "rock" and c == "scissor") or \
        (b == "paper" and c == "rock") or \
        (b == "scissor" and c == "paper"):
        print("You Win!")
        points += 1
    else:
        print("You Lose!")

print("🎯 Total Points:", points)