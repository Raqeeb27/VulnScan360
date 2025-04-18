import platform

# Get a general identification of the operating system
os_name = platform.system()
print(f"Operating System: {os_name}")

# Get more detailed information about the platform
platform_info = platform.platform()
print(f"Platform Information: {platform_info}")

# You can also get specific details:
release_info = platform.release()
print(f"OS Release: {release_info}")

version_info = platform.version()
print(f"OS Version: {version_info}")

machine_info = platform.machine()
print(f"Machine Architecture: {machine_info}")

processor_info = platform.processor()
print(f"Processor: {processor_info}")

# For more human-readable OS identification (though less precise)
uname_result = platform.uname()
print(f"Uname: {uname_result}")
print(f"System Name (uname): {uname_result.system}")
print(f"Node Name (uname): {uname_result.node}")
print(f"Release (uname): {uname_result.release}")
print(f"Version (uname): {uname_result.version}")
print(f"Machine (uname): {uname_result.machine}")
print(f"Processor (uname): {uname_result.processor}")
