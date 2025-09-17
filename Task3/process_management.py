import os
import time
def zombie_process():
    pid = os.fork()
    if pid == 0:
        print(f"[Child] PID={os.getpid()}, Parent PID={os.getppid()} -> Exiting now.")
        os._exit(0)
    else:
        print(f"[Parent] PID={os.getpid()}, created child PID={pid}")
        print("[Parent] Not calling wait(), sleeping... Run 'ps -el | grep defunct' to see zombie.")
        time.sleep(30)  
def orphan_process():
    pid = os.fork()
    if pid == 0:
        print(f"[Child] PID={os.getpid()}, Parent PID={os.getppid()} -> Sleeping...")
        time.sleep(20)
        print(f"[Child] PID={os.getpid()}, New Parent PID={os.getppid()} -> I am orphaned.")
    else:
        print(f"[Parent] PID={os.getpid()}, created child PID={pid} -> Exiting immediately.")
        os._exit(0)
if __name__ == "__main__":
    print("\n=== Task 3: Zombie & Orphan Processes ===")
    print("1. Zombie process demo")
    print("2. Orphan process demo")
    choice = input("Enter choice: ")
    if choice == "1":
        zombie_process()
    elif choice == "2":
        orphan_process()
    else:
        print("Invalid choice.")
