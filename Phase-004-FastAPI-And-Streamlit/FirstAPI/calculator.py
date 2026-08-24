from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


# =========================================================
# FastAPI Application
# =========================================================

app = FastAPI(
    title="Calculator API",
    description="A simple calculator API using FastAPI",
    version="1.0.0"
)


# =========================================================
# Request Model
# =========================================================

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str


# =========================================================
# Response Model
# =========================================================

class CalculationResponse(BaseModel):
    num1: float
    num2: float
    operation: str
    result: float
    message: str = "Calculation successful"


# =========================================================
# Routes
# =========================================================

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>🧮 Calculator API is Running!</h1>

    <p>
        Go to <a href="/docs">/docs</a>
        to test the calculator interactively.
    </p>
    """


@app.post("/calculate", response_model=CalculationResponse)
def calculate(data: CalculationRequest):

    num1 = data.num1
    num2 = data.num2
    op = data.operation.lower()

    # ADD
    if op == "add":
        result = num1 + num2
        message = f"{num1} + {num2} = {result}"

    # SUBTRACT
    elif op == "subtract":
        result = num1 - num2
        message = f"{num1} - {num2} = {result}"

    # MULTIPLY
    elif op == "multiply":
        result = num1 * num2
        message = f"{num1} × {num2} = {result}"

    # DIVIDE
    elif op == "divide":

        if num2 == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero"
            )

        result = num1 / num2
        message = f"{num1} ÷ {num2} = {result}"

    # INVALID OPERATION
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation. Use: add, subtract, multiply, or divide."
        )

    return CalculationResponse(
        num1=num1,
        num2=num2,
        operation=op,
        result=result,
        message=message
    )


# =========================================================
# Health Check
# =========================================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Calculator API"
    }