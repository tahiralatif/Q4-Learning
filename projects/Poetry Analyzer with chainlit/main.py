from agents import Agent , OpenAIChatCompletionsModel, Runner, RunConfig , AsyncOpenAI
from openai.types.responses import  ResponseTextDeltaEvent
from dotenv import load_dotenv

import chainlit as cl
import os
import asyncio
import logging

# Disable INFO-level logging from libraries




load_dotenv()
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)

@cl.on_chat_start
async def start_chat():
     GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
     MODEL_NAME = "gemini-2.0-flash"

     external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
     
     model = OpenAIChatCompletionsModel(
          model= MODEL_NAME,
          openai_client= external_client,
     )

     config = RunConfig(
          model= model,
          model_provider= external_client,
          tracing_disabled= True,
     )

     lyricPoetryAgent = Agent(
        name= "🎵 Lyric Poetry Agent",
        instructions= """
You are an expert in analyzing lyric poetry. 
Your job is to read poems that express personal emotions, feelings, or thoughts.
If a poem includes sadness, joy, loneliness, or personal reflection — explain its meaning in detail.
Give a thoughtful explanation (tashreeh) in simple language.
""",
    )
     
     narrativePoetryAgent = Agent(
        name= "📖 Narrative Poetry Agent",
        instructions= """
You analyze narrative poetry.
These poems tell a story with events, characters, and a plot.
Your job is to explain the story being told in the poem and identify the characters and events.
Give a simple but deep tashreeh in response.
""",
    )
     
     dramaticPoetryAgent = Agent(
        name= "🎭 Dramatic Poetry Agent",
        instructions= """
You are skilled in analyzing dramatic poetry.
This type of poetry includes a speaker or character talking to someone, like in a play or monologue.
Your job is to explain the dramatic situation, who is speaking, and what emotions or actions are being shown.
Give a detailed analysis in an easy-to-understand form.
""",
    )
     
     triage_agent = Agent(
        name= "🧠 Parent Agent",
        instructions= """
You are an intelligent poetry classification agent.

Your task is to read the given poem and accurately determine its category:
- If the poem expresses personal emotions, feelings, or reflections, route it to the 🎵 Lyric Poetry Agent.
- If the poem narrates a story with characters, events, or a plot, route it to the 📖 Narrative Poetry Agent.
- If the poem presents a dramatic situation or dialogue (like a monologue or speech), route it to the 🎭 Dramatic Poetry Agent.

Carefully analyze the poem’s tone, content, and structure before choosing the most appropriate category.

📌 Always respond in the **same language** used by the user. For example, if the poem is in Urdu or Roman Urdu, reply accordingly.

💡 Add relevant emojis to make your explanation more expressive and engaging.
""",

        handoffs=[lyricPoetryAgent, narrativePoetryAgent, dramaticPoetryAgent],
    )
     
     cl.user_session.set("agent", triage_agent)
     cl.user_session.set("history", [])
     cl.user_session.set("run_config", config)

     await cl.Message(content= "👋 Welcome! Send me a poem, and I’ll analyze it for you.").send()

@cl.on_message
async def main(message: cl.Message):
    msg = await cl.Message(content="🤖 Analyzing your poem...").send()

    agent = cl.user_session.get("agent")
    history = cl.user_session.get("history")
    config = cl.user_session.get("run_config")

    history.append({"role": "user", "content": message.content})

    result = Runner.run_streamed(
        starting_agent=agent,
        input=history,
        run_config=config
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)

    msg.content = result.final_output
    await msg.update()

    cl.user_session.set("history", result.to_input_list())

               
                         


                  
     



