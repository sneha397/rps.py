# 🎮 Rock, Paper, Scissors - 2 Player Game

# User inputs (case-insensitive)
user1 = input("User 1 - Select your turn (rock, paper, scissors): ").lower()
user2 = input("User 2 - Select your turn (rock, paper, scissors): ").lower()

# Assigning choices
a = "paper"
b = "scissors"
c = "rock"

# Game logic
if user1 == a and user2 == b:
    print("1 mark for User 2")
elif user1 == b and user2 == c:
    print("1 mark for User 2")
elif user1 == c and user2 == a:
    print("1 mark for User 2")
elif user1 == b and user2 == a:
    print("1 mark for User 1")
elif user1 == c and user2 == b:
    print("1 mark for User 1")
elif user1 == a and user2 == c:
    print("1 mark for User 1")
elif user1 == user2:
    print("🤝 It's a tie!")
else:
    print("❌ Invalid input by one or both players.")
