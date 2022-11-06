type bool_expr = 
    | Var of string
    | Not of bool_expr
    | And of bool_expr * bool_expr
    | Or of bool_expr * bool_expr;;
    

let rec calc = fun (p,a) (q,b) e -> match e with
    | Var(x) -> if x=p then a
                else b
    | Or(x,y) -> (calc (p,a) (q,b) x) || (calc (p,a) (q,b) y)
    | And(x,y) -> (calc (p,a) (q,b) x) && (calc (p,a) (q,b) y)
    | Not(x) ->  not(calc (p,a) (q,b) x);;


let table_two = fun p q exp ->
        [
        (true,true,calc (p,true) (q,true) exp);
        (true,false,calc (p,true) (q,false) exp);
        (false,true,calc (p,false) (q,true) exp);
        (false,false,calc (p,false) (q,false) exp);
        ];;
