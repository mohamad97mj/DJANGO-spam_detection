from main.filters.utils import *
from main.filters.primary_filter.primary_filter import PrimaryFilter
from main.filters.api_filter.api_filter import ApiFilter
from main.filters.fasttext_filter.fasttext_filter import FasttextFilter


class FilterHandler():
    def __init__(self):
        SettingsUtils.config_warning_settings()
        SettingsUtils.config_dataframe_settings()
        self.primary_filter = self.__build_primary_filter()
        self.fasttext_filter = self.__build_fasttext_filter()
        self.api_filter = self.__build_api_filter()

    def __build_primary_filter(self) -> PrimaryFilter:
        tmp_primary_filter = PrimaryFilter()
        return tmp_primary_filter

    def __build_api_filter(self) -> ApiFilter:
        tmp_api_filter = ApiFilter()
        return tmp_api_filter

    def __build_fasttext_filter(self) -> FasttextFilter:
        tmp_fasttext_filter = FasttextFilter()
        return tmp_fasttext_filter

    def train_fasttext_model(self):
        self.fasttext_filter.train()

    def load_fasttext_model(self):
        self.fasttext_filter.load()

    def predict(self, text, use_api=True, use_fasttext=True):
        result = {'text': text}
        text = Preprocessor.preprocess(text)
        result.update(self.primary_filter.predict(text))
        if result['predicted_label'] == Labels.INAPPROPRIATE.value:
            Logger.info("predicted by primary filter")
            result.update({'predicted_by': 'primary_filter'})
            return result

        if use_api:
            result.update(self.api_filter.predict(text))
            if result['predicted_label'] == Labels.INAPPROPRIATE.value:
                Logger.info("predicted by api filter")
                result.update({'predicted_by': 'api_filter'})
                return result
        if use_fasttext:
            result.update(self.fasttext_filter.predict(text))

        Logger.info("predicted by fasttext filter")
        result.update({'predicted_by': 'fasttext_filter'})
        return result

    def test(self, file, use_api=True, use_fasttext=True):
        df = FileUtils.read_excel_file(file)
        print("hello")

    def bulk_predict(self, file, use_api=True, use_fasttext=True):
        predictions = []
        texts_df = FileUtils.read_excel_file(file)
        for t in texts_df['bio']:
            predictions.append(self.predict(t))

        FileUtils.write_list_of_dicts_2excel_file(predictions, 'outputs/test.xlsx',
                                                  headers=['text', 'predicted_label', 'probability', 'predicted_by'])
        return predictions
