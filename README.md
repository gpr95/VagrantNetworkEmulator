# Testing OSPF

(Note there's a [blog post](http://serverascode.com/2015/02/02/quagga-openospfd.html) that talks a bit more about this repo and what it does.)

This repository sets up four nodes:

* Linux client
* OpenBSD router
* Two Linux servers

The OpenBSD box will use ospfd from OpenBGP. The two Linux servers will use quagga.

I don't know how useful this will be to anyone, but here it is none-the-less. :)

## Run

```bash
curtis$ vagrant up
curtis$ ansible-playbook site.yml
```

## Issues

I could not get authentication to work. This is just for testing anyways, but it would have been nice to get authentication working...I think I just ran out of time.
