# from typing import Set, Any
from typing import Any  # I haven't fully figured out that part. Pycharm did that automatically for me.

ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']


class Colors:
    """
    Setting colors and bold formatting strings for printing.
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def strong_ltr(mid_ltr='') -> str:
    """
    Defines the "strong letter" - the letter that must be used in every word. In the app, it is in the middle.
    :param mid_ltr: The strong letter, if defined before.
    :return: Strong letter
    """
    if mid_ltr == '':
        mid_ltr = input("Enter the letter that must be used in every word: ")
    mid_ltr.lower()
    #  ltrs = letters() # List of all letters
    # if mid_ltr not in ltrs:  # Checks if strong letter is in list of all letters.
    #   raise Exception ('Error, strong letter is not in letters list.')
    return mid_ltr


def letters(other_ltrs='', mid_ltr='') -> list:
    """
    Input function for the other letters. Not working great as for 11/26/22. Right now using params through funcs.
    @param other_ltrs:
    @param mid_ltr:
    @return:
    """
    if mid_ltr == '':  # if mid-letter is empty
        middle_ltr = strong_ltr()
    else:  # if mid-letter was assigned
        middle_ltr = strong_ltr(mid_ltr)

    ltrs = [middle_ltr, ]
    if other_ltrs == '':
        other_ltrs = input(
            "Please enter other letters (besides strong) for today's letter bee, with spaces between each letter: ")
        other_ltrs.lower()

    for ltr in other_ltrs:
        ltrs.append(ltr)

    return ltrs


def engl_dict() -> set:
    """
    Imports English dictionaries and returns it as set.
    # @rtype: set
    """
    from english_words import english_words_lower_alpha_set  # contains all words from a certain
    # dictionary, all lower case with no punctuation
    engl_words = english_words_lower_alpha_set
    from nltk.corpus import words as wrds
    nltk_words = set(wrds.words())
    from Webster_Dictionary import webster_dict  # My file, converted JSON and saved its keys only.
    eng_set: set[str | Any] = engl_words.union(nltk_words, webster_dict)
    return eng_set  # Dictionary contains 328,197 values (words).


def generate_words(other_ltrs='', mid_ltr='') -> list:
    """
    Extracts the fit words according to the strong (mid) letter (must use) and other letters. Not very efficient as for
    now. Word must be more than 4 letters (game rules).
    @param other_ltrs: All other letters, some of them needs to be in the word.
    @param mid_ltr: Strong letter - must be used in every word.
    @return: List of words that fits the conditions.
    """
    eng_set = engl_dict()
    all_ltrs = ab.copy()  # Copies the ab list to remove the checked letters.
    if other_ltrs != '' and mid_ltr != '':
        ltrs = letters(other_ltrs=other_ltrs, mid_ltr=mid_ltr)  # List always have 7 letters
    else:
        ltrs = letters()

    mid_ltr = str(ltrs[0])

    for ltr in ltrs:
        all_ltrs.remove(ltr)  # removes from letters in ltrs list from whole ab list

    all_words = []

    for word in eng_set:
        word = word.lower()
        if len(word) >= 4 and mid_ltr in word:  # first condition is word larger than 4 and strong (mid) letter is in.
            if ltrs[1] in word or ltrs[2] in word or ltrs[3] in word or ltrs[4] in word or ltrs[5] in word or ltrs[6] in word:
                # Mid_ltr is ltrs[0]; pycharm suggested to invert the IF statement. The word is appended if some of
                # the letters are in the word.
                all_words.append(word)

        for j in all_ltrs:
            if j in word and word in all_words:
                all_words.remove(word)

    all_words.sort()
    return all_words


class Conditions:
    # Can I create a condition class instead of writing this long line over and over again? if mid_ltr in word and
    # ltrs[0] in word and ltrs[1] in word and ltrs[2] in word and ltrs[3] in word and ltrs[4] in word and ltrs[5] in
    # word: check_strong_word =
    pass


def test() -> None:
    import time
    start_time = time.time()  # In order to check execution time, this is the start time of exec.
    # I can later define a function to take inputs.
    # mid_ltr = 'k'
    # ltrs = 'PRINGA'
    mid_ltr = 'i'
    ltrs = 'tcheal'
    # mid_ltr = 'p'
    # ltrs = 'riounl'
    words = generate_words(other_ltrs=ltrs.lower(), mid_ltr=mid_ltr.lower())

    strong_words = set()  # Creating a set so no 2 strong words will print.
    for word in words:  # Prints just the strong word
        if mid_ltr in word and ltrs[0] in word and ltrs[1] in word and ltrs[2] in word and ltrs[3] in word and ltrs[4] in word and ltrs[5] in word:
            strong_word = Colors.BOLD + Colors.BLUE + word + Colors.END  # Format with color and bold, w/ colors class.
            strong_words.add(strong_word)

    if len(strong_words) == 0:  # If the set is empty, print unsuccessful message.
        print("\nSorry, I wasn't able to find any matching strong words.\n")

    count_strong_words = 0
    for strong_wrd in strong_words:
        if len(strong_words) == 1:
            print("\nThe strong word is -", strong_wrd)
        else:
            count_strong_words += 1
            if count_strong_words == 1:
                print("\nThe strong words are: ", end="")
            elif count_strong_words == len(strong_words):  # Checks if loop reached its end, thus doesn't print comma.
                print(strong_wrd + ".")
                break  # Breaks so last element won't print twice.
            print(strong_wrd, end=", ")

    print("\n-----------------------------------------------------------------------------\n")

    clean_words = set()

    for word in words:  # Prints all other words
        if mid_ltr in word and ltrs[0] in word and ltrs[1] in word and ltrs[2] in word and ltrs[3] in word and ltrs[4] in word and ltrs[5] in word:
            continue
        clean_words.add(word)

    for i, e in enumerate(clean_words, 3):
        if i % 5 == 0:  # Every five lines ->
            print("")  # print a new line; this creates order and clean tabular view.
        print("{:^14}".format(e), end="  |  \t")

    print("\n\nI have found {wrds} words in total.".format(wrds=len(clean_words)))
    execute_time = round((time.time() - start_time), 5)  # End time of exec, rounded to 5 decimal places.
    print("It took me " + Colors.GREEN + f"{execute_time}" + Colors.END + " seconds to execute the program.")


def main() -> None:
    words = generate_words()
    # long_words = long_word()
    print("All optional words - ", words)


if __name__ == '__main__':
    test()
