import asyncio
import socket

async def handle_request(reader, writer):
    address = writer.get_extra_info('peername')
    print(f"Yangi ulanish: {address}")

    data = await reader.read(1024)
    request = data.decode('utf-8')
    print(f"Qabul qilingan request: {request}")

    response = "HTTP/1.1 200 OK\r\n\r\nServer: asyncio HTTP server"
    writer.write(response.encode('utf-8'))
    await writer.drain()

    print(f"Javob yuborildi: {address}")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_request, '127.0.0.1', 8080)
    async with server:
        await server.serve_forever()

asyncio.run(main())
```

Kodni ishga tushirish uchun quyidagilarni amalga oshiring:

1. Kodni `server.py` nomli faylga saqlang.
2. Kompyuterida terminalga kirib quyidagilarni yozib bosing:
   ```bash
python server.py
```
3. Browserda `http://127.0.0.1:8080/` manziliga kirib, serverga qabul qilingan requestni ko'rasiz.
