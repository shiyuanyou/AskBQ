"""
400 - Invalid Format	Cause: Invalid request body format.
Solution: Please modify your request body according to the hints in the error message. For more API format details, please refer to DeepSeek API Docs.

401 - Authentication Fails	Cause: Authentication fails due to the wrong API key.
Solution: Please check your API key. If you don't have one, please create an API key first.

402 - Insufficient Balance	Cause: You have run out of balance.
Solution: Please check your account's balance, and go to the Top up page to add funds.

422 - Invalid Parameters	Cause: Your request contains invalid parameters.
Solution: Please modify your request parameters according to the hints in the error message. For more API format details, please refer to DeepSeek API Docs.

429 - Rate Limit Reached	Cause: You are sending requests too quickly.
Solution: Please pace your requests reasonably. We also advise users to temporarily switch to the APIs of alternative LLM service providers, like OpenAI.

500 - Server Error	Cause: Our server encounters an issue.
Solution: Please retry your request after a brief wait and contact us if the issue persists.

503 - Server Overloaded	Cause: The server is overloaded due to high traffic.
Solution: Please retry your request after a brief wait.
"""

from enum import Enum
class RequestErrorCode(Enum):
    FORMAT_ERROR = 400
    KEY_ERROR = 401
    INSUFFICIENT_BALANCE = 402
    INVALID_PARAMETERS = 422
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    SERVER_OVERLOADED = 503

hintRequestErrorCode = {
    RequestErrorCode.FORMAT_ERROR: "Invalid Format; Please modify your request body according to the hints in the error message. For more API format details, please refer to DeepSeek API Docs.",
    RequestErrorCode.KEY_ERROR: "Authentication Fails; Please check your API key. If you don't have one, please create an API key first.",
    RequestErrorCode.INSUFFICIENT_BALANCE: "Insufficient Balance; Please check your account's balance, and go to the Top up page to add funds.",
    RequestErrorCode.INVALID_PARAMETERS: "Invalid Parameters; Please modify your request parameters according to the hints in the error message. For more API format details, please refer to DeepSeek API Docs.",
    RequestErrorCode.TOO_MANY_REQUESTS: "Rate Limit Reached; Please pace your requests reasonably. We also advise users to temporarily switch to the APIs of alternative LLM service providers, like OpenAI.",
    RequestErrorCode.INTERNAL_SERVER_ERROR: "Server Error; Please retry your request after a brief wait and contact us if the issue persists.",
    RequestErrorCode.SERVER_OVERLOADED: "Server Overloaded; Please retry your request after a brief wait.",
}
