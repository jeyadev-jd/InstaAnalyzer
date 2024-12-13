import instaloader
import json
from rich.console import Console
from rich.text import Text

console = Console()

username = 'your_username'  # Replace with your Instagram username
password = 'your_password'    # Replace with your Instagram password

L = instaloader.Instaloader()

try:
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, username)

    followers = set(profile.get_followers())
    following = set(profile.get_followees())

    with open("followers.json", "w") as f:
        json.dump([f.username for f in followers], f)

    with open("following.json", "w") as f:
        json.dump([f.username for f in following], f)

    with open("followers.json", "r") as f:
        followers_set = set(json.load(f))

    with open("following.json", "r") as f:
        following_set = set(json.load(f))

    mutual = followers_set.intersection(following_set)
    not_followed_back = followers_set - following_set

    console.print("=" * 40)

    heading = "          InstaAnalyzer          "
    author = "          by Jeyadev          "

    console.print(Text(heading, style="bold red"), justify="center")
    console.print(Text(author, style="bold blue"), justify="center")

    console.print("=" * 40)

    console.print(f"\nHello, {username}! Here are your results:\n", style="green")

    console.print("🔗 Mutual Followers:", style="blue")
    if mutual:
        for user in mutual:
            console.print(f"  - {user}", style="green")
    else:
        console.print("  - None")

    console.print("\n👥 Not Followed Back:", style="yellow")
    if not_followed_back:
        for user in not_followed_back:
            console.print(f"  - {user}", style="green")
    else:
        console.print("  - You follow everyone back!")

    console.print("\n" + "=" * 40
