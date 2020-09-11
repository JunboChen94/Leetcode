//79. Word Search
//
//Given a 2D board and a word, find if the word exists in the grid.
//
//The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.The same letter cell may not be used more than once.
//
//Example:
//
//board =
//[
//    ['A', 'B', 'C', 'E'],
//    ['S', 'F', 'C', 'S'],
//    ['A', 'D', 'E', 'E']
//]
//
//Given word = "ABCCED", return true.
//Given word = "SEE", return true.
//Given word = "ABCB", return false.


///// SOLUTION!!!
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (word.size() == 0) return false;
        int m = board.size();
        int n = board[0].size();
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (search(board, word, 0, x, y, m, n)) return true;
            }
        }
        return false;
    }

    bool search(vector<vector<char>>& board, string word, int d, int x, int y, int m, int n) {
        if (x < 0 || x == n || y < 0 || y == m || word[d] != board[y][x]) return false;

        // if end been found, return true
        if (d == word.length() - 1) return true;

        // find the next value
        char cur = board[y][x];
        board[y][x] = 0;   // make sure it will not get the same value
        bool found = search(board, word, d + 1, x + 1, y, m, n)
            || search(board, word, d + 1, x - 1, y, m, n)
            || search(board, word, d + 1, x, y + 1, m, n)
            || search(board, word, d + 1, x, y - 1, m, n);
        board[y][x] = cur; // return the value back
        return found;
    }
};