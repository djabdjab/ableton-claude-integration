# Ableton-Claude Integration Guide

## Overview

AI-powered music production workspace connecting Claude AI with Ableton Live 12 Suite via the Model Context Protocol (MCP). This setup enables natural language control of Ableton Live for music creation, production assistance, session analysis, and interactive learning.

**GitHub Repository**: https://github.com/djabdjab/ableton-claude-integration

---

## What This Does

With Claude connected to Ableton Live, you can:

- **Create music with natural language**: "Create a new MIDI track with a synth and add a 4-bar chord progression in C minor"
- **Control production workflow**: "Add reverb to track 2", "Start playback", "Set the tempo to 120 BPM"
- **Get AI production assistance**: "How can I improve the mix?", "What effects should I add to this vocal track?"
- **Session analysis**: "What's in my current project?", "Analyze the arrangement"
- **Interactive learning**: Ask Claude to explain techniques while demonstrating them in real-time

---

## Tech Stack

- **Ableton Live 12 Suite** (12.3.2)
- **Claude AI** via Model Context Protocol (MCP)
- **AbletonMCP** - Python-based MCP server for Ableton control
- **Python 3.14+**
- **uv** - Python package manager
- **Node.js** - For additional tooling

---

## Installation Instructions

### Prerequisites

- Ableton Live 10 or newer (tested with Live 12.3.2)
- Python 3.8+ (we're using Python 3.14.0)
- Node.js and npm
- Homebrew (macOS)

### Step 1: Install uv Package Manager

```bash
brew install uv
```

### Step 2: Test AbletonMCP Server

```bash
uvx ableton-mcp
```

You'll see connection errors initially - this is expected until the Ableton remote script is installed.

### Step 3: Install Ableton Remote Script

**CRITICAL**: Live 12 uses a different path than Live 11!

**✅ Correct path for Live 12:**
```bash
~/Music/Ableton/User Library/Remote Scripts/AbletonMCP/
```

**❌ Old Live 11 path (doesn't work in Live 12):**
```bash
~/Library/Preferences/Ableton/Live 12.x.x/User Remote Scripts/
```

**Installation command:**
```bash
cd ~/ableton-claude-integration
curl -L -o remote_script.py "https://raw.githubusercontent.com/ahujasid/ableton-mcp/main/AbletonMCP_Remote_Script/__init__.py"
mkdir -p ~/Music/Ableton/User\ Library/Remote\ Scripts/AbletonMCP
cp remote_script.py ~/Music/Ableton/User\ Library/Remote\ Scripts/AbletonMCP/__init__.py
```

### Step 4: Configure Ableton Live

1. Launch Ableton Live
2. Go to **Preferences** (or Settings)
3. Navigate to **Link, Tempo & MIDI** tab
4. In the **Control Surface** dropdown, select **"AbletonMCP"**
5. Set both **Input** and **Output** to **"None"**
6. Close Preferences (settings auto-save)

**Note**: If "AbletonMCP" doesn't appear, completely quit Ableton (Cmd+Q) and restart. Ableton only scans for remote scripts on launch.

### Step 5: Configure Claude Code

Create or edit `~/.config/claude/config.json`:

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

### Step 6: Restart Claude Code

Restart your Claude Code session to load the MCP server. When connected, you should see a **🔨 hammer icon** indicating the MCP server is active.

---

## Troubleshooting

### Issue: "AbletonMCP" doesn't appear in Ableton's Control Surface dropdown

**Solution 1**: Check the installation path
- Live 12 only scans `~/Music/Ableton/User Library/Remote Scripts/`
- The old Preferences path is deprecated in Live 12+

**Solution 2**: Restart Ableton completely
- Quit Ableton (Cmd+Q), don't just close the window
- Relaunch Ableton
- Check Preferences → Link, Tempo & MIDI again

**Solution 3**: Verify the remote script file
```bash
ls -la ~/Music/Ableton/User\ Library/Remote\ Scripts/AbletonMCP/
```
You should see `__init__.py` (45KB file)

### Issue: MCP server can't connect to Ableton

**Check 1**: Is Ableton running?
**Check 2**: Is AbletonMCP selected in Ableton's Control Surface settings?
**Check 3**: Are Input/Output both set to "None"?

### Issue: Claude Code doesn't show hammer icon

**Solution**: Check your config file:
```bash
cat ~/.config/claude/config.json
```
Make sure the JSON is valid and restart Claude Code.

---

## How to Use

### Basic Commands

**Track Creation**
- "Create a new MIDI track"
- "Add an audio track named 'Vocals'"
- "Create a MIDI track with a synth"

**MIDI Generation**
- "Add a 4-bar chord progression in C minor"
- "Create a drum pattern"
- "Generate a bassline"

**Transport Control**
- "Start playback"
- "Stop playback"
- "Set tempo to 120 BPM"

**Effects & Instruments**
- "Add a reverb to track 2"
- "Load a compressor on the master track"
- "What instruments are available?"

**Session Analysis**
- "What tracks are in my current project?"
- "Analyze the arrangement"
- "What's the current tempo?"

**Production Advice**
- "How can I improve the mix?"
- "What effects should I use for this vocal?"
- "Suggest a chord progression in G major"

### Advanced Workflows

**Collaborative Composition**
```
"Create a new project with:
- A drum track with a 4-bar house beat
- A bassline in E minor
- A pad track with sustained chords
- Set the tempo to 124 BPM"
```

**Learning Mode**
```
"Teach me how to create a sidechain compression effect.
Show me step-by-step in Ableton."
```

**Mix Analysis**
```
"Analyze my current mix and suggest improvements
for clarity and separation between instruments."
```

---

## Project Ideas & Future Directions

### Immediate Use Cases

1. **Natural Language Music Creation**
   - Generate chord progressions, melodies, drum patterns
   - Experiment with AI-suggested arrangements
   - Rapid prototyping of musical ideas

2. **Production Assistant**
   - Real-time mixing advice
   - Effect chain suggestions
   - Sound design guidance

3. **Learning Tool**
   - Interactive tutorials
   - Technique demonstrations
   - Music theory explanations with live examples

4. **Session Organization**
   - Auto-naming tracks based on content
   - Color-coding and grouping suggestions
   - Project cleanup and optimization

### Advanced Concepts

5. **Generative Composition System**
   - AI-driven arrangement decisions
   - Style-based MIDI generation
   - Algorithmic music creation

6. **Intelligent Mixing Assistant**
   - Analyze frequency conflicts
   - Suggest EQ and compression settings
   - Auto-balance mix levels

7. **Sample & Loop Management**
   - Semantic search through sample libraries
   - AI-powered sample recommendations
   - Automatic sample organization

8. **Live Performance Mode**
   - Real-time improvisation suggestions
   - Dynamic arrangement control
   - Adaptive effects processing

### Integration Expansions

9. **Multi-Tool Workflow**
   - Connect Claude to multiple music tools
   - Cross-platform project management
   - Unified creative assistant

10. **Custom Max for Live Devices**
    - Build specialized AI-controlled devices
    - Create custom control interfaces
    - Develop unique performance tools

---

## Max for Live Considerations

### Why Consider Max for Live?

**Pros:**
- **Future-proof**: Ableton's preferred approach for custom control
- **Hot-reloadable**: No need to restart Ableton
- **More flexible**: Create custom UIs and control paradigms
- **Direct API access**: Full access to Live's object model
- **You already own it**: Suite includes Max for Live
- **Rich ecosystem**: Integrate with existing M4L devices

**Cons:**
- **Learning curve**: Requires learning Max/MSP visual programming
- **Initial complexity**: Takes longer to set up
- **Another layer**: More moving parts to debug

### When to Use Max for Live

**Use Remote Script (current setup) when:**
- You want to get started immediately
- You need basic control and MIDI generation
- You don't need custom UI elements
- You're focused on music creation, not tool building

**Use Max for Live when:**
- You want to build custom interfaces
- You need real-time audio processing integration
- You want to create reusable devices
- You're building tools for others to use
- You want to learn Max (it's worth it!)

### Hybrid Approach

You can use **both**:
1. Start with Remote Script for immediate functionality
2. Build specific Max for Live devices for custom features
3. Create a unified system combining both approaches

**Example hybrid workflow:**
- Remote Script handles basic track/MIDI control
- Custom M4L device for AI-driven audio effects
- M4L UI for visualization and feedback

---

## Architecture Overview

```
┌─────────────┐
│  Claude AI  │
│ (via MCP)   │
└──────┬──────┘
       │ Model Context Protocol
       │
┌──────▼──────────┐
│  AbletonMCP     │
│  Python Server  │
│  (uvx ableton-  │
│   mcp)          │
└──────┬──────────┘
       │ TCP Socket (JSON)
       │ Port 8099
┌──────▼──────────┐
│  Remote Script  │
│  (__init__.py)  │
│  Lives in:      │
│  User Library/  │
│  Remote Scripts │
└──────┬──────────┘
       │ Live API
┌──────▼──────────┐
│  Ableton Live   │
│      12.3.2     │
└─────────────────┘
```

### Communication Flow

1. **User** → Natural language command to Claude
2. **Claude** → Processes intent, calls MCP tools
3. **MCP Server** → Sends JSON command over TCP socket
4. **Remote Script** → Receives command, calls Live API
5. **Ableton Live** → Executes action (create track, add MIDI, etc.)
6. **Remote Script** → Returns result/status
7. **MCP Server** → Formats response
8. **Claude** → Presents result to user in natural language

---

## Command Reference

### Available MCP Tools

The AbletonMCP server exposes these tools to Claude:

- `create_midi_track` - Create new MIDI track
- `create_audio_track` - Create new audio track
- `add_midi_clip` - Add MIDI clip with notes
- `get_tracks` - List all tracks in project
- `get_devices` - List available devices/plugins
- `add_device` - Add effect or instrument to track
- `set_tempo` - Change project tempo
- `play` - Start playback
- `stop` - Stop playback
- `get_song_info` - Get project information

*(Full API documentation available in AbletonMCP GitHub repo)*

---

## Development Setup

### Local Project Structure

```
~/ableton-claude-integration/
├── README.md              # Setup instructions
├── NOTION_GUIDE.md       # This comprehensive guide
├── remote_script.py      # Backup of Ableton remote script
└── .git/                 # Version control
```

### Git Repository

**Remote**: https://github.com/djabdjab/ableton-claude-integration

**Commit everything:**
```bash
cd ~/ableton-claude-integration
git add .
git commit -m "Update documentation"
git push
```

---

## Resources

### Official Documentation
- [AbletonMCP GitHub](https://github.com/ahujasid/ableton-mcp)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Ableton Live API Documentation](https://docs.cycling74.com/max8/vignettes/live_api_overview)

### Learning Resources
- [Max for Live Tutorials](https://www.ableton.com/en/live/max-for-live/)
- [Ableton Forum - Remote Scripts](https://forum.ableton.com/)
- [MCP Server Examples](https://github.com/modelcontextprotocol)

### Community
- AbletonMCP Discord (link in GitHub repo)
- Ableton Forum
- r/ableton on Reddit

---

## Next Steps

### Immediate Actions

1. ✅ Installation complete
2. ✅ Ableton configured
3. ✅ Claude Code connected
4. **→ Start experimenting with natural language commands**
5. **→ Build your first AI-assisted track**

### Short-term Goals

- [ ] Create a sample project using only natural language
- [ ] Document favorite commands and workflows
- [ ] Build a library of useful prompts
- [ ] Experiment with different musical styles
- [ ] Test session analysis features

### Long-term Vision

- [ ] Learn Max for Live basics
- [ ] Build custom M4L devices for specific workflows
- [ ] Create reusable templates for AI-assisted production
- [ ] Develop unique performance tools
- [ ] Share your creations and tools with the community

---

## Tips & Best Practices

### For Best Results

1. **Be specific**: Instead of "make music", try "create a 4-bar house beat at 126 BPM"
2. **Iterate**: Start simple, then refine with follow-up requests
3. **Combine commands**: "Create a track, add a synth, and generate a chord progression"
4. **Ask for explanations**: "Why did you choose these chords?"
5. **Learn as you go**: "Teach me how this effect works"

### Workflow Suggestions

**Morning Session**: "Analyze yesterday's project and suggest improvements"
**Idea Sketching**: "Generate 3 different bassline ideas in D minor"
**Learning Mode**: "Show me how to create tension and release in a track"
**Finishing**: "Review the mix and suggest final touches"

### Limitations to Know

- MIDI generation is based on AI interpretation (may need refinement)
- Complex multi-track arrangements may need step-by-step guidance
- Real-time audio processing requires Max for Live
- Some advanced features may need direct Ableton interaction

---

## Changelog

### 2026-01-08: Initial Setup
- Installed AbletonMCP server
- Configured Ableton Live 12.3.2
- Connected Claude Code via MCP
- Created GitHub repository
- **Key lesson**: Live 12 requires User Library path, not Preferences path

---

## Questions & Support

### Getting Help

1. **Check troubleshooting section above**
2. **Review AbletonMCP GitHub issues**
3. **Ask Claude for specific help**
4. **Post in Ableton Forum**
5. **Join AbletonMCP Discord community**

### Contributing

Found a useful workflow? Built something cool? Share it:
- Add to this document
- Commit to the GitHub repo
- Share with the community

---

**Happy music making! 🎵🤖**
