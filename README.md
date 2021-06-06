# TMVP

This is a minimum viable product for a Tesseract-based microservice, that recieves an image and return its text.

## Build

```
docker build -t vsis/tmvp .
```

## Run

```
docker run --rm -p 5000:5000 vsis/tmvp
```

## Use

There are some examples in `example` dir you may use.

```
curl -v -F file=@examples/receipt.png localhost:5000/img
```
