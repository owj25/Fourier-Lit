import re
import numpy as np

def count_syllables(word):
    """Estimate syllable count in a word using a simple vowel-grouping method."""
    word = word.lower()
    word = re.sub(r'[^a-z]', '', word)  # Remove punctuation
    syllables = re.findall(r'[aeiouy]+', word)  # Find vowel clusters
    return max(1, len(syllables))  # At least one syllable per word


word = []
letters = []
length = []
sylls = []


def analyze_poem(poem):
    """Analyzes the poem line by line."""
    data = []
    lines = poem.split("\n")

    for line in lines:
        words = line.split()
        num_words = len(words)
        num_letters = sum(len(word) for word in words)
        visual_length = len(line)  # Approximate visual length (monospace)
        num_syllables = sum(count_syllables(word) for word in words)

        word.append(num_words)
        letters.append(num_letters)
        length.append(visual_length)
        sylls.append(num_syllables)

        data.append({
            "line": line,
            "words": num_words,
            "letters": num_letters,
            "visual_length": visual_length,
            "syllables": num_syllables
        })

    return data


def fourier_analysis(data):
    """Performs Fourier Transform and returns frequency data."""
    N = len(data)
    fft_result = np.fft.fft(data)  # Compute Fourier Transform
    frequencies = np.fft.fftfreq(N)  # Get frequency bins
    magnitudes = np.abs(fft_result)  # Get magnitude of FFT coefficients

    return list(zip(frequencies, magnitudes))  # Return (freq, magnitude) pairs


with open("/Users/student/Desktop/TWLunformatted.txt", "r", encoding="utf-8") as file:
    poem_text = file.read()

# Analyze the poem
poem_analysis = analyze_poem(poem_text)

if len(word) == len(letters) == len(length) == len(sylls):
    print("Data Collection Complete.")
    print("Word Count data:", word)
    print("Letter Count data:", letters)
    print("Length data:", length)
    print("Syllable Count data:", sylls)

#for i, line_data in enumerate(poem_analysis):
 #   print(f"Line {i + 1}: {line_data}")

print("Beggining Fourier Analysis...")

word_spectrum = fourier_analysis(word)
letter_spectrum = fourier_analysis(letters)
visual_spectrum = fourier_analysis(length)
syllable_spectrum = fourier_analysis(sylls)

with open("TWL_fourier_results.txt", "w") as file:
    file.write("Frequency Spectrum Data:\n\n")

    def save_spectrum(name, spectrum):
        file.write(f"{name}:\n")
        for freq, mag in spectrum:
            file.write(f"{freq:.5f}, {mag:.5f}\n")
        file.write("\n")

    save_spectrum("Word Count", word_spectrum)
    save_spectrum("Letter Count", letter_spectrum)
    save_spectrum("Visual Length", visual_spectrum)
    save_spectrum("Syllable Count", syllable_spectrum)

print("Fourier data saved to fourier_results.txt")

