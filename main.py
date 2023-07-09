# Strong knowledge of Amazon Web Services, particularly Elastic
# Beanstalk, EC2, RDS, SQS, S3, Codecommit, CodePipeline, and CodeDeploy

# Coin change Problem with Good time and space complexity
def coinChange(self, coins: list[int], amount: int) -> int:
    # dp[i] := fewest # Of coins to make up i
    dp = [0] + [amount + 1] * amount

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == amount + 1 else dp[amount]


def Task1(s):
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    ss = list(s)
    return ''.join([a.upper() if i == 0 or (i > 0 and ss[i - 1] == '_') else a.lower()
                    for i, a in enumerate(ss) if a.lower() in alpha])


if __name__ == '__main__':
    limit = 1_000_000
    my_list = ['apple', 'banana', 'cherry', 'date']
    print()
