from typing import List

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: List[WebSocket] = []
        
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    async def send_message(self, message:str, websocket: WebSocket):
        await websocket.send_text(message)
        
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        

manager = ConnectionManager()