package frontend_app

import (
	"fmt"
	"strings"
)

// StringInSlice checks if a string is present in a slice of strings.
func StringInSlice(a string, list []string) bool {
	for _, b := range list {
		if strings.ToLower(a) == strings.ToLower(b) {
			return true
		}
	}
	return false
}

// FormatError formats an error message with a given error code and a list of arguments.
func FormatError(code int, args...interface{}) string {
	return fmt.Sprintf("Error %d: %s", code, fmt.Sprint(args...))
}