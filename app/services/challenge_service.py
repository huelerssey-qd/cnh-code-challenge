class ChallengeService:
    def calculate(self, operation: str, operands: list[float]) -> float:
        if operation == "sum":
            return sum(operands)
        if operation == "subtract":
            return operands[0] - sum(operands[1:])
        if operation == "multiply":
            result = 1
            for num in operands:
                result *= num
            return result
        if operation == "divide":
            result = operands[0]
            for num in operands[1:]:
                if num == 0:
                    raise ValueError("Division by zero")
                result /= num
            return result
        raise ValueError("Unsupported operation")
