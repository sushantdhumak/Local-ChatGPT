# Local ChatGPT with Ollama and Chainlit

A powerful local alternative to ChatGPT built with [Ollama](https://ollama.ai/) and [Chainlit](https://docs.chainlit.io/), allowing you to run large language models completely on your own hardware with a clean chat interface.

![image](https://github.com/user-attachments/assets/242c070d-28b9-40f6-9332-06db95ea5502)


## Features

- 🚀 **100% Local**: All processing happens on your machine with no data sent to external servers
- 🖼️ **Vision Support**: Upload and analyze images with multimodal LLMs
- 💬 **Chat Interface**: Clean, interactive UI powered by Chainlit
- 🔄 **Streaming Responses**: Real-time token streaming for a natural chat feel
- 🧠 **Conversation Memory**: Maintains context throughout your conversation
- ⚡ **Fast Setup**: Get running in minutes with simple installation steps
- 🛡️ **Error Handling**: Robust error management for a smooth user experience

## Requirements

- Python 3.9+ 
- [Ollama](https://ollama.ai/) installed and running
- At least 8GB RAM (16GB+ recommended for larger models)
- CUDA-compatible GPU recommended for best performance

## Usage

1. Start the Chainlit app:
   ```bash
   chainlit run local_chatgpt.py
   ```

2. Open your browser and navigate to http://localhost:8000

3. Start chatting with your local AI assistant!

## Configuration

You can customize the application by editing the following variables at the top of `local_chatgpt.py`:

```python
MODEL_NAME = "granite3.2-vision"  # Change to your preferred model
SYSTEM_PROMPT = "You are a helpful assistant with vision capabilities. You can see and understand images."
```

Available models depend on what you've pulled with Ollama. Some popular options:
- `llama3.2:70b-vision` - Best overall performance with vision capabilities
- `gemma:7b` - Smaller, faster model with good performance
- `llama3:8b` - Good balance of speed and capabilities
- `mixtral:8x7b` - Excellent reasoning capabilities

## Image Support

To use images in your conversation:
1. Click the pin sign in the chat interface
2. Select an image file
3. Type your question about the image
4. The model will analyze and respond to both your text and the image

## Troubleshooting

**Model loading errors**:
- Ensure Ollama is running (`ollama serve`)
- Verify the model is downloaded (`ollama list`)
- Check your RAM/VRAM availability

**Slow responses**:
- Try a smaller model like `gemma:7b` or `llama3:8b`
- Ensure your GPU drivers are up-to-date if using CUDA

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Ollama](https://ollama.ai/) for making local LLMs accessible
- [Chainlit](https://docs.chainlit.io/) for the excellent chat interface framework
- All the open-source LLM creators whose models can be used with this application
