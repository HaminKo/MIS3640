import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    # strippables = string.punctuation + string.whitespace

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        for word in line.split():
            
            word = word.strip(strippables)
            word = word.lower()
            
            # if word in hist:
            #     hist[word] += 1
            # else:
            #     hist[word] = 1

            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist.keys())


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    def take_second(item):
        return item[1]
    return sorted(hist.items(), key=take_second, reverse=True)


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    return most_common(hist)[:num]


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    d3 = {}
    for word in d1:
        if word not in d2:
            d3[word] = d1[word]
    return d3

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    freq_hist = {}
    word_count = 0
    for word in hist:
        freq_hist[word] = hist[word]
        freq_hist[word] += word_count
        word_count += hist[word]
    random_word = random.randint(1, word_count)

    # prev_word = list(freq_hist.keys())[0]
    # for word in freq_hist:
    #     if freq_hist[word] >= random_word and freq_hist[prev_word] < random_word:
    #         return word
    #     prev_word = word

    word_list = list(freq_hist.items())
    start = 0
    end = len(word_list)
    if random_word == 1:
        return word_list[0][0]
    while start < end:
        x = (start + end)//2
        current_number = word_list[x][1]
        previous_number = word_list[x-1][1]
        if random_word <= current_number and random_word > previous_number:
            return word_list[x][0]
        elif random_word > current_number:
            start = x
        elif random_word < current_number:
            end = x


def main():
    hist = process_file('Pride and Prejudice.txt', skip_header=True)
    # print(hist)
    # print('Total number of words:', total_words(hist))
    # print('Number of different words:', different_words(hist))

    # t = most_common(hist)
    # print('The most common words are:')
    # for freq, word in t[0:20]:
    #     print(word, '\t', freq)

    # words = process_file('words.txt', skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()
