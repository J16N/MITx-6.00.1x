def alpha_order_substr(s):
    result = tmp = ''

    for i in range(len(s)):
        tmp += s[i]
        if len(tmp) > len(result): result = tmp
        if i > len(s) - 2: break
        if s[i] > s[i + 1]: tmp = ''

    return result

print("Longest substring in alphabetical order is:", alpha_order_substr(s))