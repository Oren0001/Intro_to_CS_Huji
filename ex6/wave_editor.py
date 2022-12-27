##########################################################################
# FILE : wave_editor.py
# WRITER : Oren Motiei , oren503
# EXERCISE : intro2cs2 ex6 2020
# DESCRIPTION: A Program that edits audio files of type wav.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################
import wave_helper
import math

ERROR_MSG = "The input must be one of the numbers:"
INVALID_INPUT = "The input is invalid. Please try again."
ENTRY_MENU = ("1", "2", "3")
FILE_CHANGE_MENU = ("1", "2", "3", "4", "5", "6", "7", "8")
SAMPLE_RATE = 2000
MAX_VOLUME = 32767
MIN_VOLUME = -32768
VOLUME_CHANGE = 1.2
PARAMETER = 1/16
FREQUENCIES = {"A": 440, "B": 494, "C": 523, "D": 587,
               "E": 659, "F": 698, "G": 784}


def run_entry_menu():
    """Displays the entry menu, and returns the user's choice from it."""
    while True:
        user_choice = input("Please enter one of the following numbers:\n"
                            "1. Change a wave file.\n"
                            "2. Compose a melody.\n"
                            "3. Exit the program.")
        if user_choice not in ENTRY_MENU:
            print(ERROR_MSG, ENTRY_MENU)
            continue
        return user_choice


def get_wav_file():
    """The function Asks the user for a wav file name,
       and Returns a tuple with 2 elements: the first is
       the sample rate, and the second is the audio data."""
    while True:
        wav_filename = input("Please enter the wav file name: ")
        result = wave_helper.load_wave(wav_filename)
        if result == -1:
            print(INVALID_INPUT)
            continue
        return result


def change_wav_file(sample_rate, audio_data):
    """
    Changes the wav file according to the user's choice.
    :param sample_rate: The number of audio samples which represent a second.
    :param audio_data: A list of lists. Each list is a pair of integers.
    """
    while True:
        user_choice = run_file_change_menu()
        if user_choice == FILE_CHANGE_MENU[7]:
            run_finish_menu(sample_rate, audio_data)
            return
        audio_data = change_audio_data(user_choice, audio_data)


def run_file_change_menu():
    """Displays the file change menu, and returns the user's choice from it."""
    while True:
        user_choice = input("Please enter one of the following numbers:\n"
                            "1. Reverse audio.\n"
                            "2. Audio deprivation.\n"
                            "3. Speed acceleration.\n"
                            "4. Speed deceleration.\n"
                            "5. Volume amplification.\n"
                            "6. Volume lowering.\n"
                            "7. Low pass filter.\n"
                            "8. Move to the ending menu.")
        if user_choice not in FILE_CHANGE_MENU:
            print(ERROR_MSG, FILE_CHANGE_MENU)
            continue
        return user_choice


def run_finish_menu(sample_rate, audio_data):
    """Asks the user for a name, then saves the audio with it"""
    while True:
        wav_filename = input("Enter a name that will be used to"
                             " save the file: ")
        result = wave_helper.save_wave(sample_rate, audio_data, wav_filename)
        if result == -1:
            print(INVALID_INPUT)
            continue
        return


def change_audio_data(user_choice, audio_data):
    """
    Changes the audio data according to the user's choice.
    :param user_choice: A string that represents the user's choice from
                       the file change menu.
    :param audio_data: A list of lists. Each list is a pair of integers.
    :return: Returns a modified audio data.
    """
    if user_choice == FILE_CHANGE_MENU[0]:
        audio_data.reverse()
    elif user_choice == FILE_CHANGE_MENU[1]:
        execute_audio_deprivation(audio_data)
    elif user_choice == FILE_CHANGE_MENU[2]:
        audio_data = execute_speed_acceleration(audio_data)
    elif user_choice == FILE_CHANGE_MENU[3]:
        audio_data = execute_speed_deceleration(audio_data)
    elif user_choice == FILE_CHANGE_MENU[4]:
        execute_volume_amplification(audio_data)
    elif user_choice == FILE_CHANGE_MENU[5]:
        execute_volume_lowering(audio_data)
    elif user_choice == FILE_CHANGE_MENU[6]:
        audio_data = execute_low_pass_filter(audio_data)
    print("The file has been changed successfully.")
    return audio_data


def execute_audio_deprivation(audio_data):
    """Changes the audio data values to their negative values."""
    for item in audio_data:
        for i in range(2):
            if -item[i] > MAX_VOLUME:
                item[i] = MAX_VOLUME
            elif -item[i] < MIN_VOLUME:
                item[i] = MIN_VOLUME
            else:
                item[i] = -item[i]


def execute_speed_acceleration(audio_data):
    """Accelerates the speed of the audio."""
    faster = list()
    for i in range(0, len(audio_data), 2):
        faster.append(audio_data[i])
    return faster


def execute_speed_deceleration(audio_data):
    """Slows down the speed of the audio. Returns the modified audio data."""
    slower = list()
    for i in range(len(audio_data) - 1):
        slower.append(audio_data[i])
        avg = [(audio_data[i][0]+audio_data[i+1][0]) // 2,
               (audio_data[i][1] + audio_data[i+1][1]) // 2]
        slower.append(avg)
    slower.append(audio_data[-1])
    return slower


def execute_volume_amplification(audio_data):
    """Amplifies the volume of the audio."""
    for item in audio_data:
        for i in range(2):
            new_value = int(VOLUME_CHANGE * item[i])
            if new_value > MAX_VOLUME:
                item[i] = MAX_VOLUME
            elif new_value < MIN_VOLUME:
                item[i] = MIN_VOLUME
            else:
                item[i] = new_value


def execute_volume_lowering(audio_data):
    """Lowers the volume of the audio."""
    for item in audio_data:
        for i in range(2):
            item[i] = int(1/VOLUME_CHANGE * item[i])


def execute_low_pass_filter(audio_data):
    """Blurs the audio. Returns the modified audio data."""
    filtered = list()
    n = len(audio_data)
    for i in range(n):
        filtered.append([])
        for j in range(2):
            if i == 0:
                filtered[i].append(int((audio_data[i][j]
                                        + audio_data[i+1][j]) / 2))
            elif i == n-1:
                filtered[i].append(int((audio_data[i-1][j]
                                        + audio_data[i][j]) / 2))
            else:
                filtered[i].append(int((audio_data[i-1][j] + audio_data[i][j]
                                        + audio_data[i+1][j]) / 3))
    return filtered


def read_txt_file():
    """Reads the given file, and returns it as a list."""
    guide = list()
    while True:
        filename = input("Please enter the name of the guidelines file: ")
        try:
            with open(filename) as f:
                for line in f:
                    guide.extend(line.split())
            return guide
        except FileNotFoundError as error_msg:
            print(error_msg)


def create_audio_data(guide):
    """
    Creates an audio data using the given guidelines.
    :param guide: A list of chars to play, and numbers that represent
                  the play time.
    :return: A list of lists. Each list is a pair of integers.
    """
    audio_data = list()
    for index in range(0, len(guide), 2):
        play_time = int(guide[index + 1])
        if guide[index] == "Q":
            for i in range(int(play_time * PARAMETER * SAMPLE_RATE)):
                audio_data.append([0, 0])
        else:
            frequency = FREQUENCIES[guide[index]]
            samples_per_cycle = SAMPLE_RATE / frequency
            for i in range(int(play_time * PARAMETER * SAMPLE_RATE)):
                sample = int(MAX_VOLUME *
                             math.sin(math.pi * 2 * i/samples_per_cycle))
                audio_data.append([sample, sample])
    return audio_data


def main():
    """Calls all the functions in this program directly or indirectly."""
    while True:
        user_choice = run_entry_menu()
        if user_choice == ENTRY_MENU[0]:
            change_wav_file(*get_wav_file())
        elif user_choice == ENTRY_MENU[1]:
            guide = read_txt_file()
            audio_data = create_audio_data(guide[:])
            change_wav_file(SAMPLE_RATE, audio_data)
        else:
            return


if __name__ == "__main__":
    main()
