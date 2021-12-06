import pandas as pd
import matplotlib.pylot as plt
import raw_data
import clean_data

data = raw_data()
overdosegraphdatade = clean_data()
overdosegraphdataus = clean_data()
overdosegraphdataregion = clean_data()


class Visuals:

    def graph1(overdosegraphdatade):
        return overdosegraphdatade.plot(x='12 Month-ending Period', y='Data Value', rot=0,
                                        title='12 Month-ending Yearly Overdose in Delaware', figsize=(15, 10), fontsize=12)


    def graph2(overdosegraphdataus):
        return overdosegraphdataus.plot(x='12 Month-ending Period', y='Data Value', rot=0,
                                        title='12 Month-ending Yearly Overdose: United States', figsize=(15, 10),
                                        fontsize=12)


    def graph3(overdosegraphdataregion):
        return overdosegraphdataregion.groupby('State')['Data Value'].plot(x='12 Month-ending Period', y='Data Value',
                                                                           title='12 Month-ending Regional Overdoses',
                                                                           figsize=(15, 10), legend=True)