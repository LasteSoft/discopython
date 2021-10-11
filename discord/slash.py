import requests

def command_create(name, description, botid, TOKEN, type=None):
    if type is None:
            url = f"https://discord.com/api/v8/applications/{int(botid)}/commands"

# This is an example CHAT_INPUT or Slash Command, with a type of 1
            json = {
                "name": name,
                "type": 1,
                "description": description,
                "options": []
                    }

# For authorization, you can use either your bot token
            headers = {
                "Authorization": f"Bot {TOKEN}"
            }

# or a client credentials token for your app with the applications.commands.update scope
            headers = {
                "Authorization": "Bearer applications.commands.update"
            }

            r = requests.post(url, headers=headers, json=json)
            return
    url = f"https://discord.com/api/v8/applications/{int(botid)}/commands"

# This is an example CHAT_INPUT or Slash Command, with a type of 1
    json = {
        "name": name,
        "type": int(type),
        "description": description,
        "options": []
    }

# For authorization, you can use either your bot token
    headers = {
        "Authorization": f"Bot {TOKEN}"
    }

# or a client credentials token for your app with the applications.commands.update scope
    headers = {
        "Authorization": "Bearer applications.commands.update"
    }

    r = requests.post(url, headers=headers, json=json)
