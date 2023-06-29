from typing import List
from DeleteMessages.bot import DeleteBot as Bot


async def mass_delete_messages(client: Bot, chat_id: int, message_ids: List[int]):
    return await client.delete_messages(
        chat_id=chat_id,
        message_ids=message_ids,
        revoke=True
    )
    
