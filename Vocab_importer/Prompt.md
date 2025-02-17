## Gradio prompt



Give me a vocab language importer where we have a field that allows us to import a thematic category for the generation of language vaocab WHen submitting that text field it should hit an api endpoint to invoke an LLM chat completions in Gradio on the server side and then pass that information back to the front-end it has to create a structured json output like this example:

{ "groups": [ { "name": "Basic Words" }, { "name": "Common Phrases" }, { "name": "Numbers" }, { "name": "Family Members" }, { "name": "Food Items" } ], "words": [ { "kannada_word": "ನಮಸ್ಕಾರ", "english_word": "Hello", "parts": { "type": "greeting" }, "groups": ["Basic Words", "Common Phrases"] }, { "kannada_word": "ಧನ್ಯವಾದ", "english_word": "Thank you", "parts": { "type": "courtesy" }, "groups": ["Basic Words", "Common Phrases"] }, { "kannada_word": "ಒಂದು", "english_word": "One", "parts": { "type": "number" }, "groups": ["Numbers"] }, { "kannada_word": "ಅಮ್ಮ", "english_word": "Mother", "parts": { "type": "relation" }, "groups": ["Family Members"] }, { "kannada_word": "ಅನ್ನ", "english_word": "Rice", "parts": { "type": "food" }, "groups": ["Food Items"] } ] }

the json that is outputted back to the fornt end shoukd be copyable so it should be sent ti an input field and there should be a copy button so that it can be copied to the clipboard and that should give an alert that it was copied to the users clipboard
