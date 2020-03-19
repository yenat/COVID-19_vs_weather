from wwo_hist import retrieve_hist_data
import os
os.chdir("top-20")
# 'Anhui','Beijing','Chongqing', 'Fujian','Gansu','Guangdong','Guangxi','Guizhou','Hainan',' Hebei','Heilongjiang','Henan',
#,'Shanghai','Shanxi','Sichuan','Tianjin','Tibet','Xinjiang','Yunnan','Zhejiang'
#'Albania','Algeria','Andorra','Antigua','Barbuda','Argentina','Armenia','Aruba','Australia',
#'Azerbaijan','South Korea', 'China','Italy','Iran','Spain','France','Germany',,'United Kingdom'
#'Switzerland','Netherlands','Norway','Austria','Belgium','Sweden','Denmark','Japan','Malaysia','Qatar','Canada','Singapore'
#China,Italy,Iran,Spain,South Korea,France,Germany,United States,Switzerland,United #Kingdom,Netherlands,Norway,Austria,Belgium,Sweden,Denmark,Japan,Malaysia,Qatar,Canada
frequency = 24
start_date = '22-JAN-2020'
end_date = '17-MAR-2020'
api_key = '114f3a175c0d46abb0e142906201703'
location_list = ['Azerbaijan','South_Korea', 'China','Italy','Iran','Spain','France','Germany','United_Kingdom']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)


