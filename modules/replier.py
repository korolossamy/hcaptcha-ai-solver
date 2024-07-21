import json
from requests import post

class Replier:
    def reply(self, questions: str):
        res = post(
            url = "https://api.deepinfra.com/v1/openai/chat/completions",
            json = {
                "model": "meta-llama/Meta-Llama-3-70B-Instruct",
                "messages": [
                    {
                        "role": "system",
                        "content": "Be a helpful assistant"
                    },
                    {
                        "role": "user",
                        "content": f"srictly respond to the following question with only and only one single word, number, or phrase :  Question: {questions}"
                    }
                ],
                "stream": True
            },
            headers = {
                "Accept": "text/event-stream",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "302",
                "Content-Type": "application/json",
                "Host": "api.deepinfra.com",
                "Origin": "https://deepinfra.com",
                "Referer": "https://deepinfra.com/",
                "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-Deepinfra-Source": "web-page"
            },
            stream = True
        )

        first = True
        result = []

        for chunk in res.iter_lines():
            if not chunk.startswith(b"data: "):
                continue

            try:
                json_line = json.loads(chunk[6:])
                choices = json_line.get("choices", [{}])

                if choices[0].get("finish_reason"):
                    break
                token = choices[0].get("delta", {}).get("content")
                if token:
                    if first:
                        token = token.lstrip()
                    if token:
                        first = False
                        result.append(token)
            except json.JSONDecodeError:
                pass
        
        return ''.join(result)