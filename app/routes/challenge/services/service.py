def execute_operation(operation: str, operands: list[float]) -> float:
    if not operands:
        raise ValueError("Operand list is empty")

    if operation == "sum":
        return sum(operands)
    elif operation == "subtract":
        return operands[0] - sum(operands[1:])
    elif operation == "multiply":
        result = 1
        for num in operands:
            result *= num
        return result
    elif operation == "divide":
        result = operands[0]
        for num in operands[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result /= num
        return result
    else:
        raise ValueError(f"Unsupported operation: {operation}")
