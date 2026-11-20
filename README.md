# Humanoid Voice Assistant

## Overview

The Humanoid Voice Assistant is a Python-based speech interaction subsystem developed for the **5G-Enabled Cognitive AI Humanoid Robot**. It enables voice-driven human–robot interaction through speech recognition, intent classification, knowledge retrieval, AI-based response generation, and speech synthesis.

The system processes spoken input, identifies the underlying user intent, and dynamically routes the query to the appropriate processing module. It supports conversational interactions, factual question answering, and real-time news retrieval. Ollama with a LLaMA model is integrated to provide context-aware conversational responses.

## System Architecture

The voice assistant follows a modular processing pipeline:

1. **Audio Acquisition:** Captures user speech through a digital I2S microphone.
2. **Speech-to-Text (STT):** Converts the recorded audio into textual input.
3. **Intent Classification:** Classifies the transcribed query into predefined categories:
   - Factual queries
   - Conversational and reasoning queries
   - News-related queries
4. **Query Routing:** Activates the corresponding Python processing module based on the identified intent.
5. **Response Generation:**
   - **Factual queries:** Retrieve relevant information using Wikipedia.
   - **Conversational queries:** Generate context-aware responses using Ollama and the LLaMA model.
   - **News queries:** Fetch current news information through NewsAPI.
6. **Text-to-Speech (TTS):** Converts the generated textual response into audio output.
7. **Audio Output:** Delivers the synthesized response through an amplifier and speaker.

## Technology Stack

### Software
- **Programming Language:** Python
- **AI/LLM Runtime:** Ollama
- **Language Model:** LLaMA
- **Speech Processing:** Speech-to-Text and Text-to-Speech
- **Intent Classification:** Python-based intent routing
- **Knowledge Retrieval:** Wikipedia API
- **News Retrieval:** NewsAPI
- **Operating Environment:** Raspberry Pi OS / Linux

### Hardware
- Raspberry Pi (4 GB RAM) – Primary processing unit
- Digital I2S Microphone – Audio input
- PAM8403 Audio Amplifier – Audio amplification
- 8-ohm Speaker – Voice output

## Processing Workflow

```text
       User Voice Input
              |
              v
       I2S Microphone
              |
              v
       Audio Acquisition
              |
              v
        Speech-to-Text
              |
              v
      Intent Classification
              |
       +------+------+
       |      |      |
       v      v      v
    Factual  Conversational  News
       |      |      |
       v      v      v
   Wikipedia  Ollama/   NewsAPI
      API     LLaMA       |
       |      |           |
       +------+-----------+
              |
              v
       Response Generation
              |
              v
        Text-to-Speech
              |
              v
       PAM8403 Amplifier
              |
              v
          Speaker
```

## Key Features

- Voice-based human–robot interaction.
- Speech transcription and intent-based query routing.
- AI-powered conversational response generation using a locally hosted LLaMA model.
- Knowledge retrieval through Wikipedia.
- Real-time news retrieval through NewsAPI.
- Audio response generation through text-to-speech synthesis.
- Modular Python architecture for independent development and extension of processing components.

## Role in the Humanoid System

The voice assistant acts as the primary auditory interaction interface of the humanoid robot. It enables users to communicate with the robot through natural language and provides processed responses through audio output.

The subsystem is designed to complement the computer vision and motor control modules, contributing to the overall perception, interaction, and response capabilities of the humanoid platform.

## Current Development Status

The speech processing pipeline and its individual functionalities have been developed and tested independently. Integration with the complete humanoid architecture, including synchronized execution with computer vision and motor control, remains part of the ongoing system development.

## Future Enhancements

- Development of a dedicated conversational AI model optimized for the humanoid's onboard processor.
- Improved multi-turn dialogue and contextual memory.
- Integration of wake-word detection and voice activity detection.
- Reduced inference latency through model quantization and optimized edge deployment.
- Integration with vision and motor control modules for context-aware physical interaction.
- Exploration of 5G-assisted edge processing for computationally intensive tasks.

## Project Context

**Project:** 5G-Enabled Cognitive AI Humanoid for Interactive Systems

**Platform:** Raspberry Pi-based humanoid robot

**Domain:** Artificial Intelligence, Speech Processing, Embedded Systems, Human–Robot Interaction and 5G Communication
