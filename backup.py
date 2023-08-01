import subprocess
import time
import json

def run_command_in_screen_session(session_name, command):
    try:

        # Create a detached screen session with the specified name
        subprocess.run(["screen", "-d", "-m", "-S", session_name])
        print(f"Screen session '{session_name}' created successfully.")

        # Wait for a brief moment to ensure the session is up and running
        time.sleep(1)

        # Runthe command inside the screen session
        subprocess.run(["screen", "-S", session_name, "-X", "stuff", f"{command}\n"])
        print(f"Command '{command}' executed in screen session '{session_name}'.")

    except FileNotFoundError:
        print("Error: 'screen' command not found. Make sure GNU Screen is installed.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
session_name = "test"
command_to_execute = "ls -l"
run_command_in_screen_session(session_name, command_to_execute)