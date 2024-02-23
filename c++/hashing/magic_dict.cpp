class MagicDictionary {
public:
    /** Initialize your data structure here. */
    std::unordered_map<std::string, bool> hDict;
    MagicDictionary() : hDict() {}
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        hDict.clear();
        for (std::string word : dict) {
            hDict[word] = true;
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        std::vector<std::string> letters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
        
        for (int i = 0; i < word.length(); i++) {
            for (std::string l : letters) {
                std::string newStr = word;
                newStr.replace(i, 1, l);
                if (hDict.find(newStr) != hDict.end() && newStr != word) {
                    return true;
                }
            }
        }
        return false;
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * bool param_2 = obj.search(word);
 */