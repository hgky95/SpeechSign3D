import speech_recognition as sr
from PIL import Image

ENGLISH_TEXT_OUTPUT_PATH = "output/speech_to_english.txt"


def text_to_asl(text, image_folder, output_image):
    """
    Convert English text to ASL using corresponding images.

    Args:
        text (str): The English text to be converted.
        image_folder (str): Folder containing ASL images (e.g., "a.jpg", "b.jpg", etc.).
        output_image (str): Path to save the generated ASL output image.
    """
    text = text.lower()  # Convert text to lowercase to match image filenames
    images = []

    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            image_path = f"{image_folder}/{char}.png"
            try:
                img = Image.open(image_path)
                images.append(img)
            except FileNotFoundError:
                print(f"Image for '{char}' not found in {image_folder}.")
        elif char == " ":  # Add a gap for spaces
            images.append(None)  # Represent a space with None

    # Combine images into one strip
    if not images:
        print("No valid characters found in the text.")
        return

    # Calculate the total width and maximum height of the output image
    total_width = sum(img.width if img else 50 for img in images)  # 50px gap for spaces
    max_height = max(img.height if img else 0 for img in images)

    # Create a new blank image for the result
    result = Image.new("RGB", (total_width, max_height), (255, 255, 255))

    # Paste images onto the result image
    x_offset = 0
    for img in images:
        if img:
            result.paste(img, (x_offset, 0))
            x_offset += img.width
        else:  # Add space for gaps
            x_offset += 50

    # Save the result image
    result.save(output_image)
    print(f"ASL image saved as: {output_image}")

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
    output_path = speech_to_text("./input/winter_is_coming.wav")
    english_text = read_text_file(output_path)
    text_to_asl(
        text=english_text,
        image_folder="letters",
        output_image="output/output.jpg"
    )