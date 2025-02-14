import os
import subprocess
import psutil
import platform
import shutil
from datetime import datetime


class MacOSToolkit:

    @staticmethod
    def run_shell_command(command):
        """Runs a shell command and returns the output."""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()

    @staticmethod
    def list_files_in_directory(path):
        """Lists all files in the specified directory."""
        return os.listdir(path)

    @staticmethod
    def get_system_info():
        """Returns basic system information like macOS version."""
        system_info = {
            'OS': platform.system(),
            'macOS Version': platform.mac_ver()[0],
            'Processor': platform.processor(),
            'Architecture': platform.architecture()[0]
        }
        return system_info

    @staticmethod
    def check_disk_usage(path="/"):
        """Checks the disk usage for a specific path."""
        usage = shutil.disk_usage(path)
        return {
            'Total': usage.total,
            'Used': usage.used,
            'Free': usage.free,
            'Percent': usage.percent
        }

    @staticmethod
    def get_running_processes():
        """Returns a list of running processes."""
        processes = []
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            processes.append(proc.info)
        return processes

    @staticmethod
    def get_uptime():
        """Returns the system uptime in a human-readable format."""
        uptime_seconds = psutil.boot_time()
        uptime = datetime.fromtimestamp(uptime_seconds)
        return uptime.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def create_directory(path):
        """Creates a new directory if it does not exist."""
        try:
            os.makedirs(path, exist_ok=True)
            return f"Directory {path} created successfully."
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def check_if_file_exists(file_path):
        """Checks if a file exists."""
        return os.path.exists(file_path)

    @staticmethod
    def copy_file(source, destination):
        """Copies a file from source to destination."""
        try:
            shutil.copy(source, destination)
            return f"File copied from {source} to {destination}."
        except FileNotFoundError:
            return "Source file not found."
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def kill_process(pid):
        """Kills a process given its PID."""
        try:
            process = psutil.Process(pid)
            process.terminate()
            return f"Process {pid} terminated."
        except psutil.NoSuchProcess:
            return f"Process with PID {pid} not found."
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def get_mac_address():
        """Returns the MAC address of the primary network interface."""
        interfaces = psutil.net_if_addrs()
        for interface in interfaces:
            if psutil.net_if_stats()[interface].isup:
                for snic in interfaces[interface]:
                    if snic.family == psutil.AF_LINK:
                        return snic.address
        return "No MAC address found."
if __name__ == "__main__":
    toolkit = MacOSToolkit()

    # Test running a shell command (example: 'uptime')
    print("Shell Command Output:")
    print(toolkit.run_shell_command('uptime'))
    
    # List files in the home directory
    print("\nFiles in '/Users':")
    print(toolkit.list_files_in_directory('/Users'))
    
    # Get system info
    print("\nSystem Information:")
    print(toolkit.get_system_info())
    
    # Check disk usage
    print("\nDisk Usage Information:")
    print(toolkit.check_disk_usage())
    
    # List running processes
    print("\nRunning Processes:")
    processes = toolkit.get_running_processes()
    for proc in processes:
        print(proc)
    
    # Get system uptime
    print("\nSystem Uptime:")
    print(toolkit.get_uptime())
    
    # Create a new directory
    print("\nCreating a New Directory:")
    print(toolkit.create_directory('/Users/zavala_tm20/new_folder'))
    
    # Check if a file exists
    print("\nCheck if a File Exists:")
    print(toolkit.check_if_file_exists('/path/to/file'))
    
    # Copy a file
    print("\nCopying a File:")
    print(toolkit.copy_file('/path/to/source/file', '/path/to/destination/file'))
    
    # Kill a process by PID (example PID: 12345)
    print("\nKill Process:")
    print(toolkit.kill_process(12345))
    
    # Get MAC address
    print("\nMAC Address:")
    print(toolkit.get_mac_address())
