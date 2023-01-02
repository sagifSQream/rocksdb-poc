# RocksDB Server

This is a lightweight RocksDB Server based on jetty.

Java client: https://github.com/iamyulong/rocksdb-client-java

## Features

* Multiple concurrent databases;
* Simple API interface and client libraries;
* Basic Authentication;
* Batch `put`, `get` and `remove` operations.

## Prerequisites

You need to have a Java 8 or above runtime installed.

## Get started


Once boot up, you can check if it's working via http://localhost:4080.

## REST API

All calls made to the server host. for example. if server runs on localhost port 4080 and you want to call create end point do POST request to http://localhost:4080/create

> Note: ALL request below are http __POST__ requests.

All valid requests response with json body in the form of:

```javascript
{
  "code": 200,  //status code of request
  "message": "OK", //OK on success and error message on failure
  "body": null or value //if the request has data from server.
}
```


### /create

Create a database. In this example, create a database name `sagi`

__request body__

```javascript
{
"name": "sagi"
}
```

### /put 

write multiple keys and there values into a database. You can upload objects by setting a byte array to base64. Keys can also be based64

__request body__

```javascript
{
"name": "sagi",
"keys":["k1","k2"],
"values":["v1","v2"]
}
```

### /get 

read multiple keys from database. The return value is base64 encoded. you need to decode the values

__request body__

```javascript
{
"name": "sagi",
"keys":["k1"]
}
```

__response_body__

```javascript
{
  "code": 200,
  "message": "OK",
  "body": [
    "vw=="
  ]
}
```

