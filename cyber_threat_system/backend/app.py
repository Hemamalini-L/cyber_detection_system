try:
    from flask import Flask, jsonify
    from flask_socketio import SocketIO
    from flask_cors import CORS
    import threading
    import time
    import eventlet
    # Make sure threat_detection.py is in the same folder!
    from threat_detection import analyze_packet
    print("--- [SYSTEM START] Intelligence Engine Loading ---")
except ImportError as e:
    print(f"--- [CRITICAL ERROR] Missing Library: {e} ---")
    print("Run: pip install flask flask-socketio flask-cors eventlet")
    exit()

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

def background_thread():
    print("--- [MONITORING] Network Traffic Simulation Active ---")
    while True:
        try:
            data = analyze_packet()
            socketio.emit('new_packet', data)
            time.sleep(2.5) 
        except Exception as e:
            print(f"Error in simulation: {e}")

if __name__ == '__main__':
    threading.Thread(target=background_thread, daemon=True).start()
    print("--- [SERVER] Dashboard Link Established on Port 5000 ---")
    socketio.run(app, debug=True, port=5000)