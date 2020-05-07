package main

import "fmt"

func main() {
	s := "abedabcdababcdse"
	pattern := "abcdababcd"
	result := kmpSearch(s, pattern)
	fmt.Println(result)
}

func kmpSearch(s string, p string) bool {
	match := partMatch(p)
    lens := len(s)
	lenp := len(p)
	schars := []rune(s)
	pchars := []rune(p)
	index := 0 //matched number
	for i := 0; i < lens; i++ {
		for index >= 0 {
			if schars[i] == pchars[index] {
				index++
				if index == lenp {
					return true
				}
				break
			} else if index == 0 {
				break
			} else {
				index = match[index-1]
			}
		}
	}
	return false
}

func partMatch(pattern string) []int {
	chars := []rune(pattern)
	result := make([]int, len(chars))
	for index, char := range chars {
		if index == 0 {
			result[0] = 0
			continue
		}
		preMatchNum := result[index-1]
		for preMatchNum >= 0 {
			if chars[preMatchNum] == char {
				result[index] = preMatchNum + 1
				break
			} else if preMatchNum == 0 {
				result[index] = 0
				break
			} else {
				preMatchNum = result[preMatchNum-1]
			}
		}
	}
	return result
}
