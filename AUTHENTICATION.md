# API Authentication Setup

## Authentication Method
This API uses **Token-Based Authentication** to secure its endpoints.

### Steps to Authenticate:
1. Obtain your API token:
   - Log in to the Django admin panel.
   - Navigate to **Tokens** under the **Auth Token** section.
   - Copy your token.
2. Include the token in the `Authorization` header for each API request:


## Testing the Authentication
- Use tools like Postman or `curl` to make requests:
- **Example: Fetch All Books**
 ```bash
 curl -X GET http://localhost:8000/api/books/ \
 -H "Authorization: Token <your_token>"
 ```
- **Example: Borrow a Book**
 ```bash
 curl -X POST http://localhost:8000/api/transactions/ \
 -H "Authorization: Token <your_token>" \
 -H "Content-Type: application/json" \
 -d '{"user": 1, "book": 2}'
 ```

## Notes
- Only authenticated users can access the API.
- Tokens can be generated per user in the Django admin panel or programmatically.

