package main

import (
    "fmt"
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
    "sort"
	"bufio"
	"os"
)

type Item struct {
    UserId int64
    Amount int64
}
type Items []Item
func (q Items) Len() int {return len(q)}
func (q Items) Less(i, j int) bool {
    return q[i].Amount > q[j].Amount
}
func (q Items) Swap(i, j int) {
    q[i], q[j] = q[j], q[i]
}

func main() {
    db, err := sql.Open("mysql", ":@tcp(:)/")
    if err != nil {
        fmt.Println("connection to mysql failed:", err)
        return
    }
    rows, _ := db.Query("")

    queue := make(Items, 0, 10000)
    totalNum := 0
    for rows.Next() {
        totalNum++
        item := new(Item)
        err = rows.Scan(&item.UserId, &item.Amount)
        queue = append(queue, *item)
        if len(queue) >= 10000 {
            sort.Sort(queue)
            queue = queue[0:1000]
            fmt.Printf("total num: %d\n", totalNum)
        }
    }
    sort.Sort(queue)
    queue = queue[0:1000]
	store("text.txt", queue)
}

func store(filePath string, queue Items) {
	file, err := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
        fmt.Println(err)
		return
	}
	defer file.Close()
	writer := bufio.NewWriter(file)
	defer writer.Flush()

    for _, item := range queue {
		str := fmt.Sprintf("%d,%d", item.UserId, item.Amount)
		fmt.Fprintln(writer, str)
	}
}
