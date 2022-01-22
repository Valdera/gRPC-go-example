.PHONY: protos

protos:
	protoc greet/greetpb/greet.proto --go_out=plugins=grpc:./greet/
	protoc calculator/calculatorpb/calculator.proto --go_out=plugins=grpc:./calculator/
	protoc blog/blogpb/blog.proto --go_out=plugins=grpc:./blog/

server:
	go run ./blog/blog_server .

client:
	go run ./blog/blog_client .
