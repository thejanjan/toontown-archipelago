from typing import Any, Dict, List

from toontown.archipelago.packets.serverbound.serverbound_packet_base import ServerBoundPacketBase


# Send this message to the server, tell it which clients should receive the message and the server will
# forward the message to all those targets to which any one requirement applies.
class BouncePacket(ServerBoundPacketBase):

    def __init__(self):
        super().__init__()
        self.cmd = "Bounce"

        # 	Optional. Game names that should receive this message
        self.games: List[str] = []

        # Optional. Player IDs that should receive this message
        self.slots: List[int] = []

        # Optional. Client tags that should receive this message
        self.tags: List[str] = []

        # Any data you want to send
        self.data: Dict[Any, Any] = {}

    def build(self) -> Dict[str, Any]:
        # Return all attributes
        return {
            'cmd': self.cmd,
            'slots': self.slots,
            'tags': self.tags,
            'data': self.data,
        }

# Example of using this packet

# bounce_packet = BouncePacket()
# bounce_packet.tags.append("DeathLink")
# await client.send_packet(bounce_packet)
