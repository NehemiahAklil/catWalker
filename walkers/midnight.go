package main

import (
	"fmt"
	"os"
	"os/exec"
	"strings"
	"time"
)

func main() {
	if len(os.Args) < 1 {
		fmt.Println("Usage: ./midnight <repoLink> <branch1> <branch2>")
		os.Exit(1)
	}

	for i := 2; i < len(os.Args); i++ {
		branch := os.Args[i]
		repo := os.Args[1]
		command := fmt.Sprintf("git clone --branch %s --single-branch %s %s", branch, repo, strings.ToUpper(branch[0:1])+branch[1:])
		cmd := exec.Command("sh", "-c", command)
		cmd.Stdout = os.Stdout
		err := cmd.Run()
		fmt.Println("Run command : ", command)
		if err != nil {
			fmt.Printf("Error running git clone on %s: %s\n", os.Args[i], err)
		}
		time.Sleep(1 * time.Second)
	}
}
