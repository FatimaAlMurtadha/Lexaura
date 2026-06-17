# This file is used to build the backend server using a multi-stage Docker build. 
# The first stage uses the official Golang image to compile the server, and the second stage uses a minimal base image to run the compiled server.
FROM golang:1.22 AS builder

WORKDIR /app
COPY . .
RUN go mod download
RUN go build -o server ./cmd/server

FROM gcr.io/distroless/base
WORKDIR /app
COPY --from=builder /app/server .
CMD ["./server"]