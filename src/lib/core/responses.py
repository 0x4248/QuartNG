class String:
    class Error:
        NO_RESPONSE = "The server did not return a response."
        SERVER_ERROR = "The server encountered an error. Please try again later."
        RATE_LIMIT_EXCEEDED = "Rate limit exceeded. Please try again later."
        NOT_FOUND = "404 The requested resource was not found."
        