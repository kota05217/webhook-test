import requests
import json
 
 #URL
webhook_url = 'https://discordapp.com/api/webhooks/URL'
 
 #文
main_content = {
  "username": "名前",
  "avatar_url": "アバター画像のURL",
  "content": "文",
  "embeds": [
    {
      "author": {
        "name": "kanachan",
        "url": "https://dummy/",
        "icon_url": "画像URL"
      },
      "title": "タイトル",
      "url": "https://dummy/",
      "description": "説明",
      "color": 16092346,
      "fields": [
        {
          "name": "文",
          "value": "文"
        }
      ],
      "footer": {
        "text": "文",
        "icon_url": "画像URL"
      }
    }
  ]
}
 
 #POST
requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})