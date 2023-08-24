# Strong knowledge of Amazon Web Services, particularly Elastic
# Beanstalk, EC2, RDS, SQS, S3, Codecommit, CodePipeline, and CodeDeploy
from collections import OrderedDict


def do_something(skit, log, *low, gos=None, **pois):
    # gos is a KeyWord parameter
    pass


def unique_names(names1: [], names2: []):
    return list(set(names1 + names2))


def sort_csv_columns(csv_data: str) -> str:
    rows = csv_data.split('\n')
    columns = rows[0].split(',')
    data = [[] for i in range(len(columns))]
    for i in range(1, len(rows)):
        values = rows[i].split(',')
        for j in range(len(values)):
            data[j].append(values[j])
    sorted_data = [x for _, x in sorted(zip(data[0], data))]
    for i in range(len(sorted_data)):
        row = ''.join(sorted_data[i])
        print(row)


def count_change(amount, coins: [int]):
    n = len(coins)
    table = [[0 for x in range(n)] for x in range(amount + 1)]
    # initialize table with base case values
    for i in range(n):
        table[0][i] = 1
    # fill up the table in a bottom-up manner
    for i in range(1, amount + 1):
        for j in range(n):
            # count solutions including coins[j]
            x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0

            # count solutions excluding coins[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y
    return table[amount][n - 1]


def has_duplicates_in_second_column(two_d_list):
    # Extract the second column values
    second_column_values = [row[1] for row in two_d_list]

    # Count the occurrences of each value in the second column
    value_counts = {}
    for value in second_column_values:
        value_counts[value] = value_counts.get(value, 0) + 1

    # Check if any value occurs more than once
    has_duplicates = any(count > 1 for count in value_counts.values())

    return has_duplicates


# Justify Words, Words justification
def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    ListOfSentences, difference, i = [], 0, 0
    ans = answer = []
    temp = []
    while i < len(words):
        if len(temp) == 0 and i < len(words) - 1:
            temp.append(words[i])
            i += 1
            continue
        if len(temp) == 0 and i == len(words) - 1:
            temp.append(words[i])
            ListOfSentences.append(temp[:])
            temp.clear()
            break
        if len(temp) > 0 and len(" ".join(temp) + " " + words[i]) <= maxWidth:
            s = " ".join(temp) + " " + words[i]
            temp.clear()
            temp.append(s)
            i += 1
            continue
        if len(temp) > 0 and len(" ".join(temp) + " " + words[i]) > maxWidth:
            ListOfSentences.append(temp[:])
            temp.clear()
            continue
    # Append any remaining words in temp as the last sentence

    # Loop through each appended sentence
    for sentence in ListOfSentences:
        difference = maxWidth - len(sentence)
        if difference > 0:
            while difference > 0:
                x = sentence.split(" ")
                sentence = [" ".join(x[:-1]) + " " + x[-1]]
                difference -= len(sentence)

            # sentence = [e + " " if sentence.index(e) < len(sentence) - 1 and maxWidth - len(sentence) > 0 else e for
            #             e in sentence]

        # reduce each sentence list in List-ofSentences to strings
    answer = [sentence for sublist in ans for sentence in sublist]
    dump = " ".join(answer)
    answer.append(dump)
    return answer


# Rain Water Collection Problem
# Appy problem with visual in react D3
def check_smaller_number_exists(nums: list[int]):
    return True


# Problem with Directions
def reduce_directions(directions: list[str]) -> list[str]:
    # dic = collections.defaultdict(int)
    i = 0
    while i < len(directions):
        if i + 1 <= len(directions) - 1 and directions[i] == "SOUTH" and directions[i + 1] == "NORTH":
            directions.remove(directions[i])
            directions.remove(directions[i])
            i = -1
            continue
        if i + 1 <= len(directions) - 1 and directions[i] == "NORTH" and directions[i + 1] == "SOUTH":
            directions.remove(directions[i])
            directions.remove(directions[i])
            i = -1
        if i + 1 <= len(directions) - 1 and directions[i] == "EAST" and directions[i + 1] == "WEST":
            directions.remove(directions[i])
            directions.remove(directions[i])
            i = -1
        if i + 1 <= len(directions) - 1 and directions[i] == "WEST" and directions[i + 1] == "EAST":
            directions.remove(directions[i])
            directions.remove(directions[i])
            i = -1
        i += 1
    my_ordered_dict = OrderedDict.fromkeys(directions)
    my_list_without_duplicates = list(my_ordered_dict.keys())
    return my_list_without_duplicates if len(my_list_without_duplicates) > 0 else []


def trap(height: list[int]) -> int:
    result = 0
    temp = 0
    wall = 0
    if len(height) < 3:
        return 0
    # handle all levels
    while any(a >= 1 for a in height) and sum(a >= 1 for a in height) >= 2:
        wall = temp = 0
        for i, e in enumerate(height):
            if e > 0 and wall == 0:
                wall = 1
                continue
            if wall == 1 and e == 0:
                temp += 1
            if wall == 1 and e > 0:
                result += temp
                temp = 0
        # move to the next level by clearing out the ground floor
        height = [a - 1 if a > 0 else 0 for a in height]
    return result


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


def build_hourglass(height):
    hourglass = ""

    # Build the top half of the hourglass
    for i in range(height):
        hourglass += " " * i + "-" * (2 * (height - i) - 1) + "\n"

    # Build the bottom half of the hourglass
    for i in range(height - 2, -1, -1):
        hourglass += " " * i + "-" * (2 * (height - i) - 1) + "\n"

    return hourglass


def rotate(s1, s2):
    i = 0
    while i < len(s1):
        for i in range(len(s1)):
            temp = s1[-1] + s1[:-1]
            if temp == s2:
                return True
    return False


class ModScope:
    def __init__(self, num):
        self.num = num

    def __mod__(self, other):
        return self.num % other.num


if __name__ == '__main__':
    x = ModScope(sum([7, 3, 6]))
    y = ModScope(3)
    print(x % y)
