import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def main():
    print("Hello from langchain-course!")
    print("Your OpenAI API Key is:", os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
