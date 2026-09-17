import json
import os


FILE_NAME = "memory.json"


# -----------------------------
# LOAD JSON
# -----------------------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return {
            "users": [],
            "tickets": []
        }

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


# -----------------------------
# SAVE JSON
# -----------------------------
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# =========================================================
# USER FUNCTIONS
# =========================================================

# ADD USER
def add_user(user):
    data = load_data()

    data["users"].append(user)

    save_data(data)

    print("User added successfully.")


# GET ONE USER
def get_user(user_id):
    data = load_data()

    for user in data["users"]:
        if user["user_id"] == user_id:
            return user

    return None


# GET ALL USERS
def get_all_users():
    data = load_data()

    return data["users"]


# EDIT USER
def update_user(user_id, updates):
    data = load_data()

    for user in data["users"]:
        if user["user_id"] == user_id:

            user.update(updates)

            save_data(data)

            
            return True

    print("User not found.")
    return False


# DELETE USER
def delete_user(user_id):
    data = load_data()

    for user in data["users"]:
        if user["user_id"] == user_id:

            data["users"].remove(user)

            save_data(data)

            print("User deleted successfully.")
            return True

    print("User not found.")
    return False


# =========================================================
# TICKET FUNCTIONS
# =========================================================

# ADD TICKET
def add_ticket(ticket):
    data = load_data()

    data["tickets"].append(ticket)

    save_data(data)



# GET ONE TICKET
def get_ticket(ticket_id):
    data = load_data()

    for ticket in data["tickets"]:
        if ticket["ticket_id"] == ticket_id:
            return ticket

    return None


# GET ALL TICKETS
def get_all_tickets():
    data = load_data()

    return data["tickets"]


# EDIT TICKET
def update_ticket(ticket_id, updates):
    data = load_data()

    for ticket in data["tickets"]:
        if ticket["ticket_id"] == ticket_id:

            ticket.update(updates)

            save_data(data)

            return True

    print("Ticket not found.")
    return False


# DELETE TICKET
def delete_ticket(ticket_id):
    data = load_data()

    for ticket in data["tickets"]:
        if ticket["ticket_id"] == ticket_id:

            data["tickets"].remove(ticket)

            save_data(data)

            print("Ticket deleted successfully.")
            return True

    print("Ticket not found.")
    return False