from detector import analyze_message


def run_single_test():
    print("=== Scam Detector ===")
    message = input("Enter a message to analyze: ")

    result = analyze_message(message)

    print("\n=== Analysis Result ===")
    print(f"Verdict: {result['verdict']}")
    print(f"Risk Score: {result['risk_score']}%")

    if result["reasons"]:
        print("Reasons:")
        for reason in result["reasons"]:
            print(f"- {reason}")
    else:
        print("No suspicious indicators found.")


def run_demo_tests():
    test_messages = [
        "Your bank account is suspended! Click here now to verify your password: http://fake-bank.com",
        "Congratulations! You are our lottery winner. Act now to claim your gift card.",
        "Hi Omar, are we still meeting tomorrow at 2 PM?",
        "Confirm your account immediately to avoid closure.",
        "Limited time payment required! Visit www.fakepay.com now!",
    ]

    print("=== Demo Test Messages ===\n")

    for i, message in enumerate(test_messages, start=1):
        result = analyze_message(message)

        print(f"Test {i}: {message}")
        print(f"Verdict: {result['verdict']}")
        print(f"Risk Score: {result['risk_score']}%")

        if result["reasons"]:
            print("Reasons:")
            for reason in result["reasons"]:
                print(f"- {reason}")
        else:
            print("No suspicious indicators found.")

        print("-" * 50)


def main():
    print("Choose an option:")
    print("1. Analyze one message")
    print("2. Run demo test set")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        run_single_test()
    elif choice == "2":
        run_demo_tests()
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()
