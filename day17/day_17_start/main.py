class User:

    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, username):
        username.followers += 1
        self.following += 1



user1 = User(
    "001",
    "grumpy-penguin"
    )

user2 = User(
    "002",
    "grumpy-donkey"
)

user1.follow(user2)

print(user1.following)
print(user1.followers)
print(user2.followers)
print(user2.following)
