import websocket
import rel
import json

def on_pong(socketApp, message):
    print("Pong'd")

def on_open(socketApp):
    # socketApp.send('{"op": "blocks_sub"}')
    socketApp.send('{"op": "addr_sub","addr": "bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h"}')
    print("Opened connection")

def on_data(socketApp, message, dataType, finCode):
    if dataType == 1:
        print(json.loads(message))

websocket.enableTrace(True)
socketApp = websocket.WebSocketApp("wss://ws.blockchain.info/inv", on_open=on_open, on_data=on_data, on_pong=on_pong)
socketApp.run_forever(dispatcher=rel, ping_interval=60, ping_timeout=10) #, ping_payload="{'op':'ping'}")  # Set dispatcher to automatic reconnection
rel.signal(2, rel.abort)  # Keyboard Interrupt
rel.dispatch()