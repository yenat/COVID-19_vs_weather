from wwo_hist import retrieve_hist_data
import os
os.chdir("top-20")
frequency = 24
start_date = '21-JAN-2020'
end_date = '17-MAR-2020'
api_key = 'YOUR_API_KEY'
location_list = ['China','Italy','Iran','Spain','South Korea','France',
'Germany','United States','Switzerland','United_Kingdom','Netherlands',
'Norway', 'Austria', 'Belgium','Sweden','Denmark','Japan','Malaysia','Qatar','Canada']

# ADD the countries that you want to get the weather data.

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)


