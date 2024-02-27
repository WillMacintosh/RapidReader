import os
import time
import signal
import shutil
import platform

clear_command = 'cls' if platform.system().lower() == 'windows' else 'clear'

current_book = None
current_word_index = 0
start_time = 0
words_per_minute = 500
word_list = []


def load_books():
    txt_files = [file for file in os.listdir() if file.endswith('.txt')]
    return txt_files


def calculate_estimated_time_remaining(total_words, current_index, wpm):
    words_remaining = total_words - current_index
    time_remaining_seconds = (words_remaining / wpm) * 60
    hours = int(time_remaining_seconds // 3600)
    minutes = int((time_remaining_seconds % 3600) // 60)
    seconds = int(time_remaining_seconds % 60)
    return hours, minutes, seconds


def signal_handler(sig, frame):
    save_progress()
    print("\nProgress saved. Exiting.")
    exit(0)


def save_progress():
    if current_book is not None:
        with open("progress.txt", "w") as progress_file:
            progress_file.write(f"{current_book}\n{current_word_index}")


def load_progress():
    global current_book, current_word_index
    try:
        with open("progress.txt", "r") as progress_file:
            lines = progress_file.readlines()
            current_book = lines[0].strip()
            current_word_index = int(lines[1].strip())
    except FileNotFoundError:
        print("No progress file found.")


def load_progress():
    global current_book, current_word_index
    try:
        with open("progress.txt", "r") as progress_file:
            lines = progress_file.readlines()
            if lines:
                current_book = lines[0].strip()
                current_word_index = int(lines[1].strip())
    except FileNotFoundError:
        print("No progress file found.")


def display_menu():
    print("Menu:")
    print("1) Start a new book")
    print("2) Change settings")
    print("3) Exit")


def load_books():
    books_directory = 'books'
    txt_files = [file for file in os.listdir(books_directory) if file.endswith('.txt')]
    return txt_files


def start_new_book():
    global current_book, current_word_index, start_time, word_list

    books = load_books()
    if not books:
        print("No books available in the books directory.")
        return

    print("Available books:")
    for index, book in enumerate(books, start=1):
        words = len(open(os.path.join('books', book)).read().split())
        time_hours, time_minutes, time_seconds = calculate_estimated_time_remaining(words, 0, words_per_minute)
        print(f"{index}) {book} - Time Remaining: {time_hours}h {time_minutes}m {time_seconds}s")

    choice = int(input("Choose a book number to start: ")) - 1
    if choice < 0 or choice >= len(books):
        print("Invalid choice.")
        return

    current_book = books[choice]
    current_word_index = 0
    word_list = open(os.path.join('books', current_book)).read().split()
    start_time = time.time()
    load_progress()


def change_settings():
    global words_per_minute
    words_per_minute = int(input("Enter words per minute: "))


def display_word(word, terminal_width):
    print(word)


def clear_screen_simulated(newline_count=100):
    print("\n" * newline_count)


def main():
    global current_word_index

    signal.signal(signal.SIGINT, signal_handler)
    load_progress()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            start_new_book()
        elif choice == "2":
            change_settings()
        elif choice == "3":
            print("Exiting the program.")
            exit(0)
        else:
            print("Invalid choice.")
            continue

        try:
            terminal_width = os.get_terminal_size().columns
        except OSError:
            terminal_width = 80

        try:
            words = len(word_list)
            for i in range(current_word_index, words):
                display_word(word_list[i], terminal_width)
                current_word_index += 1
                elapsed_time = time.time() - start_time

                hours, minutes, seconds = calculate_estimated_time_remaining(
                    words, current_word_index, words_per_minute)

                print(f"Progress: {current_word_index}/{words} ({(current_word_index / words) * 100:.2f}%)\n "
                      f"Estimated Time Remaining: {hours}h {minutes}m {seconds}s")

                time.sleep((60 / words_per_minute) - (elapsed_time % (60 / words_per_minute)))
                clear_screen_simulated()

            print("\nDone!")
            save_progress()

        except KeyboardInterrupt:
            save_progress()
            print("\nProgress saved. Exiting gracefully.")
            exit(0)


if __name__ == "__main__":
    main()
