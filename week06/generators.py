import os
import tty
import sys
import termios
import random
import string


def chain(iter1, iter2):
    for item1 in iter1:
        yield item1

    for item2 in iter2:
        yield item2


def compress(iterable, mask):
    for index, item in enumerate(iterable):
        if mask[index]:
            yield item


def cycle(iterable):
    while True:
        for item in iterable:
            yield item


def book_reader(path):
    for file_ in sorted(os.listdir(path)):
        file_path = f'{path}/{file_}'
        chapter = []
        with open(file_path, 'r') as book:
            for line in book:
                if line.startswith('#') and chapter:
                    yield ''.join(chapter)
                    chapter = [line]
                else:
                    chapter.append(line)
        yield ''.join(chapter)


def book_reader_with_space(path):
    chapters = book_reader(path)
    print(next(chapters))
    while True:
        try:
            fd = sys.stdin.fileno()
            oldSettings = termios.tcgetattr(fd)

            try:
                tty.setcbreak(fd)
                answer = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

            if answer is ' ':
                print(next(chapters))

        except StopIteration:
            print('That\'s all folks.')
            break


def chapter_words_generator(counter):
    yield [''.join(random.choice(string.ascii_lowercase)
                   for j in range(round(random.gauss(mu=5, sigma=1))))
           for i in range(counter)]


# TO DO NEW LINE
def format_chapter(chapter):
    punctuation = ['.', ',', '?', '.', '!', '.', '?',
                   ',', '.', ',', '!', ',', ',', ',', '!', '?']
    ch = random.choices(
        chapter[1:len(chapter) - 1], k=random.randint(7, len(chapter) // 4))
    for word in ch:
        try:
            index = chapter.index(word)
            chapter[index] += random.choice(punctuation)
        except ValueError:
            continue

    cap = False
    chapter[0] = chapter[0].capitalize()
    for i in range(len(chapter)):
        if chapter[i][-1] in punctuation and not cap:
            if chapter[i][-1] == ',':
                continue
            else:
                cap = True
        elif chapter[i][-1] in punctuation and cap:
            if chapter[i][-1] == ',':
                chapter[i] = chapter[i].capitalize()
                cap = False
            else:
                chapter[i] = chapter[i].capitalize()
                cap = True
        elif chapter[i][-1] not in punctuation and cap:
            chapter[i] = chapter[i].capitalize()
            cap = False
        else:
            continue
    return " ".join(chapter) + '.'


def generate_book(chapters, chapter_length):
    with open("book.txt", 'a') as f:
        for i in range(chapters):
            f.write(f'# Chapter {i + 1}\n')
            chapter = chapter_words_generator(chapter_length)
            f.write(format_chapter(next(chapter)))
            f.write('\n\n')


def main():
    #   book_reader_with_space('/home/kristin/Python101/week06/book')
    #   chapter = chapter_words_generator(100)
    #   print(format_chapter(next(chapter)))
    generate_book(10, 150)


if __name__ == '__main__':
    main()
