def stylish_ui(content):
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ 
                font-family: sans-serif; 
                background: #f0f2f5; 
                display: flex; 
                justify-content: center; 
                padding: 20px; 
                margin: 0; 
            }}
            .card {{ 
                background: white; 
                padding: 25px; 
                border-radius: 12px; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.1); 
                border-top: 8px solid #d4af37; 
                width: 100%; 
                max-width: 400px; /* Limits size on desktop, stays flexible on mobile */
                text-align: center; 
                box-sizing: border-box;
            }}
            input {{ 
                width: 100%; 
                padding: 15px; /* Larger touch targets for fingers */
                margin: 10px 0; 
                border: 1px solid #ddd; 
                border-radius: 8px; 
                box-sizing: border-box; 
                font-size: 16px; /* Prevents iOS from auto-zooming on focus */
            }}
            input[type="submit"] {{ 
                background: #4b0082; 
                color: white; 
                border: none; 
                cursor: pointer; 
                font-weight: bold; 
                margin-top: 15px; 
            }}
            hr {{ border: 0; border-top: 1px solid #eee; margin: 20px 0; }}
            .status {{ color: green; font-weight: bold; margin-bottom: 15px; }}
        </style>
    </head>
    <body>
        <div class="card">{content}</div>
    </body>
    </html>
    '''