let rec insert_at = fun a n l ->   match (n,l) with  
    | (_,[]) -> [a]  
    | (0,l) -> a::l
    | (n,h::t) -> h :: insert_at a (n-1) t;;


let insert_none_at = fun n l -> insert_at "None" n l;;
