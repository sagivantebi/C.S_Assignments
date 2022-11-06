type bool_expr =
| Var of string
| Not of bool_expr
| And of bool_expr * bool_expr
| Or of bool_expr * bool_expr;;

let rec find_var = fun i lis -> match lis with
| [] -> true
| (a,b)::[] -> b
| (a,b)::t -> if i = a then b else find_var i t;;

let rec calc = fun var_list exp -> match exp with
| Var(i) -> find_var i var_list
| Not(x) -> not (calc var_list x)
| And(x, y) -> (calc var_list x) && (calc var_list y)
| Or(x, y) -> (calc var_list x) || (calc var_list y);;

let rec solve = fun var_list tuples exp -> match (var_list,tuples) with
| ([],tuples) -> [(tuples, calc tuples exp)]
| (h::t, tuples) -> (solve t (tuples @ [(h, true)]) exp) @ (solve t (tuples @ [(h,false)]) exp);;

let table = fun l exp -> solve l [] exp;;
