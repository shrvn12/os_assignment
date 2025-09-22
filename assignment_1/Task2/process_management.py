import os
import sys

def create_children_with_exec(n, command):
    children_pids = []

    for i in range(n):
        try:
            pid = os.fork()
        except OSError as e:
            print(f"Fork failed: {e}", file=sys.stderr)
            sys.exit(1)

        if pid == 0:
            print(f"\n[Child {i+1}] PID={os.getpid()}, Parent PID={os.getppid()}, executing command: {' '.join(command)}\n")
            try:
                os.execvp(command[0], command)  
            except FileNotFoundError:
                print(f"Command not found: {command[0]}", file=sys.stderr)
                os._exit(1)
        else:
            children_pids.append(pid)
            
    for _ in children_pids:
        pid, status = os.wait()
        if os.WIFEXITED(status):
            print(f"[Parent] Child PID={pid} exited with status {os.WEXITSTATUS(status)}")
        else:
            print(f"[Parent] Child PID={pid} terminated abnormally")

def main():
    try:
        n = int(input("Enter the number of child processes: "))
        if n <= 0:
            print("Number of processes must be positive.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    command = input("Enter the Linux command to execute (e.g., 'ls -l'): ").split()

    print(f"\n[Parent] PID={os.getpid()} creating {n} children to run: {' '.join(command)}\n")
    create_children_with_exec(n, command)

if __name__ == "__main__":
    main()
