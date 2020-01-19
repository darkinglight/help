package main

import "fmt"

func main() {
	skills := []string{"wduavgggs", "ueangkskven", "nelxoztlcon", "jtwzkdctqt", "wdb", "glvavlvqkatgzz", "zfuhvohszqtai", "ros"}
	peoples := [][]string{
		{"ueangkskven"},
		{"wduavgggs", "nelxoztlcon", "wdb", "glvavlvqkatgzz"},
		{"zfuhvohszqtai"},
		{"ros"},
		{"nelxoztlcon", "jtwzkdctqt"},
		{"ueangkskven"},
		{"zfuhvohszqtai"},
		{"jtwzkdctqt", "glvavlvqkatgzz"},
		{"zfuhvohszqtai"},
		{"jtwzkdctqt", "glvavlvqkatgzz"},
	}
	result := smallestSufficientTeam(skills, peoples)
	fmt.Print(result)
}

func smallestSufficientTeam(req_skills []string, people [][]string) []int {
	var skillMap map[string]int = make(map[string]int)
	for i, v := range req_skills {
		skillMap[v] = 1 << uint(i)

	}

	dp := make(map[int]int)
	result := make(map[int][]int)
	for peopleIndex := 0; peopleIndex < len(people); peopleIndex++ {
		peopleSkillSum := 0
		for _, peopleSkill := range people[peopleIndex] {
			skillValue, ok := skillMap[peopleSkill]
			if ok {
				peopleSkillSum |= skillValue

			}

		}

		dp[peopleSkillSum] = 1
		result[peopleSkillSum] = []int{peopleIndex}

		for skillSum, peopleNum := range dp {
			newSkillSum := skillSum | peopleSkillSum
			originPeopleNum, ok := dp[newSkillSum]

			if !ok || (originPeopleNum > (peopleNum + 1)) {
				dp[newSkillSum] = peopleNum + 1
				var item []int = make([]int, len(result[skillSum]))
				copy(item, result[skillSum])
				result[newSkillSum] = append(item, peopleIndex)

			}

		}

		//	fmt.Println(peopleIndex)
		//	fmt.Println(dp)

	}
	return result[1<<uint(len(req_skills))-1]

}
