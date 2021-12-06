import pandas as pd
import raw_data

class Cleaning:

    def cleans_raw_data(data):
        # Cleans raw data and returns graph read data
        cleaned_data = data[
            (data.Indicator == 'Number of Drug Overdose Deaths') | (data.Indicator == 'Number of Deaths')]
        cleaned_data = cleaned_data.reset_index(drop=True)
        cleaned_data = cleaned_data.drop(cleaned_data.columns[[3, 6, 7, 9, 10, 11]], axis=1)
        cleaned_data = cleaned_data.reset_index(drop=True)
        cleaned_data = cleaned_data.replace(',', '', regex=True)
        cleaned_data['Data Value'] = cleaned_data['Data Value'].astype(int)
        cleaned_data['12 Month-ending Period'] = cleaned_data['Month'] + ' ' + cleaned_data['Year'].astype(str)
        cleaned_data = cleaned_data[(cleaned_data.Indicator == 'Number of Drug Overdose Deaths')]
        cleaned_data = cleaned_data.drop(cleaned_data.columns[[1, 2, 3, 5]], axis=1)

        overdosegraphdatade = cleaned_data[(cleaned_data.State == 'DE')]
        overdosegraphdataus = cleaned_data[(cleaned_data.State == 'US')]
        overdosegraphdataregion = cleaned_data[
            (cleaned_data.State == 'DE') | (cleaned_data.State == 'MD') | (cleaned_data.State == 'NJ') | (
                    cleaned_data.State == 'PA')]
        overdosegraphdataregion.set_index('12 Month-ending Period', inplace=True)

        return overdosegraphdatade, overdosegraphdataus, overdosegraphdataregion