print("Number of times bob occurs is:", len([
    s[i : i + 3] for i in range(len(s) - 2)
    if s[i : i + 3] == 'bob'
]))