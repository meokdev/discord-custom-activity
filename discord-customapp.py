from pypresence import Presence
import time

client_id = '1210159243529949184'  # Replace with your application's client ID

RPC = Presence(client_id)
RPC.connect()

set_details = "you have negative canthal tilt"
set_state = "Men smelled"
set_large_text = "shibal.online"

set_large_image = "meokdev_1"
set_small_image = "00081-3617981584_copy"


# Set up the initial presence with the start time as an integer
start_time = int(time.time())
RPC.update(
    large_image=set_large_image,  # Replace with the key of your large image asset
    small_image=set_small_image,  # Replace with the key of your small image asset
    large_text=set_large_text,

    details=set_details,  # Custom text/details
    state=set_state,  # Custom state
    join="join_secret",
    spectate="spectate_secret",
    party_size=[1, 69420],
    start=1708308420
)
print("App launch successful")

# Keep the script running to maintain the presence
while True:
    time.sleep(0.2)  # Update presence every 15 seconds
    # No need to update the start time here as it should be the same to keep the timer consistent

    RPC.update(
        large_image=set_large_image,
        small_image=set_small_image,
        details=set_details,
        large_text=set_large_text,
        state=set_state,
        join="join_secret",
        spectate="spectate_secret",
        party_size=[1, 69420],
        start=1708308420
    )
