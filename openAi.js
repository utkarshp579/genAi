import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "OPENAI_API_KEY", // put API key here from env file
});

const response = openai.responses.create({
  model: "gpt-5.4-mini",
  input: "write a haiku about ai",
  store: true,
});

response.then((result) => console.log(result.output_text));
