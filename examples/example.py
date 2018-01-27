# Import the module.
import pynite

# Put your API Key here.
token = ''

# Async loop.
async def main():
  
    # Initialize the Client.
    client = pynite.Client(token, session=aiohttp.ClientSession())

    # Fill in these variables!
    platform = ''
    # Can be pc, psn, or xbl
    name = ''

    # Get a Profile.
    profile = await client.get_player(platform, name)

    # Print your number of Kills in Solo. (Docs coming soon, and an easier way to access exact info.)
    print(profile.stats.p2.kills.value)

# Run the async loop!
loop = asyncio.get_event_loop()
loop.run_until_complete(main()) 