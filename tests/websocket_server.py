# https://saurabh-ask-jennie.medium.com/socket-programming-in-python-a-comprehensive-guide-5dea1b9d2619
import asyncio
import websockets

async def handle_client(websocket, path):
  # Receive data from the client
  data = await websocket.recv()
  print(f"Received data: {data}")
  # Send a response to the client
  response = f"Message received: {data}"
  await websocket.send(response)

# Create a WebSocket server
start_server = websockets.serve(handle_client, "localhost", 8765)

# Run the server using the asyncio event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()