from bs4 import BeautifulSoup
import requests
from csv import DictReader
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from first.utils.postgres_connection import Postgresql
 
# iterate over each line as a ordered dictionary and print only few column by column name
with open('rss_data.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        print(row['Cat_id'], row['Cat_name'])
        # response = Postgresql().execute_query("""INSERT INTO public.rss_feed_cat(cat_id, cat_name) values({}::int4,'{}')""".format(int(row['Cat_id']), row['Cat_name']))
        print('done')


# page = requests.get("https://www.monsterindia.com/jobsearch/rss-feed.html")
# soup = BeautifulSoup(page.content, 'html.parser')
# # # print(soup.find_all('td')[0].get_text())
# # gdp_table = soup.find("td", attrs={"class": "bg_purple3"})
# # # print(gdp_table)
# # gdp_table_data = gdp_table.find_all("a")  # contains 2 rows
# # # print(gdp_table_data)
# # # # Get all the headings of Lists
# # headings = []
# # for td in gdp_table_data:
# #     # print(td)
# #     # remove any newlines and extra spaces from left and right
# #     # headings.append(td.title.replace('\n', ' ').strip())
# #     print(td.find_all('title')[0].get_text())

# # # print(headings)


# for row in soup.find("td", attrs={"class": "bg_purple3"}).table.findAll('tr'):
#     # print(row)
#     try:
# 	    first_column = row.find("a").get('href').split('?cat=')[1]
# 	    # third_column = row.find('td')[1].contents

# 	    third_column = row.find("a").text
#     except:
# 	    raise
#     f = open("test.csv", "w")

	
#     f.write("{} {}\n".format(first_column,third_column))
#     # print(first_column, third_column)

#     # writer.writerow(first_column.split('?cat=')[1],third_column)