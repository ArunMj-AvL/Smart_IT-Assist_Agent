from memory import get_user, update_user
import random, string

def password_help(user_id=None):
    print("\n[IT TOOL: PASSWORD HELPER]")

    # Get the user record from memory
    user_record = get_user(user_id)

    if not user_record:
        print("-> User record not found.")
        return False

    print(
        f"Initiating verification protocol..."
    )

    # ========================================================
    # ATTEMPT 1: SECURITY QUESTIONS
    # ========================================================

    print("\n----Attempt 1 of 2----")
    print("\n[Attempt 1: Security Verification]")

    dob_input = input(
        "Enter your Date of Birth (YYYY-MM-DD): "
    ).strip()

    color_input = input(
        "Enter your Favorite Color: "
    ).strip().capitalize()

    place_input = input(
        "Enter your Birthplace / Hometown: "
    ).strip().capitalize()
    actions = ["Performed basic security verification using DOB, favorite color, and birthplace.",]
    questions_correct = (
        dob_input == user_record.get("dob") and
        color_input == user_record.get(
            "fav_color", ""
        ).capitalize() and
        place_input == user_record.get(
            "place", ""
        ).capitalize()
    )

    # ========================================================
    # SECURITY VERIFICATION SUCCESS
    # ========================================================

    if questions_correct:

        print(
            "\n-> Security verification passed successfully!"
        )

        # Generate temporary password
        temp_pass = (
            "TempPass#"
            + "".join(
                random.choices(
                    string.digits,
                    k=4
                )
            )
        )

        print(
            f"-> Temporary password generated: {temp_pass}"
        )

        # Store temporary password in memory.json
        update_user(
            user_id,
            {
                "temporary_password": temp_pass
            }
        )

        success = input(
            "Were you able to log in with this temporary password? "
            "(yes/no): "
        ).strip().lower()


        if success == "yes":
            solution = "Password reset successful via security verification."
            
            return True, solution, actions

        print(
            "-> Attempt 1 failed to resolve the issue."
        )
        

    else:

        print(
            "-> Verification failed: One or more security "
            "answers do not match company records."
        )

    # ========================================================
    # ATTEMPT 2: OTP FALLBACK
    # ========================================================

    print("\n----Attempt 2 of 2----")
    print("\n[Attempt 2: OTP Fallback Protocol]")

    print(
        "-> Generating One-Time Password (OTP)..."
    )
    actions.append("Performed OTP fallback verification after security questions failed.")

    email_input = input(
        "Enter your registered email to receive the OTP : "
    )
    email_record = user_record.get("email", "")
    if email_input.strip().lower() != email_record.lower():
        email_input = input(
                "\nEnter valid registered email to receive the OTP : "
            )
        if email_input.strip().lower() != email_record.lower():
                print(
                    "-> Error: The entered email does not match our records."
                )
                solution = "Password reset failed due to email mismatch during OTP fallback. Escalation to human support is recommended."
                return False, solution, actions
        else:
                print(
                    "\n-> Email verified successfully."
                )


                
    # Generate 4-digit OTP
    otp_code = "".join(
        random.choices(
            string.digits,
            k=4
        )
    )

    # Store OTP in memory.json
    update_user(
        user_id,
        {
            "otp": otp_code
        }
    )

    # Display OTP for demonstration
    print(
        f"-> [SIMULATED OTP]: {otp_code}"
    )

    otp_input = input(
        "Please enter the OTP provided by the system: "
    ).strip()

    # ========================================================
    # OTP VERIFICATION
    # ========================================================

    if otp_code == otp_input:

        print(
            "-> OTP verified successfully!"
        )

        # Generate temporary password
        temp_pass = (
            "TempPass#"
            + "".join(
                random.choices(
                    string.digits,
                    k=4
                )
            )
        )

        print(
            f"-> Temporary password generated: {temp_pass}"
        )

        # Store temporary password in memory.json
        update_user(
            user_id,
            {
                "temporary_password": temp_pass
            }
        )

        success = input(
            "Were you able to log in with this temporary password? "
            "(yes/no): "
        ).strip().lower()

        if success == "yes":
            solution = "Password reset successful via OTP verification."
            return True, solution, actions

        print(
            "-> Attempt 2 failed to resolve the issue."
        )
        solution = "Password reset failed after OTP verification. Escalation to human support is recommended."
        return False, solution, actions

    else:

        print(
            "-> Error: Invalid OTP entered."
        )
        solution = "Password reset failed due to invalid OTP. Escalation to human support is recommended."
        return False, solution, actions




# ============================================================
# 2. NETWORK HELP TOOL
# ============================================================

def network_help(user_id=None):
    """
    Tool for solving Wi-Fi and internet problems.
    """

    print("\n[IT TOOL: NETWORK TROUBLESHOOTER]")

    # -----------------------------
    # STEP 1
    # -----------------------------
    print("----Attempt 1 of 2----")
    print("\nStep 1: Basic Network Troubleshooting")

    print("-> Turn Wi-Fi OFF and ON.")
    print("-> Disconnect from VPN.")
    print("-> Reconnect to the Wi-Fi network.")
    actions = ["Performed basic network troubleshooting steps: toggled Wi-Fi, disconnected VPN, and reconnected to Wi-Fi."]
    success = input(
        "Did this resolve your internet issue? (yes/no): "
    ).strip().lower()

    if success == "yes":
        solution= "Basic network troubleshooting was successful."

        return True, solution, actions

    else:

        # -----------------------------
        # STEP 2
        # -----------------------------

        print("\nStep 1 was not successful.")
        print("----Attempt 2 of 2----")
        print("\nStep 2: Advanced Network Troubleshooting")

        print("-> Restart the network adapter.")
        print("-> Forget and reconnect to Wi-Fi.")
        print("-> Restart the computer.")
        actions.append("Performed advanced network troubleshooting steps: restarted network adapter, forgot and reconnected to Wi-Fi, and restarted the computer.")

        success = input(
            "Did this resolve your internet issue? (yes/no): "
        ).strip().lower()

        if success == "yes":
            solution= "Advanced network troubleshooting was successful."
            return True, solution, actions
        else:
            solution = "Network troubleshooting failed. Escalation to human support is recommended."
            return False, solution, actions


# ============================================================
# 3. PERFORMANCE HELP TOOL
# ============================================================

def performance_help(user_id=None):
    """
    Tool for solving slow laptop problems.
    """

    print("\n[IT TOOL: PERFORMANCE OPTIMIZER]")

    # -----------------------------
    # STEP 1
    # -----------------------------
    print("----Attempt 1 of 2----")

    print("\nStep 1: Basic Performance Troubleshooting")

    print("-> Close unused applications.")
    print("-> Close unnecessary browser tabs.")
    print("-> Restart the laptop.")
    actions = ["Performed basic performance troubleshooting steps: closed unused applications, closed unnecessary browser tabs, and restarted the laptop."]

    success = input(
        "Did this improve your laptop performance? (yes/no): "
    ).strip().lower()

    if success == "yes":
        solution= "Basic performance troubleshooting was successful."

        return True, solution, actions
    

    else:

        # -----------------------------
        # STEP 2
        # -----------------------------

        print("\nStep 1 was not successful.")
        print("----Attempt 2 of 2----")
        print("\nStep 2: Advanced Performance Troubleshooting")

        print("-> Open Task Manager.")
        print("-> Check applications using high CPU or RAM.")
        print("-> Close unnecessary applications.")
        actions.append("Performed advanced performance troubleshooting steps: opened Task Manager, checked applications using high CPU or RAM, and closed unnecessary applications.")

        success = input(
            "Did this resolve your laptop speed issue? (yes/no): "
        ).strip().lower()

        if success == "yes":
            solution= "Advanced performance troubleshooting was successful."
            return True, solution, actions
        else:
            solution = "Performance troubleshooting failed. Escalation to human support is recommended."
            return False, solution, actions


def application_help(user_id=None):

    print("\n[IT TOOL: APPLICATION TROUBLESHOOTER]")

    # -----------------------------
    # STEP 1
    # -----------------------------
    print("----Attempt 1 of 2----")
    print("\nStep 1: Basic Application Troubleshooting")

    application = input(
    "Which application is having the problem? "
    ).strip()

    print(f"-> Close and reopen {application}.")
    print("-> Check whether the application is responding.")
    print("-> Check whether the application is updated.")
    actions = [f"Performed basic application troubleshooting steps for {application}: closed and reopened the application, checked responsiveness, and checked for updates."]

    success = input(
    f"Did this resolve your {application} issue? (yes/no): "
    ).strip().lower()

    if success == "yes":
        solution = (
            f"Basic troubleshooting for {application} "
            "was successful."
        )

        return True, solution, actions

    else:

    # -----------------------------
    # STEP 2
    # -----------------------------

        print("\nStep 1 was not successful.")
        print("----Attempt 2 of 2----")
        print("\nStep 2: Advanced Application Troubleshooting")

        print(f"-> Restart the computer.")
        print(f"-> Check for pending updates for {application}.")
        print(f"-> Repair or reinstall {application}.")
        print(f"-> Open the application again.")
        actions.append(f"Performed advanced application troubleshooting steps for {application}: restarted the computer, checked for updates, repaired or reinstalled the application, and reopened the application.")

        success = input(
            f"Did this resolve your {application} issue? (yes/no): "
        ).strip().lower()

        if success == "yes":
            solution = (
                f"Advanced troubleshooting for {application} "
                "was successful."
            )

            return True, solution, actions

        else:
            solution = (
                f"Application troubleshooting for {application} "
                "failed. Escalation to human support is recommended."
            )

            return False, solution, actions




# ============================================================
# 4. HUMAN ESCALATION TOOL
# ============================================================

def escalate_to_human(issue_type, attempts):
    """
    Escalate the problem to human IT support
    when automated troubleshooting fails.
    """

    print("\n======================================")
    print("       HUMAN SUPPORT ESCALATION")
    print("======================================")

    print(
        f"Automated troubleshooting could not resolve "
        f"the '{issue_type}' problem."
    )

    print(f"Number of attempts: {attempts}")

    print("\n-> Escalating the issue to human IT support.")
    print("-> A support technician will contact the employee.")

def unknown_help(user_id=None):
    """
    Handle unknown issues that cannot be classified.
    """

    
    print("\n    UNKNOWN ISSUE DETECTED - ESCALATION REQUIRED")


    actions = ["The issue is unknown and could not be classified or resolved by automated tools. Escalation to human support is required."]

    solution = (
        "The issue is unknown and could not be classified or resolved "
        "by automated tools. Escalation to human support is required."
    )
    return False, solution, actions

    
