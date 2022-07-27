import websocket
import rel
import json

AlphaAddress = ""

def on_open(socketApp):
    socketApp.send('{"op": "unconfirmed_sub"}')
    print("Opened connection")

def on_data(socketApp, message, dataType, finCode):
    message = json.loads(message)
    if message['x']['inputs'][0]['prev_out']['addr'] == "bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h":
        print('Hash =', message['x']['hash'])
        print('To =', message['x']['out'][0]['addr'])
        socketApp.close()

def on_error(socketApp, e):
    socketApp.send('{"op": "unconfirmed_unsub"}')
    socketApp.close()
    print("Connection is closed, issue:",e)

def on_pong(socketApp, message):
    print("Pong: Connection is alive")

# websocket.enableTrace(True)
socketApp = websocket.WebSocketApp("wss://ws.blockchain.info/inv", on_open=on_open, on_data=on_data, on_error=on_error, on_pong=on_pong)
socketApp.run_forever(dispatcher=rel, ping_interval=60, ping_timeout=10)  # Set dispatcher to automatic reconnection
rel.signal(2, rel.abort)  # Keyboard Interrupt
rel.dispatch()