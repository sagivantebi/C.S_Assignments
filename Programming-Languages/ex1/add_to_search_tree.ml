type 'a binnary_tree = 
    | Empty
    | Node of 'a * 'a binnary_tree * 'a binnary_tree;;


let rec add_to_search_tree = fun t n -> match t with 
        Empty-> Node(n, Empty,Empty)
    |   Node(v,t1,t2) -> if (v > n) then Node(v,add_to_search_tree t1 n,t2)
                         else Node(v,t1,add_to_search_tree t2 n);;
