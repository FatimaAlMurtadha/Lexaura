# Backend Dockerfile
# Builds the Go service and runs the compiled binary.

FROM golang:1.26 AS builder

WORKDIR /app
COPY go.mod ./
RUN go mod download

COPY . .
RUN go build -o /app/backend ./server

FROM gcr.io/distroless/base-debian12
WORKDIR /app
COPY --from=builder /app/backend /app/backend
EXPOSE 8000
CMD ["/app/backend"]