package main

import (
    "net/http"
    "log"
    "fmt"
)

func myHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello there!\n")
    log.Println("receive request.")
}

func main() {
    http.HandleFunc("/", myHandler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
