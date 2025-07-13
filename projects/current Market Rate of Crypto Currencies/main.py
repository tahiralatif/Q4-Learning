
from agents import AsyncOpenAI, Agent, OpenAIChatCompletionsModel, Runner, RunConfig
import os
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from tools import get_crypto_price
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()


@cl.on_chat_start
async def start_chat():
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "gemini-2.0-flash"

    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )

    agent = Agent(
        name="CryptoDataAgent",
        instructions="Fetch live market prices for cryptocurrencies like BTC, ETH using Binance public API.",
        tools=[get_crypto_price]
    )

    cl.user_session.set("agent", agent)
    cl.user_session.set("history", [])
    cl.user_session.set("run_config", config)

    await cl.Message(content=" ").send()


@cl.on_message
async def main(message: cl.Message):
    msg = await cl.Message(content="Processing your request...").send()

    agent = cl.user_session.get("agent")
    history = cl.user_session.get("history")
    run_config = cl.user_session.get("run_config")

    history.append({"role": "user", "content": message.content})

    result = Runner.run_streamed(
        starting_agent=agent,
        input=history,
        run_config=run_config
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent) :
            await msg.stream_token(event.data.delta)
           

    msg.content = result.final_output
    await msg.update()

    cl.user_session.set("history", result.to_input_list())
    print(result.final_output)
