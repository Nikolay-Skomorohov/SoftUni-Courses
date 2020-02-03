def palindrome(word, index):
    if word[index] == word[::-1][index]:
        if index == (len(word) - 1):
            return f"{word} is a palindrome"
        else:
            return palindrome(word, index + 1)
    else:
        return f"{word} is not a palindrome"
