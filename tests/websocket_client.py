# https://saurabh-ask-jennie.medium.com/socket-programming-in-python-a-comprehensive-guide-5dea1b9d2619
# https://pypi.org/project/websockets/
import asyncio
import websockets

async def connect_to_server():
  async with websockets.connect("ws://localhost:8765") as websocket:
    # Send data to the server
    await websocket.send("Hello, WebSocket Server!")
    # Receive a response from the server
    response = await websocket.recv()
    print(f"Received data: {response}")

# Connect to the WebSocket server using the asyncio event loop
asyncio.get_event_loop().run_until_complete(connect_to_server())