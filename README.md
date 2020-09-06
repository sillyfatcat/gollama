# go/llama

![gollama](https://raw.githubusercontent.com/sillyfatcat/gollama/master/gollama/frontend/static/img/gollama.png)

go/llama is an opensource solution to golinks often seen in tech companies. 
I recently started working at a company that does not have support for golinks so I decided to write my own. 

## Getting Started

### Prerequisites

 * Python3

### Installing

```bash
python setup.py install
```

## Usage

Edit local host file to resolve DNS `go` to `127.0.0.2`.

 * Windows: C:\Windows\System32\drivers\etc\hosts
 * Mac: /private/etc/hosts
 * Linux: /etc/hosts

Your `hosts` file should look something like this
```
...
127.0.0.1 localhost # example
127.0.0.2 go
...
```


```bash
cd gollama
python manage.py migrate
python manage.py runserver 127.0.0.2:80
```

NOTE: On macOS you will need to perform the following `sudo ifconfig lo0 alias 127.0.0.2 up` in order to add `127.0.0.2` to the loopback address. 

Once this is setup `http://go` should route you to the home dashboard where you can create new links. 

To  use these links just type `http://go/{SHORTHAND}`

### Docker

If you want to use Docker, you can use the `docker-compose build` to build the docker image

```bash
docker-compose build
docker-compose up
``` 

After this, manually connect to the docker container and run the migrate command

Get the Docker ID using this

```bash
docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
5a4954f79b81        gollama_web         "python gollama/mana…"   About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp   gollama_web_1
439fe553430b        postgres            "docker-entrypoint.s…"   6 minutes ago        Up About a minute   5432/tcp                 gollama_db_1
docker exec -t -i 5a4954f79b81 bash
----
cd gollama
python manage.py migrate
```


NOTE: The `docker-compose.yml` is not production ready as it has hardcoded credentials, DO NOT USE THIS FOR PRODUCTION

## Contributing

Feel free to open any pull requests in the github page, I will review them as they come in. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [go/links](https://www.golinks.io/), for hooking me up and never letting me go
* [Ben](https://www.twitch.tv/taberif_), for debugging with me
* [Maryann](https://www.twitch.tv/maryann), the Llama artist
