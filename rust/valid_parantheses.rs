//takes string as input
fn is_valid(s: String) -> bool { //returns boolean value
    let mut stack = Vec::new();//mutable vector act like a stack

    for c in s.chars() {//iterating over string
        stack.push(match c {//pushing matching closing bracket in stack vector
            '(' => ')',
            '[' => ']',
            '{' => '}',
            _ => {//c could be valid or invalid closing bracket 
                if Some(c) == stack.pop() {//valid closing bracket 
                    continue;
                } else {//invalid closing bracket
                    return false;
                }
            }
        })
    }
    //some open bracket might not closed
    stack.is_empty()
}