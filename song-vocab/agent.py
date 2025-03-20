import os
import json
from typing import Dict
import requests

class Agent:
    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"

    async def process_message(self, message_request: str) -> Dict:
        try:
            # Extract song name from request
            song_name = self.extract_song_name(message_request)
            print(f"Processing song: {song_name}")  # Debug print
            
            # Get and analyze lyrics using Ollama
            analysis = await self.get_and_analyze_lyrics(song_name)
            
            return {
                "song_name": song_name,
                "analysis": analysis
            }

        except Exception as e:
            print(f"Error in process_message: {str(e)}")  # Debug print
            return {"error": str(e)}

    def extract_song_name(self, message: str) -> str:
        """Extract Kannada song name from the message"""
        prefixes = ["find lyrics for", "search for", "find", "lyrics of"]
        message = message.lower()
        for prefix in prefixes:
            if message.startswith(prefix):
                message = message[len(prefix):].strip()
        return message

    async def get_and_analyze_lyrics(self, song_name: str) -> Dict:
        """Get and analyze Kannada lyrics using Ollama"""
        try:
            prompt = f"""
            Analyze this Kannada song: "{song_name}"
            
            Provide information in this exact JSON format:
            {{
                "lyrics": "full lyrics in Kannada script",
                "analysis": {{
                    "song_name": {{
                        "kannada": "name in Kannada script",
                        "english": "English transliteration"
                    }},
                    "singer": "singer name",
                    "composer": "composer name",
                    "movie": "movie or album name",
                    "year": "year of release",
                    "vocabulary": [
                        {{
                            "word": "Kannada word",
                            "frequency": number,
                            "meaning": "English meaning",
                            "part_of_speech": "noun/verb/etc"
                        }}
                    ],
                    "themes": ["theme1", "theme2"],
                    "cultural_context": "cultural significance"
                }}
            }}
            
            Ensure the response is valid JSON.
            """

            print("Sending request to Ollama...")  # Debug print
            
            # Make request to Ollama
            response = requests.post(
                self.ollama_url,
                json={
                    "model": "mistral",
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            print(f"Ollama response status: {response.status_code}")  # Debug print
            
            if response.status_code != 200:
                print(f"Error response: {response.text}")  # Debug print
                raise Exception("Failed to get response from Ollama")

            response_json = response.json()
            print("Got response from Ollama")  # Debug print
            
            # Parse the response text as JSON
            try:
                result = json.loads(response_json['response'])
                return result
            except json.JSONDecodeError as e:
                print(f"JSON parse error: {str(e)}")  # Debug print
                print(f"Raw response: {response_json['response']}")  # Debug print
                raise Exception("Failed to parse Ollama response as JSON")

        except Exception as e:
            print(f"Error in get_and_analyze_lyrics: {str(e)}")  # Debug print
            raise Exception(f"Error getting and analyzing lyrics: {str(e)}")
