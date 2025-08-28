import os
from dotenv import load_dotenv
#gonna use this for the conversations
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig



load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")
print(f"Loaded API Key: {API_KEY}")
if not API_KEY or not AGENT_ID:
    raise ValueError("Missing API_KEY or AGENT_ID. Check your .env file and variable names.")



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

def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

conversation.start_session()
