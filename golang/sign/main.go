package main

import (
	"crypto/md5"
	"flag"
	"fmt"
	_ "github.com/joho/godotenv/autoload"
	"io"
	"net/url"
	"os"
	"sort"
)

var (
	h         bool
	urlString string
)

func init() {
	flag.BoolVar(&h, "h", false, "show this script's usage")
	flag.StringVar(&urlString, "url", "", "url, example: http://xxx.com/aaa?param=1")
	flag.Usage = Usage
}

func main() {
	flag.Parse()

	if h || (urlString == "") {
		flag.Usage()
	}

	parseUrl(urlString)
}

func parseUrl(urlString string) {
	u, err := url.Parse(urlString)
	if err != nil {
		panic(err)
	}

	params, _ := url.ParseQuery(u.RawQuery)
	sign := makeSign(params)
	params.Set("sn", sign)
	u.RawQuery = params.Encode()

	fmt.Println(u)
}

func makeSign(params url.Values) string {
	var keys []string
	for key := range params {
		keys = append(keys, key)
	}
	sort.Strings(keys)
	var md5String string
	for _, key := range keys {
		if key == "sn" {
			continue
		}
		md5String = fmt.Sprintf("%s%s=%s|", md5String, key, params.Get(key))
	}
	tl := params.Get("tl")
	if tl == "" {
		panic("tl is empty. please add tl to url's params.")
	}
	secret := os.Getenv(tl)
	if secret == "" {
		panic("tl not exist in .env")
	}
	md5String = fmt.Sprintf("%s%s", md5String, secret)
	fmt.Println(md5String)
	sign := makeMd5(md5String)
	return sign
}

func makeMd5(md5String string) string {
	h := md5.New()
	io.WriteString(h, md5String)
	result := fmt.Sprintf("%x", h.Sum(nil))
	return result
}

func Usage() {
	fmt.Fprintln(os.Stderr, "sign script")
	fmt.Fprintln(os.Stderr, "Version: v1.0.0")
	fmt.Fprintf(os.Stderr, "Usage: %s [-h] -url=htpp://test.com/login?tl=test\n", os.Args[0])
	fmt.Fprintln(os.Stderr, "Options:")
	flag.PrintDefaults()
	os.Exit(0)
}
