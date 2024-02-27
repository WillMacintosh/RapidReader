# RapidReader

## Overview
SpeedRead Terminal is an innovative command-line application designed to enhance your reading speed and comprehension by presenting books in a word-by-word format at a configurable speed. Ideal for voracious readers and those looking to improve their reading pace, this tool taps into the power of rapid serial visual presentation (RSVP) to minimize eye movement and potentially increase reading speed.

RapidReader is a CLI tool that takes a text file as an input, and outputs the words one-by-one quickly in order to allow the user to read the contents quickly. You are able to change the speed based on personal preference. This uses Rapid Serial Visual Presentation to minimise eye movement and increase reading speed. If you have a PDF that you'd like to read quickly, use an online PDF to TXT converter and upload it to the /books/ folder. I use this program myself regularly.

![Program in action](https://i.imgur.com/dCpFp2Q.gif)

### Features
- **Dynamic Book Loading**: Automatically detects and loads `.txt` files from the books directory, making it easy to add new books.
- **Progress Tracking**: Saves your current position in a book, allowing for seamless reading sessions over multiple sittings.
- **Customisable Reading Speed**: Enables the user to set their desired words per minute (WPM), tailoring the experience to their comfort level.
- **Estimate Time to Completion**: Provides an estimated reading time remaining for the current book, helping users manage their reading sessions.
- **Graceful Exit and Save**: Safely saves progress upon exit, ensuring no loss of data even during unexpected interruptions.

### Requirements
- Python 3
- No external Python packages are required

### Setup
1. Ensure Python 3 is installed on your system.
2. Place your `.txt` book files in a directory named `books` within the same directory as the program.
3. No further setup is required

### Usage
1. Start the program by running `python main.py` in your terminal.
2. Follow the on-screen menu to choose your action:
   - **Start a new book**: Begins a new reading session with a book of your choice from the `books` directory.
   - **Change settings**: Adjust your preferred words per minute (WPM) setting for reading.
   - **Exit**: Safely exits the program, saving your current progress.
3. To resume reading where you left off, simply restart the program and your progress will be automatically loaded.

### Functionality Breakdown
- `load_books()`: Scans the `books` directory and returns a list of available `.txt` files.
- `calculate_estimated_time_remaining()`: Calculates the estimated time remaining based on the total number of words, current index, and WPM setting.
- `signal_handler()`: Catches interrupt signals to save progress before exiting.
- `save_progress()`: Writes the current book and word index to a file for progress tracking.
- `load_progress()`: Loads reading progress from the progress file at startup.
- `display_menu()`: Displays the main menu for user interaction.
- `start_new_book()`: Initiates a new reading session with a selected book.
- `change_settings()`: Allows the user to change their WPM setting.
- `display_word()`: Displays a single word from the book in the terminal.
- `clear_screen_simulated()`: Clears the terminal screen between words to simulate the RSVP effect.
- `main()`: The main program loop that handles menu selection and book reading.
