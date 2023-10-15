# AI research assistant agent
Relevant references for developing an AI research assistant agent. I searched for online projects implementing AI assistants building on LangChain and vector stores.

+ James Briggs, "Chatbots with RAG: LangChain Full Walkthrough," YouTube, September 20, 2023, <https://www.youtube.com/watch?v=LhnCsygAvzY>.
    + This ~35-minute video discusses developing the AI assistant combining LangChain and Pinecone as the cloud vector store. The vector store was built by combining arXiv papers with a strategy (self-references) that we could export. The code is unpolished, but the combination of big picture and detail is excellent. It is the best guide I found for our goals as of October 16, 2023. Use his conceptual figures as a guide for our projects. I like the brain analogies he uses.

    + James Briggs has other videos he posted in the last half a year building to this point. The content is rougher. He combined them in a playlist: [Building an AI assistant](https://www.youtube.com/playlist?list=PLIUOU7oqGTLjpy44hZWE62K3RG4RTvuWt).

+ Shane Duggan, "LangChain tutorial – How to build a custom knowledge chatbot," FreeCodeCamp, June 1, 2023, <https://www.freecodecamp.org/news/langchain-how-to-create-custom-knowledge-chatbots/>.
    + This source gives a good conceptual overview of developing a custom knowledge chatbot. The diagrams are good. The description touches on the main tools necessary. It includes code we could test as an example to complement aspects from the James Briggs tutorial case.

+ Jakub Misilo, "AI Agents tutorial: How to use and build AI agents," lablab.ai, May 16, 2023, <https://lablab.ai/t/ai-agents-tutorial-how-to-use-and-create-them>.
    + This Tutorial follows a similar structure to Duggan 2023's Tutorial, providing a great added value in using Wolfram Alpha as a tool in the agent so it can address mathematical issues. However, the overall structure of the Tutorial could be more informative on the big picture.

+ Kamal Dhungana, "Exploring LangChain chains & agents: A quick overview," Medium, September 25, 2023, <https://medium.com/@kbdhunga/exploring-langchain-chains-agents-a-quick-overview-9d0a8c4d7ba0>.
    + This Tutorial provides a detailed implementation of an agent. I like it mainly because it shows how to access all the tools directly available for an Agent in LangChain (although some need APIs).

+ Charles Suárez, "Building a Custom Chat Agent for Document QA with Langchain, GPT-3.5 and Pinecone," Medium, September 3, 2023, <https://pub.aimind.so/building-a-custom-chat-agent-for-document-qa-with-langchain-gpt-3-5-and-pinecone-e3ae7f74e5e8>
    + This Tutorial is comprehensive and provides a good structure for the AI Python package. It includes the use of Pinecone. It complements well Dhungana 2023.

+ LangChain Blog, "Chat with your data using OpenAI, Pinecone, Airbyte and LangChain," LangChain, August 8, 2023, <https://blog.langchain.dev/chat-with-your-data-using-openai-pinecone-airbyte-langchain/>
    + This Tutorial from LangChain brings the game of developing AI bots incorporating Airbyte for unstructured data.

+ Avikumar Talaviya, "Building custom Q&A applications using LangChain and Pinecone vector database," Analytics Vidhya, September 12, 2023, <https://www.analyticsvidhya.com/blog/2023/08/qa-applications/>:
    + Tutorial combining OpenAI, LangChain, and Pinecone. It includes widgets for the interaction.
    + The Analytics Vidhya site has a page in [Medium](https://medium.com/analytics-vidhya) with different articles of interest.

+ Pere Martra, "Create your data analyst assistant with LangChain agents," Towards AI, August 7, 2023, <https://towardsai.net/p/machine-learning/create-your-own-data-analyst-assistant-with-langchain-agents>.
    + Tutorial to incorporate pandas as a tool in the LangChain agent to analyze data. The implementation is fundamental. However, it is a good example to give additional functionality in the analysis.
    
