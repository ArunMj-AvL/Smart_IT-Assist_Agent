
from agent import run_helpdesk_agent
from memory import get_user
from classifier import classify_issue


print("\n==============================================")
print("       WELCOME TO SMART IT HELPDESK AGENT")
print("================================================")



while True:

    print("\n--------------------------------------")

    # -----------------------------
    # GET USER ID
    # -----------------------------
    user_id = input(
        "Enter your USER ID (or type 'exit'): "
    ).strip()

    # Check EXIT immediately
    if user_id.lower() == "exit":
        print("\nThank you. Goodbye!")
        break

    # -----------------------------
    # CHECK USER
    # -----------------------------
    user = get_user(user_id)

    while not user:

        print("\n⚠ User ID verification failed.")
        print("Please enter a valid User ID to continue.\n")
        print("(Check capslock and ensure you are using the correct User ID.)")
        print("\n--------------------------------------")
        user_id = input(
            "Enter your USER ID (or type 'exit'): "
        ).strip()

        # If user enters exit inside the validation loop
        if user_id.lower() == "exit":
            print("\nThank you. Goodbye!")
            exit()

        user = get_user(user_id)

    print(f"\nWelcome, {user['name']}! 👋")
    print("I'm here to help you resolve your IT issue.\n")
    # -----------------------------
    # GET PROBLEM
    # -----------------------------
    description = input(
        "What IT issue are you experiencing? \n(Describe the problem in detail or type 'exit' to quit): "
    ).strip()
    if description.lower() == "exit":
        print("\nThank you. Goodbye!")
        break
    while not description:
        print("\nPlease enter a problem.")
        description = input(
            "What IT issue are you experiencing? \n(Describe the problem in detail or type 'exit' to quit): "
        ).strip()

    # -----------------------------
    # SEND TO AGENT
    # -----------------------------
    issue_type = classify_issue(description)
    result = run_helpdesk_agent(
        user_id,
        issue_type,
        description
    )

    # -----------------------------
    # HANDLE AGENT RESULT
    # -----------------------------
    if result == "resolved":

        print("\n✓ Ticket completed successfully. Thank you, " + user['name'] + "! Goodbye!")

    elif result == "escalated":

        print("\n⚠ Your ticket has been sent to human IT support. Thank you for your patience, " + user['name'] + ". Goodbye!")

    else:

        print("Contact human IT support for further assistance, " + user['name'] + ".")


