#include <iostream>
#include <vector>
#include <string>
#include <cctype> // For isdigit() and isalpha()
using namespace std;

// Function to classify tokens
vector<string> lexicalAnalyzer(const string& expression) {
    vector<string> tokens;
    string token = "";

    for (size_t i = 0; i < expression.length(); ++i) {
        char ch = expression[i];

        // Handle numbers (including decimals)
        if (isdigit(ch) || (ch == '.' && !token.empty() && isdigit(token.back()))) {
            token += ch;
        }
        // Handle variables (letters)
        else if (isalpha(ch) || ch == '_') {
            if (!token.empty() && !isalpha(token.back())) {
                tokens.push_back(token);
                token = "";
            }
            token += ch;
        }
        // Handle multi-character operators like >=, <=, ==, !=, etc.
        else if (ch == '>' || ch == '<' || ch == '=' || ch == '!') {
            if (!token.empty()) {
                tokens.push_back(token);
                token = "";
            }
            string op(1, ch); // Start forming the operator
            if (i + 1 < expression.length() && expression[i + 1] == '=') {
                op += expression[++i]; // Add '=' for multi-character operators
            }
            tokens.push_back(op);
        }
        // Handle logical operators (&&, ||)
        else if (ch == '&' || ch == '|') {
            if (!token.empty()) {
                tokens.push_back(token);
                token = "";
            }
            string op(1, ch);
            if (i + 1 < expression.length() && expression[i + 1] == ch) {
                op += expression[++i]; // Add the second '&' or '|'
            }
            tokens.push_back(op);
        }
        // Handle standalone symbols (e.g., +, -, *, /, (, ), etc.)
        else if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '(' || ch == ')' || ch == ',' || ch == ';') {
            if (!token.empty()) {
                tokens.push_back(token);
                token = "";
            }
            tokens.push_back(string(1, ch));
        }
        // Handle spaces
        else if (isspace(ch)) {
            if (!token.empty()) {
                tokens.push_back(token);
                token = "";
            }
        }
    }

    // Add the last token, if any
    if (!token.empty()) {
        tokens.push_back(token);
    }

    return tokens;
}

int main() {
    string expression;
    cout << "Enter an expression: ";
    getline(cin, expression);

    vector<string> tokens = lexicalAnalyzer(expression);

    cout << "Tokens:" << endl;
    for (const string& token : tokens) {
        cout << token << endl;
    }

    return 0;
}
