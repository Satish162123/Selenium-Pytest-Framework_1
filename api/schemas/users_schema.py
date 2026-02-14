users_schema = {
    "type": "object",
    "properties": {
        "users": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "firstName": {"type": "string"},
                    "lastName": {"type": "string"}
                },
                "required": ["id", "firstName", "lastName"]
            }
        }
    },
    "required": ["users"]
}
