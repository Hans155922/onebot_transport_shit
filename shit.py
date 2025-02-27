import getset
import hmac
from flask import Flask, request, jsonify
import requests

setting = getset.load_set()
print("当前服务配置:")
print(f"http_server http://{setting['listen_host']}:{setting['listen_port']}", end="")
print(f"，token={setting['listen_token']}" if setting["listen_token"] else "")
print(f"http_client http://{setting['bot_host']}:{setting['bot_port']}", end="")
print(f"，token={setting['bot_token']}" if setting["bot_token"] else "")
id = getset.load_id()
if id["target"]:
    print(f"当前搬屎配置:从 {id['source']} 搬到 {id['target']}")
else:
    print(f"请搬屎添加目标。")
    exit()


def get_forward_msg(id):
    headers = {"Content-Type": "application/json"}
    if setting["bot_token"]:
        headers["Authorization"] = f"Bearer {setting['bot_token']}"
    response = requests.post(f"http://{setting['bot_host']}:{setting['bot_port']}/get_forward_msg", json={"message_id": id}, headers=headers)
    return response.status_code, response.json()


def send_forward_msg(msg="", group_id=None, user_id=None):
    data = {"messages": msg, "prompt": "[聊天记录]"}
    if group_id:
        data["group_id"] = group_id
    if user_id:
        data["user_id"] = user_id
    headers = {"Content-Type": "application/json"}
    if setting["bot_token"]:
        headers["Authorization"] = f"Bearer {setting['bot_token']}"
    response = requests.post(f"http://{setting['bot_host']}:{setting['bot_port']}/send_forward_msg", json=data, headers=headers)
    return response.status_code, response.json()


def get_group_list():
    headers = {"Content-Type": "application/json"}
    if setting["bot_token"]:
        headers["Authorization"] = f"Bearer {setting['bot_token']}"
    response = requests.post(f"http://{setting['bot_host']}:{setting['bot_port']}/get_group_list", headers=headers)
    return response.status_code, response.json()


def rec_msg(msg):
    if msg["post_type"] == "message":
        if msg["message_type"] == "group":
            if msg["group_id"] in id["source"]:
                if msg["message"][0]["type"] == "forward":
                    code, data = get_forward_msg(msg["message"][0]["data"]["id"])
                    if code == 200:
                        msgs = data["data"]["messages"]
                        send = []
                        for a in msgs:
                            send.append({"type": "node", "data": {"user_id": 10000, "nickname": "QQ用户", "content": a["message"]}})
                        code, group = get_group_list()
                        if code == 200:
                            all_group = []
                            for i in group["data"]:
                                all_group.append(i["group_id"])
                        else:
                            print(f"获取群列表失败{group}")
                            return "get_group_list_error"
                        for send_id in id["target"]:
                            if send_id != msg["group_id"]:
                                if send_id in all_group:
                                    code, data = send_forward_msg(send, group_id=send_id)
                                    print(f"群组{send_id} 发送成功" if code == 200 else f"{send_id} {data}")
                                else:
                                    code, data = send_forward_msg(send, user_id=send_id)
                                    print(f"用户{send_id} 发送成功" if code == 200 else f"{send_id} {data}")
                        return "ok"
                    else:
                        print(data)
                    return "token_error"
                return "not_forward"
            return "not_in_source"
        return "not_group_msg"
    return "notc_msg"


app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive():

    if setting["listen_token"]:
        sig = hmac.new(setting["listen_token"].encode("utf-8"), request.get_data(), "sha1").hexdigest()
        received_sig = request.headers["X-Signature"][len("sha1=") :]
        if sig == received_sig:
            return jsonify({"status": rec_msg(request.json)})
        else:
            print("token不符，请检查listen_token配置")
            return jsonify({"error": "Unauthorized"}), 401
    else:
        return jsonify({"status": rec_msg(request.json)})


if __name__ == "__main__":
    app.run(host=setting["listen_host"], port=setting["listen_port"])
