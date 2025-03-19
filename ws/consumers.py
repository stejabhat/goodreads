import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ReadingProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            await self.accept()
        else:
            await self.close()

    async def receive(self, text_data):
        data = json.loads(text_data)
        progress = data["progress"]
        book_id = data["book_id"]

        # Broadcast update
        await self.channel_layer.group_send(
            f"reading_progress_{self.user.id}",
            {"type": "progress_update", "progress": progress, "book_id": book_id}
        )

    async def progress_update(self, event):
        await self.send(text_data=json.dumps(event))
