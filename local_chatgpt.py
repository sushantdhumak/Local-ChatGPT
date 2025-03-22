# ===============================================
# Local ChatGPT with Ollama and Chainlit
# ===============================================

import chainlit as cl
import ollama
from typing import List, Optional
import logging

# -----------------------------------------------
# Set up logging
# -----------------------------------------------

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------------------------
# Configuration
# -----------------------------------------------

MODEL_NAME = "granite3.2-vision"
SYSTEM_PROMPT = "You are a helpful assistant with vision capabilities. You can see and understand images."

# -----------------------------------------------
# Chainlit handlers
# -----------------------------------------------

@cl.on_chat_start
async def start_chat():
    """Initialize the chat session with system prompt and welcome message."""
    try:
        # Initialize the chat history with system message
        cl.user_session.set(
            "interaction",
            [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                }
            ],
        )

        # Send welcome message with streaming
        msg = cl.Message(content="")
        start_message = f"Hello, I'm your 100% local alternative to ChatGPT running on {MODEL_NAME}. How can I help you today?"

        for token in start_message:
            await msg.stream_token(token)

        await msg.send()
        
    except Exception as e:
        logger.error(f"Error in chat initialization: {str(e)}")
        await cl.Message(content=f"There was an error starting the chat. Please try again.").send()

# -----------------------------------------------

@cl.step(type="tool")
async def process_message(input_message: str, images: Optional[List[str]] = None):
    """Process user messages and images with Ollama."""
    try:
        # Get current interaction history
        interaction = cl.user_session.get("interaction")
        
        # Add user message to history
        if images:
            interaction.append({
                "role": "user",
                "content": input_message,
                "images": images
            })
        else:
            interaction.append({
                "role": "user",
                "content": input_message
            })
        
        # Call Ollama API
        response = ollama.chat(
            model=MODEL_NAME,
            messages=interaction,
            stream=False
        ) 
        
        # Add assistant response to history
        interaction.append({
            "role": "assistant",
            "content": response.message.content
        })
        
        # Update session with new interaction
        cl.user_session.set("interaction", interaction)
        
        return response
    
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        return {"message": {"content": f"I encountered an error: {str(e)}"}}

# -----------------------------------------------

@cl.on_message 
async def main(message: cl.Message):
    """Handle incoming messages and process them."""
    # Show typing indicator
    # await cl.Message(content="").send(typing=True)
    
    try:
        # Extract images if present
        images = [file.path for file in message.elements if "image" in file.mime]
        
        # Process message with or without images
        if images:
            tool_res = await process_message(message.content, images)
        else:
            tool_res = await process_message(message.content)

        # Stream response back to user
        msg = cl.Message(content="")
        
        for token in tool_res.message.content:
            await msg.stream_token(token)

        await msg.send()
        
    except Exception as e:
        logger.error(f"Error in message handler: {str(e)}")
        await cl.Message(content=f"Sorry, I encountered an error: {str(e)}").send()

# -----------------------------------------------