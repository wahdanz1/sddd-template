#!/bin/bash

# Set up virtual environment
uv venv

# Activate virtual environment
.venv\scripts\activate  # On Windows use: venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

echo "Setup complete! Don't forget to set up your .env file with your API keys."