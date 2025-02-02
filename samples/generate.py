from primitive_tts.speech import speak
from time import sleep


speech_samples = (
    'system online',
    'lorem ipsum',
    'attention captain I have finished my analysis',
    'my job is to churn butter',
    # pangrams
    'the quick brown fox jumps over the lazy dog',
    'sphinx of black quartz judge my vow',
    'the five boxing wizards jump quickly',
    'pack my box with five dozen liquor jugs',
    'how vexingly quick daft zebras jump',
)

for sample in speech_samples:
    speak(sample, output_file=f'{sample.replace(" ", "-")}.wav')
    sleep(1)
