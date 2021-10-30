# Simple Log / Email Server

## Description

A very simple flask server for logging request message to log (to disk) and sending email for the purpose of penetration testing.

After getting access to a compromised machine, you may set up a reverse shell or simply send some message back to the attacker.

In the second case, for example, when a hacker stole the WIFI password from a computer using rubber ducky, it needs to be sent back to the hacker. Typing the script to send an email in command line is time consuming, and you may expose your email address. In this case, you can simply send a post request to this log server, and you will have access to the stolen password in your email or in the log file.

## Usage

There are only 2 routes in the server

### /

Send a post request to the root route (`http://server`), and put the message in form data with "data" as the key.

### /email

Same as `/`, just add `email` to the url.

Send a post request to `http://server/email`, and put the message in form data with "data" as the key.

If you need this route to work, make sure you enter your email address and password in `.env`

It's using gmail smtp server for by default, so you have to use a gmail as your from address. Change it in `send_email.py` if you wish to use some other server.

## Dockerfile

I made a docker image and it's on docker hub (support gmail only, build your own if you want).

Also you may want to generate a app password for gmail. For security reasons, gmail may not let you use your general email.

Here is how to use it

```bash
touch log.log
docker run -d \
    --restart unless-stopped \
    -e EMAIL_ADDRESS=<gmail> \
    -e EMAIL_PASSWORD=<password> \
    -p 3000:3000 \
    --name log-server \
    -v $PWD/log.log:/root/simple-log-server/log.log \
    huakunshen/simple-log-server:latest
```
