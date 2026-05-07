import xmlrpc.client

# Connect to server
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:

    try:
        input_value = int(input("Enter number: "))

        result = proxy.calculate_factorial(input_value)

        print(f"Factorial of {input_value} is: {result}")

    except Exception as e:
        print("Error:", e)