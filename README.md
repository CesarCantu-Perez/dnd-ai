**D&D AI Dungeon Master**

An AI-powered Dungeon Master designed to run interactive Dungeons & Dragons-style fantasy adventures.

The project combines a large language model with a traditional game engine to create an interactive role-playing experience while keeping game mechanics, dice rolls, and character statistics controlled by deterministic Python code.

Project Status: Early Development — Version 1

Overview

**The goal of this project is to create an AI Dungeon Master capable of:**

Running interactive fantasy adventures
Roleplaying NPCs and describing the game world
Maintaining campaign continuity
Tracking player characters and game state
Performing dice rolls and game calculations
Managing combat encounters
Saving and loading campaigns

The AI is responsible primarily for storytelling and roleplay, while the Python game engine handles deterministic game mechanics.

Architecture

The planned architecture separates AI behavior from the underlying game rules:

                    Player
                      │
                      ▼
              ┌───────────────┐
              │    AI DM      │
              │  Story/NPCs   │
              └───────┬───────┘
                      │
             ┌────────┴────────┐
             ▼                 ▼
      ┌─────────────┐   ┌──────────────┐
      │ Game Engine │   │    Memory    │
      │             │   │              │
      │ Dice        │   │ Campaigns    │
      │ Combat      │   │ NPCs         │
      │ Characters  │   │ Events       │
      └─────────────┘   └──────────────┘
             │                 │
             └────────┬────────┘
                      ▼
                  SQLite DB

A key design goal is to prevent the AI from independently determining game mechanics.

For example, rather than allowing the AI to invent the result of an attack:

Player attacks Goblin
        │
        ▼
Python Game Engine
        │
        ├── Roll d20
        ├── Add attack modifier
        ├── Compare against AC
        └── Calculate damage
        │
        ▼
AI Dungeon Master
        │
        ▼
Narrates the result

This separation provides more consistent and reproducible game behavior.

**Current Features for Version 1 — In Development:**
  - Python project structure -- Done
  - Virtual environment -- Done
  - OpenAI API integration -- Done
  - AI Dungeon Master
  - Character system
  - Game state management
  - Dice engine
  - Campaign memory
  - NPC system
  - Combat system
  - Campaign save/load

**Planned Features:**
  - Character System

**Players will eventually be able to create and manage characters including:**

Name
Race
Class
Level
Ability scores
Hit points
Armor class
Equipment
Inventory
Spells
Game Engine

**The game engine will handle deterministic mechanics such as:**

Dice rolls
Ability checks
Saving throws
Attack rolls
Damage
Hit points
Combat turns
Character statistics
AI Dungeon Master

**The AI will handle:**

World descriptions
NPC dialogue
NPC personalities
Story progression
Player interaction
Dynamic encounters
Narrative responses
Campaign Memory

**The system will maintain long-term campaign information such as:**

Important events
NPC relationships
Player decisions
Quests
Locations
Important discoveries
World-state changes
Installation
Requirements
Python 3.12+
An OpenAI API key
Git
Clone the Repository
git clone https://github.com/YOUR-USERNAME/dnd-ai.git
cd dnd-ai
Create a Virtual Environment

**Windows:**

python -m venv .venv

**Activate it:**

.venv\Scripts\activate
Install Dependencies
python -m pip install -r requirements.txt
Configure the API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

Never commit your .env file or expose your API key publicly.

**Run the Application**
python main.py

**The development roadmap is:**

Basic AI DM
     ↓
Character System
     ↓
Game State
     ↓
Dice Engine
     ↓
Campaign Memory
     ↓
Structured AI Responses
     ↓
Tool Calling
     ↓
Combat Engine
     ↓
NPC System
     ↓
Web Interface

The goal is to maintain a clear separation between AI-generated content and deterministic game mechanics.

**Future versions may include:**

Web interface
Multiplayer campaigns
Voice-based Dungeon Master
AI-generated character portraits
Procedurally generated maps
Advanced NPC memory
Dynamic quest generation
Campaign analytics
Multiple AI personalities
Mobile interface

Disclaimer: This project is an independent fan-made project inspired by tabletop role-playing games. It is not affiliated with or endorsed by Wizards of the Coast.

Author
CC
