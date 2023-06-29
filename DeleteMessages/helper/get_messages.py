from typing import List
from DeleteMessages.bot import DeleteBot as Bot 
from DeleteMessages.helper import mass_delete_messages

async def get_messages(client: Bot, chat_id: int, min_message_id: int, max_message_id: int, filter_type_s: List[str]):
    messages_to_delete = []
    async for msg in client.iter_messages(chat_id):
        message = await client.get_messages(chat_id)
        for file_type in tuple(["document", "video", "audio", "photo", "sticker", "voice", "animation"]):
            media = getattr(message, file_type)
            if media:
                if min_message_id <= msg.id <= max_message_id:
                    if len(filter_type_s) > 0:
                        for filter_type in filter_type_s:
                            obj = getattr(msg, filter_type)
                            if obj:
                                messages_to_delete.append(msg.id)
                    else:
                        messages_to_delete.append(msg.id)
                # append to the list, based on the condition
                if len(messages_to_delete) > 99:
                    await mass_delete_messages(
                        client,
                        chat_id,
                        messages_to_delete
                    )
                    messages_to_delete = []
        # I don't know if there's a better way to delete messages
        if len(messages_to_delete) > 0:
            await mass_delete_messages(
                client,
                chat_id,
                messages_to_delete
            )
            messages_to_delete = []
