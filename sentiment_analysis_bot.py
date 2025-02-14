from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji : str
    sentiment : float

def getMood (input, *, sensitivity):

    """
    Analyze the mood of a given text and return a Mood object containing the emoji and sentiment polarity.

    :param input_text: The input text to be analyzed
    :param sensitivity: 0.0 (super sensitive) - 1.0 (ultra nonsensitive)
    :return: A Mood object containing the emoji representing the mood and the sentiment polarity value
    """

    polarity = TextBlob(input).sentiment.polarity

    happyThreshold = sensitivity
    sadThreshold = -sensitivity

    if polarity >= happyThreshold:
        return Mood('😊', polarity)
    elif polarity <= sadThreshold:
        return Mood('😠', polarity)
    else:
        return Mood('😐', polarity)

def run_bot():
    print('Bot: Enter some text and I will perform a sentiment analysis on it.')
    while True:
        user_input = input('You: ').lower()
        if user_input == "exit":
            break
        mood: Mood = getMood(user_input, sensitivity=0.0)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')


if __name__ == '__main__':
    run_bot()


