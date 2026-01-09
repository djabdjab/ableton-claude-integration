# Ableton-Claude Integration

AI-powered music production workspace connecting Claude AI with Ableton Live 12 Suite.

## Features

- Natural language music creation and sound design
- Production assistance and workflow automation
- AI-powered session analysis and feedback
- Interactive learning and tutorial capabilities

## Tech Stack

- **Ableton Live 12 Suite**
- **Claude AI** via Model Context Protocol (MCP)
- **AbletonMCP** - MCP server for Ableton control
- **Python 3.14+**

## Setup Instructions

### Prerequisites

- Ableton Live 10 or newer (tested with Live 12.3.2)
- Python 3.8+ (tested with Python 3.14.0)
- Node.js and npm
- Homebrew (macOS)

### Installation Steps

1. **Install uv package manager**
   ```bash
   brew install uv
   ```

2. **Test AbletonMCP server installation**
   ```bash
   uvx ableton-mcp
   ```

3. **Install Ableton Remote Script**
   - Download the remote script from [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp)
   - Create folder: `~/Library/Preferences/Ableton/Live 12.3.2/User Remote Scripts/AbletonMCP/`
   - Place `__init__.py` in the AbletonMCP folder

4. **Configure Ableton Live**
   - Launch Ableton Live
   - Go to Preferences → Link, Tempo & MIDI
   - Select "AbletonMCP" from Control Surface dropdown
   - Set both Input and Output to "None"

5. **Configure Claude Code**
   - Create or edit `~/.config/claude/config.json`
   - Add the following configuration:
   ```json
   {
     "mcpServers": {
       "AbletonMCP": {
         "command": "uvx",
         "args": ["ableton-mcp"]
       }
     }
   }
   ```

6. **Restart Claude Code**
   - Restart your Claude Code session to load the MCP server
   - You should see a hammer icon when the MCP server is connected

## Usage

Once connected, you can use natural language to:

- **Create tracks**: "Create a new MIDI track with a synth"
- **Generate MIDI**: "Add a 4-bar chord progression in C minor"
- **Control playback**: "Start playback" or "Stop the session"
- **Load instruments**: "Add a reverb to track 2"
- **Analyze sessions**: "What's in my current project?"
- **Get production advice**: "How can I improve the mix?"

## Project Status

Installation complete! Ready to test the connection.
