import speech_recognition as sr

ENGLISH_TEXT_OUTPUT_PATH = "output/speech_to_english.txt"


def speech_to_text(audio_path):
    """
        Converting speech to English text
        :param
            audio_path: audio file path (e.g: wav)
        :return
            str: a .txt file path with English text
    """
    recognizer = sr.Recognizer()
    output_path = ENGLISH_TEXT_OUTPUT_PATH

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            text_output = recognizer.recognize_google(audio)
            write_to_file(text_output, output_path)
        except Exception as e:
            print("Speech recognition service error", e)

    return output_path


def read_text_file(file_path):
    """
        Read text from file path
        :param
            file_path: text file path
        :return
            str: a content from this file
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except IOError:
        print(f"Error: Facing error when read file at {file_path}")
        return None


def write_to_file(content, filename):
    """
        Write content to file
        :param
            content: text content
            filename: output file name
    """
    try:
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(content)
        print(f"Content successfully written to {filename}")
    except IOError:
        print(f"An error occurred while writing to {filename}")


if __name__ == '__main__':
    speech_to_text("./input/Winter_is_coming_speech.wav")