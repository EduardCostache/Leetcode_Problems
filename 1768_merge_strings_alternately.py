def solution(word1, word2) -> str:
    output = ''

    word1_len = len(word1)
    word2_len = len(word2)

    shortest_word = min(word1_len, word2_len)

    for i in range(shortest_word):
        output += word1[i]
        output += word2[i]

    missing_letters = ''

    if(len(word1) > len(word2)):
        n_missing_letters = word1_len - shortest_word
        missing_letters = word1[-n_missing_letters:]
    elif(len(word1) < len(word2)):
        n_missing_letters = word2_len - shortest_word
        missing_letters = word2[-n_missing_letters:]

    return output + missing_letters

test1 = 'ab'
test2 = 'pq'

print(solution(test1, test2))