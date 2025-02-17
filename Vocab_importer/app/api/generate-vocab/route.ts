import { Groq } from "groq-sdk";
import { StreamingTextResponse } from "ai";

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY!,
});

export async function POST(req: Request) {
  const { messages } = await req.json();

  const response = await groq.chat.completions.create({
    messages,
    model: "mixtral-8x7b-32768",
    temperature: 0.7,
    stream: true,
  });

  return new StreamingTextResponse(response.stream());
} 