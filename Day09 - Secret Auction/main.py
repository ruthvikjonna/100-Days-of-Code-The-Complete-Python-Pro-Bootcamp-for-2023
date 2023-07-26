import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the Secret Auction Program!")

bidding = {}
other_bidders = "yes"
while other_bidders != "no":
    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n$"))

    bidding[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls')

name = ""
highest_bid = 0
for key in bidding:
    if bidding[key] > highest_bid:
        name = key
        highest_bid = bidding[key]

print(f"The winner is {name} with a bid of ${highest_bid}!")
