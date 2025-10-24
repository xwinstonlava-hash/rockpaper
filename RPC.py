import random

print("🕹️ Welcome to Rock, Paper & Scissors Game! 🕹️\n")

choices = ["Rock", "Paper", "Scissor"]
rounds = int(input("Enter the number of rounds you want to play: "))
points = 0

for i in range(1, rounds + 1):
    print(f"\nRound {i}️⃣")
    player = input("Pick Rock, Paper, or Scissor: ").capitalize()
    computer = random.choice(choices)
    print(f"💻 Computer chose: {computer}")

    if player == computer:
        print("🤝 It's a Tie!")
    elif (player == "Rock" and computer == "Scissor") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissor" and computer == "Paper"):
        print("🎉 You Win!")
        points += 1
    else:
        print("😢 You Lose!")

print(f"\n🏆 Total Points: {points} / {rounds}")
