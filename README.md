# 💤 Bedtime Story Generator (Ages 5–10)

This Python project generates a creative and age-appropriate bedtime stories for children ages 5–10.  
It features a **storytelling agent**, a **judge agent**, and a **refinement agent** that improves stories based on feedback.

---
## 🚀 Features
- **Story Request Input**: Any story idea can be submitted.  
- **Category Selection**: User can manually pick a category, or let the LLM classify automatically.  
  Categories include: Action/Adventure, Calming, Silly, Fantasy, Emotional.  
- **Story Generation**: The Storyteller agent generates a story following age-appropriate rules.  
- **Judging Options**:  
  - **LLM Judge**: Automatic scoring, critique, and suggested improvements.  
  - **User Judge**: Manual score, critique, and improvements.  
- **Refinement Agent**: Uses feedback to rewrite and improve the story while preserving its original idea.  

---

## 🛠 Requirements

- Python 3.10+  
- OpenAI Python SDK: `pip install openai`  
- OpenAI API Key stored as environment variable:

---

## Block Diagram

┌───────────────────────────┐
│        User Input         │
│  - Story request          │
│  - Category (optional)    │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│   Category Agent          │
│ - If user provides, use it│
│ - If auto, LLM classifies │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│   Storyteller Agent       │
│ - Generates initial story │ │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│    Judge Selection        │
│ - LLM Judge               │
│ - User Judge              │
└─────────────┬─────────────┘
              │
   ┌──────────┴──────────┐
   │                     │
   ▼                     ▼
┌───────────────┐   ┌───────────────┐
│  LLM Judge    │   │  User Judge   │
│ - JSON score  │   │ - Manual score│
│ - Critique    │   │ - Critique    │
│ - Improvements│   │ - Improvements│
└──────┬────────┘   └──────┬────────┘
       │                   │
       └──────────┬────────┘
                  ▼
       ┌─────────────────────┐
       │ Refinement Agent    │
       │ - Uses feedback     │
       │   (LLM or user)     │
       │ - Produces improved │
       │   story             │
       └─────────┬───────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Final Output     │
        │ - Improved story │
        │ - Feedback info  │
        └──────────────────┘

---

# ▶️ Running the Program
Run: python main.py

Follow the prompts:
1. Enter your story idea/request.
2. Choose a category (LLM Auto or manual).
3. Receive generated story.
4. Choose judging method (LLM or manual).
5. Provide or review feedback.
6. Receive newly refined story based on feedback

---

# 🎉 Example Output
✨ Welcome to the Storyteller Generator ✨

What kind of story do you want to hear? > A story about a rainy day. There are two charaters: Toriel and Frisk. Toriel is a goat mother and Frisk and is a human child. Toriel has adopted Frisk and is working on getting Frisk to warm up to her. She loves making butterscotch pie.

Do you want to:
1. Enter a category yourself
2. Let the LLM categorize your request
Choose 1 or 2 > 2

LLM categorized your story as: **Emotional**

🎉 Your Story is Ready! 🎉

Once upon a time, on a rainy day, Toriel the goat mother and Frisk the human child were inside their cozy home. Toriel had adopted Frisk and was trying her best to make Frisk feel loved and comfortable. Despite her efforts, Frisk was still a bit hesitant to warm up to Toriel. 

As the rain pitter-pattered against the windows, Toriel decided to bake Frisk's favorite butterscotch pie. The sweet aroma filled the house, and soon enough, Frisk couldn't resist the delicious treat. With a warm slice of pie in hand, Toriel and Frisk sat by the fireplace, sharing giggles and stories. In that moment, Frisk realized that home wasn't just a place but also a feeling of love and warmth. And Toriel knew that love takes time to grow but is always worth the wait. And so, on that rainy day, their bond grew stronger, one slice of pie at a time.

Who should judge the story?
1. LLM Judge
2. You
Choose 1 or 2 > 1

🤖 LLM Judge Results:
 {
    "score": {
        "Clarity": 8,
        "Imagination": 7,
        "Age appropriateness": 9,
        "Emotional warmth": 9,
        "Story structure": 8
    },
    "critique": "Overall, the story is well-written and engaging for children. It effectively conveys the message of love and bonding. However, there could be more vivid descriptions to enhance the imagination of the young readers.",
    "improvements": [
        "Add more descriptive language to create a more vivid picture in the reader's mind",
        "Consider adding more dialogue between Toriel and Frisk to further develop their relationship",
        "Ensure a consistent flow in the story structure to keep the young readers engaged"
    ]
}

We have taken in feedback for the story! Here is a new and improved story based on given feedback

🌟 Improved Story 🌟

Once upon a time, on a rainy afternoon, Toriel the gentle goat mother and Frisk the curious human child found themselves cozied up in their quaint home. Toriel, who had lovingly taken Frisk under her care, was determined to show the child the warmth of a true home. Despite Frisk's initial hesitance, Toriel's kind gestures slowly began to melt away the walls around the child's heart.

As the raindrops danced against the window panes, Toriel decided to whip up a batch of Frisk's favorite butterscotch pie. The sweet scent wafted through the air, drawing Frisk closer to the kitchen with eager anticipation. With a steaming slice of pie in hand, Toriel and Frisk settled by the crackling fireplace, their laughter filling the room. In that moment, Frisk felt a sense of belonging and love that transcended mere words. And Toriel, with a knowing smile, understood that true bonds are nurtured with patience and care, just like a pie that bakes slowly to perfection. And so, as the rain continued to pour outside, their hearts grew closer with each shared moment, creating a home filled with love and warmth.