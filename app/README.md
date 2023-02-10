# app
## 概要
入力したキーワードに一致する楽曲情報を表示します。  
楽曲情報はspotify APIを利用しています。  
https://developer.spotify.com/documentation/web-api/

## フォルダ構成
```txt
app     
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
demo    
        migrations    
                __init__.py
        static 
            css     
                base.css
                index.css
                loading.css
                results.css
        templates     
            base.html
            demo    
                index.html
                index2.html
                loading.html
                results.html
        __init__.py
        admin.py
        apps.py
        dummy_data.json
        form.py
        models.py
        spotify.py
        tests.py
        urls.py
        views.py
manage.py
README.md
requirements.txt
```

## 作成内容
- app 
  - プロジェクト
- demo
  - デモアプリ
  - 画面構成
    - index2.html: トップ画面
    - index.html: 検索画面
    - results.html: 結果表示画面 

## Tips
- アプリを追加
  1. 以下コマンドをプロジェクトディレクトリ配下で実行
      ```sh
      python manage.py startapp <appname>
      ```
      \* アプリ名にハイフンは利用できない  
  2. settings.py
      ```
      INSTALLED_APPS = [
        ...
        '<appname>.apps.<Appname>Config'
      ]
      ```
      ※ Appnameは必ずキャメルケースであること