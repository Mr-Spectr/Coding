class Solution {
public:
    bool wordPattern(string pattern, string s) {
        std::stringstream ss(s);
        std::string word;
        std::vector<std::string> words;
        
        // Split the string s into words
        while (ss >> word) {
            words.push_back(word);
        }
        
        // If the number of characters in pattern and words don't match, return false
        if (pattern.length() != words.size()) {
            return false;
        }
        
        std::unordered_map<char, std::string> char_to_word;
        std::unordered_map<std::string, char> word_to_char;
        
        for (int i = 0; i < pattern.length(); ++i) {
            char currentChar = pattern[i];
            std::string currentWord = words[i];
            
            // Check mapping from character to word
            if (char_to_word.count(currentChar)) {
                if (char_to_word[currentChar] != currentWord) {
                    return false;
                }
            } else {
                char_to_word[currentChar] = currentWord;
            }
            
            // Check mapping from word to character
            if (word_to_char.count(currentWord)) {
                if (word_to_char[currentWord] != currentChar) {
                    return false;
                }
            } else {
                word_to_char[currentWord] = currentChar;
            }
        }
        
        return true;
        
    }
};