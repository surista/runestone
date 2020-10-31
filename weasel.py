import random
import string

def random_weasel():
        a = string.ascii_lowercase+' '
        text = random.choices(a, k=28)
        return ''.join(text)

def edit_distance(source):
    """
    target: string from random_weasel
    source: "methinks it is like a weasel"
    returns: the minimum edit distance between two strings
    """
    target = "methinks it is like a weasel"
    # build matrix of correct size with all values set to 0
    # we add one to length for the '#' placeholder at the start of each string
    sol = [[0 for x in range(len(target)+1)] for y in range(len(source)+1)]

    # initialize first row
    for row in range(len(target)+1):
        for col in range(1):
            sol[0][row] = row

    # initialize first column
    for row in range(len(source)+1):
        for col in range(1):
            sol[row][0] = row

    # compare each letter in target to each letter in source
    # if letters are the same, carry over x-1,y-1 value
    # if letters are different, take minimum of one up and one left and add 1
    for row in range(len(source)):
        for col in range(len(target)):
            if source[row] == target[col]:  # if same, carry over x-1,y-1 value
                sol[row+1][col+1] = sol[row][col]
            else:
                sol[row+1][col+1] = (min(sol[row+1][col], sol[row][col+1]))+1
    return ((sol[len(source)][len(target)]), source)


def generate_scores(n):
    """
    repeatedly generate and call random weasel
    Keep best score
    """
    best_score = 9999
    best_string = ""
    for x in range(n):
        test_result = edit_distance(random_weasel())
        test_score, test_string = test_result[0], test_result[1]
        if test_score < best_score:
            best_score = test_score
            best_string = test_string
    return best_score, best_string

sol = generate_scores(100000)
print(sol)

