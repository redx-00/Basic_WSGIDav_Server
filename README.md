# WsgiDAV for Wispbyte

A small authenticated WebDAV server using WsgiDAV and Cheroot.

## Deploy

1. Create a **Python** server in Wispbyte.
2. Upload the contents of this folder to the server's root directory.
3. In **Startup → Additional Python Packages**, add:
   `WsgiDAV[cheroot]>=4.3,<5`
   (Alternatively, keep `requirements.txt` and use the normal Python startup setup.)
4. In **Startup → Environment Variables**, set:
   - `DAV_USER` = your chosen username
   - `DAV_PASSWORD` = a long, unique password
   - `DAV_ROOT` = `storage` (optional)
5. Set the startup command to `python main.py`.
6. Start the server and check the Console for the listening port.

The app binds to `0.0.0.0` and uses `SERVER_PORT`, then `PORT`, then `8080`.

## Connect

Use the public address and port shown by Wispbyte in a WebDAV client.
The WebDAV path is `/`. Enter the username and password you configured.

## Storage

Files are stored in the `storage/` directory. Back up this folder separately.

## Security notes

- Do not leave `DAV_PASSWORD` unset or use a guessable password.
- WebDAV supports file uploads, edits, moves, and deletions. Only share credentials
  with people you trust.
- This starter uses HTTP at the application layer. Basic authentication is enabled
  for client compatibility and is not safe over an unencrypted public connection.
  Use an HTTPS endpoint/reverse proxy before sending credentials or private files
  over the internet. Do not treat a Wispbyte address as HTTPS unless the panel
  or your proxy actually provides TLS.
- The server has no public anonymous access.
