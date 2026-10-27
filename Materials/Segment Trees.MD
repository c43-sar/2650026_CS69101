# Segment Trees Pseudocodes from Gemini 3.6 Flash

```  
// Global constants and arrays
MAX_DATSIZE = 10^5
data = ARRAY[0 .. 4 * MAX_DATSIZE - 1] OF INTEGER OR NULL
active = ARRAY[0 .. MAX_DATSIZE - 1] OF BOOLEAN initialized to FALSE
size = 0                             // Tracks total active leaf elements
rangefn = SUM                       // Default binary range function


// -------------------------------------------------------------------
// Set Range Function
// -------------------------------------------------------------------
SET-RANGEFN(name, custom_fn)
    if custom_fn is provided:
        rangefn = custom_fn
    else if name = "SUM":
        rangefn = (first_val, second_val) -> first_val + second_val
    else if name = "MIN":
        rangefn = (first_val, second_val) -> min(first_val, second_val)
    else if name = "MAX":
        rangefn = (first_val, second_val) -> max(first_val, second_val)


// -------------------------------------------------------------------
// Helper to check if a node or its subtrees contain active elements
// -------------------------------------------------------------------
HAS-ACTIVE(node, left_bound, right_bound)
    if left_bound = right_bound:
        return active[left_bound]
    midpoint = floor((left_bound + right_bound) / 2)
    left_child = 2 * node + 1
    right_child = 2 * node + 2
    return HAS-ACTIVE(left_child, left_bound, midpoint) or HAS-ACTIVE(right_child, midpoint + 1, right_bound)


// -------------------------------------------------------------------
// Point Insertion
// -------------------------------------------------------------------
INSERT(target_index, value, left_bound = 0, right_bound = MAX_DATSIZE - 1, node = 0)
    if left_bound = right_bound:
        if active[target_index] is FALSE:
            active[target_index] = TRUE
            size = size + 1          // Increment active element count
        data[node] = value
        return

    midpoint = floor((left_bound + right_bound) / 2)
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    if target_index <= midpoint:
        INSERT(target_index, value, left_bound, midpoint, left_child)
    else:
        INSERT(target_index, value, midpoint + 1, right_bound, right_child)

    // Recompute aggregate without relying on identity elements
    left_has = HAS-ACTIVE(left_child, left_bound, midpoint)
    right_has = HAS-ACTIVE(right_child, midpoint + 1, right_bound)

    if left_has and right_has:
        data[node] = rangefn(data[left_child], data[right_child])
    else if left_has:
        data[node] = data[left_child]
    else if right_has:
        data[node] = data[right_child]


// -------------------------------------------------------------------
// Point Deletion
// -------------------------------------------------------------------
DELETE(target_index, left_bound = 0, right_bound = MAX_DATSIZE - 1, node = 0)
    if not HAS-ACTIVE(node, left_bound, right_bound):
        return

    if left_bound = right_bound:
        if active[target_index] is TRUE:
            active[target_index] = FALSE
            size = size - 1          // Decrement active element count
            data[node] = NULL
        return

    midpoint = floor((left_bound + right_bound) / 2)
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    if target_index <= midpoint:
        DELETE(target_index, left_bound, midpoint, left_child)
    else:
        DELETE(target_index, midpoint + 1, right_bound, right_child)

    // Recompute aggregate after deletion
    left_has = HAS-ACTIVE(left_child, left_bound, midpoint)
    right_has = HAS-ACTIVE(right_child, midpoint + 1, right_bound)

    if left_has and right_has:
        data[node] = rangefn(data[left_child], data[right_child])
    else if left_has:
        data[node] = data[left_child]
    else if right_has:
        data[node] = data[right_child]
    else:
        data[node] = NULL


// -------------------------------------------------------------------
// Inorder Traversal
// -------------------------------------------------------------------
TRAVERSE(left_bound = 0, right_bound = MAX_DATSIZE - 1, node = 0)
    if not HAS-ACTIVE(node, left_bound, right_bound):
        return

    if left_bound = right_bound:
        if active[left_bound]:
            PRINT "Leaf", left_bound, ":", data[node]
        return

    midpoint = floor((left_bound + right_bound) / 2)
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    TRAVERSE(left_bound, midpoint, left_child)
    PRINT "Internal Aggregate [", left_bound, "..", right_bound, "]:", data[node]
    TRAVERSE(midpoint + 1, right_bound, right_child)


// -------------------------------------------------------------------
// Range Query (No Identity Element Required)
// -------------------------------------------------------------------
RANGE-QUERY(query_start, query_end, left_bound = 0, right_bound = MAX_DATSIZE - 1, node = 0)
    if right_bound < query_start or query_end < left_bound or not HAS-ACTIVE(node, left_bound, right_bound):
        return NULL

    if query_start <= left_bound and right_bound <= query_end:
        return data[node]

    midpoint = floor((left_bound + right_bound) / 2)
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    left_res = RANGE-QUERY(query_start, query_end, left_bound, midpoint, left_child)
    right_res = RANGE-QUERY(query_start, query_end, midpoint + 1, right_bound, right_child)

    if left_res is not NULL and right_res is not NULL:
        return rangefn(left_res, right_res)
    else if left_res is not NULL:
        return left_res
    else:
        return right_res
 ```
