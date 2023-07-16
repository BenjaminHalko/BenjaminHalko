def format_leaderboard(leaderboard):
    top_moves = sorted([[moves, user] for user, moves in leaderboard.items()], key=lambda x: x[0])
    value = "| Moves | User |\n| :-: | :-: |\n"
    for moves, user in top_moves[:10]:
        value += f"| {moves} | [ @{user}](https://github.com/{user}) |\n"
    return value

def format_history(history):
    value = "| Move | User |\n| :-: | :-: |\n"
    for moves, user in history:
        value += f"| {moves} | [ @{user}](https://github.com/{user}) |\n"
    return value

def format_stats(stats):
    value = "| Stat | Value |\n| :-: | :-: |\n"
    for stat, val in stats.items():
        value += f"| {stat} | {val} |\n"
    return value

def updateReadme(name, ID, info, board, leaderboard, history, stats):
    readme = ""
    with open("README.md", "r") as f:
        readme = f.read()
    readme = readme.split(f"<!-- {ID} -->\n")
    readme[1] = f"""<details align="center" open><summary><h2>{name}</h2></summary><p>
<table align="center">
<tr></tr>
<tr><td>
<p align="center">{info}</p><p>

{board}<details align="left"><summary><h3>History of moves for this game</h3></summary><p>

{format_history(history)}</details>

<details align="left"><summary><h3>Top 10 most active players</h3></summary><p>

{format_leaderboard(leaderboard)}</details>

<details align="left"><summary><h3>Stats</h3></summary><p>

{format_stats(stats)}</details>
</td></tr>
</table>
</details>
"""
    readme = f"<!-- {ID} -->\n".join(readme)
    with open("README.md", "w") as f:
        f.write(readme)