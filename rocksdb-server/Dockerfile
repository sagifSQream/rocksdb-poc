FROM docker.io/openjdk:8

WORKDIR /app

COPY conf/ ./conf
COPY bin/rocksdb-server-2.0/lib/ ./lib/

VOLUME [ "/data" ]

ENTRYPOINT [ "/bin/bash", "-c"]
CMD [ "java -cp \"./lib/*\" com.ranksays.rocksdb.server.Main --sync" ]
