from main.filters.utils import *
from main.filters.primary_filter.primary_filter import PrimaryFilter
from main.filters.api_filter.api_filter import ApiFilter
from main.filters.fasttext_filter.fasttext_filter import FasttextFilter
import requests


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

    def predict(self, bio, use_api=True, use_fasttext=True):
        result = {'bio': bio}
        bio = Preprocessor.preprocess(bio)
        result.update(self.primary_filter.predict(bio))
        if result['predicted_label'] == Labels.INAPPROPRIATE.value:
            # Logger.info("predicted by primary filter")
            result.update({'predicted_by': 'primary filter'})
            return result

        if use_api:
            response = self.api_filter.predict(bio)
            if response:
                result.update(response)
                if result['predicted_label'] == Labels.INAPPROPRIATE.value:
                    # Logger.info("predicted by api filter")
                    result.update({'predicted_by': 'api filter'})
                    return result

            else:
                Logger.warn("Failed to use api filter")

        if use_fasttext:
            result.update(self.fasttext_filter.predict(bio))

        # Logger.info("predicted by fasttext filter")
        result.update({'predicted_by': 'fasttext filter'})
        return result

    def test(self, file, use_api=True, use_fasttext=True):
        tp = tn = fp = fn = 0
        texts_df = FileUtils.read_excel_file(file)
        for index, row in texts_df.iterrows():
            predicted_label = self.predict(row['bio'])['predicted_label']
            label = row['label']
            if predicted_label == 'appropriate':
                if label == 'appropriate':
                    tp += 1
                else:
                    fp += 1
            else:
                if label == 'appropriate':
                    fn += 1
                else:
                    tn += 1
            precision = tp / tp + fp
            recall = tp / tp + fn
            return {
                'precision': precision,
                'recall': recall,
            }

    def bulk_predict(self, file, use_api=True, use_fasttext=True):
        predictions = []
        bios_df = FileUtils.read_excel_file(file)
        for t in bios_df['bio']:
            predictions.append(self.predict(t))

        FileUtils.write_list_of_dicts_2excel_file(predictions, 'media/predictions.xlsx',
                                                  headers=['bio', 'predicted_label', 'probability', 'predicted_by'])
