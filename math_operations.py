import sys

# Retrieve input values from command-line arguments
if len(sys.argv) != 4:
    print("Content-Type: text/html\n")
    print("<h3>Error: Invalid number of arguments provided.</h3>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]
except ValueError:
    print("Content-Type: text/html\n")
    print("<h3>Error: Invalid numerical input.</h3>")
    sys.exit(1)

result = None
error_message = ""

if operation == "add":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "mul":
    result = num1 * num2
elif operation == "div":
    if num2 == 0:
        error_message = "Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    error_message = "Invalid operation selected."

# Additional conditions
if result is not None:
    if result > 100:
        result *= 2
    elif result < 0:
        result += 50

# Print the output in HTML format
print("Content-Type: text/html\n")
print("<html><body>")
if error_message:
    print(f"<h3>{error_message}</h3>")
else:
    print(f"<h3>Result: {result}</h3>")
print("</body></html>")
