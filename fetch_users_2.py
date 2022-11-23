import requests
import json

token = 'M..yODMzN.....OTQ5N..E3MA.GirWn7.nl08..HxOynI3lDFLT..u0pnZACS-pc' # Token goes inside the qoutes
channel_id = "1029083378886135858" # Channel id goes inside the quotes


# Do not edit anything below
def retrieve_messages(channelid):
    num = 0
    data = {}
    limit = 50
    headers = {"authorization": token}
    last_message_id = None

    while True:
        query_parameters = f"limit={limit}"

        if last_message_id is not None:
            query_parameters += f"&before={last_message_id}"

        r = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages?{query_parameters}",
            headers=headers,
        )

        jsonn = json.loads(r.text)
        if len(jsonn) == 0:
            break

        for value in jsonn:
            already_fetched = list(data.keys())
            if value["author"]["id"] not in already_fetched:
                data[value["author"]["id"]] = value["author"]["username"]

            last_message_id = value["id"]
            num = len(already_fetched)

    print("Number of users we collected is", num)
    return data


data = retrieve_messages(channel_id)
with open("users.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
with open("ids.txt","w", encoding="utf-8") as f:
    for i in data:
        f.write(F"{i}\n")