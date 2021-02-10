import json


class KeyValueStore:
    def __init__(self):
        self.data = {}
    
    def get(self, key):
        return self.data[key]

    def SET(self, key, value):
        self.data[key] = value

    def delete(self, key):
        del self.data[key]


    def execute(self, string_operation):
        response = "Sorry I don't understand the command."
        command, key, value = 0, 1, 2
        operands = string_operation.split(" ")
        if operands[command] == "get":
            response = self.get(operands[key])
        elif operands[command] == "SET":
            self.SET(operands[key], operands[value])
            response = f"key {operands[key]} SET to {operands[value]}"
        elif operands[command] == "delete":
            self.elete(operands[key])
            response = f"key {key} deleted"
        elif operands[command] == "show":
            response = str(self.data)
        else:
            pass
        return response
