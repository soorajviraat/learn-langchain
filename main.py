import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()  # Load environment variables from .env file


def main():
    print("Hello from langchain-course!")

    info = """
    Mark Cuban (born July 31, 1958) is an American businessman and television personality. He is the former principal owner and current minority owner of the Dallas Mavericks of the National Basketball Association (NBA) and co-owner of 2929 Entertainment. From 2012 to 2025, he was also one of the main "sharks" on the ABC reality television series Shark Tank.[2] As of May 2025, Forbes has estimated his net worth to be US$6 billion.[3]

    Born in Pittsburgh, Pennsylvania, Cuban was involved in ventures from a young age, from selling garbage bags to running newspapers during a strike. He graduated from the Kelley School of Business at Indiana University and embarked on a diverse business career that included founding MicroSolutions and Broadcast.com, both of which he sold at substantial profits. Cuban's investments span various industries, from technology and media to sports and entertainment. He has been a prominent figure in the NBA, known for his active involvement with the Mavericks (with which he won the 2011 NBA Championship as owner), and disputes with the league's management. In his side ventures, Cuban has been involved in philanthropy, political commentary, and reality television.
    """

    summary_prompt = """
    Summarize the text {info} in a single sentence and get 2 interesting facts about the person.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["info"],
        template=summary_prompt,
    )

    llm = ChatOpenAI(model="gpt-5", temperature=0)
    # llm = ChatOllama(model="gemma3:270m", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"info": info})
    print(response.content)



if __name__ == "__main__":
    main()
