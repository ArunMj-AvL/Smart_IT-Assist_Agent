# Smart IT Helpdesk Agent

An Agentic AI based Smart IT Helpdesk system that automatically identifies common IT problems, selects the appropriate troubleshooting tool, attempts to resolve the issue, stores ticket information, and escalates unresolved issues to human IT support.

---

## 1. Project Title

**Smart IT Helpdesk Agent**

An Agentic AI based system for automated IT issue troubleshooting and support ticket management.

---

## 2. Business Problem

Employees frequently face common IT problems such as:

* Password and login issues
* Wi-Fi and network problems
* Slow or hanging laptops
* Application and software issues

In a traditional IT helpdesk, employees may need to contact support staff even for simple and repetitive problems. This increases the workload of IT support teams and can result in longer response times.

The Smart IT Helpdesk Agent provides an automated first level of support by identifying the employee's problem and performing appropriate troubleshooting steps.

---

## 3. Why an Agent is Useful for This Problem

An agent is useful because the system does not simply provide a fixed response to the user.

The agent:

* Observes the user's problem description
* Classifies the issue
* Decides which troubleshooting tool should be used
* Performs the selected troubleshooting action
* Evaluates whether the problem was resolved
* Uses an alternative troubleshooting path when the first attempt fails
* Escalates the issue to human support when automated troubleshooting is unsuccessful
* Stores ticket information and actions in persistent memory

This makes the system more dynamic and decision-oriented than a simple input-and-response application.

---

## 4. Agent Goal

The main goal of the Smart IT Helpdesk Agent is to:

> **Automatically identify and troubleshoot common employee IT problems, resolve them through appropriate automated actions whenever possible, maintain ticket history, and escalate unresolved problems to human IT support.**

The system aims to reduce repetitive IT support work and provide faster first-level assistance to employees.

---

## 5. Architecture

The project follows a modular architecture consisting of an input layer, classification layer, agent/controller layer, troubleshooting tools, and persistent memory.

```text
                         USER
                           |
                           v
                       main.py
                           |
                           v
                    classifier.py
                           |
                    Detected Issue
                           |
                           v
                       agent.py
                    Agent Controller
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
       Three_Tools.py  Troubleshooting  Escalation
             |
     +-------+-------+-------+---------+
     |       |       |       |         |
     v       v       v       v         v
 Password  Network Performance Application Unknown
   Tool      Tool      Tool      Tool      Tool
     |       |       |       |         |
     +-------+-------+-------+---------+
                           |
                           v
                       memory.py
                           |
                           v
                      memory.json
```

### Project Components

| File             | Responsibility                                                                                                    |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| `main.py`        | Takes user input, validates the User ID, and starts the helpdesk process                                          |
| `classifier.py`  | Classifies the user's problem into an issue category                                                              |
| `agent.py`       | Acts as the main controller and makes decisions about ticket creation, tool selection, resolution, and escalation |
| `Three_Tools.py` | Contains the troubleshooting and escalation tools                                                                 |
| `memory.py`      | Provides functions for reading and updating users and support tickets                                             |
| `memory.json`    | Stores persistent user and ticket information                                                                     |
| `README.md`      | Contains project documentation                                                                                    |

---

## 6. Agent Workflow

The Smart IT Helpdesk Agent follows the workflow:

```text
Observe
   ↓
Classify
   ↓
Create Ticket
   ↓
Decide / Select Tool
   ↓
Perform Troubleshooting
   ↓
Evaluate Result
   ↓
 ┌───────────────┐
 │               │
Success        Failure
 │               │
 ↓               ↓
Resolve       Escalate
 │               │
 └───────┬───────┘
         ↓
     Store State
```

### Detailed Workflow

1. The employee enters their User ID.
2. The system verifies the User ID using `memory.json`.
3. The employee describes their IT problem.
4. `classifier.py` analyzes the description.
5. The issue is classified as:

   * `LOGIN ISSUE`
   * `NETWORK`
   * `PERFORMANCE`
   * `APPLICATION`
   * `UNKNOWN`
6. `agent.py` creates a support ticket with a unique Ticket ID.
7. The agent selects the appropriate troubleshooting tool.
8. The selected tool performs troubleshooting actions.
9. The user indicates whether the problem has been resolved.
10. If successful, the ticket is marked **Resolved**.
11. If automated troubleshooting fails, the agent escalates the ticket to human IT support.
12. The ticket status, actions taken, and solution information are stored in `memory.json`.

---

## 7. Tools / Actions

The project contains multiple tools that allow the agent to perform different actions.

### 1. Password Helper

`password_help()`

Handles password and login problems.

It performs:

* Security verification using Date of Birth, favorite color, and birthplace
* Temporary password generation
* OTP-based fallback verification
* Temporary password storage
* Success/failure evaluation

The OTP and temporary password are stored in `memory.json` for the prototype.

---

### 2. Network Troubleshooter

`network_help()`

Handles Wi-Fi and internet problems.

It provides:

**Attempt 1:**

* Turn Wi-Fi off and on
* Disconnect from VPN
* Reconnect to Wi-Fi

**Attempt 2:**

* Restart the network adapter
* Forget and reconnect to Wi-Fi
* Restart the computer

If the problem remains unresolved, the agent escalates the issue.

---

### 3. Performance Optimizer

`performance_help()`

Handles slow or hanging laptop problems.

It provides:

**Attempt 1:**

* Close unused applications
* Close unnecessary browser tabs
* Restart the laptop

**Attempt 2:**

* Open Task Manager
* Check applications using high CPU or RAM
* Close unnecessary applications

---

### 4. Application Troubleshooter

`application_help()`

Handles application and software problems.

It provides:

**Attempt 1:**

* Close and reopen the application
* Check whether the application is responding
* Check for updates

**Attempt 2:**

* Restart the computer
* Check for pending updates
* Repair or reinstall the application
* Open the application again

---

### 5. Human Escalation

`escalate_to_human()`

This tool is used when automated troubleshooting cannot resolve the problem.

The system:

* Identifies that automated troubleshooting failed
* Displays the issue type
* Records the number of attempts
* Escalates the problem to human IT support
* Updates the ticket status to `Escalated`

---

### 6. Unknown Issue Handler

`unknown_help()`

Handles problems that cannot be identified by the current classifier.

The system records that the issue could not be classified and recommends escalation to human IT support.

---

## 8. Memory / State

The project uses a simple JSON-based persistent memory system instead of a database.

### `memory.py`

`memory.py` provides functions to manage users and support tickets, including:

* `add_user()`
* `get_user()`
* `update_user()`
* `delete_user()`
* `add_ticket()`
* `get_ticket()`
* `update_ticket()`
* `delete_ticket()`

### `memory.json`

The JSON file stores:

#### User information

* User ID
* Name
* Email
* Department
* Role
* Date of Birth
* Favorite Color
* Birthplace
* OTP
* Temporary Password

#### Ticket information

* Ticket ID
* User ID
* Problem Type
* Problem Description
* Ticket Status
* Actions Taken
* Solution
* Escalation Status

This allows the agent to maintain state even after the current interaction has finished.

---

## 9. How to Run the Project

### Step 1: Clone the Repository

Clone the project repository from GitHub.

### Step 2: Open the Project Folder

Open the project folder in a terminal or command prompt.

### Step 3: Run the Application

Run:

```bash
python main.py
```

### Step 4: Enter User ID

For example:

```text
Enter your USER ID (or type 'exit'): USR001
```

### Step 5: Describe the IT Problem

For example:

```text
What IT issue are you experiencing?
My Wi-Fi is not working
```

The system will classify the issue and automatically select the appropriate troubleshooting tool.

### Requirements

The project uses Python and standard Python libraries. No external AI framework, database, cloud service, or UI framework is required.

---

## 10. Sample Input / Output

### Example 1 — Password Issue

**Input:**

```text
Enter your USER ID: USR001

What IT issue are you experiencing?
I forgot my password
```

**System:**

```text
Support ticket created successfully. Ticket ID: TKT123

Problem detected: LOGIN ISSUE

[IT TOOL: PASSWORD HELPER]

----Attempt 1 of 2----

Enter your Date of Birth (YYYY-MM-DD):
Enter your Favorite Color:
Enter your Birthplace / Hometown:

Security verification passed successfully!

Temporary password generated: TempPass#1234

Were you able to log in with this temporary password? (yes/no):
```

If successful:

```text
Issue resolved successfully.

Ticket completed successfully.
```

---

### Example 2 — Network Issue

**Input:**

```text
User ID: USR002

Problem:
My Wi-Fi is not working
```

**System:**

```text
Problem detected: NETWORK

[IT TOOL: NETWORK TROUBLESHOOTER]

----Attempt 1 of 2----

Step 1: Basic Network Troubleshooting

-> Turn Wi-Fi OFF and ON.
-> Disconnect from VPN.
-> Reconnect to the Wi-Fi network.

Did this resolve your internet issue? (yes/no):
```

If the first attempt fails, the system proceeds to the advanced troubleshooting path.

---

### Example 3 — Escalation

If automated troubleshooting fails:

```text
--- Automatic Resolution Failed ---

======================================
       HUMAN SUPPORT ESCALATION
======================================

Automated troubleshooting could not resolve the problem.

-> Escalating the issue to human IT support.
-> A support technician will contact the employee.
```

The ticket is then stored with:

```text
Status: Escalated
Escalated: true
```

---

## 11. Limitations

The current prototype has the following limitations:

* Issue classification is keyword-based rather than using a real Large Language Model.
* Troubleshooting actions are simulated through instructions and user responses.
* The system does not directly interact with real employee computers or network devices.
* OTP and temporary passwords are stored in `memory.json` for demonstration purposes and are not suitable for a production security system.
* JSON storage is suitable for a small prototype but is not ideal for a large-scale IT helpdesk.
* The system currently supports a limited number of IT issue categories.
* There is no integration with real enterprise systems such as ServiceNow, email systems, Active Directory, or network monitoring platforms.

---

## 12. Future Improvements

The project can be improved by adding:

* LLM-based intelligent issue classification
* More IT troubleshooting tools
* Real-time system and network diagnostics
* Integration with ServiceNow or other ticketing systems
* Database-based persistent memory
* Email or notification support
* Integration with Active Directory for account management
* Automatic log collection and analysis
* More advanced multi-step agent decision-making
* Human-in-the-loop support
* Authentication and secure OTP handling
* Dashboard and reporting capabilities

---

## Agentic AI Concept

The key agentic behavior of this project can be summarized as:


Observe
   ↓
Classify
   ↓
Decide
   ↓
Act
   ↓
Evaluate
   ↓
Resolve / Escalate
   ↓
Store
```

Unlike a simple system that follows:

User Input → Response
```

the Smart IT Helpdesk Agent makes decisions about **which action to perform, evaluates the result, follows alternative paths when necessary, and determines when to stop or escalate the task.**

---

## Conclusion

The Smart IT Helpdesk Agent demonstrates how an agent-based approach can automate first-level IT support. The system combines issue classification, decision-making, multiple troubleshooting tools, persistent memory, ticket management, and human escalation into a simple Python-based terminal application.

The project provides a foundation that can later be extended with LLMs, real IT integrations, databases, and more advanced autonomous troubleshooting.
