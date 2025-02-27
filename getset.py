import os
import json


def load_set():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    set_file = os.path.join(script_dir, 'set.json')

    default_set = {
        "listen_host": "127.0.0.1",
        "listen_port": 4321,
        "listen_token": "",
        "bot_host": "127.0.0.1",
        "bot_port": 6666,
        "bot_token": "",
    }

    if os.path.exists(set_file):
        print("开始读取服务配置。")
        with open(set_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            merged_set = data.copy()
            for key, value in default_set.items():
                if key not in merged_set:
                    merged_set[key] = value
            if data != merged_set:
                print("服务配置不全，更新配置。")
                with open(set_file, 'w', encoding='utf-8') as file:
                    json.dump(merged_set, file, ensure_ascii=False, indent=4)
            return merged_set
    else:
        print("没有服务配置，使用默认配置。")
        with open(set_file, 'w', encoding='utf-8') as file:
            json.dump(default_set, file, ensure_ascii=False, indent=4)
        return default_set


def load_id():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    set_file = os.path.join(script_dir, 'id.json')

    default_set = {"source": [1032915502], "target": []}

    if os.path.exists(set_file):
        print("开始读取ID配置。")
        with open(set_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            merged_set = data.copy()
            for key, value in default_set.items():
                if key not in merged_set:
                    merged_set[key] = value
            if data != merged_set:
                print("ID配置不全，更新配置。")
                with open(set_file, 'w', encoding='utf-8') as file:
                    json.dump(merged_set, file, ensure_ascii=False, indent=4)
            return merged_set
    else:
        print("没有ID配置，使用默认配置。")
        with open(set_file, 'w', encoding='utf-8') as file:
            json.dump(default_set, file, ensure_ascii=False, indent=4)
        return default_set