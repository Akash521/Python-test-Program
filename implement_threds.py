import threading

# Create a lock
lock = threading.Lock()

# Shared value to be incremented
value = 0

# Function to increment the value
def increment_value():
    global value
    with lock:
        value += 1

# Simulating concurrent API calls
def api_call():
    # Perform API logic
    increment_value()

# Create and start multiple threads for concurrent API calls
threads = []
for _ in range(10):
    thread = threading.Thread(target=api_call)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the final value
print(threads)