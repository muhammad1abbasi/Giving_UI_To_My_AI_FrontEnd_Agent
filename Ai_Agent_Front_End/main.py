from agents import Runner , Agent, OpenAIChatCompletionsModel , AsyncOpenAI , RunConfig
import os
from dotenv import load_dotenv
import chainlit as cl


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="Front-End exper",
    instructions="You are a Front-End Expert"
)

@cl.on_chat_start
async def handle_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello Iam am AI assistant How can i help you ").send()




@cl.on_message

async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    await msg.send()
    result = await Runner.run(
        agent,
        input=history,
        run_config=config
    )

    



    history.append({"role": "user", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()