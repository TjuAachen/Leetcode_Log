class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_string = str(secret)[::-1]
        guess_string = str(guess)[::-1]
        guess_len = len(guess_string)
        num_bulls = 0
        record_secret = [0] * 10
        record_guess = [0] * 10
        for i, char in enumerate(secret_string):
            if i < guess_len and guess_string[i] == char:
                num_bulls += 1
            index = ord(char) - ord('0')
            record_secret[index] += 1
            
            index2 = ord(guess_string[i]) - ord('0')
            record_guess[index2] += 1
        total = 0
        for i in range(10):
            total += min(record_secret[i], record_guess[i])
        return str(num_bulls) + 'A' + str(total - num_bulls) + 'B'
            