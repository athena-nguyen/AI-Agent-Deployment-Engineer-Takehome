import os
import json
from openai import OpenAI

"""
Before submitting the assignment, describe here in a few sentences what you would have built next if you spent 2 more hours on this project:

I would like to implement a way to have the user to continue refining the story until they are satisfied. 
I would also like to implement more refined prompts for generating the story. For refined prompts I would've loved to talk to real children book authors to better understand what makes a children's story good.
Also if I had more time I would like to have implemented some fun illustrations to accompany the stories.

"""

# ---------------------------------------------------------
# Base model call — DO NOT CHANGE THE MODEL (assignment rule)
# ---------------------------------------------------------
def call_model(prompt: str, max_tokens=3000, temperature=0.1) -> str:
    OPENAI_API_KEY = "Add key here"
    client = OpenAI(
    # This is the default and can be omitted
        api_key=os.getenv(OPENAI_API_KEY)
    )
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        stream=False,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message.content # type: ignore

example_requests = "A story about a girl named Alice and her best friend Bob, who happens to be a cat."

# -----------------------------
# Category Classifier (Auto Mode)
# -----------------------------
def categorize_request(request: str) -> str:
    prompt = f"""
        You classify story requests into one of the following categories:
        - Action/Adventure
        - Calming
        - Silly
        - Fantasy
        - Emotional

        Return ONLY the category name.

        Request: "{request}"
        """
    category = call_model(prompt)
    return category.strip()

# -----------------------------
# Storytelling Agent
# -----------------------------
def storyteller_agent(request: str, category: str) -> str:
    prompt = f"""
        You are a children's storyteller specializing in stories for ages 5–10.

        Write a **fun, engaging story** based on the request:
        "{request}"

        Story Category: {category}

        Rules:
        - Keep it appropriate for ages 5 to 10
        - Use imagination, warmth, and emotion
        - Keep the story simple and easy to follow
        - Include a soft moral lesson
        - If there are characters make them fun and relatable to the child reader
        - Make sure the vocabulary used are common words in a typical word bank for a child between the ages 5 to 10
        - The story needs to be written in 1 to 2 paragraphs

        Return ONLY the story text.
        """
    story = call_model(prompt, temperature=0.8)
    return story.strip()

# -----------------------------
# LLM Judge Agent
# -----------------------------
def judge_agent(story: str) -> dict:
    prompt = f"""
        You are a strict children's story quality judge.

        Evaluate the following story for ages 5 to 10:

        STORY:
        \"\"\"{story}\"\"\"

        Score the story from 1 to 10 on:
        - Clarity
        - Imagination
        - Age appropriateness
        - Emotional warmth
        - Story structure

        Provide:
        - A short critique
        - A list of improvements the storyteller should make

        Return ONLY valid JSON with keys:
        "score", "critique", "improvements"
        """
    judge_raw = call_model(prompt)

    # Try to parse JSON
    try:
        return json.loads(judge_raw)
    except Exception:
        return {
            "score": 5,
            "critique": "LLM returned invalid JSON.",
            "improvements": []
        }
    
# -----------------------------
# User Judge Option
# -----------------------------
def user_judge(story: str) -> dict:
    print("\nHere is your story! Please judge it.\n")
    print("--------------------------------------------------")
    print(story)
    print("--------------------------------------------------")

    score = input("\nOn a scale of 1–10, how good was the story? > ")
    critique = input("What feedback would you give? > ")
    improvements = input("List any improvements you'd suggest. (Comma separated) > ")

    return {
        "score": score,
        "critique": critique,
        "improvements": improvements.split(",")
    }

# ----------------------------
#  Story Refinement Agent
#  (Uses either user or LLM feedback)
# ----------------------------
def refinement_agent(original_story: str, feedback: dict) -> str:
    prompt = f"""
        You are a story refinement agent.

        Your job is to improve the story based on the following feedback:

        FEEDBACK:
        Score: {feedback.get("score")}
        Critique: {feedback.get("critique")}
        Improvements: {feedback.get("improvements")}

        Original Story:
        \"\"\"{original_story}\"\"\"

        Rewrite the story with better:
        - clarity
        - imagination
        - emotions
        - structure
        - age-appropriate language
        - character development

        Keep it appropriate for ages 5 to 10.
        Preserve the main idea but improve overall quality.

        Write 1 to 2 paragraphs.
        """
    return call_model(prompt)


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    print("\n✨ Welcome to the Storyteller Generator ✨\n")

    # User request
    user_request = input("What kind of story do you want to hear? > ")

    # Category choice
    print("\nDo you want to:")
    print("1. Enter a category yourself")
    print("2. Let the LLM categorize your request")
    category_choice = input("Choose 1 or 2 > ")

    if category_choice == "1":
        user_category = input("Enter your own category: > ")
        category = user_category.strip()
    else:
        category = categorize_request(user_request)
        print(f"\nLLM categorized your story as: **{category}**")

    # Generate the story
    story = storyteller_agent(user_request, category)
    print("\n🎉 Your Story is Ready! 🎉\n")
    print(story)

    # Judge Choice
    print("\nWho should judge the story?")
    print("1. LLM Judge")
    print("2. You")
    judge_choice = input("Choose 1 or 2 > ")

    if judge_choice == "1":
        result = judge_agent(story)
        print("\n🤖 LLM Judge Results:\n", json.dumps(result, indent=4))
    else:
        result = user_judge(story)
        print("\n🧑 Your Judgement:\n", json.dumps(result, indent=4))

    # Refine story
    print("\nWe have taken in feedback for the story! Here is a new and improved story based on given feedback")
    improved_story = refinement_agent(story, result)
    print("\n🌟 Improved Story 🌟\n")
    print(improved_story)



if __name__ == "__main__":
    main()