import { Groq } from "groq-sdk"

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,
})

export async function generateVocabulary(theme: string) {
  const prompt = `Generate a structured JSON output for a vocabulary list in the theme of "${theme}". The output should include groups and words in Kannada and English, following this structure:
  {
    "groups": [
      { "name": "Group Name" }
    ],
    "words": [
      {
        "kannada_word": "ಕನ್ನಡ ಪದ",
        "english_word": "English Word",
        "parts": {
          "type": "word type"
        },
        "groups": ["Group Name"]
      }
    ]
  }
  Include at least 5 groups and 15 words related to the theme and give the proper translation for each word.
  Good example:
  {
  "groups": [
    { "name": "Colors" },
    { "name": "Animals" }
  ],
  "words": [
    {
      "kannada_word": "ಕೆಂಪು",
      "english_word": "Red",
      "parts": {
        "type": "Adjective"
      },
      "groups": ["Colors"]
    },
    {
      "kannada_word": "ಹಸಿರು",
      "english_word": "Green",
      "parts": {
        "type": "Adjective"
      },
      "groups": ["Colors"]
    },
    {
      "kannada_word": "ಹಸು",
      "english_word": "Cow",
      "parts": {
        "type": "Noun"
      },
      "groups": ["Animals"]
    },
    {
      "kannada_word": "ಹಕ್ಕಿ",
      "english_word": "Bird",
      "parts": {
        "type": "Noun"
      },
      "groups": ["Animals"]
    }
  ]
}
It is good because the translation for the kannada word is correct and matches the english word and is in the same group.


  Bad example:
   {
      "kannada_word": "ಬೆಂಡಕಾಯಿ",
      "english_word": "Eggplant",
      "parts": {
        "type": "Noun"
      },
      "groups": [
        "Vegetables"
      ]
  It is bad because the translation for the kannada word is actually okra but you gave it as eggplant.
  Some words are not in the same group.
  
      
      `

  const completion = await groq.chat.completions.create({
    messages: [{ role: "user", content: prompt }],
    model: "mixtral-8x7b-32768",
  })

  return JSON.parse(completion.choices[0]?.message?.content || "{}")
}

