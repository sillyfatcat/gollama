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

Edit local host file to resolve DNS `go` to `127.0.0.2:80`.

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
python manage.py runserver 127.0.0.2:80
```

Once this is setup `http://go` should route you to the home dashboard where you can create new links. 

To  use these links just type `http://go/{SHORTHAND}`

## Contributing

Feel free to open any pull requests in the github page, I will review them as they come in. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [go/links](https://www.golinks.io/)
* [Ben](https://www.twitch.tv/taberif_), for debugging with me
* [Maryann](https://www.twitch.tv/maryann), the Llama artist
