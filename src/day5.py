import sys
import math


def part1(lines: list[str]) -> int:
    rules = list(map(lambda line: line.split("|"), filter(lambda line: "|" in line,  lines)))
    books = list(map(lambda line: line.split(","), filter(lambda line: "," in line,  lines)))

    return sum(list(map(lambda book: get_middle_page(book), filter(lambda book: page_order_correct(book, rules), books))))

def page_order_correct(book: list[str], rules: list[str]) -> bool:
    for rule in rules:
        try:
            if book.index(rule[0]) > book.index(rule[1]):
                return False
        except ValueError:
            continue

    return True

def get_middle_page(book: list[int]):
    return int(book[math.floor(len(book) / 2)])

def part2(lines: list[str]) -> int:
    rules = list(map(lambda line: line.split("|"), filter(lambda line: "|" in line,  lines)))
    books = list(map(lambda line: line.split(","), filter(lambda line: "," in line,  lines)))

    incorrect_books = filter(lambda book: not page_order_correct(book, rules), books)
    reordered_books = map(lambda book: re_order_pages(book, rules), incorrect_books)
    middle_pages = map(lambda book: get_middle_page(book), reordered_books)
    return sum(list(middle_pages))

def re_order_pages(book: list[str], rules: list[str]) -> list[str]:
    for rule in rules:
        if rule[0] in book and rule[1] in book:
            if book.index(rule[0]) > book.index(rule[1]):
                new_book = book[:]
                new_book[book.index(rule[0])] = book[book.index(rule[1])]
                new_book[book.index(rule[1])] = book[book.index(rule[0])]
                return re_order_pages(new_book, rules)
        
    return book
