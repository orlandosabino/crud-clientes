"""
Client Management System (CRUD) — Python
=========================================

A command-line application to manage client records using
object-oriented programming (OOP) and in-memory storage.

Features:
    - Create: register new clients with auto-generated IDs
    - Read:   list all clients or search by ID
    - Update: edit name, email, or phone
    - Delete: remove a client with confirmation

Author: [Orlando Sabino]
Date:   [11/2026]
Purpose: Portfolio project — AI Trainer transitioning to Python developer.
"""

# ============================================================
#  MODEL
# ============================================================

class Client:
    """Represents a single client in the system."""

    def __init__(self, client_id: int, name: str, email: str, phone: str):
        """
        Initialize a new client.

        Args:
            client_id: Unique identifier (auto-generated).
            name:      Full name of the client.
            email:     Contact email address.
            phone:     Contact phone number.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self) -> str:
        """Return a readable representation used by print()."""
        return (f"ID: {self.client_id} | "
                f"Name: {self.name} | "
                f"Email: {self.email} | "
                f"Phone: {self.phone}")


# ============================================================
#  APPLICATION STATE
# ============================================================

clients: list[Client] = []      # In-memory storage
next_id: int = 1                # Auto-incrementing ID counter


# ============================================================
#  CRUD OPERATIONS
# ============================================================

def create_client() -> None:
    """Prompt the user for data and add a new client."""
    global next_id

    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.\n")
        return

    email = input("Email: ").strip()
    phone = input("Phone: ").strip()

    new_client = Client(next_id, name, email, phone)
    clients.append(new_client)
    next_id += 1

    print(f"Client '{name}' registered with ID {new_client.client_id}.\n")


def list_clients() -> None:
    """Print all registered clients."""
    if not clients:
        print("No clients registered yet.\n")
        return

    print("\n--- CLIENT LIST ---")
    for client in clients:
        print(client)
    print(f"\nTotal: {len(clients)} client(s).\n")


def find_client_by_id(client_id: int) -> Client | None:
    """
    Return the client with the given ID, or None if not found.

    Args:
        client_id: The ID to search for.
    """
    for client in clients:
        if client.client_id == client_id:
            return client
    return None


def update_client() -> None:
    """Prompt for an ID and update the matching client's fields."""
    if not clients:
        print("No clients to update.\n")
        return

    list_clients()

    try:
        client_id = int(input("Enter the client ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.\n")
        return

    client = find_client_by_id(client_id)
    if not client:
        print(f"Client with ID {client_id} not found.\n")
        return

    print("Leave a field empty to keep its current value.\n")

    new_name = input(f"New name ({client.name}): ").strip()
    new_email = input(f"New email ({client.email}): ").strip()
    new_phone = input(f"New phone ({client.phone}): ").strip()

    if new_name:
        client.name = new_name
    if new_email:
        client.email = new_email
    if new_phone:
        client.phone = new_phone

    print("Client updated successfully.\n")


def delete_client() -> None:
    """Prompt for an ID and delete the matching client after confirmation."""
    if not clients:
        print("No clients to delete.\n")
        return

    list_clients()

    try:
        client_id = int(input("Enter the client ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.\n")
        return

    client = find_client_by_id(client_id)
    if not client:
        print(f"Client with ID {client_id} not found.\n")
        return

    confirm = input(f"Delete client '{client.name}'? (y/n): ").strip().lower()
    if confirm == "y":
        clients.remove(client)
        print("Client deleted successfully.\n")
    else:
        print("Operation cancelled.\n")


# ============================================================
#  USER INTERFACE
# ============================================================

MENU = """
========================================
     CLIENT MANAGEMENT SYSTEM
========================================
1 - Add client
2 - List clients
3 - Update client
4 - Delete client
0 - Exit
"""


def show_menu() -> None:
    """Print the main menu."""
    print(MENU)


def main() -> None:
    """Run the main application loop."""
    print("Welcome to the Client Management System!")

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_client()
        elif choice == "2":
            list_clients()
        elif choice == "3":
            update_client()
        elif choice == "4":
            delete_client()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


# ============================================================
#  ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()