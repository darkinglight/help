package main

import (
	dataapi "gin/pkg/myapi/data"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.GET("/health", GetHealthHandler)
	router.GET("/health-dataapi", dataapi.GetDataAPIHealthHandler)

	s := &http.Server{
		Addr:    ":8000",
		Handler: router,
	}
	s.ListenAndServe()
}

func GetHealthHandler(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"code":    0,
		"message": "Service is alive!",
	})
}
