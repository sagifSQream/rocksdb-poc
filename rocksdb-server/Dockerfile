FROM openjdk:8

WORKDIR /app

COPY conf/ ./conf
COPY bin/rocksdb-server-2.0/lib/ ./lib/
COPY bin/entrypoint.sh ./entrypoint.sh

VOLUME [ "/data" ]

ENTRYPOINT [ "/bin/bash", "-c"]
CMD [ "java -cp \"./lib/*\" com.ranksays.rocksdb.server.Main" ]
