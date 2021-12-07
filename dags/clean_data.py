import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def import_raw_data():
    # Imports raw data and returns a DataFrame
    raw_data = pd.read_csv(
        '/Users/roethelchristine/airflow/airflow/data/VSRR_Provisional_Drug_Overdose_Death_Counts.csv')
    data = pd.DataFrame(raw_data)

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

    overdosegraphdatade.plot(x='12 Month-ending Period', y='Data Value', rot=0,
                             title='12 Month-ending Yearly Overdose in Delaware', figsize=(15, 10), fontsize=12)


    # overdosegraphdataregion.groupby('State')['Data Value'].plot(x='12 Month-ending Period', y='Data Value',
    #                                                             title='12 Month-ending Period: Regional Overdoses',
    #                                                             figsize=(15, 10), legend=True)

    # plt.show()
    plt.savefig(
        f"/Users/roethelchristine/airflow/airflow/jpgs/overdosegraphde.jpg")

    overdosegraphdataus.plot(x='12 Month-ending Period', y='Data Value', rot=0,
                             title='12 Month-ending Yearly Overdose: United States', figsize=(15, 10),
                             fontsize=12)

    plt.savefig(
        f"/Users/roethelchristine/airflow/airflow/jpgs/overdosegraphus.jpg")