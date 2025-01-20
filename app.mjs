import dotenv from "dotenv";
import OpenAI from "openai";
import readline from "readline";

// Load environment variables from .env file
dotenv.config();

// Initialize OpenAI with the API key from the environment variable
const openai = new OpenAI({
  apiKey: process.env.API_KEY,
});

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("Type 'exit' to end the conversation.");

const conversationLoop = async () => {
  let systemMessage = "You are a helpful assistant.";
  let conversationHistory = [{ role: "system", content: systemMessage }];

  while (true) {
    const userInput = await new Promise((resolve) => {
      rl.question("You: ", resolve);
    });


    if (userInput.toLowerCase() === "exit") {
      console.log("Goodbye!");
      break;
    }

   
    conversationHistory.push({ role: "user", content: userInput });

    try {
     
      const completion = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        messages: conversationHistory,
      });


      const assistantResponse = completion.choices[0].message.content;
      console.log(`Response: ${assistantResponse}`);

      //Convo history add
      conversationHistory.push({ role: "assistant", content: assistantResponse });
    } catch (error) {
      console.error("Error:", error.response?.data || error.message);
      break; 
    }
  }


  rl.close();
};


conversationLoop();



