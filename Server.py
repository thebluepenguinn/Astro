import http.server, requests, winreg
import os, sys
import win32pipe, win32file, pywintypes, threading
import time

PIPE_NAME = r"\\.\pipe\serverPipe"
BUFFER_SIZE = 1024

def handle_client(pipe_handle):
    #single client connection comms
    print(f"Client Connected.")
    try:
        while True:
            #Read messages
            #win32file.ReadFile returns (errorCode, dataBuffer)
            hr, data = win32file.ReadFile(pipe_handle, BUFFER_SIZE)
            if not data:
                break
            message = data.decode('big5'). strip()
            print(f"[RECEIVED] {message}")
            
            #send response
            response = f"Server Processed: {message}"
            win32File.WriteFile(pipe_handle, response.econde('big5'))

    except pywintypes.error as e:
        #broken pipe
        print(f"Client disconnected or error: {e}")
    finally:
        win32File.CloseHandle(pipe_handle)
        print(f"Closed.")

def start_pipe():
    print(f"Connecting: {PIPE_NAME}")
    while True:
            #create pipe instance
            pipe_handle = win32pipe.CreateNamedPipe
            (PIPE_NAME,
            win32pipe.PIPE_ACCESS_DUPLEX,
            win32pipe.PIPE_TYPE_MESSAGE | 
            win32pipe.PIPE_READMODE_MESSAGE | 
            win32pipe.PIPE_WAIT,
            win32pipe.PIPE_UNLIMITED_INSTANCES,
            BUFFER_SIZE,BUFFER_SIZE, 0, None)
            
            #wait for client to connect
            try:
                win32pipe.ConnectNamedPipe(pipe_handle, None)
                #Handle client in new thread
                client_thread = threading.Thread(target=handle_client, args = (pipe_handle,))
                client_thread.start()
            except Exception as e:
                win32pipe.CloseHandle(pipe_handle)
                print(f"Failed to connect to pipe: {e}")

if _name_ == "def main":
    start_pipe()

"""           RUN_KEY_PATH = r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run\"
SERVICE_NAME = ""
def open():
    try:
        key_handle = winreg.OpenKey(HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run\)

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services

response = requests.get('api.git')

def main():"""