import json
import socket
from Config import Config


class Connection:

    @staticmethod
    def __send_request(requestData):
        conn: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((Config.SERVER_NAME, Config.SERVER_PORT))
        jsonData = json.dumps(requestData)
        conn.send(bytes(f'{jsonData}', "utf-8"))
        response = conn.recv(1024)
        conn.close()
        print(response)

        return json.loads(response.decode("utf-8"))

    @staticmethod
    def send_request(controller, route, requestData=None):
        request = {
            "action": {
                "controller": controller,
                "route": route
            },
        }
        if requestData is not None:
            request["data"] = requestData

        return Connection.__send_request(request)
