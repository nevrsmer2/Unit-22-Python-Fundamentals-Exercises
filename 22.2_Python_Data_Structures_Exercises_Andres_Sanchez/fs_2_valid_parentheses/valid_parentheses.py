def valid_parentheses(parens):

    count = 0

    for paren in parens:
        if paren == '(':
            count += 1
        elif paren == ')':
            count -= 1

        # fast fail: too many right parens
    if count < 0:
        return False
    return count == 0

# Question about condition.  If  count = 2 when valid_parentheses("))") , how does it return False given the condition if count < 0 (when count = 2)?





# Code I wrote:
# def valid_parentheses(parens):
#     true_parens = ['()', '()()', '(()())']
#     return parens in true_parens

# *This will not work if there is content within the parenthesis

    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """