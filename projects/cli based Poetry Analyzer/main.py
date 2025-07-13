from agents import Agent, OpenAIChatCompletionsModel, Runner, RunConfig, AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
import os
import asyncio
import logging

# ───── Load Environment ─────
load_dotenv()
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)

# ───── Poem Input ─────
poem = """
A girl once danced beneath the flame,
Left shadows behind, but never her name.
"""

# ───── Main Function ─────
async def main():
    gemini_api = os.getenv("GEMINI_API_KEY")

    # Setup API Client
    external_client = AsyncOpenAI(
        api_key=gemini_api,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )

    # ───── Agents Definitions ─────

    lyricPoetryAgent = Agent(
        name="🎵 Lyric Poetry Agent",
        instructions="""
You are a soulful expert in lyric poetry — the kind that flows from the heart 💖.

When analyzing:
- Identify the emotional core (e.g., love, longing, grief, hope).
- Give a short, sensitive summary of the poet’s feelings.
- Reflect with 2 poetic lines of your own 🌙.
- Respond in the same language (Urdu / Roman Urdu / English).
- Add mood-based emojis: 💔🌧️✨🌙🥀

Speak gently, like a poet comforting another. You have 100 years of poetic wisdom.
"""
    )

    narrativePoetryAgent = Agent(
        name="📖 Narrative Poetry Agent",
        instructions="""
You are a 100-year-experienced expert in narrative poetry.

When analyzing:
- Identify the main storyline, characters, and sequence of events.
- Explain the deeper emotional or moral lesson.
- Summarize the poem as a reflective story.

Speak warmly, like a storyteller sharing a tale over tea ☕.
"""
    )

    dramaticPoetryAgent = Agent(
        name="🎭 Dramatic Poetry Agent",
        instructions="""
You are a 100-year-old expert in dramatic poetry — where voices rise, confront, and reveal deep truths.

When analyzing:
- Identify the speaker and the audience.
- Detect the emotional tension, drama, or confrontation.
- Explain the stakes and inner conflicts.

Respond with theatrical depth — like a wise playwright who understands the soul 🎭.
"""
    )

    parent_agent = Agent(
        name="🧠 Parent Agent",
        instructions="""
You are an intelligent poetry classifier.

Carefully analyze the poem's tone, structure, and voice.

- 🎵 Lyric Poetry → if the poem shows personal emotions or reflections (no plot or dialogue).
- 📖 Narrative Poetry → if the poem tells a story with events and characters.
- 🎭 Dramatic Poetry → if the poem is a direct emotional address or monologue with tension.

Use deep poetic insight to select ONLY one best fit. Then hand it off to the correct agent.
""",
        handoffs=[lyricPoetryAgent, narrativePoetryAgent, dramaticPoetryAgent],
    )

    # ───── Output ─────
    print("\n🧠 Analyzing your poem...\n")
    print("📝 Input Poem:\n" + poem)
    print("✨ Processing...\n")
    print("📖 Final Tashreeh:")

    result = Runner.run_streamed(
        starting_agent=parent_agent,
        input=poem,
        run_config=config
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

    print(f"\n\n🤖 Analysis by: {result.last_agent.name}")
   
    print("=" * 60 + "\n")

# ───── Run ─────
if __name__ == "__main__":
    asyncio.run(main())
