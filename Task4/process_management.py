import os

def inspect_process(pid):
    status_file = f"/proc/{pid}/status"
    exe_file = f"/proc/{pid}/exe"
    fd_dir = f"/proc/{pid}/fd"

    try:
        with open(status_file, "r") as f:
            name, state, vm_size = None, None, None
            for line in f:
                if line.startswith("Name:"):
                    name = line.split()[1]
                elif line.startswith("State:"):
                    state = " ".join(line.split()[1:])
                elif line.startswith("VmSize:"):
                    vm_size = " ".join(line.split()[1:])
            print(f"Process Name : {name}")
            print(f"Process State: {state}")
            print(f"Memory Usage : {vm_size}")

        try:
            exe_path = os.readlink(exe_file)
            print(f"Executable   : {exe_path}")
        except FileNotFoundError:
            print("Executable   : [Not available]")

        try:
            fds = os.listdir(fd_dir)
            print(f"Open FDs     : {len(fds)}")
            for fd in fds:
                try:
                    target = os.readlink(os.path.join(fd_dir, fd))
                    print(f"  FD {fd} -> {target}")
                except OSError:
                    print(f"  FD {fd} -> [unavailable]")
        except FileNotFoundError:
            print("Open FDs     : [Not available]")

    except FileNotFoundError:
        print(f"Process with PID {pid} does not exist.")


if __name__ == "__main__":
    pid = input("Enter PID to inspect: ")
    if pid.isdigit():
        inspect_process(pid)
    else:
        print("Invalid PID")
