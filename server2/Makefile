all:server client
server:server.c
	gcc -o server server.c
server_multi:server_multi.c
	gcc -o server_multi server_multi.c
client:client.c
	gcc -o client client.c
clean:
	rm -f server
	rm -f server_multi
	rm -f client
	rm -f core
