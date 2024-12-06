import pyvista as pv
import speech_recognition as sr

ENGLISH_TEXT_OUTPUT_PATH = "output/speech_to_english.txt"
THREE_D_MODELS = "3D_models/ASL"
GLB_EXTENSION = ".glb"

number_map = {
    'zero': THREE_D_MODELS + '0' + GLB_EXTENSION,
    'one': THREE_D_MODELS + '1' + GLB_EXTENSION,
    'two': THREE_D_MODELS + '2' + GLB_EXTENSION,
    'three': THREE_D_MODELS + '3' + GLB_EXTENSION,
    'four': THREE_D_MODELS + '4' + GLB_EXTENSION,
    'five': THREE_D_MODELS + '5' + GLB_EXTENSION,
    'six': THREE_D_MODELS + '6' + GLB_EXTENSION,
    'seven': THREE_D_MODELS + '7' + GLB_EXTENSION,
    'eight': THREE_D_MODELS + '8' + GLB_EXTENSION,
    'nine': THREE_D_MODELS + '9' + GLB_EXTENSION,
}


def speech_to_text(audio_path):
    """
        Converting speech to English text
        :param
            audio_path: audio file path (e.g: wav)
        :return
            str: english text
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            text_output = recognizer.recognize_google(audio, language='en-US')
        except Exception as e:
            print("Speech recognition service error", e)

    return text_output


def load_and_display_3d_file(english_text):
    """
    Load and display 3D files (.glb)

    Parameters:
    english_text: 1, 2, 3, etc
    """
    three_d_file_path = number_map.get(english_text.lower())
    mesh = pv.read(three_d_file_path)
    mesh.plot(show_scalar_bar=False)


if __name__ == '__main__':
    english_text = speech_to_text("./input/9.wav")
    load_and_display_3d_file(english_text)