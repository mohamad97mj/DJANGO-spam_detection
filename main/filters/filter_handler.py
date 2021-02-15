from main.filters.utils import FileUtils, SettingsUtils, Labels, Preprocessor
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
        text = Preprocessor.preprocess(text)

        result = self.primary_filter.predict(text)
        if result['predicted_label'] == Labels.INAPPROPRIATE.value:
            return result

        if use_api:
            result = self.api_filter.predict(text)
            if result['predicted_label'] == Labels.INAPPROPRIATE.value:
                return result
        if use_fasttext:
            result = self.fasttext_filter.predict(text)
        return result
