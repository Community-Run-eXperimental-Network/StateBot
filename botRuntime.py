# Bot subroutines here

import mastodon

# Runs the bot code
def botStart(serverAddress, serverPort, client_id, client_secret, access_token, base_url):
    # Create a Mastodon client
    client = mastodon.Mastodon(client_id=client_id, client_secret=client_secret, access_token=access_token, api_base_url=base_url)
    pass