
# ============================================================
# SMART IT HELPDESK AGENT
# ============================================================
#
# INDEX
# ------------------------------------------------------------
# 1. Import Required Modules
# 2. Agent Configuration
# 3. Create Support Ticket
# 4. Generate Unique Ticket ID
# 5. Select Appropriate IT Tool
# 6. Main Agent Controller
#    6.1 Ticket Creation
#    6.2 Tool Selection
#    6.3 Attempt 1
#    6.4 Attempt 2
#    6.5 Escalation
# ============================================================


# ============================================================
# 1. IMPORT REQUIRED MODULES
# ============================================================

# Import IT troubleshooting tools.
# These functions perform the actual support actions.
from Three_Tools import (
    password_help,
    network_help,
    performance_help,
    application_help,
    escalate_to_human,
    unknown_help
)

# Import the issue classification function.
# This can be used to identify the type of IT problem.
from classifier import classify_issue

# Import memory functions used to store and update ticket information.
from memory import (
    add_ticket,
    update_ticket,
    get_ticket
)

# JSON is used to read the existing ticket information
# from memory.json.
import json

# Random is used to generate a unique ticket number.
import random


# ============================================================
# 2. AGENT CONFIGURATION
# ============================================================

# Maximum number of automated troubleshooting attempts
# before the issue is escalated to human support.
MAX_ATTEMPTS = 2


# ============================================================
# 3. CREATE SUPPORT TICKET
# ============================================================

def create_ticket(ticket, user_id, issue_type, description):
    """
    Create a new IT support ticket and store it in memory.

    Parameters:
        ticket       : Unique ticket ID
        user_id      : Employee/User ID
        issue_type   : Type of IT problem
        description  : User's problem description
    """

    # Create the ticket information as a dictionary.
    ticket = {
        "ticket_id": ticket,
        "user_id": user_id,
        "problem_type": issue_type,
        "description": description,
        "status": "Open",
        "actions_taken": [],
        "solution": None,
        "escalated": False
    }

    # Store the newly created ticket in persistent memory.
    add_ticket(ticket)

    # Return the ticket ID so the agent can use it later.
    return ticket["ticket_id"]


# ============================================================
# 4. GENERATE UNIQUE TICKET ID
# ============================================================

def generate_ticket_id():

    # Open memory.json and read the existing stored data.
    with open("memory.json", "r") as file:
        memory = json.load(file)

    # Create a list to store all existing ticket IDs.
    existing_ids = []

    # Go through every existing ticket and collect its ID.
    for ticket in memory["tickets"]:
        existing_ids.append(ticket["ticket_id"])

    # Keep generating IDs until a unique one is found.
    while True:

        # Generate a random number between 1 and 999.
        number = random.randint(1, 999)

        # Create the ticket ID in the format TKT001, TKT002, etc.
        ticket_id = f"TKT{number:03d}"

        # Check whether the generated ID already exists.
        if ticket_id not in existing_ids:

            # Return the new unique ticket ID.
            return ticket_id


# ============================================================
# 5. SELECT APPROPRIATE IT TOOL
# ============================================================

def select_tool(issue_type):
    """
    Decide which IT troubleshooting tool should be used
    based on the detected issue type.
    """

    # If the problem is related to a password,
    # select the password troubleshooting tool.
    if issue_type.lower() == "login issue":
        return password_help
        

    # If the problem is related to network/Wi-Fi,
    # select the network troubleshooting tool.
    elif issue_type.lower() == "network":
        return network_help

    # If the problem is related to laptop performance,
    # select the performance troubleshooting tool.
    elif issue_type.lower() == "performance":
        return performance_help

    elif issue_type.lower() == "application":
        return application_help
    
    elif issue_type.lower() == "unknown":
        return unknown_help
    # If no matching tool is available,
    # return None.
    else:
        return None


# ============================================================
# 6. MAIN AGENT CONTROLLER
# ============================================================

def run_helpdesk_agent(user_id, issue_type, description):

    # --------------------------------------------------------
    # Display the Smart IT Helpdesk Agent header.
    # --------------------------------------------------------

    # --------------------------------------------------------
    # 6.1 CREATE TICKET
    # --------------------------------------------------------

    # Generate a unique ticket ID.
    ticket = generate_ticket_id()

    # Create and store the ticket in memory.
    ticket_id = create_ticket(
        ticket,
        user_id,
        issue_type,
        description
    )

    # Display the generated ticket ID.
    print(f"\n✓ Support ticket created successfully. Ticket ID: {ticket}")

    print("\n====================================")
    print("       --- Diagnosis in Progress ---")
    print("====================================")

    # Display the problem type detected by the system.
    print(f"\nProblem detected: {issue_type}")
    if issue_type.lower() == "unknown":
        description = input(
            "\nI couldn't identify the problem type. Please describe your issue in detail: "
        ).strip()
        issue_type = classify_issue(description)
        update_ticket(
            ticket_id,
            {
                "problem_type": issue_type,
                "description": description
            }
        )
        print(f"\nProblem detected: {issue_type}")

    


    # --------------------------------------------------------
    # 6.2 SELECT TOOL
    # --------------------------------------------------------


    # Select the appropriate troubleshooting tool
    # based on the issue type.
    tool = select_tool(issue_type)


    # If there is no suitable tool,
    # return an unknown result.
    if tool is None:

        print("\n⚠ I'm unable to determine the appropriate support tool for this issue.")

        return "unknown"



    # --------------------------------------------------------
    # 6.3 TROUBLESHOOTING ATTEMPTS
    # --------------------------------------------------------


    # Execute the selected troubleshooting tool.
    result, solution, actions = tool(user_id)

    # Record the action performed during Attempt 1.
    

    # Update the ticket memory with the action performed.
    update_ticket(
        ticket_id,
        {
            "actions_taken": actions,
            "solution": solution
        }
    )

    # Check whether the first troubleshooting attempt
    # successfully resolved the issue.
    if result==True:

        # Update the ticket status to Resolved.
        update_ticket(
            ticket_id,
            {
                "status": "Resolved",
                "solution": solution
            }
        )

        print("\n✓ Issue resolved successfully.")

        # Stop the agent because the problem is solved.
        return "resolved"



    # --------------------------------------------------------
    # 6.4 ESCALATION
    # --------------------------------------------------------

    # Both automated attempts failed.
    # The stopping condition has now been reached.
    print("\n--- Automatic Resolution Failed ---")

    # Escalate the issue to human IT support.
    escalate_to_human(
        issue_type,
        MAX_ATTEMPTS
    )

    # Update the ticket to show that it was escalated.
    update_ticket(
        ticket_id,
        {
            "status": "Escalated",
            "escalated": True,
            "solution": None
        }
    )

    # Return the final status to main.py.
    return "escalated"















# # --------------------------------------------------------
    # # 6.4 ATTEMPT 2
    # # --------------------------------------------------------

    # # Inform the user that the first attempt failed.
    # print("\n--- Attempt 1 was not successful ---")

    # print("Let's try another approach.")

    # print("\n--- Attempt 2 ---")

    # # Execute the troubleshooting tool again.
    # # This represents the second decision/action path.
    # result = tool()

    # # Record Attempt 2 in the agent's memory.
    # actions.append(
    #     f"{tool.__name__} - Attempt 2"
    # )

    # # Update the ticket with both actions.
    # update_ticket(
    #     ticket_id,
    #     {
    #         "actions_taken": actions
    #     }
    # )

    # # Check whether Attempt 2 successfully resolved the problem.
    # if result==True:

    #     # Update the ticket as resolved.
    #     update_ticket(
    #         ticket_id,
    #         {
    #             "status": "Resolved",
    #             "solution": solution
    #         }
    #     )

    #     print("\n✓ Issue resolved successfully.")

    #     # Stop the agent because the problem has been solved.
    #     return "resolved"