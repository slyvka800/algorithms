
def find_ways_count(matrix, w, h):
    # initialize whole array with one, for case when Indiana only goes right
    ways_arr = [[1 for _ in range(w)] for _ in range(h)]

    incrementer_for_letter = dict()
    # counting for each column how many times we met specific letter
    letter_was_in_column = dict()

    for i in range(w):
        for j in range(h):
            letter = matrix[j][i]
            # if next right plate has the same letter we decrement it in order to count only mega jump later
            # P.S. mega jump means jump on the right from plate with specific letter to plate with the same letter
            if i+1 < w:
                if matrix[j][i] == matrix[j][i+1]:
                    ways_arr[j][i+1] -= 1

            # ways count increases by sum of ways counts to the same letter but in previous column
            if letter in incrementer_for_letter:
                ways_arr[j][i] += incrementer_for_letter[letter]

            # prepare ways count gain in that column for specific letter (prepare incrementer for main incrementer)
            if letter in letter_was_in_column:
                letter_was_in_column[letter] += ways_arr[j][i]
            else:
                letter_was_in_column[letter] = ways_arr[j][i]

        # when column ended we increment incrementer for letters that we met
        for (letter, count) in letter_was_in_column.items():
            if letter in incrementer_for_letter:
                incrementer_for_letter[letter] += letter_was_in_column[letter]
            else:
                incrementer_for_letter[letter] = letter_was_in_column[letter]
        letter_was_in_column = dict()

    return ways_arr


if __name__ == '__main__':

    w, h = map(int, input().split(" "))

    matrix = [list(input())[:w] for i in range(h)]
    ways_count = find_ways_count(matrix, w, h)

    # print sum of ways counts to top right and bottom left corners of corridor
    print(ways_count[0][w-1] + ways_count[h-1][w-1])