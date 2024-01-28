
  fn longest_common_prefix(strs: Vec<String>) -> String{
    // first check weather emty string "" present in vector or not
    match strs.is_empty(){
    // 
      true => "".to_string(),
      // 
      _ => {
        // skip(x) use to skip first `x` elements
        // fold() method use to apply closure on strs[i]
        // acc is common_prefix
        // setting initial value of acc i.e acc = strs[0].0 
        // defining closure for comparison
        strs.iter().skip(1).fold(strs[0].clone(), |acc,x| {
          acc
          // getting current common prefix characters 
            .chars()
          // zip() method gives iterator over characters of acc & (strs[i])
            .zip(x.chars())
          // comparing characters of acc & strs[i]
          // returns an iterator over the pairs of characters that match the condition set by the closure
            .take_while(|(x,y)| x==y)
          // map() takes only one charecter from pair  
            .map(|(x,_)| x)
          // forming string of charecter i.e common prefix
            .collect()
        })
      }
    }
  }


fn main(){
  let input = vec!["4flsfd".to_string(), "flow".to_string(), "flerew".to_string()];
  println!("{}",longest_common_prefix(input));

}