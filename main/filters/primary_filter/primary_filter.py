# word based filter
from main.filters.utils import FileUtils, Labels
from main.filters.utils.preprocessor import Preprocessor
from os import path


class PrimaryFilter():
    RESOURCE_DIR = 'main/filters/resources/'
    english_spam_words_path = path.join(RESOURCE_DIR, 'english-spam-words.xlsx')
    english_swear_words_path = path.join(RESOURCE_DIR, 'english-swear-words.xlsx')
    finglish_spam_words_path = path.join(RESOURCE_DIR, 'finglish-spam-words.xlsx')
    finglish_swear_words_path = path.join(RESOURCE_DIR, 'finglish-swear-words.xlsx')
    persian_spam_words_path = path.join(RESOURCE_DIR, 'persian-spam-words.xlsx')
    persian_swear_words_path = path.join(RESOURCE_DIR, 'persian-swear-words.xlsx')
    all_lists_path = [
        english_spam_words_path,
        english_swear_words_path,
        finglish_spam_words_path,
        finglish_swear_words_path,
        persian_spam_words_path,
        persian_swear_words_path
    ]

    def __init__(self):
        self.filter_list = []
        self.__read_filter_list()

    def predict(self, text):
        for c in self.filter_list:
            for w in c:
                if str(w) in Preprocessor.tokenize(text):
                    predicted_label = Labels.INAPPROPRIATE.value
                    break
            else:
                predicted_label = Labels.APPROPRIATE.value

        formatted_prediction = {
            'predicted_label': predicted_label,
            'probability': 1
        }

        return formatted_prediction

    def __read_filter_list(self):
        for p in self.all_lists_path:
            s = FileUtils.read_excel_file(p)
            lst = s.iloc[:, 0].tolist()
            self.filter_list.append(lst)
