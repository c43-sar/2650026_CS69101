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
SET-RANGEFN(name, fn)
    if fn is provided:
        rangefn = fn
    else if name = "SUM":
        rangefn = (x, y) -> x + y
    else if name = "MIN":
        rangefn = (x, y) -> min(x, y)
    else if name = "MAX":
        rangefn = (x, y) -> max(x, y)


// -------------------------------------------------------------------
// Helper to check if a node or its subtrees contain active elements
// -------------------------------------------------------------------
HAS-ACTIVE(v, l, r)
    if l = r:
        return active[l]
    mid = floor((l + r) / 2)
    return HAS-ACTIVE(2*v + 1, l, mid) or HAS-ACTIVE(2*v + 2, mid + 1, r)


// -------------------------------------------------------------------
// Point Insertion
// -------------------------------------------------------------------
INSERT(p, x, l = 0, r = MAX_DATSIZE - 1, v = 0)
    if l = r:
        if active[p] is FALSE:
            active[p] = TRUE
            size = size + 1          // Increment active element count
        data[v] = x
        return

    mid = floor((l + r) / 2)
    if p <= mid:
        INSERT(p, x, l, mid, 2*v + 1)
    else:
        INSERT(p, x, mid + 1, r, 2*v + 2)

    // Recompute aggregate without relying on identity elements
    left_has = HAS-ACTIVE(2*v + 1, l, mid)
    right_has = HAS-ACTIVE(2*v + 2, mid + 1, r)

    if left_has and right_has:
        data[v] = rangefn(data[2*v + 1], data[2*v + 2])
    else if left_has:
        data[v] = data[2*v + 1]
    else if right_has:
        data[v] = data[2*v + 2]


// -------------------------------------------------------------------
// Point Deletion
// -------------------------------------------------------------------
DELETE(p, l = 0, r = MAX_DATSIZE - 1, v = 0)
    if not HAS-ACTIVE(v, l, r):
        return

    if l = r:
        if active[p] is TRUE:
            active[p] = FALSE
            size = size - 1          // Decrement active element count
            data[v] = NULL
        return

    mid = floor((l + r) / 2)
    if p <= mid:
        DELETE(p, l, mid, 2*v + 1)
    else:
        DELETE(p, mid + 1, r, 2*v + 2)

    // Recompute aggregate after deletion
    left_has = HAS-ACTIVE(2*v + 1, l, mid)
    right_has = HAS-ACTIVE(2*v + 2, mid + 1, r)

    if left_has and right_has:
        data[v] = rangefn(data[2*v + 1], data[2*v + 2])
    else if left_has:
        data[v] = data[2*v + 1]
    else if right_has:
        data[v] = data[2*v + 2]
    else:
        data[v] = NULL


// -------------------------------------------------------------------
// Inorder Traversal
// -------------------------------------------------------------------
TRAVERSE(l = 0, r = MAX_DATSIZE - 1, v = 0)
    if not HAS-ACTIVE(v, l, r):
        return

    if l = r:
        if active[l]:
            PRINT "Leaf", l, ":", data[v]
        return

    mid = floor((l + r) / 2)
    TRAVERSE(l, mid, 2*v + 1)
    PRINT "Internal Aggregate [", l, "..", r, "]:", data[v]
    TRAVERSE(mid + 1, r, 2*v + 2)


// -------------------------------------------------------------------
// Range Query (No Identity Element Required)
// -------------------------------------------------------------------
RANGE-QUERY(i, j, l = 0, r = MAX_DATSIZE - 1, v = 0)
    if r < i or j < l or not HAS-ACTIVE(v, l, r):
        return NULL

    if i <= l and r <= j:
        return data[v]

    mid = floor((l + r) / 2)
    left_res = RANGE-QUERY(i, j, l, mid, 2*v + 1)
    right_res = RANGE-QUERY(i, j, mid + 1, r, 2*v + 2)

    if left_res is not NULL and right_res is not NULL:
        return rangefn(left_res, right_res)
    else if left_res is not NULL:
        return left_res
    else:
        return right_res
 ```
