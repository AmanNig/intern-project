# # from intent import classify_intent
# # from tarot_reader import perform_reading

# # def main():
# #     print("🔮 Welcome to TarotTara 🔮 (type 'exit' to quit)")
# #     while True:
# #         question = input("\nAsk your question:\n> ")
# #         if question.lower() in {"exit", "quit"}:
# #             print("Goodbye! 🌟")
# #             break

# #         intent = classify_intent(question)
# #         print(f"\n✨ Intent detected: {intent}")

# #         print("\n🃏 Drawing cards and interpreting...")
# #         result = perform_reading(question, intent)

# #         if intent == "timeline":
# #            print(f"\n🔍 TarotTara says:\nCard: {result['card']}\nTimeframe: {result['date_range'][0].strftime('%b %#d')}–{result['date_range'][1].strftime('%b %#d')}\nInterpretation: {result['interpretation']}")
# #         else:
# #             cards_str = ", ".join(result['cards'])
# #             print(f"\n🔍 TarotTara says:\nCards: {cards_str}\nInterpretation: {result['interpretation']}")

# # if __name__ == "__main__":
# #     main()

# from intent import classify_intent
# from tarot_reader import perform_reading

# def main():
#     print("🔮 Welcome to TarotTara – your magical tarot guide (type 'exit' to quit)")

#     while True:
#         question = input("\n🧘 Ask your question:\n> ")
#         if question.lower() in {"exit", "quit"}:
#             print("🌙 Farewell. Trust the journey ahead.")
#             break

#         # Step 1: Classify the user's intent
#         intent = classify_intent(question)
#         print(f"\n✨ Intent detected: {intent}")

#         # Step 2: Perform tarot reading based on intent
#         print("🃏 Drawing cards and interpreting...")
#         result = perform_reading(question, intent)

#         if "error" in result:
#             print(f"⚠️ Error: {result['error']}")
#             continue

#         # Step 3: Display results
#         print("\n🔍 TarotTara says:")

#         if intent == "timeline":
#             card = result['card']
#             date_range = result['date_range']
#             print(f"Card: {card}")
#             print(f"Timeframe: {date_range[0].strftime('%B %#d')} – {date_range[1].strftime('%B %#d')}")
#             print(f"\nInterpretation:\n{result['interpretation']}")
#         else:
#             cards = result.get("cards", [])
#             print(f"Cards Drawn: {', '.join(cards)}")
#             print(f"\nInterpretation:\n{result['interpretation']}")

# if __name__ == "__main__":
#     main()

import time
from intent import classify_intent
from tarot_reader import perform_reading

def main():
    print("🔮 Welcome to TarotTara – your magical tarot guide (type 'exit' to quit)")

    while True:
        question = input("\n🧘 Ask your question:\n> ")
        if question.lower() in {"exit", "quit"}:
            print("🌙 Farewell. Trust the journey ahead.")
            break

        total_start = time.time()

        # Step 1: Classify the user's intent
        intent_start = time.time()
        intent = classify_intent(question)
        intent_duration = time.time() - intent_start
        print(f"\n✨ Intent detected: {intent} (in {intent_duration:.2f} sec)")

        # Step 2: Perform tarot reading based on intent
        print("🃏 Drawing cards and interpreting...")
        prediction_start = time.time()
        result = perform_reading(question, intent)
        prediction_duration = time.time() - prediction_start

        total_duration = time.time() - total_start

        if "error" in result:
            print(f"⚠️ Error: {result['error']}")
            continue

        # Step 3: Display results
        print("\n🔍 TarotTara says:")

        if intent == "timeline":
            card = result['card']
            date_range = result['date_range']
            print(f"Card: {card}")
            print(f"Timeframe: {date_range[0].strftime('%B %#d')} – {date_range[1].strftime('%B %#d')}")
            print(f"\nInterpretation:\n{result['interpretation']}")
        else:
            cards = result.get("cards", [])
            print(f"Cards Drawn: {', '.join(cards)}")
            print(f"\nInterpretation:\n{result['interpretation']}")

        # Step 4: Timing Summary
        print(f"\n⏱️ Timing Summary:")
        print(f"• Intent classification: {intent_duration:.2f} sec")
        print(f"• Prediction (LLM + RAG): {prediction_duration:.2f} sec")
        print(f"• Total time: {total_duration:.2f} sec")

if __name__ == "__main__":
    main()


