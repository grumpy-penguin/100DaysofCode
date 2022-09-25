
PLACEHOLDER = "[name]"

with open(".\\Input\\Names\\invited_names.txt", mode="r") as names:
    for name in names.readlines():
        with open(".\\Input\\Letters\\starting_letter.txt", "r") as letter:
            for line in letter.readlines():
                with open(f".\\Output\\ReadyToSend\\letter_for_{name.strip()}.txt", mode="a") as invite:
                    invite.write(line.replace(PLACEHOLDER, name.strip()))
