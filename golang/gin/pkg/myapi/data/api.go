package data

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func GetDataAPIHealthHandler(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"code":    0,
		"message": "Data API is alive",
	})
}
