import os
from dotenv import load_dotenv
#gonna use this for the conversations
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig



load_dotenv()

AGENT_ID = os.getenv("agent_0001k3rwnd1vej5swt868gsp4hj1")
API_KEY = os.getenv("sk_e535a7f7cd7b0467e9c1924b884895474f2ddea0a8a867f7")

#informing jarvis of user's existence
user_name = "Kenshin"
schedule = "Picking up little brother from school at 2pm, Going to gym straight after that"
prompt = f"You are a helpful assistant that acts like Jarvis from Ironman, hence the name. You will also help around with video games, computer technology for gamers and random stuff throughout the day. I have included a schedule here {schedule} "
first_message = f"Greetings {user_name}, to what do I owe the pleasure today?"


Conversation_override = {
    "agent": {
        "prompt":{
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig(
    Conversation_config_override=Conversation_override,
    extra_body={},
    dynamic_variables={},
)

client = ElevenLabs(api_key=API_KEY)

Conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
)