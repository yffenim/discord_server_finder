# formatted for aws lambda

import sys
import json 
import cloudscraper
import discord
# import pandas as pd
# import datetime
from bs4 import BeautifulSoup


def tester():
# def lambda_handler(event, context):
    tag = "buffy"
    pages = 50

    # Constants
    HEADERS = {'User-Agent': 'Mozilla/5.0'}

    # Variables
    servers = []

    # Iterate over each page for a tag
    for page in range(1, pages + 1):
        url = f"https://disboard.org/servers/tag/{tag}/{page}?sort=-member_count"
        scraper = cloudscraper.create_scraper()
        resource = scraper.get(url).text
        soup = BeautifulSoup(resource, 'html.parser')

        # Iterate over each server
        for server_info in soup.find_all(class_='server-info'):
            server_name = server_info.find(class_="server-name")
            server_name_link = server_name.find('a')

            server_id = server_name_link['href'].split('/')[2]
            # server_created_at = discord.utils.snowflake_time(int(server_id))

            server_online = server_info.find(class_="server-online")

            parent = server_info.parent.parent
            tags = []
            for tag_ in parent.find_all(class_="tag"):
                tag_name = tag_.find(class_="name")
                tags.append(tag_name.contents[0].strip())

            # Check servers without online counts
            if hasattr(server_online, 'contents'):
                members_online_count = server_online.contents[0].strip()
            else:
                members_online_count = "N/A"

            # Create a server
            server = [
                server_name_link.contents[0].strip(),
                members_online_count,
                # server_created_at,
                f"https://disboard.org{server_name_link['href']}"
        ]
            server.extend(tags)
        
            # Add each server found
            servers.append(server)

    # return unique servers
    unique_servers = []
    for i in servers:
        if i not in unique_servers:
            unique_servers.append(i)

    j = json.dumps(unique_servers, indent=4, sort_keys=True, default=str)
    # print(unique_servers)
    print(j)
    return j

    # print(servers)
    # print(unique_servers)

    # df = pd.DataFrame(
    #     servers,
    #     columns=[
    #         'Server Name',
    #         'Members Online',
    #         'Creation Date',
    #         "Invite Link",
    #         'Tag 1',
    #         'Tag 2',
    #         'Tag 3',
    #         'Tag 4',
    #         'Tag 5'
    #     ]
    # )

    # # df = df.drop_duplicates()
    # result = df.to_json(orient="split")
    # parsed = json.loads(result)
    # j = json.dumps(parsed, indent=4)
    # # j = json.dumps(parsed, indent=4, sort_keys=True, default=str)
    # print(j)

tester()

############ unused for returning json ############
# reason for unuse is now willing to deal w/ py syntax rn with formatting the json and with dealing with changing datetime to acceptable datatype for AWS to serialize into JSON

